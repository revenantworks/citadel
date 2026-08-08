# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/), versioning: [SemVer](https://semver.org/).

## [1.1.0] — 2026-08-06

- Card reading now fetches `reports/<date>.html` and shows it as a live
  Artifact (pastes the HTML into a fenced ```html block so claude.ai
  renders it in the side panel) instead of relaying markdown text.

## [1.0.0] — 2026-08-06

- First release: claude.ai companion for Project Longshot — card reading,
  bankroll/dashboard status, placed-bet logging (`placed`/`placed_stake`),
  coaching-note capture, pause/resume guidance.
- Differentiators: hard decision-support-only and never-fabricate rules,
  BACKTEST-label preservation, honest degradation to copy-paste blocks when
  no GitHub write path exists.
- Vault pack member #2 (`-picker` motif), companion to
  revenantworks-vault-edgepicker; registry integration deferred.

Released under the MIT license.

## 2026-08-07 — renamed revenant-vault-bookpicker → revenantworks-vault-bookpicker

Brand v2.1.0 migration: the retired bare-`revenant` token gave way to the full
mark across every product surface. Name-only change — directory, frontmatter,
and cross-references; body and version unchanged (continuous history).

## 2026-08-07 — renamed revenantworks-vault-bookpicker → revenantworks-ossuary-cardcaller

Owner-approved pack rename: the `vault` pack became **ossuary** and its naming
motif moved from `-picker` to `-caller` (`-picker` released back to unclaimed).
Collision-checked before execution — `-caller` grades RARE as a skill/agent
motif and `cardcaller` is unclaimed on npm, PyPI, and crates.io with a single
0★ GitHub namesake; the evidence is recorded in the citadel repo's
`audit/COLLISION.md`. Name-only change — directory, `name`, `metadata.pack`,
`metadata.profile`, the `cardcaller` trigger token in `description`, and
cross-references; body and version unchanged (continuous history).

## 2026-08-07 — corrected `metadata.brand` to `revenantworks`

The v2.1.0 migration above renamed the directory, `name`, and cross-references
but left `metadata.brand` on the retired bare-`revenant` token. Corrected
against the skillwright pack registry's Build defaults row (the brand token
that stamps `metadata.brand` is `revenantworks`) and the brand definition,
where `revenant` is reserved for sub-brand carriage and the community layer
and is explicitly **not** the house mark. Metadata-only change — one
frontmatter field; body and version unchanged (continuous history).

## 2026-08-07 — relocated to `revenantworks/citadel`; pack registration completed

Owner decision: the citadel is the canonical home for every skill. This member
now lives at `packs/ossuary/skills/revenantworks-ossuary-cardcaller/` in
`revenantworks/citadel`; the `MickMacPW/longshot` copy at `skills/` is a
declared downstream mirror kept for the sibling's cloud-routine clone, and is
never the source of truth.

Pack registration, deferred since 1.0.0, is done in the same pass: the `ossuary`
members, budgets, and seams tables now exist in the citadel pack registry, so
`references/pack.md` is generated rather than absent, the one boundary pair
(linecaller ↔ cardcaller) is declared — recorded as carried on this member's
description only, with the cold re-judge owed — and the pack ships a marketplace
entry (`ossuary` 1.0.0). `README.md` updated for the canonical home and the
generated manifest. Body, `description`, and version unchanged (continuous
history).
