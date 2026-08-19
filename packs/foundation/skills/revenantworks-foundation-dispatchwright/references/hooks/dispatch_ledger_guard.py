#!/usr/bin/env python3
"""dispatch_ledger_guard.py — PreToolUse hook (matcher: Task|Agent|Workflow) for
revenantworks-foundation-dispatchwright.

Fixed 2026-08-18 — four fail-open defects, all reproduced on the live file
before the fix. The selftest below covers each one end to end; if you edit this
file, run `--selftest` and expect it to fail loudly rather than quietly pass.

  D1  NO SESSION ID WAS A TOTAL NO-OP. `flag_is_live` returned False whenever
      the payload carried no session id, so every Task/Agent/Workflow call
      without one sailed past the guard. Now a fresh flag with a session id the
      guard cannot correlate ENFORCES the ledger check instead of skipping it.
  D2  EXIT 1 ON ANY EXCEPTION. Claude Code blocks a PreToolUse call only on
      exit code 2; 1 is a non-blocking error. Only json.load was wrapped, so a
      throw anywhere later failed OPEN. The whole body is wrapped now and every
      path returns 0 or 2. Never 1.
  D3  A STALE LEDGER DISARMED THE GUARD FOREVER. find_ledger took the newest
      ledger by mtime with no age limit and no tie to the live run, so one old
      populated ledger in a directory passed every dispatch there for good. A
      ledger now has to sit inside the same staleness window that keeps the
      flag live, or name the current session outright.
  D4  JUNK CELLS COUNTED AS TIERED. `_populated` rejected only "", "-" and the
      em dash, so a row of TBD / ? / x satisfied "names its model, effort and
      surface". The three cells are now validated per field.

Pairs with dispatch_gate.py. That hook sets a mode-flag file
(`~/.claude/dispatch-mode.json`, session id + timestamp) when a prompt looks
like a fan-out. This hook reads it on every Task/Agent/Workflow call:

  - Flag absent, unreadable, stale, or owned by a DIFFERENT session -> exit 0.
    Dispatch mode is not active here; there is nothing to enforce.
  - Flag live for this session, or fresh but not correlatable -> the run ledger
    must exist, must be current, and must carry a properly tiered row. Anything
    else exits 2 with a short reason on stderr.

This is deliberately a coarse check, stated plainly rather than overclaimed: it
confirms *a* tiered row exists in the run's current ledger, not that the
SPECIFIC unit about to be dispatched has one -- correlating a Task call's own
tool_input against a specific ledger row would need a unit id the tool_input
has no standard place to carry. The coarse form still catches the failure mode
that matters most: a wave launched with a missing, stale, or untiered ledger.

FAILS CLOSED whenever it is armed and cannot prove the dispatch is tiered --
that is the point of this hook. dispatch_gate.py is the opposite and must stay
that way: it runs on every prompt, and a gate that can block is how the
2026-08-18 incident locked the owner out of a whole session.

Run `python dispatch_ledger_guard.py --selftest` to exercise the flag logic,
the ledger currency rule, the cell validators, and the real exit codes of all
four defects against temp fixtures. Stdlib only.
"""
import csv
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

GATED_TOOLS = {"Task", "Agent", "Workflow"}

# Defensive cap beyond the session-id check: a live flag from the SAME session
# id is still ignored past this age, in case a session id were ever reused
# across an unexpectedly long gap. The session-id match is the primary test.
# The SAME window decides whether a ledger is current (D3) -- one mechanism,
# not two, so raising this raises both together.
STALE_SECONDS = 12 * 60 * 60
# A file written seconds ago can carry a timestamp slightly in the future when
# the clock steps or a network drive disagrees. Tolerate that much skew rather
# than reading a just-written ledger as bogus.
CLOCK_SKEW_SECONDS = 5 * 60

# Session ids the gate writes when the prompt payload had none. Treated as "no
# session id at all" on the flag side.
UNCORRELATABLE_SESSION_IDS = {"", "unknown-session", "unknown", "none", "null"}


def flag_path() -> Path:
    """The mode-flag file. CLAUDE_DISPATCH_FLAG exists so --selftest can run
    the real main() against a temp flag without touching the live one."""
    override = os.environ.get("CLAUDE_DISPATCH_FLAG")
    if override:
        return Path(override)
    return Path.home() / ".claude" / "dispatch-mode.json"


def read_flag() -> dict | None:
    try:
        data = json.loads(flag_path().read_text(encoding="utf-8"))
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def _fresh(ts: float | int | None, now: float | None = None) -> bool:
    """True if `ts` sits inside the staleness window. Shared by the flag check
    and the ledger currency check so the two can never drift apart."""
    if not isinstance(ts, (int, float)) or isinstance(ts, bool):
        return False
    now = time.time() if now is None else now
    age = now - ts
    return -CLOCK_SKEW_SECONDS <= age <= STALE_SECONDS


def flag_state(flag: dict | None, session_id: str) -> str:
    """One of: absent, stale, other-session, uncorrelated, live.

    D1 lives here. The old code returned False -- allow everything -- whenever
    the payload carried no session id, which made a session-less PreToolUse
    payload a free pass around the entire guard. A guard that cannot correlate
    must not conclude "not my session"; it can only conclude "I do not know".
    So a FRESH flag plus an uncorrelatable session id on either side returns
    "uncorrelated", and the caller enforces the ledger check exactly as it does
    for "live". Fail closed on the doubt.

    Blocking outright on "uncorrelated" would be worse, not better: it leaves
    the owner no remedy but deleting the flag by hand for the next 12 hours.
    Enforcing the ledger keeps the real invariant -- an untiered dispatch is
    impossible -- while a correctly tiered wave still runs.

    An absent or long-stale flag still returns early. Nothing was ever armed
    for anyone, and blocking there would lock out every Task call on a machine
    that simply never uses dispatch mode."""
    if not flag:
        return "absent"
    if not _fresh(flag.get("ts")):
        return "stale"
    flag_session = str(flag.get("session_id") or "").strip()
    payload_session = str(session_id or "").strip()
    if (
        flag_session.lower() in UNCORRELATABLE_SESSION_IDS
        or payload_session.lower() in UNCORRELATABLE_SESSION_IDS
    ):
        return "uncorrelated"
    if flag_session != payload_session:
        return "other-session"
    return "live"


def flag_is_live(flag: dict | None, session_id: str) -> bool:
    """Kept for callers that only want the yes/no. `flag_state` carries the
    reason, and main() uses that."""
    return flag_state(flag, session_id) == "live"


def ledger_names_session(path: Path, session_id: str) -> bool:
    """A ledger can tie itself to a session explicitly: the session id written
    anywhere in the ledger text, or in a sibling file named `session` in the
    run directory. Nothing writes those today -- the Markdown and CSV schemas
    in references/ledger-schema.md carry no session column -- so this is the
    forward path, not the primary test, and its absence is never a failure."""
    sid = str(session_id or "").strip()
    if not sid or sid.lower() in UNCORRELATABLE_SESSION_IDS:
        return False
    try:
        if sid in path.read_text(encoding="utf-8", errors="replace"):
            return True
    except Exception:
        pass
    marker = path.parent / "session"
    try:
        if marker.is_file() and sid in marker.read_text(encoding="utf-8", errors="replace"):
            return True
    except Exception:
        pass
    return False


def ledger_is_current(path: Path, session_id: str, now: float | None = None) -> bool:
    """D3. A ledger counts only if it belongs to the run that is live right
    now: it names the current session, or it was written inside the same
    staleness window that keeps the flag live. Without this a single populated
    ledger left in a directory passed every dispatch made there, forever."""
    if ledger_names_session(path, session_id):
        return True
    try:
        mtime = path.stat().st_mtime
    except Exception:
        return False
    return _fresh(mtime, now)


def ledger_candidates(cwd: str) -> list[Path]:
    """Every ledger the conventions allow, newest first. CLAUDE_DISPATCH_LEDGER
    names one file directly and wins outright."""
    env = os.environ.get("CLAUDE_DISPATCH_LEDGER")
    if env:
        p = Path(env)
        return [p] if p.is_file() else []
    root = Path(cwd or ".")
    found = list(root.glob(".dispatch/runs/*/ledger.md")) + list(root.glob(".dispatch/runs/*/ledger.csv"))
    candidates = [p for p in found if p.is_file()]

    def _mtime(p: Path) -> float:
        try:
            return p.stat().st_mtime
        except Exception:
            return 0.0

    candidates.sort(key=_mtime, reverse=True)
    return candidates


def find_ledger(cwd: str, session_id: str = "") -> Path | None:
    """The newest ledger that is still current for this run. A stale one is not
    a ledger for this purpose -- returning it and passing would be the D3 bug."""
    for p in ledger_candidates(cwd):
        if ledger_is_current(p, session_id):
            return p
    return None


# ---------------------------------------------------------------------------
# D4 -- what counts as a tiered cell.
#
# The rule, stated once so it does not need editing every time a model ships:
#
#   model    Must not be a known placeholder token, must contain a letter, and
#            must look like a NAME rather than a word: it carries a digit
#            (gpt-5, o3, Haiku 4.5) or joins two alphanumeric chunks with a
#            space, hyphen, dot, slash, underscore or colon (Claude Opus,
#            claude-opus-5). No list of model names appears anywhere here, so a
#            model released tomorrow passes on the day it ships while "TBD",
#            "?", "x", "auto" and "model" all fail.
#   effort   A genuinely closed vocabulary -- the harness defines it, not the
#            model vendors, so enumerating it is safe and it does not churn.
#            The cell passes if any of those words appears in it, which lets
#            "high", "effort: high" and "high (extended thinking)" through.
#   surface  Free text by design (subagent (background), main conversation, a
#            worktree name). No vocabulary is possible, so the bar is: not a
#            placeholder, at least four characters, and it contains a letter.
#            That rejects the junk a hurried row carries without pretending to
#            validate something this hook cannot see.
#
# The check is a floor, not a proof. It stops an untiered row, not a wrong one.
# ---------------------------------------------------------------------------
PLACEHOLDER_CELLS = {
    "", "-", "--", "---", "—", "–", "_", ".", "..", "...", "…",
    "?", "??", "???", "!", "n/a", "na", "n.a.", "nil", "null", "none", "nan",
    "tbd", "tba", "todo", "to do", "unknown", "unk", "unset", "undefined",
    "x", "xx", "xxx", "y", "yy", "z", "zz", "foo", "bar", "baz", "qux",
    "auto", "automatic", "default", "any", "same", "same as above", "ditto",
    "idem", "model", "effort", "surface", "tier", "fill", "fill in", "fillme",
    "fill me in", "placeholder", "pending", "wip", "tk", "tktk", "later",
    "see above", "as above", "n/k", "unspecified",
}

EFFORT_WORDS = {
    "none", "off", "zero", "minimal", "min", "low", "medium", "med", "moderate",
    "standard", "normal", "default-effort", "high", "higher", "xhigh", "veryhigh",
    "max", "maximum", "ultra", "think", "megathink", "ultrathink", "extended",
}


def _norm(cell: str) -> str:
    """Lowercase, collapse whitespace, drop surrounding punctuation."""
    s = " ".join(str(cell or "").split()).strip().lower()
    return s.strip("`*\"'()[[]{}<>.,;:!")


def _is_placeholder(cell: str) -> bool:
    return _norm(cell) in PLACEHOLDER_CELLS


def names_a_model(cell: str) -> bool:
    s = str(cell or "").strip()
    if _is_placeholder(s) or len(s) < 2:
        return False
    if not any(c.isalpha() for c in s):
        return False
    if any(c.isdigit() for c in s):
        return True
    return bool(re.search(r"[A-Za-z0-9][ \-._/:][A-Za-z0-9]", s))


def names_an_effort(cell: str) -> bool:
    s = _norm(cell)
    if not s or s in PLACEHOLDER_CELLS - EFFORT_WORDS:
        return False
    words = set(re.findall(r"[a-z]+", s))
    return bool(words & EFFORT_WORDS)


def names_a_surface(cell: str) -> bool:
    s = str(cell or "").strip()
    if _is_placeholder(s) or len(s) < 4:
        return False
    return any(c.isalpha() for c in s)


CELL_CHECKS = {
    "model": names_a_model,
    "effort": names_an_effort,
    "surface": names_a_surface,
}


def _populated(cells: dict[str, str]) -> bool:
    """True only if every one of model, effort and surface plausibly names a
    real value. The old version rejected "", "-" and the em dash and nothing
    else, so TBD / ? / x read as tiered (D4)."""
    for name, value in cells.items():
        check = CELL_CHECKS.get(name)
        if check is None:
            if not str(value or "").strip():
                return False
            continue
        if not check(value):
            return False
    return True


def ledger_has_populated_row(path: Path) -> bool:
    """True if the ledger names at least one row whose model, effort and
    surface cells all plausibly name a real value. Supports the two forms
    ledger-schema.md allows: a Markdown pipe table, or a CSV with a header."""
    text = path.read_text(encoding="utf-8", errors="replace")
    needed = ("model", "effort", "surface")

    if path.suffix.lower() == ".csv":
        rows = list(csv.reader(io.StringIO(text)))
        if len(rows) < 2:
            return False
        header = [h.strip().lower() for h in rows[0]]
        idx = {name: header.index(name) for name in needed if name in header}
        if len(idx) < len(needed):
            return False
        for row in rows[1:]:
            if len(row) <= max(idx.values()):
                continue
            if _populated({name: row[i] for name, i in idx.items()}):
                return True
        return False

    # Markdown pipe table.
    lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return False
    header_cells = [c.strip().lower() for c in lines[0].strip().strip("|").split("|")]
    idx: dict[str, int] = {}
    for name in needed:
        for i, cell in enumerate(header_cells):
            if name in cell:
                idx[name] = i
                break
    if len(idx) < len(needed):
        return False
    for ln in lines[1:]:
        stripped = ln.strip().strip("|")
        cells = [c.strip() for c in stripped.split("|")]
        # The `|---|---|` (or `|:---:|`) separator row: split FIRST, then check
        # each cell -- checking the raw string's character set was wrong, since
        # the inner "|" separators survive stripping only the outer pair and
        # poison a whole-string subset test (`{'-', '|'} <= {'-', ''}` is False
        # even for a genuine all-dash row).
        if all(set(c) <= {"-", ":"} for c in cells):
            continue
        if max(idx.values()) < len(cells) and _populated({name: cells[i] for name, i in idx.items()}):
            return True
    return False


TIERED_LEDGER = (
    "| unit_id | task | class | model | effort | surface |\n"
    "|---------|------|-------|-------|--------|---------|\n"
    "| U1 | thing | judgment | Claude Opus 5 | high | subagent (background) |\n"
)


def _run_guard(payload: dict, flag: dict | None, tmp: Path, env_extra: dict | None = None) -> int:
    """Run this file as the real hook, in a subprocess, against a temp flag.
    The selftest asserts on EXIT CODES, not on internal returns -- D2 was
    exactly the kind of bug an internals-only test cannot see."""
    flag_file = tmp / "flag.json"
    if flag is None:
        if flag_file.exists():
            flag_file.unlink()
    else:
        flag_file.write_text(json.dumps(flag), encoding="utf-8")
    env = dict(os.environ)
    env["CLAUDE_DISPATCH_FLAG"] = str(flag_file)
    env.pop("CLAUDE_DISPATCH_LEDGER", None)
    env.update(env_extra or {})
    proc = subprocess.run(
        [sys.executable, str(Path(__file__).resolve())],
        input=payload if isinstance(payload, str) else json.dumps(payload),
        capture_output=True,
        text=True,
        env=env,
    )
    return proc.returncode


def selftest() -> int:
    """Covers the four fixed defects at the exit-code level, plus the flag and
    parsing logic. Every case names the defect it guards, so a future edit that
    reopens one fails here by name."""
    problems = []
    now = time.time()

    # --- flag logic, including D1 ---------------------------------------
    live = {"session_id": "abc", "ts": now}
    if flag_state(live, "abc") != "live":
        problems.append("a fresh flag with a matching session id should read live")
    if flag_state(live, "different-session") != "other-session":
        problems.append("a flag from a different session id should not enforce")
    if flag_state({"session_id": "abc", "ts": now - STALE_SECONDS - 3600}, "abc") != "stale":
        problems.append("a flag older than STALE_SECONDS should read stale")
    if flag_state(None, "abc") != "absent":
        problems.append("a missing flag should never enforce")
    # D1: the payload carries no session id.
    if flag_state(live, "") != "uncorrelated":
        problems.append("D1: a fresh flag plus an empty payload session id must enforce, not skip")
    if flag_state({"session_id": "unknown-session", "ts": now}, "abc") != "uncorrelated":
        problems.append("D1: a fresh flag whose own session id is the unknown sentinel must enforce")
    if flag_state({"session_id": "abc", "ts": now - STALE_SECONDS - 3600}, "") != "stale":
        problems.append("D1: a stale flag must still be stale even with no payload session id")

    # --- cell validators, D4 --------------------------------------------
    for good in ("Claude Opus 5", "Claude Haiku 4.5", "claude-sonnet-5", "gpt-5", "o3", "Claude Opus"):
        if not names_a_model(good):
            problems.append(f"D4: a real model name was rejected: {good!r}")
    for junk in ("", "-", "—", "TBD", "?", "x", "auto", "model", "n/a", "  "):
        if names_a_model(junk):
            problems.append(f"D4: a placeholder passed as a model name: {junk!r}")
    for good in ("none", "low", "medium", "high", "max", "effort: high", "high (extended thinking)"):
        if not names_an_effort(good):
            problems.append(f"D4: a real effort was rejected: {good!r}")
    for junk in ("", "-", "?", "x", "TBD", "42", "???"):
        if names_an_effort(junk):
            problems.append(f"D4: a placeholder passed as an effort: {junk!r}")
    for good in ("subagent (background)", "main conversation", "worktree wt-1", "cloud routine"):
        if not names_a_surface(good):
            problems.append(f"D4: a real surface was rejected: {good!r}")
    for junk in ("", "-", "?", "x", "TBD", "n/a", "  "):
        if names_a_surface(junk):
            problems.append(f"D4: a placeholder passed as a surface: {junk!r}")

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)

        # --- ledger parsing ---------------------------------------------
        empty_md = tmp / "empty.md"
        empty_md.write_text(
            "| unit_id | task | class | model | effort | surface |\n"
            "|---|---|---|---|---|---|\n"
            "| U1 | thing | mechanical |  |  |  |\n",
            encoding="utf-8",
        )
        if ledger_has_populated_row(empty_md):
            problems.append("an all-blank ledger row was read as populated")

        junk_md = tmp / "junk.md"
        junk_md.write_text(
            "| unit_id | task | class | model | effort | surface |\n"
            "|---|---|---|---|---|---|\n"
            "| U1 | thing | mechanical | TBD | ? | x |\n",
            encoding="utf-8",
        )
        if ledger_has_populated_row(junk_md):
            problems.append("D4: a row of TBD / ? / x was read as tiered")

        filled_md = tmp / "filled.md"
        filled_md.write_text(TIERED_LEDGER, encoding="utf-8")
        if not ledger_has_populated_row(filled_md):
            problems.append("a fully-populated ledger row was not recognized")

        filled_csv = tmp / "filled.csv"
        filled_csv.write_text(
            "unit_id,task,class,model,effort,surface\n"
            "U1,thing,mechanical,Claude Haiku 4.5,none,subagent (background)\n",
            encoding="utf-8",
        )
        if not ledger_has_populated_row(filled_csv):
            problems.append("a fully-populated CSV ledger row was not recognized")

        junk_csv = tmp / "junk.csv"
        junk_csv.write_text(
            "unit_id,task,class,model,effort,surface\nU1,thing,mechanical,TBD,?,x\n",
            encoding="utf-8",
        )
        if ledger_has_populated_row(junk_csv):
            problems.append("D4: a CSV row of TBD / ? / x was read as tiered")

        # --- ledger currency, D3 -----------------------------------------
        fresh_dir = tmp / "fresh" / ".dispatch" / "runs" / "r1"
        fresh_dir.mkdir(parents=True)
        fresh_ledger = fresh_dir / "ledger.md"
        fresh_ledger.write_text(TIERED_LEDGER, encoding="utf-8")
        if not ledger_is_current(fresh_ledger, "abc"):
            problems.append("a ledger written just now should read as current")
        if find_ledger(str(tmp / "fresh"), "abc") is None:
            problems.append("find_ledger did not locate a fresh ledger under .dispatch/runs/*/")

        old_dir = tmp / "old" / ".dispatch" / "runs" / "2020-01-01-ancient"
        old_dir.mkdir(parents=True)
        old_ledger = old_dir / "ledger.md"
        old_ledger.write_text(TIERED_LEDGER, encoding="utf-8")
        ancient = now - STALE_SECONDS - 3600
        os.utime(old_ledger, (ancient, ancient))
        if ledger_is_current(old_ledger, "abc"):
            problems.append("D3: a ledger older than the flag's window read as current")
        if find_ledger(str(tmp / "old"), "abc") is not None:
            problems.append("D3: find_ledger returned a stale ledger, which is the permanent-disarm bug")

        marked_dir = tmp / "marked" / ".dispatch" / "runs" / "r1"
        marked_dir.mkdir(parents=True)
        marked = marked_dir / "ledger.md"
        marked.write_text(TIERED_LEDGER + "\nsession: sess-xyz\n", encoding="utf-8")
        os.utime(marked, (ancient, ancient))
        if not ledger_is_current(marked, "sess-xyz"):
            problems.append("a ledger naming the current session should stay current despite its mtime")
        if ledger_is_current(marked, "some-other-session"):
            problems.append("D3: an old ledger naming a DIFFERENT session read as current")

        missing = find_ledger(str(tmp / "nothing-here"), "abc")
        if missing is not None:
            problems.append("find_ledger found a ledger in a directory with no .dispatch/runs/ tree")

        # --- real exit codes ---------------------------------------------
        fresh_flag = {"session_id": "abc", "ts": now}
        no_ledger_dir = tmp / "bare"
        no_ledger_dir.mkdir()

        cases = [
            # (label, payload, flag, expected exit)
            ("a non-gated tool is never touched",
             {"tool_name": "Read", "session_id": "abc", "cwd": str(no_ledger_dir)}, fresh_flag, 0),
            ("no flag on disk means nothing is armed",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(no_ledger_dir)}, None, 0),
            ("a stale flag means nothing is armed",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(no_ledger_dir)},
             {"session_id": "abc", "ts": now - STALE_SECONDS - 3600}, 0),
            ("another session's flag is not ours",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(no_ledger_dir)},
             {"session_id": "zzz", "ts": now}, 0),
            ("armed and no ledger blocks",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(no_ledger_dir)}, fresh_flag, 2),
            ("armed with a tiered fresh ledger allows",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(tmp / "fresh")}, fresh_flag, 0),
            # D1
            ("D1: no session id in the payload must still enforce",
             {"tool_name": "Task", "tool_input": {"prompt": "x"}, "cwd": str(no_ledger_dir)}, fresh_flag, 2),
            ("D1: no session id, but a tiered fresh ledger, still allows",
             {"tool_name": "Task", "tool_input": {"prompt": "x"}, "cwd": str(tmp / "fresh")}, fresh_flag, 0),
            # D2
            ("D2: an unreadable ledger blocks with 2, never 1",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(tmp / "trap")}, fresh_flag, 2),
            ("D2: unparseable stdin blocks with 2, never 1",
             "{not json at all", fresh_flag, 2),
            ("D2: empty stdin blocks with 2, never 1", "", fresh_flag, 2),
            # D3
            ("D3: a stale populated ledger no longer passes",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(tmp / "old")}, fresh_flag, 2),
            # D4
            ("D4: a ledger of junk cells no longer passes",
             {"tool_name": "Task", "session_id": "abc", "cwd": str(tmp / "junkrun")}, fresh_flag, 2),
        ]

        # D2 fixture: ledger.md is a directory, so read_text throws.
        (tmp / "trap" / ".dispatch" / "runs" / "r1" / "ledger.md").mkdir(parents=True)
        # D4 fixture: a fresh ledger whose only row is junk.
        junk_run = tmp / "junkrun" / ".dispatch" / "runs" / "r1"
        junk_run.mkdir(parents=True)
        (junk_run / "ledger.md").write_text(junk_md.read_text(encoding="utf-8"), encoding="utf-8")

        for label, payload, flag, expected in cases:
            code = _run_guard(payload, flag, tmp)
            if code != expected:
                problems.append(f"{label}: expected exit {expected}, got {code}")
            if code not in (0, 2):
                problems.append(f"{label}: exit {code} is neither allow (0) nor block (2)")

    if problems:
        for p in problems:
            print(f"DISPATCH_LEDGER_GUARD SELFTEST FAIL: {p}")
        return 2
    print(
        "dispatch_ledger_guard selftest: OK (flag states incl. uncorrelated, "
        "ledger currency, cell validators, and 13 real exit-code cases covering "
        "all four 2026-08-18 defects)"
    )
    return 0


def _guard(data: dict) -> int:
    tool_name = data.get("tool_name", "")
    if tool_name not in GATED_TOOLS:
        return 0

    session_id = str(data.get("session_id") or "")
    state = flag_state(read_flag(), session_id)
    if state in ("absent", "stale", "other-session"):
        return 0  # dispatch mode is not active for this session

    cwd = data.get("cwd") or os.getcwd()
    ledger = find_ledger(cwd, session_id)
    if ledger is None:
        stale_seen = [str(p) for p in ledger_candidates(cwd)]
        extra = (
            f" Ledgers were found but none is current for this run: {', '.join(stale_seen)}."
            f" A ledger counts only if it names this session or was written in the last"
            f" {STALE_SECONDS // 3600}h."
            if stale_seen else ""
        )
        print(
            "dispatch_ledger_guard: dispatch mode is active for this session but no current run "
            "ledger was found (checked CLAUDE_DISPATCH_LEDGER, then .dispatch/runs/*/ledger.{md,csv} "
            "under the cwd)." + extra + " Write the ledger row -- model, effort, surface, from "
            "promptwright's target table -- before this dispatch. See references/ledger-schema.md.",
            file=sys.stderr,
        )
        return 2

    if not ledger_has_populated_row(ledger):
        print(
            f"dispatch_ledger_guard: {ledger} carries no row that names a model, an effort, and a "
            "surface. Placeholders such as TBD, ?, x or a dash do not count. Tier the unit through "
            "promptwright first and write the real row before dispatching it.",
            file=sys.stderr,
        )
        return 2

    return 0


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return selftest()
    # D2. Every path below returns 0 or 2. Claude Code blocks a PreToolUse call
    # ONLY on exit code 2 -- a bare traceback exits 1, which it reads as a
    # non-blocking error and runs the tool anyway. So the whole body is wrapped,
    # and an unexpected fault blocks rather than waving the dispatch through on
    # exactly the path this hook exists to protect.
    try:
        try:
            data = json.load(sys.stdin)
        except Exception as e:
            raise RuntimeError(f"the PreToolUse payload on stdin could not be parsed ({e})") from e
        if not isinstance(data, dict):
            raise RuntimeError("the PreToolUse payload on stdin was not a JSON object")
        return _guard(data)
    except Exception as e:
        print(
            f"dispatch_ledger_guard: blocking because the guard itself failed -- {type(e).__name__}: {e}. "
            "It cannot prove this dispatch is tiered, so it fails closed. Fix the fault, or disarm the "
            "guard by deleting the flag file (~/.claude/dispatch-mode.json); removing the PreToolUse "
            "block from ~/.claude/settings.json turns it off for good.",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    sys.exit(main())
