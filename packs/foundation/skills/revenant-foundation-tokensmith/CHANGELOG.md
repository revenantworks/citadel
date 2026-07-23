# Changelog

## [1.1.0] - 2026-07-23

Uniformity layer (Forge Run 3, Phase 2). Added the `metadata.volatile` block declaring `measurement.md` as a calendar (60-day) surface, and a matching `## Volatile surfaces` section, so `skillsmith upkeep` can sweep it pack-wide. Moved Restraint to the canonical position (after Load budget) and added a uniform `## Anti-patterns` section. No change to slim/audit/budget/refresh modes, the waste taxonomy, or the measurement doctrine. Brand centralization (same version, unreleased): removed the per-run `brand:` report-flavor switch — reports, sheets, and rewrites always ship neutral; brand is applied via `brandsmith apply`. Phase 3 (same version, unreleased, 5E): model-tier questions now route to promptsmith `Entry — Model` specifically, with a durable tier→cost note — tokensmith reasons in tiers (frontier > flagship > balanced > fast) and never names a specific model. Phase 4 (same version, unreleased): `measurement.md` re-verified and restamped 2026-07-23 — Anthropic cache mechanics sharpened (≤4 breakpoints; 1.25×/2× writes for 5-min/1-hr TTL; 0.10× reads; TTL refresh-on-read; reads excluded from input rate limits); the stale OpenAI ~50% cached-read figure corrected to ~0.10× on current families (5.4 onward) with GPT-5.6's 1.25× cache-write billing and 30-minute minimum noted; skill-metadata discovery cost sharpened to a measured median ~80 tokens/skill (range ~55–235). Phase 6 eval refresh (2026-07-23): Case 15 rewritten — outputs are always neutral and a brand request routes to `brandsmith apply`; the retired per-run `brand:` switch removed from the suite.

## [1.0.0] - 2026-07-14

Citadel launch baseline. Uniform pack reset at the public rebirth of the
foundation pack under `revenantworks/citadel` - every member restamped 1.0.0
for the Citadel 1.0 release. This member was previously at 1.0.0 under the
predecessor repo; that iteration history is retired to the private archive.
Capabilities as shipped are documented in SKILL.md and README.md.

Released under the MIT License. See LICENSE.
