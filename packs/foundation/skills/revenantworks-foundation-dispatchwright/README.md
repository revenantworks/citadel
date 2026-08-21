# revenantworks-foundation-dispatchwright

Runs a session's fan-out. Turns one large request — a rebuild, a re-architecture, a sweep
across many repos or skills — into units small enough to finish, tiers each one through
promptwright, dispatches it with a durability contract, and reconciles the result against the
repo itself, never against an agent's own report.

What separates it from ad hoc multi-agent orchestration:

- **It never picks a model.** Every unit's tier, model, and effort come from promptwright's
  Entry — Model plan grain, copied into the ledger verbatim.
- **Every unit is done when it is on the remote, not when it is written.** Commit and push are
  one atomic call, pushed after every finished piece of work, never held to the end.
- **A ledger row, not a report, is the record.** Reconcile checks every row against
  `git rev-parse origin/main`; a unit's own account of what it did is never the proof.
- **Resume never redoes landed work.** The first action on picking up a dead or stalled run is
  reading origin and the ledger — before anything else.
- **Waves are capped.** Six concurrent units, two nesting levels, a worktree for every writer, a
  stagger across launch, and a check of the remaining usage window before a top-tier wave.

**Workflow:** Shape check → Decompose → Tier → Durability contract → Wave execution → Escalation
→ Reconcile

## Package contents

```
revenantworks-foundation-dispatchwright/
├── SKILL.md                      # entry point — scope, shape check, decompose, tier, durability
│                                  # contract, wave execution, escalation, reconcile, anti-patterns
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── ledger-schema.md          # the run ledger's fields, a worked row, and where it lives
│   ├── unit-brief-template.md    # the copy-paste brief every dispatched unit carries
│   └── anti-patterns.md          # the 13 failure modes, one line each, with the 2026-08-17 examples
└── evals/                        # in full folder-zips, excluded from .skill
    ├── trigger-evals.md          # 10 should-fire, 10 should-not, 2 injection probes
    └── RESULTS.md                # authored-not-run ledger — what running the suite still owes
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your
skills directory, or upload the archive in Claude settings. Trigger it by saying `dispatchwright`,
by describing a request that spans many agents, repos, skills, or files at once, or by naming a
stalled fan-out that needs to resume without redoing landed work. Self-contained: no executable
code ships. `git` and the surface's subagent/Task tools are optional — without `git` a run still
plans, tiers and dispatches but reports an unverifiable row as unverified rather than done;
without subagent tools a run ends at the tiered plan and the ledger.

The two forcing hooks are not package contents. They are rig infrastructure, kept in the
`claude-skills` repo under `.claude/hooks/` and installed from there into `~/.claude/hooks/` by a
rig that wants them. Nothing below depends on them.

## Entry points

| Entry | What it does |
|---|---|
| **plan** | Runs Shape check first — says so and stops if the request isn't a real fan-out. Otherwise decomposes, tiers via promptwright, writes the ledger, and presents the wave plan once, gated |
| **dispatch** | An approved plan → a ledger row per unit before launch, then the wave runs per the wave-execution caps |
| **resume** | A dead, stalled, or usage-limited run → reads origin and the ledger first, re-dispatches only what is unfinished or unverified |
| **audit** | Reconciles a running or finished run against `git rev-parse origin/main`; read-only, reports and never re-dispatches on its own |

## The three seams

- **Tiering is promptwright's.** dispatchwright hands promptwright the unit list and copies back
  the target table; it never invents a tier.
- **Where the trigger lives is rigwright's.** The hook or CLAUDE.md rule that makes a big request
  reach for dispatchwright is rigwright's placement call.
- **Unattended runs are agentwright's, whole.** A cron job or anything firing with nobody reading
  the result is out of scope here.

## Durability contract, in one line

Atomic commit+push, pushed after every finished piece of work and before any report, a ledger row
at dispatch/commit/push, and `git log --oneline origin/main -5` plus the ledger as resume's first
action — never the last.

## What did not land at 1.0.0

- ~~No routing-seam row.~~ **Closed at 1.0.1 (2026-08-18).** `pack-registry.md`'s seam table now
  carries dispatchwright ↔ promptwright, ↔ rigwright, and ↔ agentwright, riding the generated
  table the way an established pack member's do. All three are recorded as one-sided, uncontested
  edges — none of the three siblings' descriptions name dispatchwright back — which is the
  accurate state, not a placeholder for a future negotiation.
- **No assertion suite.** `evals/` ships trigger evals only; a mechanical `test-cases.md` proving
  the durability contract and Reconcile behavior under a live dispatch is owed.
- **No cold-listing judge.** `evals/RESULTS.md` records the trigger suite as authored, not run.

## What landed at 1.0.1

- **Shipped hooks synced to the fixed live originals.** `references/hooks/dispatch_gate.py` and
  `dispatch_ledger_guard.py` had drifted to the pre-fix, fail-open versions while the installed
  hooks at `~/.claude/hooks/` were repaired (D1-D4, see CHANGELOG.md). Both files are now byte-for-
  byte the fixed versions, and both selftests pass against the copies shipped here.

## What landed at 1.2.0

- **The forcing hooks left the package; the profile went back to standalone.** `dispatch_gate.py`,
  `dispatch_ledger_guard.py` and `dispatch_patterns.txt` moved to the `claude-skills` repo's own
  `.claude/hooks/`. No line of either script changed and both selftests pass from the new
  location. With no executable code shipped, and `git` and subagent tools restated as optional
  with their degradation named, `profile: standalone` is true again — earned by the change, not
  by the label.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
