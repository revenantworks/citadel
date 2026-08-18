#!/usr/bin/env python3
"""dispatch_ledger_guard.py — PreToolUse hook (matcher: Task|Agent|Workflow) for
revenantworks-foundation-dispatchwright.

Pairs with dispatch_gate.py. That hook sets a mode-flag file
(`~/.claude/dispatch-mode.json`, session id + timestamp) when a prompt looks
like a fan-out. This hook reads it on every Task/Agent/Workflow call:

  - Flag absent, or stale (a different session, or older than STALE_SECONDS) ->
    exit 0. Dispatch mode is not active for this session; nothing to enforce.
  - Flag live -> look for the run ledger (path convention from
    references/ledger-schema.md: `<cwd>/.dispatch/runs/*/ledger.{md,csv}`, or
    the env override CLAUDE_DISPATCH_LEDGER naming the file directly) and exit 2
    with a short reason on stderr when no ledger is found, or the ledger has no
    row carrying a non-empty model, effort, and surface.

This is deliberately a coarse check, stated plainly rather than overclaimed: it
confirms *a* populated row exists in the run's ledger, not that the SPECIFIC
unit about to be dispatched has one -- correlating a Task call's own
tool_input against a specific ledger row would need a unit id the tool_input
has no standard place to carry. The coarse form still catches the failure mode
that matters most: a wave launched with an empty or missing ledger. Tighten it
if a project adopts a convention for passing the unit id through.

FAILS CLOSED while the flag is live and the ledger check fails -- that is the
point of this hook; a broken matcher does not save you here the way it does
in dispatch_gate.py. Run `python dispatch_ledger_guard.py --selftest` to
exercise the flag-staleness and ledger-parsing logic against temp fixtures,
no live hook I/O involved. Stdlib only.
"""
import csv
import io
import json
import os
import sys
import tempfile
import time
from pathlib import Path

FLAG_PATH = Path.home() / ".claude" / "dispatch-mode.json"
GATED_TOOLS = {"Task", "Agent", "Workflow"}
# Defensive cap beyond the session-id check: a live flag from the SAME session
# id is still ignored past this age, in case a session id were ever reused
# across an unexpectedly long gap. The session-id match is the primary test.
STALE_SECONDS = 12 * 60 * 60


def read_flag() -> dict | None:
    try:
        return json.loads(FLAG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None


def flag_is_live(flag: dict | None, session_id: str) -> bool:
    if not flag or not session_id:
        return False
    if flag.get("session_id") != session_id:
        return False
    ts = flag.get("ts")
    if not isinstance(ts, (int, float)):
        return False
    return (time.time() - ts) <= STALE_SECONDS


def find_ledger(cwd: str) -> Path | None:
    env = os.environ.get("CLAUDE_DISPATCH_LEDGER")
    if env:
        p = Path(env)
        return p if p.is_file() else None
    root = Path(cwd or ".")
    candidates = list(root.glob(".dispatch/runs/*/ledger.md")) + list(root.glob(".dispatch/runs/*/ledger.csv"))
    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


def _populated(cells: dict[str, str]) -> bool:
    return all(v.strip() and v.strip() not in ("-", "—") for v in cells.values())


def ledger_has_populated_row(path: Path) -> bool:
    """True if the ledger names at least one row with non-empty model, effort,
    and surface cells. Supports the two forms ledger-schema.md allows: a
    Markdown pipe table, or a CSV with a header row."""
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


def selftest() -> int:
    """Exercises flag staleness and ledger parsing against temp fixtures --
    no real hook JSON, no real ~/.claude/dispatch-mode.json touched."""
    problems = []

    now = time.time()
    live = {"session_id": "abc", "ts": now}
    if not flag_is_live(live, "abc"):
        problems.append("a fresh flag with a matching session id should read live")
    if flag_is_live(live, "different-session"):
        problems.append("a flag from a different session id should read stale")
    if flag_is_live({"session_id": "abc", "ts": now - STALE_SECONDS - 3600}, "abc"):
        problems.append("a flag older than STALE_SECONDS should read stale even with a matching session id")
    if flag_is_live(None, "abc"):
        problems.append("a missing flag should never read live")

    with tempfile.TemporaryDirectory() as td:
        empty_md = Path(td) / "empty.md"
        empty_md.write_text(
            "| unit_id | task | class | model | effort | surface |\n"
            "|---|---|---|---|---|---|\n"
            "| U1 | thing | mechanical |  |  |  |\n",
            encoding="utf-8",
        )
        if ledger_has_populated_row(empty_md):
            problems.append("an all-blank ledger row was read as populated")

        filled_md = Path(td) / "filled.md"
        filled_md.write_text(
            "| unit_id | task | class | model | effort | surface |\n"
            "|---|---|---|---|---|---|\n"
            "| U1 | thing | mechanical | Claude Haiku 4.5 | none | subagent (background) |\n",
            encoding="utf-8",
        )
        if not ledger_has_populated_row(filled_md):
            problems.append("a fully-populated ledger row was not recognized")

        filled_csv = Path(td) / "filled.csv"
        filled_csv.write_text(
            "unit_id,task,class,model,effort,surface\n"
            "U1,thing,mechanical,Claude Haiku 4.5,none,subagent (background)\n",
            encoding="utf-8",
        )
        if not ledger_has_populated_row(filled_csv):
            problems.append("a fully-populated CSV ledger row was not recognized")

        missing = find_ledger(td)
        if missing is not None:
            problems.append("find_ledger found a ledger in a directory with no .dispatch/runs/ tree")

        run_dir = Path(td) / ".dispatch" / "runs" / "2026-08-18-demo"
        run_dir.mkdir(parents=True)
        (run_dir / "ledger.md").write_text(filled_md.read_text(encoding="utf-8"), encoding="utf-8")
        found = find_ledger(td)
        if found is None or found.name != "ledger.md":
            problems.append("find_ledger did not locate the ledger under .dispatch/runs/*/ledger.md")

    if problems:
        for p in problems:
            print(f"DISPATCH_LEDGER_GUARD SELFTEST FAIL: {p}")
        return 2
    print("dispatch_ledger_guard selftest: OK (flag staleness + Markdown/CSV ledger parsing)")
    return 0


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return selftest()
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # can't read the payload -- nothing to enforce against

    tool_name = data.get("tool_name", "")
    if tool_name not in GATED_TOOLS:
        return 0

    session_id = data.get("session_id", "")
    flag = read_flag()
    if not flag_is_live(flag, session_id):
        return 0  # dispatch mode not active for this session

    cwd = data.get("cwd") or os.getcwd()
    ledger = find_ledger(cwd)
    if ledger is None:
        print(
            "dispatch_ledger_guard: dispatch mode is active for this session but no run ledger "
            "was found (checked CLAUDE_DISPATCH_LEDGER, then .dispatch/runs/*/ledger.{md,csv} "
            "under the cwd). Write the ledger row -- model, effort, surface, from promptwright's "
            "target table -- before this dispatch. See references/ledger-schema.md.",
            file=sys.stderr,
        )
        return 2

    if not ledger_has_populated_row(ledger):
        print(
            f"dispatch_ledger_guard: {ledger} carries no row with model, effort, and surface all "
            "filled in. Tier the unit through promptwright first and write the row before "
            "dispatching it.",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
