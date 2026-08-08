# revenantworks-ossuary-cardcaller

Ossuary pack member #2 (`-caller` motif), whose canonical home is
`revenantworks/citadel` at `packs/ossuary/skills/`. The claude.ai companion to Project
Longshot: reads the Daily Bet Card the cloud routine produces, explains it,
shows bankroll/dashboard status, records what Alex actually bet, and
captures coaching notes that train the model. Decision-support only — the
sibling `revenantworks-ossuary-linecaller` (Claude Code) and the "Longshot Daily
Card" cloud routine own the pipeline itself; this skill never runs it and
never touches a sportsbook.

## Install on claude.ai

Settings → Capabilities → **Skills** → *Create skill* → upload
`revenantworks-ossuary-cardcaller.skill` (or the folder's files). Then use it from
the **Project Longshot** claude.ai Project (whose instructions reference
it), or anywhere by saying "cardcaller".

Requires: the Claude GitHub connector with access to `MickMacPW/longshot`.
Without repo access it degrades honestly — asks for a paste, labels
everything unverified.

## Package

```
revenantworks-ossuary-cardcaller/
├── SKILL.md
├── references/  companion-contract.md (exact write-back shapes) · pack.md
├── evals/trigger-evals.md
├── README.md · CHANGELOG.md · LICENSE
```

`references/pack.md` is generated from the pack registry by `tools/build.py`
in the citadel repo — never hand-edit it.

Changelog: CHANGELOG.md. Pack registration is **done** (2026-08-07), the same
run that relocated both members into citadel: roster, budget, and seam rows are
in the registry and the manifest is derived from them.
