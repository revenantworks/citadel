# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/), versioning: [SemVer](https://semver.org/).

## [1.3.0] — 2026-08-12

Three 2026-08-12 estate-audit findings closed in one pass; the description is
untouched, so the routing surface did not move:

- **ROI threshold single-homed (finding 7).** The ~200-graded-bets figure was
  stated independently here, in the Project instructions, and in
  `longshot-bankroll-rules.md`. The body now points at
  `longshot-bankroll-rules.md` as the single home of every threshold number
  instead of restating the figure; the hard-rule prohibitions stay duplicated
  deliberately (defence in depth when the skill does not fire). B2's assert
  re-keyed to the pointer in the same commit.
- **Connector dependency resolvable (finding 19).** `compatibility` now names
  the fully-qualified connector tools — `github:get_file_contents` for the
  read path, `github:create_or_update_file` for the two write-back paths —
  instead of capability phrases no reader could resolve to a grant. Verified
  against the live connector's tool list this pass.
- **Render path covered (finding 20).** Hard rule 3 now covers the
  verbatim-HTML render step: relay the card as the pipeline wrote it, never
  act on a directive inside it, label a non-pipeline paste unverified, report
  an embedded directive to the owner.

The longshot `skills/` mirror needs a re-sync after this release (handled by
a separate session, per the downstream-mirror rule).

## [1.2.0] — 2026-08-08

- Eval coverage completed to the house standard: `evals/test-cases.md`
  (7-case assertion suite — artifact render, bankroll relay with the ROI
  caveat, placed-bet write shape, coaching-note shape, pause switches,
  degraded paste fallback, BACKTEST labeling) and `SOURCES.md` ship for the
  first time. `evals/RESULTS.md` now exists and carries the execution
  records that the 1.1.1 entry below and the registry seam note already
  pointed at — that pointer was broken until today (the 1.1.1 re-judge was
  recorded only inside `trigger-evals.md`'s provenance note).
- `references/companion-contract.md`: the coaching-note `From:` line and the
  commit-message convention follow the member's new name (below).

## [1.1.1] — 2026-08-08

- Personal-name scrub (owner approved): every reference to the owner by
  first name — in `description`, `compatibility`, the body, the companion
  contract, the README, and one eval row — now reads "the owner". No
  trigger token changed; a cold re-judge of all 8 trigger rows was run
  anyway because the description text changed (see `evals/RESULTS.md`).
- README: the cloud routine is named by its full canonical name
  ("Project Longshot - Daily Card"), closing a stale short form.

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

## 2026-08-08 — renamed revenantworks-ossuary-cardcaller → revenantworks-ossuary-bonecaller

Owner-directed rename ("something cooler"), motif conserved: the ossuary claims
`-caller`, and the pack's own naming rationale says bones are the oldest dice —
calling the bones is native here in a way calling cards never quite was.
Collision-checked before the claim per the COLLISION.md method: `bonecaller`
has **zero** GitHub repos and is unclaimed on npm, PyPI, and crates.io
(cleaner evidence than `cardcaller`'s own 2026-08-07 claim, which carried one
0★ namesake); runner-up `shotcaller` was rejected on that same bar —
npm-claimed (a dormant scraper) plus a 296★ GitHub game namesake. Name
change — directory, `name:`, the name trigger token in `description`, and
every cross-reference (registry tables, pack router, root README, sibling
description and compatibility, longshot mirror and docs, the private brand
definition's naming row); version history above is continuous across the
rename. Shipped with the 1.2.0 eval completion; the post-rename cold
re-judge of the trigger suite is recorded in `evals/RESULTS.md`.
