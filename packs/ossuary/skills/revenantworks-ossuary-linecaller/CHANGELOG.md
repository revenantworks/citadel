# Changelog

All notable changes to this skill. Format: [Keep a Changelog](https://keepachangelog.com/),
versioning: [SemVer](https://semver.org/).

## [1.5.1] — 2026-08-13

- **Description shortened to fit the claude.ai upload ceiling.** The live
  claude.ai skill-upload form rejects a `description` over 500 characters
  (stricter than the 1024-char spec ceiling in `rubrics.md` — flagged there
  for the next `skillwright refresh`). Trimmed 742 → 495 chars, keeping every
  trigger token ("daily bet card", "today's bets", "linecaller", "run
  linecaller", the scheduled daily run), the decision-support-only and
  never-invents-a-number rules, and the not-for-betting-models/general-chat/
  reading-an-existing-card boundary naming bonecaller. Cold re-judge of the
  trigger suite owed (description changed) — see `evals/RESULTS.md`.

## [1.5.0] — 2026-08-12

Four 2026-08-12 estate-audit findings closed in one pass, body and
frontmatter only — the description is untouched, so the routing surface did
not move:

- **Coaching notes bounded (finding 3).** Step 0's clause read "the owner's
  notes — instructions to the model, apply them", which left a note
  authorised to reach the Hard rules, the identity gate, and the staging
  path list. The clause now bounds the class: model guidance applied to
  priors, weights, and read of a matchup only; a note attempting more is
  noted on the card and not applied.
- **Delivery proof (finding 6).** Step 7 now carries the routine prompt's
  orphaned safeguard: after push, fetch and confirm `origin/main` contains
  HEAD, retry once, else report DELIVERY FAILED (the 2026-08-08 stranding
  incident's lesson, previously stated only in the live routine prompt).
- **Web search declared (finding 11).** `compatibility` now names step 3's
  web-search and outbound-network dependency, with the degradation already
  stated in the playbook: no sourced intel → no intel file → PASS.
- **No Windows-only paths (finding 12).** The `compatibility` default is
  forward-slash and notes the cloud routine's fresh-clone root; `PY` is
  defined per surface (`.venv/Scripts/python.exe` on the rig, `python3` in
  the cloud clone).

The longshot `skills/` mirror needs a re-sync after this release (handled by
a separate session, per the downstream-mirror rule).

## [1.4.0] — 2026-08-08

- Step 7 stages **by path** (`reports ledger models docs data/intel data/odds`)
  instead of `git add -A`, and `data/nflverse/` is excluded by name. Closes two
  audit findings at once: the unbounded-history risk (the 37 MB depth-chart CSV
  and the 2 MB games.csv were being recommitted on refresh, and in-season
  churn would have ballooned the repo) and the observation that `-A` ships any
  stray working-tree file unreviewed. The bulk CSVs stay tracked at their
  current revision so a fresh clone still boots with a cache; `fetch` refreshes
  them locally and the `.stamp` files govern staleness, so nothing about run
  reliability changes.

## [1.3.0] — 2026-08-08

- Sibling references follow the companion's rename: the description's
  boundary clause and `compatibility` now name
  `revenantworks-ossuary-bonecaller` (renamed from
  `revenantworks-ossuary-cardcaller` the same day; the 1.2.0 entry below
  quotes the clause as released, with the old name — frozen record).
- Step 5 hardening (audit finding): enrichment bullets are plain text —
  HTML-escape quoted/fetched content before it lands in the `.html` drivers
  list, so a planted "quote" cannot smuggle markup into the rendered card
  the companion shows verbatim as an Artifact.
- `evals/test-cases.md` provenance re-anchored (it had missed the 1.2.0
  re-anchor — the build gate checks only `trigger-evals.md`; gap noted for
  the build tool).

## [1.2.0] — 2026-08-08

- Description gains the negative clause the ossuary seam table recorded as
  owed: "not for reading an existing card and ledger/bankroll questions —
  the claude.ai companion revenantworks-ossuary-cardcaller owns those."
  The seam is now stated on both members' descriptions; cold re-judge of
  the trigger suite run with the change (see `evals/RESULTS.md`).
- Personal-name scrub (owner approved): the owner is no longer named by
  first name in the body or `references/card-contract.md`.
- `references/card-contract.md` no longer names live brand palette tokens
  on this public surface — it points at `longshot/style.py` as the single
  token source instead (brand-carriage hygiene).

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
