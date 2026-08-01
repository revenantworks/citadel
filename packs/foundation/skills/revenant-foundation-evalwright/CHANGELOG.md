# Changelog — revenant-foundation-evalwright

## [1.0.1] — 2026-08-01

Frozen-record marker added to the `evals/` files that cite predecessor-era
version numbers. Those designations predate the 2026-07-31 re-baseline, and
two of the tag names were later reused by unrelated releases, so a reader
could take a historical entry for a current one. The rows, verdicts, dates
and counts are untouched — only a header marker was added, so nothing about
what was executed or when has moved.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Derives a coverage map from the target — a skill or SKILL.md, a prompt
  card, or an agent spec: entry points from the description, behavior paths
  (restraint, overrides, degradation, multi-turn) from the body.
- Generates two artifacts: the should/shouldn't trigger-eval table with
  near-misses, edge note, and tuning rule, and the assertion suite with
  negative assertions first-class.
- Count integrity: stated case counts must exactly match the actual case
  count and the re-derived coverage-map row count.
- Zero-runtime-dependency law: every generated suite runs cold by hand — no
  tooling, no harness — and the skill's own audits check that first.
- Audit scores 1–10 across five checks — coverage, boundary pairs, assertion
  mechanics, count integrity, self-containment — with a stated N/A rule when
  no trigger set is supplied; refresh is diff-scoped, regenerating only
  touched cases and re-verifying counts.
- Six-state restraint table with explicit flags; no volatile surfaces —
  refresh is event-driven by target change, so pack upkeep sweeps correctly
  skip it.
