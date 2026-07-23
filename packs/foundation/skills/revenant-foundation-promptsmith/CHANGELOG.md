# Changelog

## [1.1.0] - 2026-07-23

Uniformity layer (Forge Run 3, Phase 2). Added the `metadata.volatile` frontmatter block declaring `model-snapshot.md` as a calendar (60-day) surface, and a matching `## Volatile surfaces` section, so `skillsmith upkeep` can sweep it pack-wide. Promoted model-data refresh from a Behavior-notes subsection to a first-class `## Entry — Refresh` (cross-references updated). Added a uniform `## Anti-patterns` section consolidating the skill's own failure modes. No change to the build pipeline, scoring, or output contract. Brand centralization (same version, unreleased): the HTML prompt card now ships fully brand-neutral (a neutral "Prompt Card" label, no baked-in wordmark or `<title>`); the revenant identity is applied via `brandsmith apply`. Phase 3 (same version, unreleased): added `## Entry — Model` — a standalone tier + model recommendation for a live task (no prompt built), reusing the Phase 5 tier taxonomy (durable) with names from the snapshot; `promptsmith model` added to the bare-invocation and README.

## [1.0.1] - 2026-07-14

The load-budget line for evals/
reworded to "maintenance archive — never loaded at runtime" — the pack's
registered packaging default ships full folder-zips including evals/, so the
prior "not in installs" claim was inaccurate. Post-launch pack audit, finding
P2-2; behavior unchanged.

## [1.0.0] - 2026-07-14

Citadel launch baseline. Uniform pack reset at the public rebirth of the
foundation pack under `revenantworks/citadel` - every member restamped 1.0.0
for the Citadel 1.0 release. This member was previously at 1.0.0 under the
predecessor repo; that iteration history is retired to the private archive.
Capabilities as shipped are documented in SKILL.md and README.md.

Released under the MIT License. See LICENSE.
