# Changelog

## [1.1.1] - 2026-07-24

foundation-v1.1.1 hygiene release (pack-wide audit; every finding mechanically verified).

- SOURCES.md: removed the 'no stamped volatile file ships' line (contradicted the shipped calendar-class platform-notes.md since U-9); platform-notes statistics now carry source attributions or a vendor-reported marker
- evals: provenance re-anchored (derivation history preserved)

## [1.1.0] - 2026-07-23

Uniformity layer (Forge Run 3, Phase 2). Added a `metadata.volatile: []` frontmatter block and a matching `## Volatile surfaces` section declaring agentsmith carries no calendar baseline (durable doctrine), so `skillsmith upkeep` skips it correctly. Moved the Restraint section to the canonical position (after Load budget, before the entries) and added a uniform `## Anti-patterns` section. No change to the design checklist, trust-tier rule, or scoring. Phase 4 (same version, unreleased, U-9): new stamped baseline `references/platform-notes.md` (verified 2026-07-23) — what current platforms provide to enforce the checklist: Claude Code's three-gate model (permissions / sandbox / hooks, with the hook-as-attack-surface CVEs recorded), Cowork's native scheduler cadences, the OpenAI Agents SDK guardrail/approval primitives (Agent Builder EOL noted), MCP allowlisting, layered kill-switch doctrine per 2026 CISA/NSA guidance, and the injection state of the art — plus a checklist-area → platform-mechanism map. `metadata.volatile` upgraded from `[]` to a calendar (60-day) entry, the Volatile surfaces section rewritten to match, and a new `## Entry — Refresh` ("agentsmith refresh") added with README and description updates. Phase 6 eval refresh (2026-07-23): trigger #23 added for Entry — Refresh (23 queries, 12/11); Case 16 added asserting refresh scope (platform-notes only; checklist untouched).

## [1.0.0] - 2026-07-14

Citadel launch baseline. Uniform pack reset at the public rebirth of the
foundation pack under `revenantworks/citadel` - every member restamped 1.0.0
for the Citadel 1.0 release. This member was previously at 1.0.0 under the
predecessor repo; that iteration history is retired to the private archive.
Capabilities as shipped are documented in SKILL.md and README.md.

Released under the MIT License. See LICENSE.
