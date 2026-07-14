# Changelog

All notable changes to the citadel repository and its packs are recorded here.
The format follows Keep a Changelog and packs use Semantic Versioning; releases
tag per pack as `<pack>-vX.Y.Z`, and each member keeps its own `CHANGELOG.md`.

## [foundation-v1.0.0] - 2026-07-14

**Citadel 1.0 - launch release.** First public release under
`revenantworks/citadel`: marketplace-native layout (one plugin per pack under
`packs/`), marketplace name `revenant` (installs read `foundation@revenant`),
and the foundation pack - eight standalone smiths - uniformly baselined at
member version 1.0.0. Manifests are registry-derived via `tools/build.py`
(`--check` is the CI drift guard); CI validates every push and attaches all
member zips to the release on tag. Prior iteration history is retired to the
private archive.
