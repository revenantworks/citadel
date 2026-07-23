# Changelog

All notable changes to the citadel repository and its packs are recorded here.
The format follows Keep a Changelog and packs use Semantic Versioning; releases
tag per pack as `<pack>-vX.Y.Z`, and each member keeps its own `CHANGELOG.md`.

## [Unreleased]

`tools/build.py` now validates each member's `metadata.volatile` block (U-7,
Forge Run 3 Phase 5): the block must exist (`[]` for none), classes must be
`calendar` or `event-driven`, declared files must exist, and calendar surfaces
additionally need a sane `cadence_days` (7–365) and a dated header stamp —
checked in both `--check` (CI) and full-build modes.

## [foundation-v1.0.0] - 2026-07-14

**Citadel 1.0 - launch release.** First public release under
`revenantworks/citadel`: marketplace-native layout (one plugin per pack under
`packs/`), marketplace name `revenant` (installs read `foundation@revenant`),
and the foundation pack - eight standalone smiths - uniformly baselined at
member version 1.0.0. Manifests are registry-derived via `tools/build.py`
(`--check` is the CI drift guard); CI validates every push and attaches all
member zips to the release on tag. Prior iteration history is retired to the
private archive.
