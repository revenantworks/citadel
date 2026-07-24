# Trigger Evals — 20 queries (10 should / 10 shouldn't)

Read each cold against name + description only. Provenance: derived from revenant-foundation-evalsmith v1.0.0, 2026-07-14. Re-anchored to v1.1.1, 2026-07-24 (foundation-v1.1.1 hygiene pass; suite content reviewed at the 2026-07-23 6A refresh).

| # | Query | Expected |
|---|---|---|
| 1 | "write trigger evals for my new skill" | SHOULD |
| 2 | "build an assertion suite for this SKILL.md" | SHOULD |
| 3 | "evalsmith audit this suite" | SHOULD |
| 4 | "generate test cases for this prompt card" | SHOULD |
| 5 | "the intro says 18 cases but I count 22 — check my suite" | SHOULD — count integrity |
| 6 | "evalsmith refresh — I just shipped v1.2 of the skill" | SHOULD |
| 7 | "does this agent spec have regression coverage?" | SHOULD |
| 8 | "are my should/shouldn't queries balanced?" | SHOULD |
| 9 | "score my eval coverage" | SHOULD |
| 10 | "evalsmith" | SHOULD — bare invocation |
| 11 | "write unit tests for this Python function" | SHOULD NOT — code tests, engineering tooling |
| 12 | "build me a skill for meal planning" | SHOULD NOT — skillsmith |
| 13 | "fix this prompt, it keeps rambling" | SHOULD NOT — promptsmith |
| 14 | "design a test strategy for our API" | SHOULD NOT — engineering test strategy |
| 15 | "run my test suite and show failures" | SHOULD NOT — execution, not authoring |
| 16 | "evaluate which laptop I should buy" | SHOULD NOT — loresmith |
| 17 | "A/B test my landing page copy" | SHOULD NOT — marketing experimentation |
| 18 | "benchmark Sonnet vs Opus on my workload" | SHOULD NOT — skill-creator / harness tooling |
| 19 | "QA this website for broken links" | SHOULD NOT — web testing tooling |
| 20 | "grade my essay" | SHOULD NOT — content feedback, not suites |

**Edge note.** Sharpest pair: 2 vs 11 — "tests for my skill" routes here, "tests for my function" never does; the description's "for skills, prompts, and agent specs" carries that line. Tuning rule: misses on 1–10 → push the generator triggers; fires on 11–20 → tighten "code unit tests and QA" in the boundary sentence.
