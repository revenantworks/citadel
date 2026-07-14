# revenant-foundation-evalsmith

Authors and audits eval suites for skills, prompts, and agent specs — a build-time generator, never a runtime dependency. What it writes stays inside the target: self-contained manual checklists a reader can run cold.

## Commands

| Say | Get |
|---|---|
| "write trigger evals / test cases for <target>" | Coverage map → trigger evals + assertion suite, gated once |
| "evalsmith audit" (+ a suite or target) | Five-check scoreline + finding catalog with exact fixes |
| "evalsmith refresh" (after the target changed) | Diff-scoped regeneration, counts re-verified |
| "evalsmith" | One-line intro + what it needs |

## The law

Generated suites are data, not calls — no step in them may require evalsmith, a script, or a harness. Self-containment is the first thing its own audits check.

## Package

    revenant-foundation-evalsmith/
    ├── SKILL.md
    ├── README.md · CHANGELOG.md · SOURCES.md · LICENSE
    ├── references/
    │   ├── eval-doctrine.md          # coverage maps, mechanics, count integrity, audit scoring
    │   └── pack.md                   # foundation roster (advisory)
    └── evals/                        # version-control archive; excluded from .skill payloads
        ├── test-cases.md             # 13-case assertion-only suite
        └── trigger-evals.md          # 20 should/shouldn't queries

## Versioning

Semver; history in CHANGELOG.md. Provenance: built 2026-07-13 under an owner override of the roadmap's §2.6 extraction trigger, with the zero-runtime-dependency law as the build condition.

MIT — see LICENSE.
