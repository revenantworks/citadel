# Rubrics — Best-Practices Baseline and Policy Profiles

Rubric A is universal: every skill, any profile, is scored against it. Profiles replace a one-size charter: a skill is scored against the profile **it declares** (frontmatter `metadata.profile`, inherited from its pack), never against a stricter one it didn't claim.

## Contents

- Rubric A — published best practices + niche-research sources (volatile baseline, refresh target)
- Scoring anchors
- The universal rule
- Profiles: standalone · standard · custom
- Pack conformance checks
- Audit application notes

---

## Rubric A — published best practices

> **Last verified: 2026-07-23.** This baseline section is the **only** part of this file "skillsmith refresh" regenerates. Every build and audit re-researches these sources fresh; this baked list is the fallback when search is unavailable — flag it as possibly stale when used that way. Canonical sources, in order: Anthropic Agent Skills best-practices and overview docs (platform.claude.com / docs.claude.com → agents-and-tools/agent-skills), the Agent Skills open standard (agentskills.io — published 2025-12-18; **the anthropics/skills repo now carries an explicit pointer file, `spec/agent-skills-spec.md`, that redirects to agentskills.io/specification as the single canonical spec**; the format itself is stable — frontmatter name/description, ≤500-line guidance, progressive disclosure unchanged, and now adopted beyond Anthropic by OpenAI Codex and GitHub Copilot), the engineering blog post "Equipping agents for the real world with Agent Skills," the anthropics/skills repository (including skill-creator), the Claude Help Center article "How to create custom skills," and — for the plugin packaging target — the Claude Code plugin docs (code.claude.com/docs/en/plugins). Community cross-checks only.

**Niche-research sources** — the niche verdict checks each of these before declaring a niche open (all verified live 2026-07-12): the Agent Skills open standard's ecosystem (agentskills.io, above) · **skills.sh** — community skill directory with install counts, topics, and per-agent listings · **github.com/anthropics/skills** — official examples; doubles as a plugin marketplace (`anthropic-agent-skills`) · **github.com/anthropics/claude-plugins-official** — Anthropic-managed curated plugin directory · **github.com/anthropics/claude-plugins-community** — public community plugin directory (submissions flow through clau.de/plugin-directory-submission) · **github.com/anthropics/knowledge-work-plugins** — role-plugin reference architecture (skills + commands + connectors) · **github.com/VoltAgent/awesome-agent-skills** — high-volume curated skill index · **skillsmp.com** — community skills marketplace · **agentskill.sh** — large multi-category skills marketplace · **openagentskill.com** — skill resolve/trust-scoring directory · **awesomeskills.dev** — community skill index (these three verified live 2026-07-13; **Skillstore and ClawHub** are cited in ecosystem lists — ClawHub as one of the three major marketplaces alongside SkillsMP and Skills.sh in a ~490K-skill ecosystem, per 2026-07-23 cross-checks — but not yet verified live here: candidates only, not checked sources) · plus GitHub topic and curated-list scans for the specific job. A dead source at check time is noted and skipped, never silently dropped from this list.

- **name** — ≤64 chars, lowercase letters/digits/hyphens only, no leading/trailing/consecutive hyphens, no XML tags, no reserved words ("claude", "anthropic"); folder name matches the frontmatter `name` exactly
- **description** — ≤1024 chars, non-empty, no XML tags, third person, states WHAT it does and WHEN to trigger with the words a user would actually say; lean pushy (skills under-trigger); all when-to-use lives here, not in the body
- **discoverability test** — from name + description alone, ten realistic requests route correctly; routing is set at this level, not in the body
- **body size** — SKILL.md ≤500 lines; split to reference files past ~300; the context window is a public good
- **progressive disclosure** — reference links one level deep; long reference files (~150+ lines) carry a table of contents; mutually exclusive contexts live in separate files
- **instruction style** — explain-the-why over CAPS imperatives; reserve MUST/NEVER for genuinely fragile steps; match instruction freedom to task fragility
- **no rot** — no time-sensitive facts hard-coded outside a stamped volatile file; no Windows-style paths
- **dependencies declared** — every tool, script, package, or sibling skill named in frontmatter (`compatibility` / `metadata`) and docs; scripts state whether they are run or read
- **evals exist** — a way to tell the skill worked: trigger evals plus an assertion suite, or a stated reason neither applies
- **security** — every bundled file audited: no instructions that don't match the stated purpose, no secrets, untrusted input treated as data

## Scoring anchors

1–10 per dimension, overall = average to one decimal. **1–3** absent or broken · **4–6** present but drifts — output or triggering varies · **7–8** ship-ready, minor tweaks · **9–10** consistently correct as-is. Anchor to the skill's real job: a missing TOC on a 40-line reference is a non-issue; on a 300-line one it's a real defect.

## The universal rule

**No undeclared dependencies.** Profiles differ in what a skill may depend on; none permit hiding it. A skill that quietly assumes a tool, a sibling, or an installed package fails its profile — whichever profile that is.

## Profiles

**standalone** — the strictest profile. Dependencies: web search only, plus the surface's native file tools for delivery with stated graceful degradation where absent. No executable code shipped. Volatile facts isolated in stamped single-update-surface files with a staleness rule (default 60 days). Load budget declared in SKILL.md (≤3 reference loads standard). Works identically on chat, Code, and API surfaces.

**standard** — tools, scripts, packages, and MCPs allowed, each declared with install/availability notes and per-surface behavior (e.g., "no network on the plain API"). Scripts state run-vs-read. Sibling-skill references allowed under the composition contract: which siblings, and absence behavior (degrade or hard-require) stated in the description or compatibility notes.

**custom** — a pack-defined policy list registered in `pack-registry.md` (e.g., "internal-only: may assume the org's MCP server; must not call public web"). Audits score against the listed policies verbatim. A custom profile that omits the universal rule is invalid.

## Pack conformance checks

A pack may register conformance checks in `pack-registry.md` — pack-charter rules scored on every member audit alongside Rubric A and the declared profile. Standard anchors; a failed check is a P1 finding naming the exact addition. Registered for `foundation` (adopted 2026-07-13):

- **C-1 drift-audit verb** — the skill carries a first-class way to score an existing artifact of its own kind against the standard it implements and report drift *without rewriting it* (a dedicated audit or verification entry, or a stated score-only path).
- **C-2 neutral default** — outputs default to a spec-clean neutral identity; brand and persona voice are strictly opt-in per run. A skill with no identity surface at all passes as structurally N/A.

Checks are pack charter, not universal law: a skill outside the registering pack is never scored against them.

## Audit application notes

Read the audited skill's declared profile first; score against that. Tools on a standard-profile skill are checked for declaration quality, not existence. A skill with no declared profile is scored against Rubric A plus the universal rule only, with a P1 finding to declare one. When the audited skill's pack registers a canonical repo (pack-registry), drift audits also diff the installed copy against that repo's current state and report installed-vs-canonical drift alongside Rubric A; when the repo is unreachable, score rubric-only and say so. When a build request's profile is looser than the skill needs, note once that a standalone-clean build is possible — an offer, not a nag.
