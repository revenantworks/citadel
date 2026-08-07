# Sources

Where this skill's guidance comes from, and how to re-check it. Anything time-sensitive lives in `references/surface-notes.md` behind its own stamp — this file records provenance, not current values.

**Verified as of 2026-07-30.**

## Claude Projects and profile preferences

| Claim | Source | Grade |
|---|---|---|
| Instructions apply to every chat; context not shared between chats unless in knowledge | Claude Help Center — "What are projects", "How can I create and manage projects" | published |
| RAG auto-scales knowledge capacity on paid plans | Claude Help Center — "What are projects" | published |
| Flat structure, no nesting, no cross-project access | Claude Help Center | published |
| ~8,000-character instruction budget | Consistent secondary sources; no Anthropic figure | **reported** |
| ~1,500-character profile preference budget | Consistent secondary sources; no Anthropic figure | **reported** |

## CLAUDE.md and the memory hierarchy

| Claim | Source | Grade |
|---|---|---|
| Four-scope hierarchy; higher scopes load first | Claude Code docs — memory | published |
| `@path` imports, relative and absolute, nesting several hops | Claude Code docs — memory | published |
| `CLAUDE.local.md` deprecated in favour of imports; imports work across worktrees | Claude Code docs — memory | published |
| Delivered as a user message after the system prompt, no strict-compliance guarantee | Claude Code docs — memory, troubleshooting | published |
| Imports load at launch and do not reduce context cost | Claude Code docs | published |
| `/init` generates a baseline; `/memory` inspects loaded files | Claude Code docs | published |
| ~200-line working budget | Community norm on context-rot grounds; no enforced cap | **reported** |

## Settings, permissions, and MCP configuration

| Claim | Source | Grade |
|---|---|---|
| Settings merge by scope with a managed layer above all | Claude Code docs — settings | published |
| Permission evaluation order deny → ask → allow, first match wins | Claude Code docs — settings | published |
| `.claude/settings.local.json` auto-gitignored | Claude Code docs — settings | published |
| MCP servers in `.mcp.json` (project) / `~/.claude.json` (user), not in `settings.json` | Claude Code docs — MCP; settings | published |
| `.mcp.json` location — root vs `.claude/` | Sources disagree; root used, flagged open in `surface-notes.md` | **open** |

## Auto-memory

| Claim | Source | Grade |
|---|---|---|
| Claude Code accumulates its own memory separately from CLAUDE.md, with an index loaded at session start; `/memory` audits or disables | Claude Code docs — memory | published |

## Skill-format conformance

Built against the Agent Skills format as documented at platform.claude.com (agents-and-tools/agent-skills, overview and best practices) and the open standard at agentskills.io, re-verified 2026-07-30: frontmatter `name` and `description`, ≤500-line body guidance, progressive disclosure, one-level reference links.

## Niche scan

Checked before building, 2026-07-30: agentskills.io · skills.sh · anthropics/skills · anthropics/claude-plugins-community · VoltAgent/awesome-agent-skills · lobehub skills directory · claudeskills.info. Scaffold and `CLAUDE.md`-generation incumbents exist, including first-party `/init`; no incumbent found offering cross-surface placement or a score-only drift audit, which is where this skill's claim sits.

## Re-checking

`rigwright refresh` re-verifies `references/surface-notes.md` against these sources and restamps that file only. Nothing else here is time-sensitive. Where a **reported** figure becomes published, move the row and note the move — never silently promote it.
