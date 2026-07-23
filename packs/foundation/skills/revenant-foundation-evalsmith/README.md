# revenant-foundation-evalsmith

Authors and audits eval suites for skills, prompts, and agent specs — a build-time generator, never a runtime dependency. What separates it from benchmark harnesses and QA tooling: what it writes stays **inside the target** as self-contained manual checklists a reader can run cold, with no evalsmith, script, or harness present. Derives what a target claims to do, then writes the suite that proves it — or scores the suite it already has. Zero scripts, so it behaves identically on claude.ai, Claude Code, and the API.

**Workflow:** Intake → Read target → Coverage map → Generate / Score / Refresh → Handback

## Package contents

```
revenant-foundation-evalsmith/
├── SKILL.md                      # entry point — three entries, coverage map, zero-dep law
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── eval-doctrine.md          # coverage maps, mechanics, count integrity, audit scoring
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── test-cases.md             # assertion-only suite
    └── trigger-evals.md          # should/shouldn't queries
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by asking to write trigger evals, test cases, or an assertion suite, or by saying `evalsmith` (subcommands: `evalsmith audit`, `evalsmith refresh`).

## Entry points

| Entry | What it does |
|---|---|
| **generate** | A target → coverage map → trigger evals + assertion suite, gated once, for the target's `evals/` folder |
| **audit** | "evalsmith audit" at an existing suite → five-check scoreline (coverage, boundary pairs, assertion mechanics, count integrity, self-containment) + finding catalog with exact fixes |
| **refresh** | "evalsmith refresh" after the target changed → diff-scoped regeneration (only touched cases, retired paths named), counts re-verified |

## Commands & switches

| Invocation | What it does |
|---|---|
| `evalsmith` | Bare invocation — one-line intro + what it needs |
| `evalsmith audit` | Score an existing suite (or a target whose suite should be checked) |
| `evalsmith refresh` | Re-derive after the tested target changed |

| In-request switch | Effect |
|---|---|
| "apply all" / "just write it" | Skips the single gate |
| a subjective-output target | Trigger evals still apply; the assertion suite is skipped with a stated reason (`<no-suite>`) |

## Staying current

No volatile surface (`metadata.volatile: []`). evalsmith stores no baseline of its own — `evalsmith refresh` fires when the *target* it tested changes (event-driven), not when an internal baseline ages, so nothing here goes stale on a clock and `skillsmith upkeep` skips it.

## Changelog

See [CHANGELOG.md](CHANGELOG.md). Provenance: foundation skill #7 — built with the zero-runtime-dependency law as the build condition.
