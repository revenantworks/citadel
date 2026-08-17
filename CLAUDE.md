# CLAUDE.md — claude-skills

The canonical home of every Revenantworks Agent Skill (repository
`revenantworks/claude-skills`; renamed from `citadel` 2026-08-17). Two packs under
`packs/` — **foundation** (nine `-wright` members) and **ossuary** (two
`-caller` members) — each with its own router `CLAUDE.md` that loads when you
work under that pack. This root file exists because the repo's top level,
`tools/`, and `audit/` previously loaded no standing context at all (audit
finding `citadel-no-root-claude-md`, 2026-08-15).

## Layout

- `packs/<pack>/skills/<member>/` — SKILL.md + references + evals; the pack's
  `.claude-plugin/plugin.json` carries the pack version, which must equal its
  entry in `.claude-plugin/marketplace.json` (the build check enforces it)
- `tools/` — `build.py` and its tests; `audit/` — COLLISION.md and audit records
- `RUNBOOK.md` · `NEXT.md` · `CHANGELOG.md` — operations, backlog, history

## Commands

```bash
python tools/build.py --check      # read-only gate: versions, counts, seams
python tools/build.py --parity     # read-only: installed-copy parity
python -m unittest discover -s tools -p "test_*.py"
python tools/build.py              # REAL build — regenerates references/pack.md manifests
```

(`python` on the rig, `python3` on Linux clones. A bare `build.py` and
`--footprint` can WRITE manifest drift — the read-only pair above is what
report-only passes are allowed to run.)

## The one arming step

The brand firewall (`.claude/hooks/firewall.py`, PreToolUse) **fails closed**:
with its gitignored `blocklist.txt` absent, every Write/Edit/Bash/PowerShell
call is blocked. On a fresh clone, recreate `.claude/hooks/blocklist.txt`
(one `regex-pattern<TAB>label` per line, work-identity tokens only — never a
name), then verify: `python .claude/hooks/firewall.py --selftest`.

## Hard rules

- **This repo is public and ships neutral.** No brand styling content here —
  the definition lives in the private brand repo and overlays at package time.
  No personal, employer, or client name, ever; the firewall's blocklist is the
  machine layer for the work-identity tokens, judgment holds the rest.
- **Edit here, then re-sync the longshot mirror** (`longshot/skills/` holds
  verbatim copies of both ossuary members; `diff -r` must stay empty). A member
  change ships to installs only via a PACK version bump — the pack version is
  the plugin cache key, so a member-only bump never ships.
- After a release: `claude plugin marketplace update revenantworks` then
  `claude plugin update <pack>@revenantworks` on the rig, and re-upload any
  installed claude.ai copies. Both surfaces, every time.
