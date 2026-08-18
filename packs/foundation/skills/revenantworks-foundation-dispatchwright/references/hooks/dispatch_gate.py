#!/usr/bin/env python3
"""dispatch_gate.py — UserPromptSubmit hook for revenantworks-foundation-dispatchwright.

Wired in settings.json as a UserPromptSubmit hook. Reads the hook JSON on stdin
(Claude Code's `{session_id, prompt, cwd, ...}` payload), tests the prompt's text
against the regexes in the sibling file `dispatch_patterns.txt` (one pattern per
line, `re.search`, case-insensitive), and on a match:

  1. Prints one JSON object to stdout carrying `hookSpecificOutput.additionalContext`
     — a note telling the model this turn looks like a fan-out and that
     dispatchwright's target table (tier, model, effort, surface per unit) must be
     produced before any Task/Agent/Workflow call.
  2. Writes a mode-flag file at `~/.claude/dispatch-mode.json` carrying the
     session id and a timestamp. `dispatch_ledger_guard.py` (the paired
     PreToolUse hook) reads this flag to decide whether to enforce the ledger
     requirement on a later Task/Agent/Workflow call in the SAME session.

FAILS OPEN, always. This hook only ever adds context or writes a small flag
file; it never blocks a prompt (UserPromptSubmit cannot exit 2 the way a
PreToolUse hook can). Any exception anywhere in the body is caught and the
process exits 0 with no output, so a broken matcher, a missing patterns file,
or an unwritable home directory never blocks an ordinary turn.

Run `python dispatch_gate.py --selftest` to check the patterns file compiles
and that a sample fan-out prompt matches while a sample ordinary prompt does
not. Stdlib only.
"""
import json
import re
import sys
import time
from pathlib import Path

HOOKS_DIR = Path(__file__).resolve().parent
PATTERNS_PATH = HOOKS_DIR / "dispatch_patterns.txt"
FLAG_PATH = Path.home() / ".claude" / "dispatch-mode.json"

ADDITIONAL_CONTEXT = (
    "dispatchwright gate: this prompt matched a fan-out pattern ({pattern!r}). "
    "Before any Task/Agent/Workflow call this turn, run dispatchwright's Shape "
    "check first (is this really a fan-out, or does the main conversation / one "
    "subagent / a skill do it cheaper?). If it is a fan-out: decompose into units, "
    "hand the unit list to promptwright's Entry - Model (plan grain) for the tier "
    "table, and write a ledger row -- model, effort, surface -- for every unit "
    "BEFORE dispatching it. See revenantworks-foundation-dispatchwright."
)


def load_patterns() -> list[str]:
    """One regex per line; blank lines and '#' comments ignored."""
    out = []
    for line in PATTERNS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return out


def first_match(prompt: str, patterns: list[str]) -> str | None:
    for pat in patterns:
        if re.search(pat, prompt, re.I):
            return pat
    return None


def write_flag(session_id: str) -> None:
    FLAG_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "session_id": session_id,
        "ts": time.time(),
        "iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "written_by": "dispatch_gate.py",
    }
    FLAG_PATH.write_text(json.dumps(payload), encoding="utf-8")


def selftest() -> int:
    """Exit non-zero if the pattern file is unusable, or the two sample
    prompts don't discriminate. Checks the machinery, not live hook I/O."""
    problems = []
    try:
        patterns = load_patterns()
    except FileNotFoundError:
        print(f"DISPATCH_GATE SELFTEST FAIL: {PATTERNS_PATH} not found")
        return 2
    if not patterns:
        problems.append("dispatch_patterns.txt is empty -- the gate would never fire")
    for pat in patterns:
        try:
            re.compile(pat)
        except re.error as e:
            problems.append(f"pattern {pat!r} does not compile: {e}")
    fan_out_sample = "Rebuild the whole estate -- every repo, every skill, sweep all of it."
    ordinary_sample = "Can you fix the typo in the README on line 12?"
    hit = first_match(fan_out_sample, patterns) if patterns else None
    miss = first_match(ordinary_sample, patterns) if patterns else "n/a"
    if not hit:
        problems.append(f"fan-out sample did not match any pattern: {fan_out_sample!r}")
    if miss:
        problems.append(f"ordinary sample matched {miss!r} and should not have: {ordinary_sample!r}")
    if problems:
        for p in problems:
            print(f"DISPATCH_GATE SELFTEST FAIL: {p}")
        return 2
    print(f"dispatch_gate selftest: OK ({len(patterns)} pattern(s) armed; "
          f"fan-out sample matched {hit!r}, ordinary sample matched nothing)")
    return 0


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return selftest()
    try:
        data = json.load(sys.stdin)
        prompt = data.get("prompt") or ""
        session_id = data.get("session_id") or "unknown-session"
        if not prompt:
            return 0
        patterns = load_patterns()
        hit = first_match(prompt, patterns)
        if hit:
            write_flag(session_id)
            out = {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": ADDITIONAL_CONTEXT.format(pattern=hit),
                }
            }
            print(json.dumps(out))
        return 0
    except Exception:
        # Fail open, unconditionally -- a broken matcher must never block an
        # ordinary prompt. No stderr either: UserPromptSubmit has no user
        # reading this hook's own diagnostics.
        return 0


if __name__ == "__main__":
    sys.exit(main())
