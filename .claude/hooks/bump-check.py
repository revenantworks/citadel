#!/usr/bin/env python3
"""Post-commit nudge for revenantworks/claude-skills.

Wired as a PostToolUse hook on Bash, conditioned to `git commit` calls
(`"if": "Bash(git commit *)"` in .claude/settings.json). It runs the read-only
gate `python tools/build.py --check` and surfaces two things as a
systemMessage: every `pack bump needed: <pack>` / `member bump needed:` line
the gate emits (shipped content moved past what a version names — the pack
version is the key installs and zips read, so the change is invisible until
it moves), and a one-line flag when the gate itself is not clean.

Never blocks (PostToolUse cannot), never edits, exit 0 always. Silent when
there is nothing to say. Stdlib only.
"""
import json
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    try:
        json.load(sys.stdin)  # payload unused beyond consuming it; the `if` rule already filtered
    except (json.JSONDecodeError, ValueError):
        pass
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
    build = root / "tools" / "build.py"
    if not build.is_file():
        return 0
    try:
        run = subprocess.run([sys.executable, str(build), "--check"], cwd=str(root),
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=25)
    except (OSError, subprocess.TimeoutExpired):
        return 0
    out = run.stdout + run.stderr
    packs = [ln.split("pack bump needed:", 1)[1].split("—", 1)[0].strip()
             for ln in out.splitlines() if "pack bump needed:" in ln]
    members = [ln.split("member bump needed:", 1)[1].split("—", 1)[0].strip().split("-")[-1]
               for ln in out.splitlines() if "member bump needed:" in ln]
    msg = [f"pack bump needed: {p}" for p in packs]
    if members:
        msg.append("member bump needed: " + ", ".join(members))
    if run.returncode != 0:
        msg.append("build.py --check is NOT clean after this commit — run `python tools/build.py --check`")
    if msg:
        print(json.dumps({"systemMessage": "claude-skills: " + " · ".join(msg)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
