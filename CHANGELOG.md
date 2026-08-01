# Changelog — citadel

Pack releases tag as `<pack>-vX.Y.Z`; member versions are independent semver.
This log starts at the foundation 1.0.0 baseline.

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
