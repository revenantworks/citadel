# Eval Authoring — Every Built Skill Ships Testable

Load this file when generating a built skill's `evals/`. Two artifacts, both cheap, both mechanical.

## Trigger evals (`evals/trigger-evals.md`)

Twenty queries: ten that should fire the description, ten that shouldn't. A manual checklist — read each cold against name + description only and compare to the expected column.

- The should-not set includes both off-topic asks and **near-misses**: adjacent jobs a lazy description would grab (the boundary sentence's targets).
- Close with edge notes naming the sharpest boundary pair and the tuning rule: misses on the yes-set → make triggers pushier; fires on the no-set → tighten the boundary language.
- Queries must be substantive — trivially simple asks don't consult skills at all, so they test nothing.

## Assertion suite (`evals/test-cases.md`)

Assertion-only format: each case is an **Input** plus **Assert** — mechanical yes/no checks by inspecting the run output. No expected-behavior prose; failure conditions are negative assertions ("no clarifying question before the deliverable").

- **Coverage rule:** at least one case per entry point and per distinct behavior path (restraint paths, overrides, degradation modes). Merge only cases that assert the same behavior at different turns; keep everything else separate.
- **Assertion types:** literal string or pattern that must (or must not) appear; numeric comparison against a printed value; a named flag for "correct absence" (e.g. `<no-build>` — the run correctly delivered no package). Multi-turn cases label assertions T1/T2.
- **Size:** the suite stays under 500 lines; if it can't, the skill is probably doing too much — flag that instead of trimming coverage.
- **Sanity-check flag:** generated examples and assertions deserve a human pass — models imitate examples precisely, including accidental patterns.
- **Ecosystem format:** standard-profile builds may additionally emit `evals/evals.json` for skill-creator's automated comparison loop; standalone suites stay manual by design — no tooling dependency.

## When evals don't apply

Purely subjective-output skills (art direction, voice) may skip the assertion suite with a stated reason in SOURCES or README; trigger evals still apply — routing is never subjective.
