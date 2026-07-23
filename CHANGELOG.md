# Changelog

All notable changes to the citadel repository and its packs are recorded here.
The format follows Keep a Changelog and packs use Semantic Versioning; releases
tag per pack as `<pack>-vX.Y.Z`, and each member keeps its own `CHANGELOG.md`.

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
