# claude-skills - Runbook

*Pairs with `tools/build.py`, `tools/release.py`, and `.github/workflows/pack-ci.yml`. The loop:*
**edit -> `python tools/build.py` -> commit -> tag `<pack>-vX.Y.Z` -> push -> CI attaches all member zips.**

**One command runs the whole close-of-pass loop (added 2026-08-17):**
`python tools/release.py foundation=X.Y.Z [ossuary=X.Y.Z] -m "<message>"` —
bump-pack, changelog gate, build, `--check`, tests, commit, tag, push with
tags, longshot mirror re-sync (commit + push there under its own identity),
`~/.claude/brand` refresh, then the list of member zips that changed and the
exact claude.ai upload list. Add `--swaps <dir> [<peer-dir>]` to also build
the branded brandwright install zip, `--export-dir <dir>` to copy every zip
plus a README.txt there, `--dry-run` to see the plan. Steps 1 to 5 below
describe what it does by hand.

## The rig install ritual (2026-08-17 — replaces the marketplace plugins)

**Edit in the repo; it is live next session.** Every foundation member and
bonecaller load on the owner's rig by user-scope junction —
`~/.claude/skills/<member>` -> `packs/<pack>/skills/<member>/` in this
working tree (PowerShell `New-Item -ItemType Junction`); linecaller's
junction points at the longshot repo's mirror copy instead, because the
cloud routine and the rig must read the same file. The marketplace plugins
`foundation@revenantworks` and `ossuary@revenantworks` were uninstalled from
the rig the same day; `claude plugin update` and the two-surface sync ritual
are **no longer part of the rig loop**. The marketplace registration itself
stays — it is how the public installs. `python tools/build.py --parity`
remains for CI and public consumers (it skips cleanly with no plugin
installed) and is not a rig step. Verify the junctions with
`ls -la ~/.claude/skills`; a missing one is recreated by the PowerShell line
above, never by re-installing the plugin.

**Post-commit hook.** `.claude/settings.json` wires a PostToolUse hook on
`git commit` (`.claude/hooks/bump-check.py`) that runs `build.py --check`
and surfaces `pack bump needed: <pack>` when shipped files differ from the
pack's current tag while its version has not moved. Advisory, never
blocking; no `ask` rules anywhere in this repo.

## Release a pack version
1. Make the change (member content, registry row, roster). On any member
   version bump, re-anchor its eval provenance lines in the same commit
   (evalwright's Provenance discipline; the build gate warns on drift).
   **Any change to a member's shipped files — evals and fixtures included —
   bumps that member's version in the same commit.** The claude.ai re-upload
   step is keyed on the member zip's version, so an unbumped change is
   invisible to the lazy-upload rule and never ships there: three members
   went out that way in foundation-v2.2.3 (brandwright/commwright/agentwright
   eval changes at unchanged versions), and for commwright the stranded
   change was the personal-name scrub itself.
2. `python tools/build.py --bump-pack <pack> <X.Y.Z>`: writes the
   marketplace entry + pack plugin.json + root CHANGELOG scaffold in one
   stroke (never hand-edit the two version fields separately: the
   1.0.0/1.1.0 split-brain shipped for a month that way).
3. `python tools/build.py`: regenerates every `references/pack.md` from the
   registry, validates all members (name/folder match, description <=1024
   chars, `compatibility` <=500 chars — the only field limit confirmed
   against a real upload error, and the reason `description` carries no
   second one, body <=500 lines, CHANGELOG head == frontmatter version,
   plugin.json == marketplace version, eval provenance freshness + table
   integrity, and the `metadata.volatile` block: legal classes, files
   exist, calendar surfaces stamped `Last verified:` with a sane cadence),
   builds `dist/` zips. `--check` = CI mode, writes nothing.
4. Commit, tag `<pack>-vX.Y.Z`, push branch + tag. Confirm CI attached the
   member zips to the Release. README points installers at Releases, so a
   tag whose assets lag main ships stale skills. Two closes on this step:
   - **Fetch the tag back**: `git fetch --tags origin`. A release cut with
     `gh release create` tags server-side and the clone never learns it, so
     any local "newest tagged version" check answers one release stale
     (ossuary-v2.2.4 sat on the remote and not in the clone for two days).
   - **Before the next bump lands, assert the current one has a tag**:
     `git tag -l "<pack>-v$(python -c "import json;print(json.load(open('packs/<pack>/.claude-plugin/plugin.json'))['version'])")"`
     must print. ossuary 2.2.2 reached main and was superseded 4.5 minutes
     later; the tag namespace still skips it (recorded in `CHANGELOG.md`).
     Either tag it or record the skip — silence is the failure.
5. **Owner machine: nothing to sync (2026-08-17).** The rig loads every
   member by junction into this working tree (see *The rig install ritual*
   above), so the tag changes nothing here beyond the longshot mirror, which
   `release.py` re-syncs. Then re-upload changed members on claude.ai below.

   > History: until 2026-08-17 this step was a two-surface ritual —
   > `claude plugin marketplace update revenantworks`, then
   > `claude plugin update <pack>@revenantworks`, then `--parity` — because the
   > plugin cache was what Claude Code loaded and the pack version was its
   > key, so a member-only bump never reached the rig. The junctions removed
   > that class of drift; `--parity` stays for CI and public consumers.

## Install / update on claude.ai
Per skill: download the member zip from Releases -> Customize -> Skills -> + ->
Create skill -> upload. `python tools/release.py` prints, at the end of every
release, which member zips changed and marks the two that are **required** on
claude.ai — bonecaller (claude.ai is its only surface) and brandwright's
branded install variant (the only brand carrier; built by
`apply-install-swaps.py`, see below) — the rest are optional convenience
copies. Every SKILL.md frontmatter carries only the six keys the upload form
accepts (name, description, license, compatibility, metadata, allowed-tools —
`build.py --check` does not enforce this; the 2026-08-14 upload failure was on
`compatibility` length, which it does). **Take the zip from the newest release overall, never
the newest release of the member's own pack.** Every release carries the full
11-member set frozen at that moment, so a pack tag advertises whatever the
other pack's members were that day: `foundation-v2.3.0` still ships a
bonecaller zip whose `compatibility` the upload form rejects. Only the latest
release has every member current. Releases stay immutable — this is a reading
rule, not an asset to go back and fix. Updating is delete-then-re-upload — the unavoidable
manual step **on personal accounts**. Team/Enterprise accounts have had
org-wide admin provisioning since Dec 2025 (as of 2026-08-01; Organization
settings -> Skills, zip upload, enabled by default with per-user opt-out).
One central upload replaces the per-user x8.

**Brand-carriage law (owner decision, 2026-07-23): the ONLY brand carrier
anywhere — repo or installs — is the locally configured brandwright.** Every
other member is brandless everywhere; branded artifacts (prompt cards
included) are produced at need via `brandwright apply`, never stored.
`apply-install-swaps.py` overlays your private files onto neutral repo copies
and emits install-ready zips; upload those, and plain `dist/` zips for anything
you did not override. The script hard-fails if pointed at the neutral definition.

**The split is not owner-specific — it is how anyone puts their own identity on
this pack.** The repo ships neutral so it can be downloaded and used as-is. If
you want your own brand on your own install, you never edit the repo: you keep a
private directory, put in it only what you want to override, and run the script.
Your branding lives on your disk and in your install. Overriding a brand already
applied is the same operation as applying a first one — the neutral repo copy is
always the input, so a rebuild cannot compound.

| Put in your swaps dir | Overlays | Effect |
|---|---|---|
| `brand-definition.md` | brandwright's `references/brand-definition.md` | your identity + voice. A second and later dir installs as a **peer** definition (brandwright 1.2.0+ holds several and selects one per run); the primary's Roster is what makes a peer reachable, and the script warns if it is missing from it |
| `LICENSE` | every member's `LICENSE` | your copyright holder |
| `brand-token.txt` | every member's `metadata.brand:` | your brand token (one line) |

All three are optional and independent. Omit one and its neutral value ships.
Every override is printed per member as it is applied — a build that silently
rewrote your copyright would be worse than one that refused to.

```bash
python3 tools/apply-install-swaps.py <your-private-dir> [<peer-dir> ...]
```

> History: 1.0.x had three swap surfaces; 1.1.0 folded voice into the
> definition (two); the 2026-07-23 law retired the prompt-card swap (one).
> 2026-08-07 generalised it: the definition swap still touches only brandwright,
> but `LICENSE` and `brand-token.txt` reach every member, so a downstream user can
> rebrand the whole pack without touching the repo.

## Install / update in Claude Code
Public consumers: `/plugin marketplace add revenantworks/claude-skills` once,
then `/plugin install <pack>@revenantworks`. No zips, no swaps: installs from
the repo; config lives in your local `~/.claude` copy. Updating: `claude plugin
marketplace update revenantworks`, then `claude plugin update
foundation@revenantworks` (both, in that order — the pack version is the
cache key). The owner's rig does none of this — it loads by junction (above).
Migrating from the pre-2.0.0 `revenant` marketplace name: remove the old
marketplace locally first, then add + install under the new name.

## Add a member or a pack
New member: build it, add its registry row (registry members table), run
`python tools/build.py`, upload per policy. New pack: add the pack row +
`**<pack> members**` table to the registry, create `packs/<pack>/` with its
`.claude-plugin/plugin.json`, add the marketplace catalog entry, run the build.

A pack needs **four** registry surfaces, not one — `**<pack> members**`,
`**<pack> budgets**` (one row per member, honest ceiling + stated reason; the
build hard-fails on undeclared overage), `**<pack> seams**` (one row per
boundary pair, or `--check` warns that every edge is unrecorded), and a
`Conformance checks (YYYY-MM-DD): ...` clause **in the pack row's own Notes
cell**. That last one is not optional decoration: the generated `pack.md`
prints a conformance line for every pack, so a pack without its own clause
gets the stated default. Before 2026-08-07 it silently got the *first* pack's
line instead — see `ossuary-v1.0.0` in `CHANGELOG.md`. Optional but expected:
`**<pack> capstone:**`, `**<pack> canonical repo:**`, a `**<pack> seam notes:**`
block, and a pack router at `packs/<pack>/CLAUDE.md`.

If a pack's members must also exist somewhere else — a repo whose runner clones
only itself — the outside copy is a **declared downstream mirror**, never a
second source of truth: keep it byte-identical, name this repo (`revenantworks/claude-skills`) as canonical in a
header note at the mirror, and record it in that repo's file map. `ossuary`'s
copy in `MickMacPW/longshot` is the worked example.

## Policies
Restamp per pack (registry Notes; default lazy): rebuild/upload only changed
members + the registry carrier. Release bar: discoverability pass, no open
P0/P1, repo/release/account parity, current capstone card.

**Brand escrow (pointer only — no brand content in this repo, per the law):**
the live definitions live in the two private brand repos; on the rig,
brandwright reads them from the fixed path `~/.claude/brand/`
(`brand-definition.md` + `brand-definition-northstar.md`, copies — a file
symlink needs admin on Windows), refreshed by `python tools/release.py
--refresh-brand` and by step 9 of every release. Those copies are read-only
for brandwright: a Build is handed back and landed in the home repo, which
then refreshes the copies. `install-definition.py` in the private brand repo
stays for **packaged consumers only** (it overlays the plugin-cache copy) and
is no longer the rig's path. A dated backup copy is kept outside any repo and
re-exported after every definition change. The **Foundation - Skill Upkeep** cloud routine carries the reminder
(`packs/foundation/upkeep-task.md`). If both the
local config and the backup are ever lost, git history holds only the older
public edition. Treat the backup as the recovery path, never the repo.
