# Changelog — citadel

Pack releases tag as `<pack>-vX.Y.Z`; member versions are independent semver.
This log starts at the foundation 1.0.0 baseline.

> **Predecessor-era version numbers do not resolve.** The pack re-baselined to
> 1.0.0 on 2026-07-31 and the pre-1.0 history was destroyed with no archive, so
> tag names from before that date (`foundation-v1.1.x` through `v1.4.x`,
> 2026-07-14 → 2026-07-27) name releases that no longer exist anywhere, as do
> the commit SHAs recorded beside them. **Two of those names have since been
> reused:** today's `foundation-v1.1.0` and `foundation-v1.1.1` are new
> releases unrelated to the predecessor tags of the same name. Where a
> pre-2026-07-31 designation appears in a frozen record — the eval `RESULTS.md`
> ledgers, `spec.md`'s history sections, `IMPROVEMENTS.md` — it is left verbatim
> because it records what was true when written; read it as a date, not a tag.
> Live code and runbooks cite dates instead, for exactly this reason.

## [foundation-v1.2.0] - 2026-08-05

The AUDIT-2026-08-05 apply pass — every verdict from the adversarial
refinement audit (report at repo root), applied member by member on approval.

- **Registry**: new rigwright ↔ tokenwright seam row (motive-keyed, signal:
  one description) closing the undeclared "trim my CLAUDE.md" / "slim my
  CLAUDE.md" boundary opened by rigwright's 2026-07-30 addition; the stale
  naming note now counts three CLAUDE.md descriptions. Seam note records the
  close. 12 → 13 seams; all nine manifests regenerated.
- **promptwright 1.3.0**: Tier routing gains the user-named-target override
  (a model or effort the user names wins — built to, noted as user-directed,
  better fit offered in one line; Entry — Model bound identically). Four
  lossless trims offset it; body lands exactly at its 8,850 budget. Case 39.
- **tokenwright 1.1.0**: description gains the rigwright boundary clause
  (802 → 894 chars). Trigger evals extended (Y11/N11), 22 rows.
- **agentwright 1.1.0**: description slimmed 992 → 950 chars, every cue
  kept; the ceiling-riding fix `build.py`'s warn text had scheduled.
- **skillwright 1.0.6**: lossless trim at the two audit-named sites (Build
  step 6 registry guard; bare-invocation cap); Case 14/17 anchors intact.
- **rigwright 1.0.2**: description names hooks in the artifact list
  (952 → 959 chars).
- Cold re-judges of the four moved routing surfaces (tokenwright,
  agentwright, rigwright trigger suites; promptwright's did not move) are
  owed and recorded as owed in each suite's provenance line, not claimed.

## [foundation-v1.1.5] - 2026-08-02

lorewright brought current, promptwright gains two tier-routing rules.

- **lorewright 1.0.2 → 1.1.2.** The v1.1.0 doctrine (Selection/Decision class
  split, four-slot Selection recommendation, seeded must-have gate,
  independent-evidence-first, coverage disclosure, purchase link) had been
  authored in a separate session and never installed — repo, marketplace, and
  cache had all silently stayed on 1.0.2 with 23 cases. Installed as built.
  **1.1.1:** Finding G1 applied — §4a's Top overall slot now states the
  must-haves gate explicitly, matching the other three slots; Case 27
  re-confirmed. Cases 30, 32, 34, 36 cold-executed for real with live
  search/fetch (the four whose Asserts need real retrieval) — 4/4 PASS,
  logged in `evals/RESULTS.md`; the remaining 12 of Cases 24–39 are authored,
  not yet cold-run. **1.1.2:** tokenwright slim, no behavior change —
  `SKILL.md` body cut ≈3040 → ≈2717 tokens; registry row raised 2700 → 2750.
- **promptwright 1.1.1 → 1.2.0.** Tier routing (Phase 5) gains two
  role-based overrides, shared by the standalone Model entry and plan grain:
  a planning/orchestrator subtask defaults one effort notch lower (high
  effort over-thinks and scope-creeps a plan); a review subtask checking
  another model's output defaults to a different model family, stakes
  permitting. Closes the gap found by a skillwright niche-verdict + gap scan
  run against a candidate 10th foundation member (an orchestration skill,
  informed by real-world r/ClaudeCode prior art) — plan grain already covers
  the candidate's stated job end-to-end except these two rules, so a new
  pack member wasn't justified. Case 38 added. Registry row raised
  8800 → 8850.
- Roster and seams unchanged (9 members, 12 seams); seven members untouched.

## [foundation-v1.1.4] - 2026-08-01

Parity tells the truth now, and carries the two records files that had no
release to travel on.

- **`--parity` widened from `SKILL.md` frontmatter to every shipped file.**
  The narrow scope reported **clean** twice while the loaded copy was stale:
  the lagging files were `ledger.md` and `spec.md`, which are not frontmatter
  and so were never compared. It now lists each file as missing, differing or
  extra, normalises line endings (a CRLF working tree vs an LF clone is not
  drift), and skips runtime markers. Verified by running it against the real
  stale install, where it named exactly the two files and nothing else.
- **skillwright 1.0.5** — Install parity re-scoped to match, with the lesson
  stated once: a detector narrower than what it certifies produces false
  assurance, which is worse than no detector because it ends the
  investigation.
- **Delivers `ledger.md` and `spec.md`** as of `8fdeeb9`, the post-1.1.3
  docs commit that had no pack bump to ride. Records only — no skill loads
  either at runtime.
- Roster and seams unchanged (9 members, 12 seams); eight members untouched.

## [foundation-v1.1.3] - 2026-08-01

Pack-wide prose pass: every member's own files (SKILL.md, README, SOURCES,
reference docs) and the root/pack-level docs (README, this file, RUNBOOK,
NEXT, the always-on router, decisions.md) were rewritten for register —
connector cleanup (em dash and " - " used to join clauses that read better as
two sentences, matched-pair parenthetical asides left alone), cross-referenced
rule duplication (a rule stated in full in two places now has one home and one
pointer), and a few wording/consistency fixes. No rule, gate, count, or entry
point moved anywhere, so no eval re-anchor is owed pack-wide.

- **commwright → 1.0.2** — its own SKILL.md and README used em dashes in the
  sentences announcing its no-dash H1 rule; the framing prose now matches the
  policy it states. Rule bodies and `humanize.md` were already dash-free.
- **skillwright → 1.0.4** — the shared "foundation seam notes" history in
  `pack-registry.md` (the seam-table's canonical source, read by every
  member's generated `pack.md`) reformatted from one ~700-word paragraph into
  a dated list, same facts; plus SOURCES.md wording and reference-file
  connector fixes.
- **promptwright → 1.1.1** — `model-snapshot.md`'s footnote markers had a gap
  (¹, ³, ⁴ with no ²); renumbered sequentially. `hostile-interpreter.md`
  trimmed to stop re-stating SKILL.md's own failure-shape definitions.
- **tokenwright → 1.0.2** — SKILL.md's Preservation-contract list was missing
  an item (dependency declarations and absence behaviors) that
  `waste-taxonomy.md` and this file both already carried; added, closing a
  real 6-vs-7 gap, not a style choice.
- **agentwright, brandwright, lorewright → 1.0.2 each** — a duplicated
  quarantined-reader rule (agentwright), a triple-duplicated per-element
  exclusion example (brandwright), and one telegraphic line (lorewright) each
  now single-homed or reworded.
- **evalwright → 1.0.2, rigwright → 1.0.1** — SKILL.md rules that restated a
  reference file's rule in full (count-drift/provenance for evalwright,
  the secrets rule for rigwright) now cross-reference their one home.
- **`spec.md`** (the live baton, not itself a member): the Current-status
  block now reflects 1.1.2/1.1.3 instead of stopping at 1.1.1; the frozen
  1.3.2-pass history paragraph gained an inline tag marking it as the
  pre-rebaseline snapshot, since the live deferral register 100+ lines later
  states a different, current register count and the two were easy to
  mistake for a contradiction.
- **`ledger.md` and `IMPROVEMENTS.md`** headers now point at this file's own
  predecessor-era disclaimer instead of independently restating it — three
  copies of the same disclaimer collapsed to one canonical text plus two
  pointers. Neither file's dated historical entries were touched, per their
  own append-only doctrine.
- **`tools/build.py` fix, found by this pass:** the seam-note extractor
  assumed the registry's seam-notes annotation was always one physical line
  and silently returned nothing otherwise. Reformatting it into a dated list
  (above) tripped that assumption and would have shipped all nine `pack.md`
  copies with the section missing; the extractor now captures a multi-line
  block up to the next top-level pack annotation. Caught before commit, not
  after.
- Roster and seams unchanged (9 members, 12 seams); no member's rules,
  counts, or entry points changed except tokenwright's one named content fix
  above.

## [foundation-v1.1.2] - 2026-08-01

Frozen records marked, so no version number anywhere in the pack can be
mistaken for a current one. Delivery release for the 1.1.1 post-tag work.

- **13 `evals/` files across 7 members gained a frozen-record header** naming
  their version numbers as predecessor-era and pointing at the root note. The
  remaining eval files already carried the disclaimer. **Rows, verdicts,
  dates, counts and pass rates are untouched.** The ledgers stay evidence,
  which is why this is a marker and not a rewrite.
- **agentwright, brandwright, commwright, evalwright, lorewright, tokenwright
  → 1.0.1; skillwright → 1.0.3** (its 1.0.2 doc fix rides here too, having
  been undeliverable at member grain).
- Also carries **skillwright 1.0.2** and the `tools/build.py` date-anchoring
  from `3a3b084`, which had no pack bump to travel on.
- **`build.py` now prunes superseded `dist/` zips.** It wrote
  `<member>-<version>.zip` and never removed the old one, so every bump left
  its predecessor sitting beside the current build: 16 zips for 9 members at
  this release. Since release-doctrine treats `dist/` as the upload source of
  truth, a stale neighbour is a mis-upload waiting to happen. `dist/` now
  holds exactly one zip per member.
- Roster and seams unchanged (9 members, 12 seams); promptwright and
  rigwright untouched.

## [foundation-v1.1.1] - 2026-08-01

Install-parity release: the tooling fix from `4800918` reaching the copies
that actually load. Cut for delivery, not for new capability.

- **The pack version is the plugin cache key.** `claude plugin update`
  compares pack versions, so a member-only bump never reaches an installed
  user: the marketplace clone moves, the loaded cache does not, and the
  update reports "already at the latest version". skillwright 1.0.1 rode main
  and stayed unreachable until this bump, which is the whole reason it
  exists. Recorded in `release-doctrine.md` — Install parity and RUNBOOK
  step 5.
- **skillwright 1.0.1** — release-doctrine's Install parity described one
  installed copy where Claude Code has two (the clone an install reads from,
  the cache it loads); now states both surfaces, the two-step order, the
  cache-key rule, and that parity knows nothing about claude.ai.
- **`tools/build.py --parity`** diffs the clone **and** the loaded cache,
  names which surface drifted, and skips each cleanly when absent (CI-safe).
  Verified against a real stale cache, not trusted on a clean run.
- Roster and seams unchanged (9 members, 12 seams); no member behavior moved.

## [foundation-v1.1.0] - 2026-08-01

- **promptwright 1.1.0** — Entry — Model gains plan grain: a handed-in plan
  with a targets ask gets a per-subtask target table (tier + model,
  effort/depth, inline-or-subagent, one-line why) instead of a single
  recommendation. A living-table contract rows an emergent mid-session
  subtask through the same tier logic before it dispatches; a standing-rule
  line rides beneath every table, its layer placement left to rigwright.
  Trigger suite 30 → 34 rows (17/17), assertion suite 36 → 37 cases; see the
  member's own CHANGELOG and `evals/RESULTS.md` for the full account.
- Router `packs/foundation/CLAUDE.md` gains the plan-table route cue and the
  living-table compose bullet.
- Roster and seams unchanged (9 members, 12 seams); no other member touched.

## foundation 1.0.0 — 2026-07-31 — the wright baseline

Nine build-time wrights, one plugin (`foundation@revenant`), each routing on
its own description and standing alone on any Agent Skills surface. Every
member ships with its references, trigger evals, and an assertion suite;
the pack's cold trigger baseline is 97/97. Versions are 1.0.0 across the
pack, plugin manifest, marketplace entry, and all nine members.

The 1.0 feature set, member by member (each member's own CHANGELOG carries
the full list):

- **skillwright** — builds, audits, ports, and integrates install-ready
  Agent Skills and whole packs: research-backed niche verdicts, dual-scored
  audits carrying the S-1…S-4 security pass and a register-only prose pass,
  sanitizing port with PORT-REPORT, pack-wide integrate under count
  integrity, 60-day refresh plus the pack-wide upkeep sweep. Ships
  spec-clean neutral.
- **promptwright** — seven-phase prompt builds with five-dimension scoring,
  a named-origin framework menu, a gated fast path, hostile-read hardening,
  the knowledge-vacuum check, S/A/B/C model-tier routing with the standalone
  `promptwright model` pick, and an optional offline HTML prompt card.
- **commwright** — channel-profile drafting under the silent H1–H9 humanize
  rules, a humanize entry for handed-in text, report-only message audits,
  cadence sets, and a pre-publish redaction sweep; it never sends.
- **agentwright** — ten-area ops-spec design sized blast-radius-first, emit
  into seven profiled platforms with per-control enforcement-gap tables, the
  five-class runtime security-scan, trust-tier doctrine, and a restraint
  that refuses autonomy plus irreversibility without a human gate.
- **lorewright** — evidence-graded verdicts ending in one direct
  recommendation with a flip condition, versioned playbooks verified against
  primary sources, four-grade claim tagging, and source-is-data-never-
  instructions injection handling.
- **brandwright** — the single home of brand and voice: the 14-group
  definition (ships neutral), the apply cascade, a seven-category drift
  audit with the P0 score floor, and four export payloads including the
  offline HTML brand-guide card.
- **evalwright** — coverage-mapped trigger-eval tables and assertion suites
  under count integrity and the zero-runtime-dependency law; five-check
  suite audits and diff-scoped refresh.
- **tokenwright** — exact-or-disclosed-estimate measurement, the W1–W10
  waste taxonomy, the nine-rung lossless→lossy ladder behind a preservation
  contract, net-cost accounting with cache mechanics, the description-cap
  rule, and set-level budget plans.
- **rigwright** — standing Claude configuration (Project instructions,
  CLAUDE.md, `.claude` layout, `.mcp.json`) built and audited through the
  seven-layer placement stack, with secrets restraint and a hard boundary to
  agentwright for anything unattended.

Pack-level:

- The always-on router (`packs/foundation/CLAUDE.md`): the routing table,
  the composition seams, and the pack conventions — neutral by default, one
  catalog one gate, audits report rather than rewrite, declared
  dependencies, stamped volatile surfaces on a 60-day cadence.
- Registry-derived build and validation (`tools/build.py`): the pack
  registry is the single source of truth for rosters; the build syncs
  manifests, validates every member, and produces the `dist/` zips;
  `--check` is CI mode, `--parity` verifies the installed clone.
- Brand-carriage law: brandwright is the only brand carrier anywhere — repo
  or installs; `tools/apply-install-swaps.py` overlays a private definition
  onto the neutral repo copy to produce the branded install zip.
- The `foundation-upkeep` cloud routine carries the volatile-surface sweep
  and the brand-escrow reminder.
