# Changelog

## [1.1.0] - 2026-07-23

Uniformity layer (Forge Run 3, Phase 2). Added the `metadata.volatile` frontmatter block declaring `model-snapshot.md` as a calendar (60-day) surface, and a matching `## Volatile surfaces` section, so `skillsmith upkeep` can sweep it pack-wide. Promoted model-data refresh from a Behavior-notes subsection to a first-class `## Entry — Refresh` (cross-references updated). Added a uniform `## Anti-patterns` section consolidating the skill's own failure modes. No change to the build pipeline, scoring, or output contract. Brand centralization (same version, unreleased): the HTML prompt card now ships fully brand-neutral (a neutral "Prompt Card" label, no baked-in wordmark or `<title>`); the revenant identity is applied via `brandsmith apply`. Phase 3 (same version, unreleased): added `## Entry — Model` — a standalone tier + model recommendation for a live task (no prompt built), reusing the Phase 5 tier taxonomy (durable) with names from the snapshot; `promptsmith model` added to the bare-invocation and README. Phase 4 (same version, unreleased): `model-snapshot.md` regenerated with a genuine lineup re-research, restamped 2026-07-23 — Claude column confirmed (Fable 5 / Opus 4.8 / Sonnet 5 / Haiku 4.5; Sonnet 5 intro pricing to 08-31); OpenAI moved to the GPT-5.6 family (Sol/Terra/Luna, GA 07-09); Gemini 3.6 Flash + 3.5 Flash-Lite added (07-21) with 3.5 Pro flagged partner-only (never recommend); Grok 4.5 added (07-08, 500K-context caveat); DeepSeek V4-Flash added and the V4 Pro promo expiry recorded. Stale refresh-procedure pointer fixed to Entry — Refresh. Phase 6 eval refresh (2026-07-23): trigger #25 added for Entry — Model (25 queries, 12/13) with the prompt-in-play edge note corrected; Case 29 added asserting the standalone recommendation contract (no prompt, flip condition, snapshot-sourced name, loresmith boundary).

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
