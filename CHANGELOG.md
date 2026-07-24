# Changelog

All notable changes to the citadel repository and its packs are recorded here.
The format follows Keep a Changelog and packs use Semantic Versioning; releases
tag per pack as `<pack>-vX.Y.Z`, and each member keeps its own `CHANGELOG.md`.

## [foundation-v1.1.1] - 2026-07-24

Hygiene release — every finding from the 2026-07-24 pack-wide audit (25-agent review;
each claim mechanically verified) fixed. No description or body rewrites; no renames;
doctrine intact. Structural work parked in the deferral register (spec.md).

- **build.py guards:** plugin.json == marketplace version (hard fail — closes the
  1.0.0-vs-1.1.0 split-brain that shipped CI-invisible for a month) · `--bump-pack`
  one-stroke version writer · eval provenance-freshness + table-orphan checks (warn
  this release, fail at the next tag) · description ≥1000-char and body >5k-token
  instrumentation warns · calendar-stamp grammar narrowed to `Last verified:` (matches
  the Cowork upkeep grep; all four calendar files already used it) · `--parity`
  installed-clone drift detector (the live drift mechanism: the marketplace clone
  only moves on update and served pre-1.1.0 descriptions for a month).
- **All 8 members patch-bumped** (agentsmith/commsmith/evalsmith/loresmith/
  promptsmith/tokensmith → 1.1.1 · brandsmith → 1.1.2 · skillsmith → 1.1.2):
  eval provenance re-anchored pack-wide (derivation history preserved); brandsmith
  orphaned trigger rows 21–22 moved into the table + Case-14 duplicate assert removed;
  loresmith owner-personal eval queries neutralized + verdict-tag legend inlined where
  its Load budget forbade the cross-file pointer; evalsmith description grammar fixed +
  Provenance-discipline section added to its own doctrine; agentsmith SOURCES
  volatile-file denial removed + survey statistics attributed; tokensmith SOURCES
  cache figure reconciled to measurement.md's corrected ~0.10×; commsmith Case 20
  added for its self-named render-through-surface-tools failure + neutral
  voice-export fixture unblocking Cases 6/7/19; skillsmith retired-Configure
  reference fixed + predecessor-era "1.2.0" SOURCES heading dated correctly.
- **Capstone card v1.4.0:** brand-carriage-law alignment (brand-config refs removed,
  Leg 4 builds neutral), Run-3 status reconciled to the registry record, stored
  branded HTML twin deleted (regenerate at need via `brandsmith apply`).
- **Repo hygiene:** stale pre-law `install-uploads/` removed (payload escrowed);
  `.claude/` gitignored; RUNBOOK release checklist gains bump/parity/asset steps,
  the claude.ai section notes Dec-2025 Team/Enterprise org-wide provisioning, and a
  brand-escrow pointer (no brand content) added. Legacy predecessor repo defanged
  (push-capable remote removed, ARCHIVED.md marker) — outside this repo.

## [foundation-v1.1.0] - 2026-07-23

**Forge Run 3 — brand decoupling, uniformity, upkeep.** All eight members move
to 1.1.0. brandsmith becomes the single home of brand and voice — every other
smith outputs spec-clean neutral, and `brandsmith apply` is the one door for
branding a built skill, prompt card, or report (skillsmith dropped `configure`
and the cascade; commsmith dropped `voice`; tokensmith dropped its per-run
`brand:` switch; the prompt card ships unbranded). A uniform layer lands across
the pack: `metadata.volatile` declarations (4 calendar / 3 event-driven / 2
none), matching Volatile-surfaces and Anti-patterns sections, canonical README
skeletons, and a pack CLAUDE.md router. New capabilities: `skillsmith upkeep`
(pack-wide staleness sweep over the volatile declarations), `promptsmith model`
(standalone tier + model recommendation), `agentsmith refresh` (new stamped
`platform-notes.md` baseline). All four calendar baselines re-verified against
primary sources and restamped 2026-07-23 (model lineups, skill-format sources,
cache mechanics, agent-platform enforcement). `tools/build.py` now validates
the `metadata.volatile` block (U-7) — existence, legal classes, sane cadence,
dated stamps — in both `--check` and full-build modes. Eval suites refreshed
diff-scoped across the pack; the 12-row trigger-partition test re-run clean at
the release bar.

## [foundation-v1.0.0] - 2026-07-14

**Citadel 1.0 - launch release.** First public release under
`revenantworks/citadel`: marketplace-native layout (one plugin per pack under
`packs/`), marketplace name `revenant` (installs read `foundation@revenant`),
and the foundation pack - eight standalone smiths - uniformly baselined at
member version 1.0.0. Manifests are registry-derived via `tools/build.py`
(`--check` is the CI drift guard); CI validates every push and attaches all
member zips to the release on tag. Prior iteration history is retired to the
private archive.
