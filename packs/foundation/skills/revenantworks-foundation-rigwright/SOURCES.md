# Sources

Where this skill's guidance comes from, and how to re-check it. Anything time-sensitive lives in `references/surface-notes.md` behind its own stamp — this file records provenance, not current values.

**Verified as of 2026-08-17** (`rigwright refresh`; the flat-structure row was carried, not re-verified — see `surface-notes.md`).

## Claude Projects and profile preferences

| Claim | Source | Grade |
|---|---|---|
| Instructions apply to every chat; context not shared between chats unless in knowledge | Claude Help Center — "What are projects", "How can I create and manage projects" | published |
| RAG auto-scales knowledge capacity on paid plans | Claude Help Center — "What are projects" | published |
| Flat structure, no nesting, no cross-project access | Carried from 2026-07-30; not stated in the Help Center articles read 2026-08-17 — consistent secondary sources | **reported** (was published) |
| Organization instructions — Team/Enterprise, 3,000 chars, precede a member's own | Claude Help Center — "Set organization instructions" | published |
| Profile field labeled "Instructions for Claude", account-wide | Claude Help Center — "Understanding Claude's personalization features" | published |
| ~8,000-character instruction budget | Consistent secondary sources; no Anthropic figure | **reported** |
| ~1,500-character profile preference budget | Consistent secondary sources; no Anthropic figure | **reported** |

## CLAUDE.md and the memory hierarchy

| Claim | Source | Grade |
|---|---|---|
| Four-scope hierarchy; higher scopes load first | Claude Code docs — memory | published |
| `@path` imports, relative and absolute, nesting several hops | Claude Code docs — memory | published |
| `CLAUDE.local.md` supported as the gitignored personal file; a home-directory import is the worktree-safe form | Claude Code docs — memory (the 2026-07-30 row read it as deprecated) | published |
| `.claude/rules/` topic files; `paths:` frontmatter scopes a rule to matching files; `~/.claude/rules/` user-level | Claude Code docs — memory | published |
| Project instructions may live at `./.claude/CLAUDE.md`; imports max four hops; external imports in a project file prompt once | Claude Code docs — memory | published |
| Delivered as a user message after the system prompt, no strict-compliance guarantee | Claude Code docs — memory, troubleshooting | published |
| Imports load at launch and do not reduce context cost | Claude Code docs | published |
| `/init` generates a baseline; `/memory` inspects loaded files | Claude Code docs | published |
| Under-200-line target per CLAUDE.md | Claude Code docs — memory ("target under 200 lines") — moved from reported 2026-08-17 | published |

## Settings, permissions, and MCP configuration

| Claim | Source | Grade |
|---|---|---|
| Settings merge by scope with a managed layer above all | Claude Code docs — settings | published |
| Permission evaluation order deny → ask → allow, first match wins; specificity does not reorder | Claude Code docs — permissions | published |
| Project `allow` rules gated on workspace trust; hooks and `env` in repo settings run before trust and in `-p`/SDK with no dialog | Claude Code docs — permissions | published |
| Skill frontmatter: `allowed-tools` is a per-turn grant, `disallowed-tools` exists, six keys accepted by claude.ai uploads | Claude Code docs — skills | published |
| `.claude/settings.local.json` auto-gitignored | Claude Code docs — settings | published |
| MCP servers in `.mcp.json` (project) / `~/.claude.json` (user), not in `settings.json` | Claude Code docs — MCP; settings | published |
| `.mcp.json` at the project root; `${VAR}` / `${VAR:-default}` expansion; project-server approval prompt | Claude Code docs — MCP (open item of 2026-07-30 closed 2026-08-17) | published |

## Auto-memory

| Claim | Source | Grade |
|---|---|---|
| Auto memory at `~/.claude/projects/<project>/memory/`; `MEMORY.md` first 200 lines / 25 KB loaded at start; `/memory` toggles, `autoMemoryEnabled`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Claude Code docs — memory | published |

## Skill-format conformance

Built against the Agent Skills format as documented at platform.claude.com (agents-and-tools/agent-skills, overview and best practices) and the open standard at agentskills.io, re-verified 2026-07-30: frontmatter `name` and `description`, ≤500-line body guidance, progressive disclosure, one-level reference links.

## Niche scan

Checked before building, 2026-07-30: agentskills.io · skills.sh · anthropics/skills · anthropics/claude-plugins-community · VoltAgent/awesome-agent-skills · lobehub skills directory · claudeskills.info. Scaffold and `CLAUDE.md`-generation incumbents exist, including first-party `/init`; no incumbent found offering cross-surface placement or a score-only drift audit, which is where this skill's claim sits.

## Re-checking

`rigwright refresh` re-verifies `references/surface-notes.md` against these sources and restamps that file only. Nothing else here is time-sensitive. Where a **reported** figure becomes published, move the row and note the move — never silently promote it.
