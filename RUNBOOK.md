# citadel - Runbook

*Pairs with `tools/build.py` and `.github/workflows/pack-ci.yml`. The loop:*
**edit -> `python tools/build.py` -> commit -> tag `<pack>-vX.Y.Z` -> push -> CI attaches all member zips.**

## Release a pack version
1. Make the change (member content, registry row, roster).
2. `python tools/build.py` - regenerates every `references/pack.md` from the
   registry, validates all members (name/folder match, description <=1024
   chars, body <=500 lines, CHANGELOG head == frontmatter version, and the
   `metadata.volatile` block - legal classes, files exist, calendar surfaces
   stamped with a sane cadence), builds `dist/` zips. `--check` = CI mode,
   writes nothing.
3. Commit, tag `<pack>-vX.Y.Z`, push branch + tag.

## Install / update on claude.ai
Per skill: download the member zip from Releases -> Customize -> Skills -> + ->
Create skill -> upload. Updating is delete-then-re-upload; no CLI exists for
consumer skill upload, so this is the one unavoidable manual step.

**Brand-carriage law (owner decision, 2026-07-23): the ONLY brand carrier
anywhere — repo or installs — is the locally configured brandsmith.** Every
other member is brandless everywhere; branded artifacts (prompt cards
included) are produced at need via `brandsmith apply`, never stored.
`apply-install-swaps.py` overlays your private definition onto the neutral
repo copy and emits the install-ready zip; upload that one, and plain `dist/`
zips for the other seven. The script hard-fails if pointed at the neutral copy.
The single config-carrying surface:

| Member | Neutral file in repo | Swap in your... |
|---|---|---|
| brandsmith | `references/brand-definition.md` | active brand definition (identity + voice) |

> History: 1.0.x had three swap surfaces; 1.1.0 folded voice into the
> definition (two); the 2026-07-23 law retired the prompt-card swap (one).

## Install / update in Claude Code
`/plugin marketplace add revenantworks/citadel` once, then
`/plugin install <pack>@revenant`. No zips, no swaps - installs from the repo;
config lives in your local `~/.claude` copy.

## Add a member or a pack
New member: build it, add its registry row (registry members table), run
`python tools/build.py`, upload per policy. New pack: add the pack row +
`**<pack> members**` table to the registry, create `packs/<pack>/` with its
`.claude-plugin/plugin.json`, add the marketplace catalog entry, run the build.

## Policies
Restamp per pack (registry Notes; default lazy): rebuild/upload only changed
members + the registry carrier. Release bar: discoverability pass, no open
P0/P1, repo/release/account parity, current capstone card.
