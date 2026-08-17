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

The production runner is the "Project Longshot - Daily Card" cloud routine.
It clones the longshot repo and reads this skill out of that repo's
`skills/` mirror, so nothing is installed for it.

Owner's rig, user scope: `scripts/install-skill.ps1` in the longshot repo
junctions **that repo's mirror copy** of this folder to
`~/.claude/skills/revenantworks-ossuary-linecaller`, so a local session
loads the same copy the routine reads. Requires: the longshot repo + its
`.venv`, git, and `gh` authenticated as MickMacPW.

Public marketplace (anyone else): `/plugin marketplace add
revenantworks/claude-skills` then `/plugin install ossuary@revenantworks` —
without the private repo the skill correctly refuses to invent anything.

## Invocations

| Trigger | Behavior |
|---|---|
| "run the daily card" / "build today's card" / "daily bet card" / "linecaller" | full daily run |
| the cloud routine, daily 13:00 UTC (a fresh clone, `python3`) | same, unattended; publishes the card to its fixed artifact page |
| `PAUSED` file at repo root | reconcile-only, then stop |

Reading an existing card, "today's bets", and ledger/bankroll questions
belong to the claude.ai companion `revenantworks-ossuary-bonecaller`.

## Staying current

`references/model-spec.md` is event-driven — re-read after any
`model_version` bump. Pack registration is **done** (2026-08-07): the roster,
budget, and seam rows live in the claude-skills registry and `references/pack.md` is
generated from them. Changelog: CHANGELOG.md.
