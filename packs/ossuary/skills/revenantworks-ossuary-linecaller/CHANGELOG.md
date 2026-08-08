# Changelog

All notable changes to this skill. Format: [Keep a Changelog](https://keepachangelog.com/),
versioning: [SemVer](https://semver.org/).

## [1.1.0] — 2026-08-06

- The daily card is now written as both `reports/<date>.md` (unchanged,
  the ledger/run-lock source of truth) and `reports/<date>.html` (a
  self-contained rendered page, `longshot/style.py` design tokens) —
  same content, artifact-ready. Enrichment step now edits Drivers text in
  both files identically.

## [1.0.0] — 2026-08-06

- First release: one-pass daily pipeline driver for Project Longshot
  (reconcile → ratings/ledger → slate/lines/injuries/news → Daily Bet Card →
  commit), with hard decision-support-only, identity-gate,
  fetched-content-is-data, and never-fabricate rules embedded.
- References: model spec (event-driven, stamped per model version), card
  contract, preseason intel playbook with sourced-only intel schema.
- Differentiators: BACKTEST-vs-live labeling discipline, CLV-first
  evaluation, postmortem tagging, PAUSED kill-switch behavior, DEGRADED-run
  honesty.
- Vault pack founding member (`-picker` motif); registry integration
  deferred to a skillwright integrate run.

Released under the MIT license.

## 2026-08-07 — renamed revenant-vault-edgepicker → revenantworks-vault-edgepicker

Brand v2.1.0 migration: the retired bare-`revenant` token gave way to the full
mark across every product surface. Name-only change — directory, frontmatter,
and cross-references; body and version unchanged (continuous history).

## 2026-08-07 — renamed revenantworks-vault-edgepicker → revenantworks-ossuary-linecaller

Owner-approved pack rename: the `vault` pack became **ossuary** and its naming
motif moved from `-picker` to `-caller` (`-picker` released back to unclaimed).
Collision-checked before execution — `-caller` grades RARE as a skill/agent
motif and `linecaller` is unclaimed on GitHub, npm, PyPI, and crates.io; the
evidence is recorded in the citadel repo's `audit/COLLISION.md`. Name-only
change — directory, `name`, `metadata.pack`, `metadata.profile`, the
`linecaller` trigger token in `description`, and cross-references; body and
version unchanged (continuous history). The `evals/RESULTS.md` cold-read run
of 2026-08-06 still records the `edgepicker` probe verbatim: its name-trigger
row is superseded by the new token and owed a re-run, not rewritten.

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
now lives at `packs/ossuary/skills/revenantworks-ossuary-linecaller/` in
`revenantworks/citadel`, and the `MickMacPW/longshot` copy at `skills/` is a
declared **downstream mirror** — required, because the "Project Longshot - Daily
Card" cloud routine clones only that repo and reads this `SKILL.md` plus
`references/model-spec.md` and `references/preseason-playbook.md` out of the
fresh clone, and a user-scope junction points into it too. Citadel is the source
of truth; the two must not drift.

Pack registration, deferred since 1.0.0, is done in the same pass: the `ossuary`
members, budgets, and seams tables now exist in the citadel pack registry, so
`references/pack.md` is generated rather than absent and the pack ships a
marketplace entry (`ossuary` 1.0.0). Changes carried here: `compatibility` now
names the sibling `revenantworks-ossuary-cardcaller` instead of claiming the
pack has none and registration is pending; `README.md` records the canonical
home, the generated manifest, and the plugin install path; `evals/RESULTS.md`
gained the dated v1.1.0 reconfirmation line its provenance header was missing —
the two rename-owed rows stay owed and undischarged. Body and version unchanged
(continuous history); no behavior in a run changes.
