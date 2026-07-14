# citadel

![pack-ci](https://github.com/revenantworks/citadel/actions/workflows/pack-ci.yml/badge.svg)

The Revenant packs marketplace — canonical home of every **Revenant** Agent Skills pack. Each pack lives under [`packs/`](packs/) and installs as one Claude Code plugin; every skill inside follows the [Agent Skills open standard](https://agentskills.io/) and stands alone on any surface that supports it (Claude.ai, Claude Code, the Claude API, compatible agents).

**Packs**

| Pack | Members | What it covers |
|---|---|---|
| [`foundation`](packs/foundation/) | 8 | The build-time smiths — skills, prompts, messages, agent specs, research, eval suites, brand identity, token budgets |

Future packs slot in as new folders under `packs/` and new rows in the marketplace catalog — one repo, one marketplace, forever.

## Install

**Claude Code — a whole pack, one command.** This repository is its own plugin marketplace:

```
/plugin marketplace add revenantworks/citadel
/plugin install foundation@revenant
```

**Claude.ai** (paid plans with code execution) — download a member zip from [Releases](../../releases), then **Customize → Skills → + → Create skill** and upload it. Per-skill, per-account.

**Claude API** — upload a member zip via the Skills API (`/v1/skills`) and reference its `skill_id` with the code execution tool.

Alternatively, copy any single skill folder from `packs/<pack>/skills/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project).

## Layout

```
.claude-plugin/marketplace.json   # the catalog — one plugin entry per pack
packs/<pack>/                     # the plugin: .claude-plugin/plugin.json · skills/ · spec.md · capstone/
brand/                            # the Revenant house brand guide + HTML card
tools/build.py                    # registry-derived sync + validation + dist zips (--check = CI mode)
```

Member versions are independent semver; pack releases tag as `<pack>-vX.Y.Z` and CI attaches every member zip to the release. Single source of truth for rosters: the pack tables in skillsmith's `brand-config.md` — `tools/build.py` derives the manifests and refuses drift.

Always comes back.

*MIT — see LICENSE.*
