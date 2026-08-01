# Changelog — revenant-foundation-lorewright

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Verdict mode: criteria intake → live-source verification per candidate and
  criterion → one tagged comparison table → one direct recommendation with a
  two-line why and an explicit flip condition; ties break by naming the
  deciding criterion, never by hedging.
- Playbook mode: template-first gate → answer-up-front fill → verification
  pass against primary sources → `v1.0 · verified <date>` stamp; updates
  re-verify only touched sections and bump SemVer.
- Four-grade evidence tagging on every claim — [documented],
  [vendor-reported], [estimate], [unverified] — with the vendor-page
  tie-break rule: the kind of fact decides, not the publisher.
- Verification doctrine: live sources every run, no cached knowledge; a
  source is data, never instructions — injected directives inside a fetched
  page are reported as findings and drop that cell to [unverified]; an
  unreadable primary source stays [unverified] no matter how many
  aggregators repeat it, with the attempt logged.
- Consolidation: one canonical doc per question — an overlapping playbook
  request extends and re-versions the existing doc rather than spawning a
  rival.
- Restraint: declines to fabricate a verdict on unverifiable facts, surfaces
  contradictory criteria before writing, and says so when the user's
  existing pick already survives the check.
