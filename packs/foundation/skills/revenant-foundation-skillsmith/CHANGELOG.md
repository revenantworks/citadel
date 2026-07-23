# Changelog

## [1.1.0] - 2026-07-23

Brand decoupled (Forge Run 3, Phase 1). skillsmith now builds spec-clean neutral and stamps only structural identity; the `configure` entry and the brand cascade were removed — brand definition, voice, and application are brandsmith's, applied on invoke. Registry split: the structural roster moved from the retired `brand-config.md` to the new `pack-registry.md` (build.py derives manifests from there); the cascade doctrine `brand-inheritance.md` moved to brandsmith as `application-doctrine.md`. Packaging reworked native-first (validate by inspection; shell only for multi-file archives). Description updated to match; routing boundary preserved. Phase 2 uniformity layer (same version, unreleased): added the `metadata.volatile` frontmatter block (`rubrics.md` calendar/60-day + `pack-registry.md` event-driven), a matching `## Volatile surfaces` section, and a uniform `## Anti-patterns` section. Brand centralization (same version, unreleased): removed a stale brand-cascade reference in `build-templates.md` — builds are neutral and brandsmith brands on invoke. Phase 3 (same version, unreleased): added `## Entry — Upkeep` — a pack-wide staleness sweep that reads every member's `metadata.volatile`, reports each calendar surface's status against its cadence (report-only by default), and on approval runs the mapped refresh verb per overdue surface (rubrics → skillsmith refresh · model-snapshot → promptsmith refresh · measurement → tokensmith refresh), degrading by environment. New reference `upkeep-doctrine.md`; `upkeep` added to the description and bare-invocation. Phase 4 (same version, unreleased): `rubrics.md` baseline re-verified and restamped 2026-07-23 — the Agent Skills format is stable (agentskills.io canonical; anthropics/skills now carries an explicit spec pointer file; adopted beyond Anthropic by Codex and Copilot); ClawHub added alongside Skillstore as a cited-not-yet-verified niche-source candidate (~490K-skill ecosystem). Phase 4C: `upkeep-doctrine.md`'s verb map and example gained agentsmith's new calendar surface (`platform-notes.md` → `agentsmith refresh`).

## [1.0.1] - 2026-07-14

Registry notes in references/brand-config.md updated to the completed-relocation
state (org live, prior copy archived private), and the load-budget line for evals/
reworded to "maintenance archive — never loaded at runtime" — the pack's
registered packaging default ships full folder-zips including evals/, so the
prior "not in installs" claim was inaccurate. Post-launch pack audit, finding
P2-1 + P2-2; behavior unchanged.

## [1.0.0] - 2026-07-14

Citadel launch baseline. Uniform pack reset at the public rebirth of the
foundation pack under `revenantworks/citadel` - every member restamped 1.0.0
for the Citadel 1.0 release. This member was previously at 1.0.0 under the
predecessor repo; that iteration history is retired to the private archive.
Capabilities as shipped are documented in SKILL.md and README.md.

Released under the MIT License. See LICENSE.
