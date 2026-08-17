# claude-skills - Runbook

*Pairs with `tools/build.py` and `.github/workflows/pack-ci.yml`. The loop:*
**edit -> `python tools/build.py` -> commit -> tag `<pack>-vX.Y.Z` -> push -> CI attaches all member zips.**

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
5. Owner machine, **both steps, in this order**. Two copies drift
   independently and refreshing the first does not move the second:

   > **2.0.0 migration note:** the marketplace was renamed `revenant` →
   > `revenantworks` (2026-08-07) and marketplace names have no rename
   > mechanism, so an install registered under the old name never sees this
   > release. One-time fix: remove the old `revenant` marketplace locally,
   > `claude plugin marketplace add` under the new name, then
   > `claude plugin update foundation@revenantworks` (the orchestrator ran
   > this on the owner machine on migration day). The steps below assume the
   > new name.

   1. `claude plugin marketplace update revenantworks` (or `git -C
      ~/.claude/plugins/marketplaces/revenantworks pull`): refreshes the clone,
      which is what an install reads FROM. It served pre-1.1.0 descriptions
      for a month.
   2. `claude plugin update <pack>@revenantworks`: rewrites
      `~/.claude/plugins/cache/revenantworks/<pack>/<version>/`, the copy Claude
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
Create skill -> upload. **Take the zip from the newest release overall, never
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
`/plugin marketplace add revenantworks/claude-skills` once, then
`/plugin install <pack>@revenantworks`. No zips, no swaps: installs from the repo;
config lives in your local `~/.claude` copy. Updating: `claude plugin
marketplace update revenantworks`, then `claude plugin update
foundation@revenantworks` (both, in that order — see the release loop above).
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
the live definition exists solely in the locally configured brandwright; a
dated backup copy is kept outside any repo and re-exported after every
definition change. The **Foundation - Skill Upkeep** cloud routine carries the reminder
(`packs/foundation/upkeep-task.md`). If both the
local config and the backup are ever lost, git history holds only the older
public edition. Treat the backup as the recovery path, never the repo.
