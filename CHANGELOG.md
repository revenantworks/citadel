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

## [foundation-v1.1.1] - 2026-08-01

Install-parity release: the tooling fix from `4800918` reaching the copies
that actually load. Cut for delivery, not for new capability.

- **The pack version is the plugin cache key.** `claude plugin update`
  compares pack versions, so a member-only bump never reaches an installed
  user: the marketplace clone moves, the loaded cache does not, and the
  update reports "already at the latest version". skillwright 1.0.1 rode main
  and stayed unreachable until this bump — which is the whole reason it
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
