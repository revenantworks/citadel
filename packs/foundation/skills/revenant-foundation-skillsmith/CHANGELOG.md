# Changelog

## [1.1.0] - 2026-07-23

Brand decoupled (Forge Run 3, Phase 1). skillsmith now builds spec-clean neutral and stamps only structural identity; the `configure` entry and the brand cascade were removed — brand definition, voice, and application are brandsmith's, applied on invoke. Registry split: the structural roster moved from the retired `brand-config.md` to the new `pack-registry.md` (build.py derives manifests from there); the cascade doctrine `brand-inheritance.md` moved to brandsmith as `application-doctrine.md`. Packaging reworked native-first (validate by inspection; shell only for multi-file archives). Description updated to match; routing boundary preserved.

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
