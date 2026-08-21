# claude-skills

![pack-ci](https://github.com/revenantworks/claude-skills/actions/workflows/pack-ci.yml/badge.svg)

This is the Revenantworks packs marketplace — the canonical home of every **Revenantworks** Agent Skills pack. Each pack lives under [`packs/`](packs/) and installs as one Claude Code plugin. Every skill inside follows the [Agent Skills open standard](https://agentskills.io/) and stands alone on any surface that supports it: Claude.ai, Claude Code, the Claude API, or a compatible agent.

**Packs**

| Pack | Members | What it covers |
|---|---|---|
| [`foundation`](packs/foundation/) | 10 | The build-time wrights — skills, prompts, messages, agent specs, standing Claude config, research, eval suites, brand identity, token budgets, session fan-out |

Further packs slot in as new folders under `packs/` and new rows in the marketplace catalog — one repo, one marketplace, one registry.

### foundation — the ten wrights

Each routes on its own description and works alone. Together they cover the build → audit → ship
loop.

| Wright | What it makes |
|---|---|
| **skillwright** | Builds, audits, and ports Agent Skills and whole packs (neutral by default) |
| **promptwright** | Builds, scores, and hardens prompts, with model-tier routing |
| **commwright** | Shapes messages per channel and audience; neutral-voice default; audits message drift |
| **agentwright** | Designs and audits autonomous-agent systems — guardrails, trust tiers, kill switches |
| **lorewright** | Research-verified verdicts and versioned playbook reference docs, every claim evidence-tagged |
| **brandwright** | Single home of brand + voice — defines, applies on invoke, and audits repos, packs, and artifacts for drift |
| **evalwright** | Authors and audits eval suites — build-time generator, zero runtime dependency |
| **tokenwright** | Measures, budgets, and slims the token footprint of LLM-facing artifacts |
| **rigwright** | Builds the standing configuration Claude reads before work — Project instructions, CLAUDE.md, repo Claude config |
| **dispatchwright** | Runs a session's fan-out — decomposes, tiers via promptwright, dispatches with a durability contract, reconciles against origin |

Installed together, foundation ships an always-on router, [`packs/foundation/CLAUDE.md`](packs/foundation/CLAUDE.md). Copy it into your project (or `~/.claude/`) so Claude reaches for the right wright and holds the pack's conventions without being asked.

## Install

- **Claude Code — a whole pack, one command.** This repository is its own plugin marketplace:

  ```
  /plugin marketplace add revenantworks/claude-skills
  /plugin install foundation@revenantworks
  ```

  Installed before 2.0.0, when the marketplace was named `revenant`? Marketplace names have no rename mechanism — remove the old `revenant` marketplace locally, then add and install under the new name (one time).

- **Claude.ai** (paid plans with code execution) — download a member zip from [Releases](../../releases), then **Customize → Skills → + → Create skill** and upload it. Per-skill, per-account.

- **Claude API** — upload a member zip via the Skills API (`/v1/skills`) and reference its `skill_id` with the code execution tool.

Alternatively, copy any single skill folder from `packs/<pack>/skills/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project). Or, working from a clone, junction or symlink `~/.claude/skills/<member>` to the member folder — an edit is then live next session. That is how the maintainer's own machine has loaded these since 2026-08-17; see `RUNBOOK.md`.

**Before you install:** every skill here is plain-text and MIT-licensed — the root `LICENSE` is the verbatim MIT text, and it covers every skill and document in the repo. Read any `SKILL.md` and its `references/` before use. Anthropic recommends running Skills only from sources you trust and auditing third-party skills first. This repo is public and auditable end to end.

## Layout

```
.claude-plugin/marketplace.json   # the catalog — one plugin entry per pack
packs/<pack>/                     # the plugin: .claude-plugin/plugin.json · skills/ · spec.md (+ ledger.md · decisions.md) · capstone/
tools/build.py                    # registry-derived sync + validation + dist zips (--check = CI mode)
tools/release.py                  # the close-of-pass loop: bump, build, check, tests, commit, tag, push, mirror, upload list
audit/                            # the standing audit record and the naming-collision registry (COLLISION.md)
RUNBOOK.md                        # release and sync procedure — read before shipping anything
NEXT.md                           # the open queue — remaining follow-ups
```

Member versions are independent semver. Pack releases tag as `<pack>-vX.Y.Z`, and CI attaches every member zip to the release. The pack tables in skillwright's `pack-registry.md` are the single source of truth for rosters; `tools/build.py` derives the manifests from them and refuses drift.

*MIT — see LICENSE.*
