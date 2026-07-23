# Citadel

![pack-ci](https://github.com/revenantworks/citadel/actions/workflows/pack-ci.yml/badge.svg)

The Revenant packs marketplace — canonical home of every **Revenant** Agent Skills pack. Each pack lives under [`packs/`](packs/) and installs as one Claude Code plugin; every skill inside follows the [Agent Skills open standard](https://agentskills.io/) and stands alone on any surface that supports it (Claude.ai, Claude Code, the Claude API, compatible agents).

**Packs**

| Pack | Members | What it covers |
|---|---|---|
| [`foundation`](packs/foundation/) | 8 | The build-time smiths — skills, prompts, messages, agent specs, research, eval suites, brand identity, token budgets |

Future packs slot in as new folders under `packs/` and new rows in the marketplace catalog — one repo, one marketplace, forever.

### foundation — the eight smiths

Each routes on its own description and works alone; together they cover the build → audit → ship loop.

| Smith | What it makes |
|---|---|
| **skillsmith** | Builds, audits, brands, and ports Agent Skills and whole packs |
| **promptsmith** | Builds, scores, and hardens prompts, with model-tier routing |
| **commsmith** | Shapes messages per channel, audience, and saved voice; audits message drift |
| **agentsmith** | Designs and audits autonomous-agent systems — guardrails, trust tiers, kill switches |
| **loresmith** | Research-verified verdicts and versioned playbook reference docs, every claim evidence-tagged |
| **brandsmith** | Builds a brand definition and audits repos, packs, and artifacts for drift |
| **evalsmith** | Authors and audits eval suites — build-time generator, zero runtime dependency |
| **tokensmith** | Measures, budgets, and slims the token footprint of LLM-facing artifacts |

## Install

**Claude Code — a whole pack, one command.** This repository is its own plugin marketplace:

```
/plugin marketplace add revenantworks/citadel
/plugin install foundation@revenant
```

**Claude.ai** (paid plans with code execution) — download a member zip from [Releases](../../releases), then **Customize → Skills → + → Create skill** and upload it. Per-skill, per-account.

**Claude API** — upload a member zip via the Skills API (`/v1/skills`) and reference its `skill_id` with the code execution tool.

Alternatively, copy any single skill folder from `packs/<pack>/skills/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project).

**Before you install:** every skill here is plain-text and MIT-licensed — read any `SKILL.md` and its `references/` before use. Anthropic recommends running Skills only from sources you trust and auditing third-party skills first; this repo is public and auditable end to end.

## Layout

```
.claude-plugin/marketplace.json   # the catalog — one plugin entry per pack
packs/<pack>/                     # the plugin: .claude-plugin/plugin.json · skills/ · spec.md · capstone/
brand/                            # the Revenant house brand guide + HTML card
tools/build.py                    # registry-derived sync + validation + dist zips (--check = CI mode)
```

Member versions are independent semver; pack releases tag as `<pack>-vX.Y.Z` and CI attaches every member zip to the release. Single source of truth for rosters: the pack tables in skillsmith's `pack-registry.md` — `tools/build.py` derives the manifests and refuses drift.

Always comes back.

*MIT — see LICENSE.*
