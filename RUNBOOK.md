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
Create skill -> upload (updating is delete-then-re-upload). **brandsmith:**
repo zips ship a *neutral* `references/brand-definition.md`; keep your
configured definition file when updating (swap it into the new zip first).

## Install / update in Claude Code
`/plugin marketplace add revenantworks/citadel` once, then
`/plugin install <pack>@revenant`.

## Add a member or a pack
New member: build it, add its registry row (brand-config.md members table),
run `python tools/build.py`, upload per policy. New pack: add the pack row +
`**<pack> members**` table to the registry, create `packs/<pack>/` with its
`.claude-plugin/plugin.json`, add the marketplace catalog entry, run the build.

## Policies
Restamp per pack (registry Notes; default lazy): rebuild/upload only changed
members + the registry carrier. Release bar: discoverability pass, no open
P0/P1, repo/release/account parity, current capstone card.
