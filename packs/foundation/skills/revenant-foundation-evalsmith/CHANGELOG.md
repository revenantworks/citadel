# Changelog

## [1.1.1] - 2026-07-24

foundation-v1.1.1 hygiene release (pack-wide audit; every finding mechanically verified).

- description: grammar fix ('...and are run by hand without evalsmith present')
- eval-doctrine: provenance-restamp-on-version-bump rule added (the defect class this skill audits others for was live in its own suite)
- evals: provenance re-anchored

## [1.1.0] - 2026-07-23

Uniformity layer (Forge Run 3, Phase 2). Added a `metadata.volatile: []` block and a matching `## Volatile surfaces` section declaring evalsmith carries no calendar baseline — its refresh is target-triggered (event-driven), not clock-driven — so `skillsmith upkeep` skips it. Moved Restraint to the canonical position (after Load budget) and added a uniform `## Anti-patterns` section. No change to generate/audit/refresh modes, the coverage map, or the zero-runtime-dependency law.

## [1.0.0] - 2026-07-14

Citadel launch baseline. Uniform pack reset at the public rebirth of the
foundation pack under `revenantworks/citadel` - every member restamped 1.0.0
for the Citadel 1.0 release. This member was previously at 1.0.0 under the
predecessor repo; that iteration history is retired to the private archive.
Capabilities as shipped are documented in SKILL.md and README.md.

Released under the MIT License. See LICENSE.
