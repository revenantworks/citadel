# revenantworks-ossuary-bonecaller

Ossuary pack member #2 (`-caller` motif), whose canonical home is
`revenantworks/claude-skills` at `packs/ossuary/skills/`. The claude.ai companion to Project
Longshot: reads the Daily Bet Card the cloud routine produces, explains it,
shows bankroll/dashboard status, records what the owner actually bet,
captures coaching notes that train the model, and explains both pause
switches without touching either. Decision-support only — the
sibling `revenantworks-ossuary-linecaller` (Claude Code) and the "Project
Longshot - Daily Card" cloud routine own the pipeline itself; this skill never runs it and
never touches a sportsbook.

Renamed from `revenantworks-ossuary-cardcaller` on 2026-08-08 — same member,
continuous history; see CHANGELOG.md.

## Install on claude.ai

Settings → Capabilities → **Skills** → *Create skill* → upload the member
zip (`revenantworks-ossuary-bonecaller-<version>.zip` from the claude-skills
build or Releases). Then use it from the **Project Longshot** claude.ai
Project (whose instructions reference it), or anywhere by saying
"bonecaller". Updating is delete-then-re-upload.

On the owner's rig a user-scope junction at
`~/.claude/skills/revenantworks-ossuary-bonecaller` points at this folder
in the claude-skills working repo, so a Claude Code session loads it too.

Reads today's card from its fixed artifact page first
(`https://claude.ai/code/artifact/69eb441f-f2ea-4736-a294-d7d4e9a41881`),
then the repo. Requires: the Claude GitHub connector with access to
`MickMacPW/longshot`. Without either it degrades honestly — asks for a
paste, labels everything unverified.

## Package

```
revenantworks-ossuary-bonecaller/
├── SKILL.md
├── references/  companion-contract.md (exact write-back shapes) · pack.md
├── evals/  trigger-evals.md · test-cases.md · RESULTS.md
├── README.md · CHANGELOG.md · SOURCES.md · LICENSE
```

`references/pack.md` is generated from the pack registry by `tools/build.py`
in the claude-skills repo — never hand-edit it.

Changelog: CHANGELOG.md. Pack registration is **done** (2026-08-07), the same
run that relocated both members into this repo (then named citadel): roster,
budget, and seam rows are in the registry and the manifest is derived from
them.
