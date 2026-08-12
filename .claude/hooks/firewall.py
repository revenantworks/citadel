#!/usr/bin/env python3
"""Brand firewall for revenantworks/citadel.

Blocks the work identity's tokens from entering this repo. Permission rules match
paths and command prefixes; they cannot see file *contents*, so a token can
land inside an otherwise legitimately-named file. This hook closes that gap.

Wired as a PreToolUse hook. Exit 2 blocks the call and returns stderr to Claude.

Scope, and its limits:
  - Write/Edit/MultiEdit/NotebookEdit - inspects file_path, content, new_string,
    and every edit in an `edits` array.
  - Bash/PowerShell - inspects the command string, so copying a file
    from the work-identity tree into citadel via the shell
    is caught too. This is a guardrail against accident, not a sandbox against
    intent: a base64'd payload or an obscure path spelling will pass.
  - Reads are NOT blocked. Reading the work-identity set from here is how a drift audit
    works; only writing its identity INTO citadel is the hazard.

The blocked vocabulary lives in blocklist.txt next to this file - untracked,
gitignored, never committed. This script is tracked and token-free. If the
blocklist is missing the hook FAILS CLOSED (exit 2): the firewall never runs
open just because its roster went missing.
"""
import json
import re
import sys
from pathlib import Path

# Terms that must never enter this repo live in this untracked file, one entry
# per line: regex-pattern<TAB>label. Lines starting with '#' and blank lines
# are ignored. A line with no tab uses the pattern as its own label.
#
# Deliberately scoped to work-identity *tokens*, never to a person's or a
# company's name. Owner decision 2026-08-07: a name is not recorded here. The
# reason is that a blocklist can only match what it stores, so blocking a name
# means writing it down - which creates the exposure the firewall exists to
# prevent, and in a file whose whole safety argument is that it stays
# gitignored. The tokens in the blocklist are project vocabulary, not
# identifying information, so they carry no such cost.
#
# Accepted consequence, stated rather than hidden: this hook does not catch a
# bare employer or client name. That case is held by judgment, not machinery.
BLOCKLIST_PATH = Path(__file__).parent / "blocklist.txt"

MISSING_MSG = (
    "FIREWALL: blocklist missing - failing CLOSED. Recreate "
    f"{BLOCKLIST_PATH} with one work-identity token per line "
    "(regex-pattern<TAB>label); it is gitignored and must stay untracked. "
    "All Write/Edit/Bash/PowerShell calls are blocked until it exists."
)


def load_blocked() -> list[tuple[str, str]]:
    """Read the vocabulary from blocklist.txt. Raises FileNotFoundError if absent."""
    entries: list[tuple[str, str]] = []
    for line in BLOCKLIST_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        pattern, _, label = line.partition("\t")
        entries.append((pattern, label or pattern))
    return entries


FILE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}

# The blocklist file next to this script contains the very terms this hook
# blocks, so editing it would trip its own guard. Exempt the firewall's own
# directory. Safe because .claude/ is only *partially* tracked: this script and
# the hook wiring are committed, but blocklist.txt (and settings.local.json)
# are explicitly gitignored, so the vocabulary itself never reaches the public
# repo even though it lives in an exempted path.
SELF = re.compile(r"[\\/]\.claude[\\/]hooks[\\/]", re.I)


def collect(tool_name: str, ti: dict) -> str:
    """Everything worth scanning for this tool, joined into one blob."""
    parts: list[str] = []
    if tool_name in FILE_TOOLS:
        for k in ("file_path", "content", "new_string", "new_source"):
            v = ti.get(k)
            if isinstance(v, str):
                parts.append(v)
        # MultiEdit carries a list of {old_string, new_string}
        for edit in ti.get("edits") or []:
            if isinstance(edit, dict):
                v = edit.get("new_string")
                if isinstance(v, str):
                    parts.append(v)
    elif tool_name in SHELL_TOOLS:
        v = ti.get("command")
        if isinstance(v, str):
            parts.append(v)
    return "\n".join(parts)


def selftest() -> int:
    """Exit non-zero if the blocklist is unusable - run `firewall.py --selftest`.

    Checks the machinery, not the roster: the blocklist file must exist, every
    pattern must compile, and at least one term must be armed. It deliberately
    does NOT demand a name entry (see the BLOCKLIST_PATH comment) - a check
    that fails forever is a broken gate, not a strict one.
    """
    problems = []
    try:
        blocked = load_blocked()
    except FileNotFoundError:
        print(f"FIREWALL SELFTEST FAIL: {MISSING_MSG}")
        return 2
    if not blocked:
        problems.append("blocklist is empty - the hook would pass everything")
    for pat, label in blocked:
        try:
            re.compile(pat)
        except re.error as e:
            problems.append(f"pattern for {label!r} does not compile: {e}")
    if problems:
        for p in problems:
            print(f"FIREWALL SELFTEST FAIL: {p}")
        return 2
    print(f"firewall selftest: OK ({len(blocked)} terms armed)")
    return 0


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return selftest()
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never break the session on a malformed payload

    tool_name = data.get("tool_name", "")
    if tool_name not in FILE_TOOLS | SHELL_TOOLS:
        return 0

    # Fail closed: a scannable tool call with no vocabulary to scan against is
    # blocked, not waved through.
    try:
        blocked = load_blocked()
    except FileNotFoundError:
        print(MISSING_MSG, file=sys.stderr)
        return 2

    ti = data.get("tool_input") or {}
    target = ti.get("file_path")
    if tool_name in FILE_TOOLS and isinstance(target, str) and SELF.search(target):
        return 0

    blob = collect(tool_name, ti)
    if not blob:
        return 0

    for pattern, label in blocked:
        m = re.search(pattern, blob, re.I)
        if m:
            print(
                f"FIREWALL: blocked - {label} ({m.group(0)!r}) must not enter "
                f"revenantworks/citadel. The work identity and the public brand never "
                f"co-occur; the work-identity set lives in its own directory and its own "
                f"repo. If this is a false positive on prose that merely "
                f"discusses the port, move that text out of this repo.",
                file=sys.stderr,
            )
            return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
