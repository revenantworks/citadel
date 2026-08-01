# citadel - Runbook

*Pairs with `tools/build.py` and `.github/workflows/pack-ci.yml`. The loop:*
**edit -> `python tools/build.py` -> commit -> tag `<pack>-vX.Y.Z` -> push -> CI attaches all member zips.**

## Release a pack version
1. Make the change (member content, registry row, roster). On any member
   version bump, re-anchor its eval provenance lines in the same commit
   (evalwright's Provenance discipline; the build gate warns on drift).
2. `python tools/build.py --bump-pack <pack> <X.Y.Z>`: writes the
   marketplace entry + pack plugin.json + root CHANGELOG scaffold in one
   stroke (never hand-edit the two version fields separately: the
   1.0.0/1.1.0 split-brain shipped for a month that way).
3. `python tools/build.py`: regenerates every `references/pack.md` from the
   registry, validates all members (name/folder match, description <=1024
   chars, body <=500 lines, CHANGELOG head == frontmatter version,
   plugin.json == marketplace version, eval provenance freshness + table
   integrity, and the `metadata.volatile` block: legal classes, files
   exist, calendar surfaces stamped `Last verified:` with a sane cadence),
   builds `dist/` zips. `--check` = CI mode, writes nothing.
4. Commit, tag `<pack>-vX.Y.Z`, push branch + tag. Confirm CI attached the
   member zips to the Release. README points installers at Releases, so a
   tag whose assets lag main ships stale skills.
5. Owner machine, **both steps, in this order**. Two copies drift
   independently and refreshing the first does not move the second:
   1. `claude plugin marketplace update revenant` (or `git -C
      ~/.claude/plugins/marketplaces/revenant pull`): refreshes the clone,
      which is what an install reads FROM. It served pre-1.1.0 descriptions
      for a month.
   2. `claude plugin update <pack>@revenant`: rewrites
      `~/.claude/plugins/cache/revenant/<pack>/<version>/`, the copy Claude
      Code actually LOADS. Restart to apply. Skipping this is how a session
      kept loading a superseded member while parity reported clean
      (2026-08-01, promptwright 1.1.0). **This compares PACK versions**, so a
      member-only bump is undeliverable: it reports "already at the latest
      version" and serves the old body. A member fix reaches an install only
      when a pack bump carries it.

   Then `python tools/build.py --parity` must report clean. It checks **both**
   surfaces across **every shipped file** (not just SKILL.md frontmatter, which
   twice read clean over a stale `ledger.md`/`spec.md`) and names which surface
   drifted and which files. Then re-upload changed members on claude.ai below.

## Install / update on claude.ai
Per skill: download the member zip from Releases -> Customize -> Skills -> + ->
Create skill -> upload. Updating is delete-then-re-upload — the unavoidable
manual step **on personal accounts**. Team/Enterprise accounts have had
org-wide admin provisioning since Dec 2025 (as of 2026-08-01; Organization
settings -> Skills, zip upload, enabled by default with per-user opt-out).
One central upload replaces the per-user x8.

**Brand-carriage law (owner decision, 2026-07-23): the ONLY brand carrier
anywhere — repo or installs — is the locally configured brandwright.** Every
other member is brandless everywhere; branded artifacts (prompt cards
included) are produced at need via `brandwright apply`, never stored.
`apply-install-swaps.py` overlays your private definition onto the neutral
repo copy and emits the install-ready zip; upload that one, and plain `dist/`
zips for the other seven. The script hard-fails if pointed at the neutral copy.
The single config-carrying surface:

| Member | Neutral file in repo | Swap in your... |
|---|---|---|
| brandwright | `references/brand-definition.md` | active brand definition (identity + voice) |

> History: 1.0.x had three swap surfaces; 1.1.0 folded voice into the
> definition (two); the 2026-07-23 law retired the prompt-card swap (one).

## Install / update in Claude Code
`/plugin marketplace add revenantworks/citadel` once, then
`/plugin install <pack>@revenant`. No zips, no swaps: installs from the repo;
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

**Brand escrow (pointer only — no brand content in this repo, per the law):**
the live definition exists solely in the locally configured brandwright; a
dated backup copy is kept outside any repo and re-exported after every
definition change. The `foundation-upkeep` cloud routine carries the reminder
(`packs/foundation/upkeep-task.md`). If both the
local config and the backup are ever lost, git history holds only the older
public edition. Treat the backup as the recovery path, never the repo.
