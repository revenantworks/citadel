# citadel - Runbook

*Pairs with `tools/build.py` and `.github/workflows/pack-ci.yml`. The loop:*
**edit -> `python tools/build.py` -> commit -> tag `<pack>-vX.Y.Z` -> push -> CI attaches all member zips.**

## Release a pack version
1. Make the change (member content, registry row, roster).
2. `python tools/build.py` - regenerates every `references/pack.md` from the
   registry, validates all members (name/folder match, description <=1024
   chars, body <=500 lines, CHANGELOG head == frontmatter version), builds
   `dist/` zips. `--check` = CI mode, writes nothing.
3. Commit, tag `<pack>-vX.Y.Z`, push branch + tag.

## Install / update on claude.ai
Per skill: download the member zip from Releases -> Customize -> Skills -> + ->
Create skill -> upload. Updating is delete-then-re-upload; no CLI exists for
consumer skill upload, so this is the one unavoidable manual step.

**Config-carrying members ship *neutral* in the repo by law — swap your private
config in before uploading.** `apply-install-swaps.py` overlays your private
files onto the neutral repo copies and emits install-ready zips; upload those,
not the neutral `dist/` zips. The script hard-fails if pointed at neutral copies.
Config-carrying surfaces:

| Member | Neutral file in repo | Swap in your... |
|---|---|---|
| brandsmith | `references/brand-definition.md` | active brand definition |
| commsmith | `references/voices.md` | saved voices |
| promptsmith | `references/prompt-card.md` | install edition of the card |

> **Coming in the 1.1.0 build (Phase 1, brand decoupling):** `voices.md` folds
> into brandsmith's definition, reducing the swap surfaces from three to two
> ({brand-definition, prompt-card}). Revisit this table when that phase lands.

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
