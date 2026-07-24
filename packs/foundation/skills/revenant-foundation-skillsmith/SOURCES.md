# Sources

This skill is assembled from public, citable material. Everything below was verified as of **2026-07-12**. The Rubric A baseline in `references/rubrics.md` carries its own Last-verified stamp and is re-researched on every build and audit — run "skillsmith refresh" to regenerate it.

## Skill authoring — Anthropic primary sources

*Applies to: `references/rubrics.md` (Rubric A), `references/build-templates.md`, `references/description-crafting.md`, `references/eval-authoring.md`.*

| Source | Key guidance |
|---|---|
| Anthropic — Agent Skills best practices. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | ≤500-line SKILL.md body; one-level-deep references; TOCs on long reference files; third-person what+when descriptions; evaluation-driven iteration; avoid time-sensitive info and Windows paths. |
| Anthropic — Agent Skills overview. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | Three-level progressive disclosure (metadata → body → bundled resources); frontmatter `name` + `description` required; trusted-source security guidance. |
| Anthropic — "Equipping agents for the real world with Agent Skills." https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | Progressive disclosure as the core design principle; start with evaluation; split unwieldy bodies; think from the executing model's perspective. |
| Anthropic — anthropics/skills repository (incl. skill-creator). https://github.com/anthropics/skills | Template-skill starting point; pushy descriptions to counter under-triggering; interview → draft → test → iterate loop; packaging conventions (`.skill` excludes `evals/`). skill-creator was also used to validate and package this skill at construction time. |
| Claude Help Center — "How to create custom skills." https://support.claude.com/en/articles/12512198-how-to-create-custom-skills | Focused single-purpose skills compose better than one large skill; clear descriptions drive invocation; start simple before adding scripts. |

## Skill format — the Agent Skills open standard

*Applies to: package structure, frontmatter fields, naming constraints.*

**Agent Skills open standard** — https://agentskills.io/ · name ≤64 chars lowercase-hyphen; description ≤1024 chars; optional `license`, `compatibility`, and `metadata` frontmatter fields (this skill's `metadata` carries version, profile, pack, and brand).

## Niche research & plugin distribution

*Applies to: the niche-research sources in `references/rubrics.md`, the Plugin target section in `references/build-templates.md`, SKILL.md build steps 3–4 and Packaging. All verified live 2026-07-12.*

| Source | Role |
|---|---|
| skills.sh — https://skills.sh | Community skill directory (install counts, topics, per-agent listings, security audits); niche-verdict incumbent scan. |
| anthropics/skills — https://github.com/anthropics/skills | Official example skills; doubles as a plugin marketplace (`anthropic-agent-skills`); niche-verdict incumbent scan. |
| anthropics/claude-plugins-official — https://github.com/anthropics/claude-plugins-official | Anthropic-managed curated plugin directory; niche-verdict incumbent scan. |
| anthropics/claude-plugins-community — https://github.com/anthropics/claude-plugins-community | Public community plugin directory; submissions flow through https://clau.de/plugin-directory-submission (`claude plugin validate` first); niche-verdict incumbent scan + distribution channel. |
| anthropics/knowledge-work-plugins — https://github.com/anthropics/knowledge-work-plugins | Role-plugin reference architecture (skills + commands + connectors); pattern source for role-shaped packs. |
| Claude Code plugin docs — https://code.claude.com/docs/en/plugins | Plugin target format: `.claude-plugin/plugin.json` manifest, `skills/` with `disable-model-invocation: true` for explicit workflows (legacy `commands/` noted), optional `.mcp.json`, marketplace registration, `claude plugin validate`. |

## Pack integration & surfaces (added at 1.1.0)

*Applies to: Entry — Integrate, `references/pack-integration.md`, the Packaging upload-path fix.*

- Claude Help Center — "Use skills in Claude" (verified 2026-07-13). https://support.claude.com/en/articles/12512180-use-skills-in-claude — custom skills upload as zips at Customize → Skills, per-account, code execution required; update = re-upload. Grounds the lazy-restamp default: installed-surface uploads are manual, one at a time.
- Claude Code docs — "Discover and install prebuilt plugins through marketplaces" (verified 2026-07-13). https://code.claude.com/docs/en/discover-plugins — `/plugin marketplace add <owner>/<repo>` + `/plugin install <name>@<marketplace>`; a repo carrying `.claude-plugin/marketplace.json` is its own marketplace. Grounds the plugin lane: one pack, one install on the Code surface.

## Pack design (added 2026-07-14; originally recorded under predecessor-era "1.2.0" numbering that never shipped — see spec D-3)

*Applies to: Entry — Pack, `references/pack-design.md`.*

- The suite-composition rules already recorded in `build-templates.md` (declared siblings, partitioned triggers as a set, one delivery) — Entry — Pack applies them at design time instead of retrofit time; no new external doctrine required.
- The 1.1.0 marketplace sources (Claude Code plugin-marketplaces docs; community submission flow in the baseline) govern the plugin/marketplace prep step; `claude plugin validate` per the same docs.

## Reference implementation

`revenant-foundation-promptsmith` (current release) — the gold-standard standalone-profile build this skill patterns its outputs on: declared load budget, tool-list test for tappable selections, stamped single-update-surface volatile files, `references/` + `evals/` split, assertion-only test suite, changelog born at 1.0.0.
