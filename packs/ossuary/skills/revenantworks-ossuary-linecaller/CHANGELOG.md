# Changelog

All notable changes to this skill. Format: [Keep a Changelog](https://keepachangelog.com/),
versioning: [SemVer](https://semver.org/).

## [1.7.0] — 2026-08-17

The 2026-08-17 audit + security scan (skillwright Rubric A and Security
classes, plus the owner's security rubric read through the OWASP Top 10 for
Agentic Applications 2026 lenses — ASI01 goal hijack, ASI02 tool misuse,
ASI03 privilege abuse, ASI06 context poisoning). Description unchanged, so
the routing surface did not move.

### Added
- **First-Monday ledger block** (owner decision). Step 6: on the first
  Monday of a month the card carries a five-line block — bankroll, month
  P&L in units, graded record, ROI, avg CLV — computed with `PY` from
  `ledger/bets.csv` + `models/bankroll.json`, never by hand or from
  memory; empty inputs read `n/a`. Definitions and placement live once, in
  `references/card-contract.md` → Monthly ledger block. A
  `python -m longshot` subcommand would be the better home for the
  arithmetic; that is owed on the longshot side, not here.
- **Step 8 publish.** Where an Artifact tool exists and the slate had
  games, the run publishes `reports/<today>.html` to the one fixed page
  (`https://claude.ai/code/artifact/69eb441f-f2ea-4736-a294-d7d4e9a41881`),
  never a new URL; skipped on no-game/PAUSED days and on a rig run. The
  cloud routine's prompt already carried this as an environment specific;
  SKILL.md is now its home.
- Assertion cases R13 (coaching-note injection probe), R14 (ledger block
  computed, not invented), R15 (publish never mints a URL) — authored, not
  run. 12 → 15. R5, R6, R12 sit on changed ground and are owed a re-run.

### Security findings and fixes
- **S-1 · P1** — hard rule 3 covered "everything fetched" but not repo
  files the run reads and did not write (nflverse/ESPN data files, intel,
  coaching notes, `LEARNINGS.md`); step 0 bounded coaching notes alone.
  Rule 3 now names every such input as data, calls a directive found
  inside a finding, and forbids any URL, path, or command taken from it
  becoming a fetch target, push destination, or shell command.
- **S-3 · P1** — the identity gate (rule 2) had no stated behavior where
  `gh` is absent, which is the production surface; the routine prompt
  patched it from outside. The gh-absent structural case (one remote,
  push only to `origin` main) is now stated in the rule itself.
- **S-2 · P2** — rule 5 said the key lives in the environment but not that
  its value is never echoed, printed, or written; the never-echo clause is
  now in the rule.
- **Output handling · P2** — step 5 writes `models/coach_overrides.json`
  and `models/coach_intent.json` (per longshot's own file map and the
  playbook) but named neither; both are now named, with "nothing else under
  `models/`".
- Tool scoping: Bash, web search, git/gh, and (new) the Artifact tool are
  named with per-surface degradation; no `allowed-tools` grant (the minimal
  grant). Frontmatter carries only the six keys claude.ai accepts.
  Hidden-text scan (zero-width unicode, HTML comments, base64, homoglyph
  domains, fetch-pipe-shell) clean 2026-08-17.

### Changed
- Stale text: `data/nflverse/` is a gitignored cache (untracked
  2026-08-17), so step 7 no longer describes it as a staging exclusion;
  README's invocation table names the cloud routine (the Task Scheduler
  runner was retired 2026-08-17) and no longer lists "today's bets", ceded
  to bonecaller at 1.6.0; README's install section leads with the routine
  and the rig junction.

## [1.6.0] — 2026-08-15

### Changed
- Description redraw (`ossuary-caller-description-overlap`): run verbs
  front-loaded ("run the daily card", "build today's card"), the bare noun
  phrase "today's bets" CEDED to bonecaller, and the boundary clause names
  the ceded tokens. Trigger suite re-anchored: row 2 flips to no-fire, ten
  rows added to the 20-row spec (`ossuary-trigger-suites-half-spec`),
  authored-not-run.
- `compatibility` drops the drive-lettered rig path
  (`linecaller-machine-path-in-shipped-frontmatter`).
- Body states why model invocation stays enabled (Rubric A dim 11 /
  `linecaller-model-invocable-push`): the production cloud routine fires
  this skill through the model, so `disable-model-invocation` would sever
  the daily card; compensating controls named in-file.

## [1.5.4] — 2026-08-14

- **`references/card-contract.md` re-synced from the longshot production
  mirror — citadel had drifted stale.** Two real fixes landed directly on
  the downstream longshot copy and were never ported back: commit `2713461`
  ("add a live weather driver, today's-risk KPI, and bets-first ordering to
  the card") and `e7e43e6` ("correct spread-pick sign and make bet
  instructions unambiguous"). Caught during the 2026-08-14 hygiene sweep's
  mirror re-sync — a routine full-directory copy from citadel would have
  silently clobbered both fixes; the sync was corrected before it shipped
  and this closes the gap the other direction. citadel is the canonical
  source again; both copies are now byte-identical.
- No trigger token, hard rule, or `compatibility`/`description` field
  changed — cold re-judge not owed.

## [1.5.3] — 2026-08-14 (correction)

- **`description` reverted to its full 742-char pre-trim text.** The 1.5.1
  entry below assumed the same 500-char ceiling seen on `compatibility`
  applied to `description` too — it never did. Two real upload attempts at
  the trimmed length (495 chars) never errored on `description`; only
  `compatibility` did (this member's own 1.5.2 entry). skillwright's own
  baked rubric caps `description` at 1024 chars, and Anthropic's help-center
  page separately states 200 — neither number is confirmed live, so this
  reverts to the fuller text rather than guess a number the product hasn't
  actually enforced. No trigger token or boundary clause differs from the
  1.2.0/1.3.0 text already cold-judged 10/10 — re-verified this pass, still
  10/10, recorded in `evals/RESULTS.md`.

## [1.5.2] — 2026-08-14

- **`compatibility` shortened to fit the claude.ai upload ceiling.** The 500-char
  limit applies to more than `description` — the live upload form also
  rejected `compatibility` at 667 chars. Trimmed to 463, keeping every fact:
  the repo/venv/git/gh dependencies, the preseason-intel web-search
  requirement and its degradation, the machine-bound note, and the bonecaller
  cross-reference. No trigger token changed — cold re-judge not owed, this
  field carries no routing.

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
