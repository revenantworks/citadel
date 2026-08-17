# revenantworks-ossuary-linecaller

First member of the **ossuary** pack (`-caller` motif), whose canonical home is
`revenantworks/claude-skills` at `packs/ossuary/skills/`. Runs one pass of the
Project Longshot daily NFL bet-card pipeline: reconcile → ratings/ledger →
slate + lines + injuries + playing-time news → Daily Bet Card → commit.
What separates it from a generic "sports betting helper": it drives one
specific, transparent, backtested model in the longshot repo, tracks its own
accuracy honestly (BACKTEST labels, CLV-first evaluation, postmortem tags),
and is decision-support-only by hard rule — it never touches a sportsbook.

## Package

```
revenantworks-ossuary-linecaller/
├── SKILL.md
├── references/  model-spec.md · card-contract.md · preseason-playbook.md · pack.md
├── evals/       trigger-evals.md · test-cases.md · RESULTS.md
├── README.md · CHANGELOG.md · SOURCES.md · LICENSE
```

`references/pack.md` is generated from the pack registry by `tools/build.py`
in the claude-skills repo — never hand-edit it.

## Install

Whole pack, from this repo's own marketplace:

```
/plugin marketplace add revenantworks/claude-skills
/plugin install ossuary@revenantworks
```

User scope, this machine: `scripts/install-skill.ps1` in the longshot repo
junctions **that repo's mirror copy** of this folder to
`%USERPROFILE%\.claude\skills\revenantworks-ossuary-linecaller`, so the daily
runner keeps working from a single fresh clone. Requires: the longshot repo +
its `.venv`, git, and `gh` authenticated as MickMacPW.

## Invocations

| Trigger | Behavior |
|---|---|
| "daily bet card" / "today's bets" / "linecaller" | full daily run |
| scheduled 9:00 AM ET run (Task Scheduler → `claude -p`) | same, headless |
| `PAUSED` file at repo root | reconcile-only, then stop |

## Staying current

`references/model-spec.md` is event-driven — re-read after any
`model_version` bump. Pack registration is **done** (2026-08-07): the roster,
budget, and seam rows live in the claude-skills registry and `references/pack.md` is
generated from them. Changelog: CHANGELOG.md.
