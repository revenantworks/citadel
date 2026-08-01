# Surface Notes — Volatile Baseline *(single update surface)*

> **Last verified: 2026-07-30.** This is the **only** file `rigwright refresh` regenerates — surface fields, caps, and load behavior drift with releases; the layer stack in SKILL.md does not. When this stamp is over 60 days old, treat every number here as possibly stale and say so before quoting one. The placement doctrine never goes stale.

The layer stack decides *where* a rule belongs; this file records what each surface currently *provides and constrains*. A run that stays at the placement level never opens this file — SKILL.md *Load budget* is the source of that rule.

**Verification discipline.** Rows marked **[published]** come from Anthropic documentation. Rows marked **[reported]** come from consistent secondary sources with no published figure behind them — these are presented to the user as guidance, never as hard limits the build validates against. Never silently promote a reported figure to a published one on refresh; if the vendor publishes it, move the row and note the move.

## Contents

- Claude Projects (claude.ai)
- Profile preferences (claude.ai)
- CLAUDE.md and the memory hierarchy
- The `.claude` directory
- MCP server configuration
- Auto-memory
- Where this file stops — the agentwright line

---

## Claude Projects (claude.ai)

**[published]** A Project is a self-contained workspace holding custom instructions, a knowledge base, and its own chats. Instructions apply to every chat in the Project. **Context is not shared between chats** in the same Project unless it lives in the instructions or the knowledge base — this is the single most misunderstood property of the surface and it drives the knowledge-file plan: anything two chats both need is a knowledge file, not something said once in a chat.

**[published]** Structure is flat. Projects do not nest, and one Project cannot read another's knowledge. **[published]** On paid plans (Pro, Max, Team, Enterprise) the knowledge base auto-scales via RAG when it approaches the context limit, expanding capacity substantially rather than failing. Free accounts are capped and must prune instead. **[published]** Team and Enterprise plans can share a Project with per-member permission levels.

**[reported]** Custom instructions are widely reported to accept roughly 8,000 characters. Anthropic publishes no figure. Treat it as a working budget, warn near it, and never fail a build on it.

**Knowledge-file plan conventions.** File names are part of retrieval — Claude uses them to decide what to pull, so `q4-2026-pricing-policy.pdf` outperforms `doc1.pdf` materially. Prefer several well-named files over one omnibus upload. Common formats (PDF, DOCX, CSV, TXT, MD, HTML) are accepted.

## Profile preferences (claude.ai)

Account-level, applies to every chat everywhere including inside Projects. **[reported]** Approximately 1,500 characters; no published figure. This is the home for identity, tone, and format preferences that never vary by project — a rule repeated in three Projects belongs here instead, and a rule that varies by project must never be here.

## CLAUDE.md and the memory hierarchy

**[published]** Memory files load automatically at session start. Files higher in the hierarchy load first and are built on by more specific ones:

| Scope | Location | Shared with |
|---|---|---|
| Enterprise policy | OS-managed system path | Everyone in the org |
| Project memory | `./CLAUDE.md` | The team, via source control |
| User memory | `~/.claude/CLAUDE.md` | Just you, all projects |
| Project local | `./CLAUDE.local.md` | **Deprecated** — use an import instead |

**[published]** `CLAUDE.md` supports `@path/to/file` imports, both relative and absolute, nesting several hops deep. Importing from the home directory is the supported way to let a teammate add personal instructions that aren't committed — the replacement for the deprecated local file, and it works correctly across git worktrees where the local file did not.

**Two properties that change how a build is written.** **[published]** `CLAUDE.md` content is delivered as a *user message after the system prompt*, not as part of the system prompt — Claude reads it and tries to follow it, with no guarantee of strict compliance, especially for vague or conflicting instructions. That is the documented basis for the layer stack's hooks rule: anything whose failure actually costs something is not safe as prose here. **[published]** Imports organize instructions but do **not** reduce context cost — imported files still load at launch. A `CLAUDE.md` split into six imported files costs what the one file cost.

**[reported]** A working budget of roughly 200 lines is the consistent community norm, on context-rot grounds rather than any enforced cap. Use it as the audit's budget dimension, stated as guidance.

**[published]** `/init` generates a baseline `CLAUDE.md` by scanning the repo, and `/memory` opens the loaded files for inspection and editing. Both are worth naming at handback — a build that ignores an existing `/init` output and writes over it is doing the user's review for them.

## The `.claude` directory

Two directories, different jobs: `./.claude/` in the repo is team configuration and is committed; `~/.claude/` is personal and is not.

| File | Scope | Committed |
|---|---|---|
| `.claude/settings.json` | Project — permissions, hooks, env, model | Yes |
| `.claude/settings.local.json` | Machine-local overrides | No — auto-gitignored |
| `~/.claude/settings.json` | User, all projects | n/a |
| `.claude/skills/<name>/SKILL.md` | Project skills | Yes |
| `.claude/agents/<name>.md` | Project subagents | Yes |

**[published]** Settings files merge, with more specific scopes overriding broader ones and a managed enterprise layer above all of them. Permission rules evaluate **deny first, then ask, then allow**, first match wins — so a broad allow cannot accidentally unlock something a specific deny already caught. Hooks are configured under the `hooks` key in `settings.json`.

**Emit rule.** A generated `settings.json` ships with explicit deny rules for destructive commands and never with a blanket allow. The generated default is the finding in an audit even where prose invites the user to tighten it — a config ships as written.

## MCP server configuration

**[published]** MCP servers are configured *outside* `settings.json`: project scope in `.mcp.json` at the repository root, user scope in `~/.claude.json`. Putting an `mcpServers` key into `settings.json` is a schema error, and it is a common enough mistake to be worth checking on any audit that finds one.

> **Open item, flagged 2026-07-30.** Most sources place `.mcp.json` at the repo root; one placed it under `.claude/`. Repo root is used here as the primary-documented location. Re-confirm on the next refresh before treating the alternate path as wrong in an audit finding.

**Emit rule.** A generated `.mcp.json` pins server versions rather than floating them, and carries no credential — env-var indirection only, with the variable named and the value never written into the file.

## Auto-memory

**[published]** Claude Code maintains its own memory separately from `CLAUDE.md`, accumulating notes across sessions under the user's Claude config directory, with an index loaded at session start. `/memory` audits, edits, or disables it.

This layer is **not authored** by a build. It is included in the stack so an audit can spot the failure mode: a user hand-writing into the auto-memory file, or a `CLAUDE.md` restating what auto-memory already learned. Both are found and reported; neither is generated.

## Where this file stops — the agentwright line

Cowork tasks, Claude Code routines (cloud), and desktop scheduled tasks are **not documented here** and are not rigwright's to emit. Their fields, cadence presets, trigger types, missed-run semantics, and enforcement surfaces live in agentwright's `platform-notes.md`, which is the pack's single home for anything that runs unattended. A run that reaches for a scheduler here has crossed the seam and should hand off by name rather than duplicating the table.
