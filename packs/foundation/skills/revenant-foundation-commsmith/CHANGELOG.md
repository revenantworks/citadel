# Changelog

## [1.1.1] - 2026-07-24

foundation-v1.1.1 hygiene release (pack-wide audit; every finding mechanically verified).

- test-cases: Case 20 added covering the self-named sharpest failure mode (render-through-surface-tools) -- previously zero coverage
- evals/fixtures/voice-export.md added: neutral spec-clean voice-profile fixture unblocking Cases 6/7/19 (no brand content, per the brand-carriage law)

## [1.1.0] - 2026-07-23

Brand decoupled (Forge Run 3, Phase 1). Voice ownership moved to brandsmith — the volatile `voices.md` and the `commsmith voice` entry were removed. commsmith now drafts neutral professional by default and applies a specific voice only when named or handed in, consuming brandsmith's exported voice profile. Description updated; channel and message behavior otherwise unchanged. Phase 2 uniformity layer (same version, unreleased): added the `metadata.volatile` block (`channel-profiles.md` event-driven), a matching `## Volatile surfaces` section, a uniform `## Anti-patterns` section, and moved Restraint to the canonical position (after Load budget). Phase 4 (same version, unreleased, U-10): `channel-profiles.md` gained its event-driven header stamp (Last restamped 2026-07-23) so the volatile declaration, the file, and `skillsmith upkeep` all read from one dated surface; the SKILL.md volatile section now points at it. Phase 6 eval refresh (2026-07-23): trigger #7 flipped (voice definition → brandsmith) and #23 added as its application-side pair (23 queries, 11/12); firewall cases re-anchored to handed-in profiles; Case 19 rewritten as definition-routes/application-stays.

## [1.0.0] - 2026-07-14

Citadel launch baseline. Uniform pack reset at the public rebirth of the
foundation pack under `revenantworks/citadel` - every member restamped 1.0.0
for the Citadel 1.0 release. This member was previously at 1.0.0 under the
predecessor repo; that iteration history is retired to the private archive.
Capabilities as shipped are documented in SKILL.md and README.md.

Released under the MIT License. See LICENSE.
