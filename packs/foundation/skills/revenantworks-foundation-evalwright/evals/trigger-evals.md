# Trigger Evals — 20 queries (10 should / 10 shouldn't)

> **Frozen record — the version numbers below are predecessor-era.** They predate
> the 2026-07-31 re-baseline, so those releases, their tags and the commit SHAs
> cited beside them no longer exist; `foundation-v1.1.0` and `foundation-v1.1.1`
> were later reused by unrelated releases (root `CHANGELOG.md`). Entries are left
> verbatim because they record what was true when written — read them by date,
> not by version.

Read each cold against name + description only. Provenance: derived from revenantworks-foundation-evalwright v1.0.0, 2026-07-14. Re-anchored to v1.1.1, 2026-07-24 (foundation-v1.1.1 hygiene pass; suite content reviewed at the 2026-07-23 6A refresh). Re-anchored to v1.1.3, 2026-07-24 (non-production-state enumeration; body-only change, the description is untouched in this pass, so no row moved). Re-anchored to v1.1.4, 2026-07-24 (outcome-set statements reconciled to that enumeration; body-only again, description untouched, no row moved). Re-anchored to v1.1.5, 2026-07-25 (Restraint's flag-vs-shape rule corrected; body-only again, description untouched, no row moved). Re-anchored to v1.1.6, 2026-07-26 (eval-doctrine.md surface-scoping repairs — map completeness, boundary-pairs N/A, refresh-touches, count-integrity scope; reference-file-only change, the description is untouched, no row moved).

| # | Query | Expected |
|---|---|---|
| 1 | "write trigger evals for my new skill" | SHOULD |
| 2 | "build an assertion suite for this SKILL.md" | SHOULD |
| 3 | "evalwright audit this suite" | SHOULD |
| 4 | "generate test cases for this prompt card" | SHOULD |
| 5 | "the intro says 18 cases but I count 22 — check my suite" | SHOULD — count integrity |
| 6 | "evalwright refresh — I just shipped v1.2 of the skill" | SHOULD |
| 7 | "does this agent spec have regression coverage?" | SHOULD |
| 8 | "are my should/shouldn't queries balanced?" | SHOULD |
| 9 | "score my eval coverage" | SHOULD |
| 10 | "evalwright" | SHOULD — bare invocation |
| 11 | "write unit tests for this Python function" | SHOULD NOT — code tests, engineering tooling |
| 12 | "build me a skill for meal planning" | SHOULD NOT — skillwright |
| 13 | "fix this prompt, it keeps rambling" | SHOULD NOT — promptwright |
| 14 | "design a test strategy for our API" | SHOULD NOT — engineering test strategy |
| 15 | "run my test suite and show failures" | SHOULD NOT — execution, not authoring |
| 16 | "evaluate which laptop I should buy" | SHOULD NOT — lorewright |
| 17 | "A/B test my landing page copy" | SHOULD NOT — marketing experimentation |
| 18 | "benchmark Sonnet vs Opus on my workload" | SHOULD NOT — skill-creator / harness tooling |
| 19 | "QA this website for broken links" | SHOULD NOT — web testing tooling |
| 20 | "grade my essay" | SHOULD NOT — content feedback, not suites |

**Edge note.** Sharpest pair: 2 vs 11 — "tests for my skill" routes here, "tests for my function" never does; the description's "for skills, prompts, and agent specs" carries that line. Tuning rule: misses on 1–10 → push the generator triggers; fires on 11–20 → tighten "code unit tests and QA" in the boundary sentence.
