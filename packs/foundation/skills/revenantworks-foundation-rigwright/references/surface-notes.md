# Surface Notes — Volatile Baseline *(single update surface)*

> **Last verified: 2026-08-17.** This is the **only** file `rigwright refresh` regenerates — surface fields, caps, and load behavior drift with releases; the layer stack in SKILL.md does not. When this stamp is over 60 days old, treat every number here as possibly stale and say so before quoting one. The placement doctrine never goes stale.

The layer stack decides *where* a rule belongs; this file records what each surface currently *provides and constrains*. A run that stays at the placement level never opens this file — SKILL.md *Load budget* is the source of that rule.

**Verification discipline.** Rows marked **[published]** come from Anthropic documentation. Rows marked **[reported]** come from consistent secondary sources with no published figure behind them: these are presented to the user as guidance, never as hard limits the build validates against. Never silently promote a reported figure to a published one on refresh; if the vendor publishes it, move the row and note the move. A claim a refresh could not reach keeps its grade and says so inline.

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

**[published]** A Project is a self-contained workspace holding custom instructions, a knowledge base, and its own chats. Instructions apply to every chat in the Project. **Context is not shared between chats** in the same Project unless it lives in the instructions or the knowledge base. This is the single most misunderstood property of the surface and it drives the knowledge-file plan: anything two chats both need is a knowledge file, not something said once in a chat.

**[published]** On paid plans (Pro, Max, Team, Enterprise) the knowledge base auto-scales via RAG when it approaches the context limit — up to 10× capacity per the Help Center — rather than failing. Free accounts are capped (five Projects, no RAG scaling) and must prune instead. **[published]** Team and Enterprise plans can share a Project with per-member permission levels (view / edit). Structure is flat: Projects do not nest and one Project cannot read another's knowledge *(carried from 2026-07-30; not stated in the Help Center articles read 2026-08-17 — consistent secondary sources and an open feature request confirm it)*.

**[published] Organization instructions** (Team / Enterprise; set by an admin or owner) — up to 3,000 characters, applied to every conversation in the organization, and taking precedence over a member's own account-wide instructions where both speak. A build for a member of such an org states which layer above it already speaks, so the Project block does not repeat it.

**[reported]** Custom instructions are widely reported to accept roughly 8,000 characters. Anthropic publishes no figure (re-checked 2026-08-17). Treat it as a working budget, warn near it, and never fail a build on it.

**Knowledge-file plan conventions.** File names are part of retrieval — Claude uses them to decide what to pull, so `q4-2026-pricing-policy.pdf` outperforms `doc1.pdf` materially. Prefer several well-named files over one omnibus upload. Common formats (PDF, DOCX, CSV, TXT, MD, HTML) are accepted.

## Profile preferences (claude.ai)

Account-level, applies to every chat everywhere including inside Projects. **[published]** The Settings field is now labeled **Instructions for Claude** ("account-wide settings that help Claude understand your general instructions"); the pack keeps *profile preferences* as the layer's name. **[reported]** Approximately 1,500 characters; no published figure (re-checked 2026-08-17). This is the home for identity, tone, and format preferences that never vary by project — a rule repeated in three Projects belongs here instead, and a rule that varies by project must never be here.

## CLAUDE.md and the memory hierarchy

**[published]** Memory files load automatically at session start, broadest scope first, so a project instruction appears in context after a user instruction:

| Scope | Location | Shared with |
|---|---|---|
| Managed policy | OS-managed system path, or the `claudeMd` key in managed settings | Everyone in the org; cannot be excluded |
| User memory | `~/.claude/CLAUDE.md` | Just you, all projects |
| Project memory | `./CLAUDE.md` or `./.claude/CLAUDE.md` | The team, via source control |
| Project local | `./CLAUDE.local.md` — add to `.gitignore` | Just you, this checkout |

Ancestor `CLAUDE.md` and `CLAUDE.local.md` files load in full at launch; files in subdirectories load on demand when Claude reads there. `CLAUDE.local.md` is supported again as the personal per-project file (the 2026-07-30 pass recorded it as deprecated); a gitignored copy exists only in the worktree that created it, so the worktree-safe form of a personal rule is a home-directory import.

**[published] `.claude/rules/`** — topic files (`testing.md`, `api-design.md`, discovered recursively) loaded at launch with the same priority as `.claude/CLAUDE.md`. A rule carrying `paths:` frontmatter (glob patterns) loads only when Claude works with matching files. `~/.claude/rules/` is the user-level counterpart and loads before project rules. This is a placement fact the layer stack now uses: a rule true only for some files is a path-scoped rule, not a `CLAUDE.md` bullet and not a skill.

**[published]** `CLAUDE.md` supports `@path/to/file` imports, relative and absolute, to a maximum depth of four hops. Importing from the home directory is the way to let a teammate add personal instructions that aren't committed and that survive worktrees. An import in a *project* file that resolves outside the working directory triggers a one-time approval dialog. Block-level HTML comments are stripped before injection — maintainer notes cost no context.

**Two properties that change how a build is written.** **[published]** `CLAUDE.md` content is delivered as a *user message after the system prompt*, not as part of the system prompt — Claude reads it and tries to follow it, with no guarantee of strict compliance, especially for vague or conflicting instructions; the docs say it in one line: Claude treats CLAUDE.md as context, not enforced configuration — to block an action regardless of what Claude decides, use a PreToolUse hook. That is the documented basis for the layer stack's hooks rule. **[published]** Imports organize instructions but do **not** reduce context cost — imported files still load at launch. A `CLAUDE.md` split into six imported files costs what the one file cost.

**[published]** Target under 200 lines per `CLAUDE.md` file: longer files consume more context and reduce adherence. *(Moved from **[reported]** to **[published]** 2026-08-17 — the memory docs now state the number; it was a community norm before.)* Use it as the audit's budget dimension.

**[published]** `/init` generates a baseline `CLAUDE.md` by scanning the repo and, where one already exists, suggests improvements rather than overwriting it; `/memory` lists and opens the memory files; `/context` shows which ones actually loaded this session; `/doctor` proposes trims for a checked-in `CLAUDE.md`. Claude Code reads `CLAUDE.md`, not `AGENTS.md` — a repo that keeps `AGENTS.md` for other agents imports it with `@AGENTS.md`. All worth naming at handback: a build that ignores an existing `/init` output and writes over it is doing the user's review for them.

## The `.claude` directory

Two directories, different jobs: `./.claude/` in the repo is team configuration and is committed; `~/.claude/` is personal and is not.

| File | Scope | Committed |
|---|---|---|
| `.claude/settings.json` | Project — permissions, hooks, env, model | Yes |
| `.claude/settings.local.json` | Machine-local overrides | No — added to global git excludes when Claude Code writes it |
| `~/.claude/settings.json` | User, all projects | n/a |
| `.claude/CLAUDE.md`, `.claude/rules/*.md` | Project instructions and rules | Yes |
| `.claude/skills/<name>/SKILL.md` | Project skills | Yes |
| `.claude/agents/<name>.md` | Project subagents | Yes |

**[published]** Settings files merge — managed above all, then command-line, local, project, user; scalars override, arrays concatenate and de-duplicate, objects deep-merge — and permission rules merge across every scope. Rules evaluate **deny first, then ask, then allow**, first match wins, and rule specificity does not change the order: a deny at any scope beats an allow at any other, and a broad deny cannot carry allowlist exceptions. Hooks are configured under the `hooks` key in any settings file (and in a skill's or subagent's frontmatter); a hook script inside the repo is referenced as `${CLAUDE_PROJECT_DIR}/...`.

**[published] Trust.** `permissions.allow` rules and `additionalDirectories` in a repo's `.claude/settings.json` apply only after the workspace-trust dialog for that folder; deny and ask rules apply regardless. Hooks and the `env` block in a repo's settings run **before** trust, and a `claude -p` or SDK session shows no dialog at all — so a committed hook is executable code the repo ships, and an unfamiliar repo is opened with `--bare` or `disableAllHooks`. Bare `Bash` (or `Bash(*)`) is the whole tool: as an allow it is a blanket allow, as a deny it removes the tool.

**Emit rules.** A generated `settings.json` ships with explicit deny rules for destructive commands and never with a blanket allow. An `ask` rule is a prompt to a human: where the file may serve an unattended session — a routine, a scheduled task, `claude -p` — nobody answers, so the call is denied or the run stalls on the prompt, and either way the task does not complete as written; a committed `settings.json` on such a path carries allow and deny only, and an interactive-only rig may keep `ask`. The generated default is the finding in an audit even where prose invites the user to tighten it: a config ships as written.

**[published] Skill frontmatter, for an audit that meets one under `.claude/skills/`.** `allowed-tools` is a per-turn permission **grant** — the listed tools run without asking while the skill is invoked — never a restriction; `disallowed-tools` removes tools from the pool; both are Claude Code fields, and claude.ai uploads, the Skills API, and `package_skill.py` accept exactly six keys (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`) and reject any other with an "Unexpected key(s)" error. The audit reports that much and hands the skill itself to skillwright.

## MCP server configuration

**[published]** MCP servers are configured *outside* `settings.json`: project scope in `.mcp.json` at the repository root (committed), user scope at the top level of `~/.claude.json`, local scope under the project's entry in `~/.claude.json`. Putting an `mcpServers` key into `settings.json` is a schema error, and it is a common enough mistake to be worth checking on any audit that finds one. `settings.json` carries only the approval and allow/deny lists (`enabledMcpjsonServers`, `disabledMcpjsonServers`, `enableAllProjectMcpServers`, `allowedMcpServers`, `deniedMcpServers`).

**[published]** An interactive session prompts before using a repo's `.mcp.json` servers; approvals committed to `.claude/settings.json` are ignored until the folder is trusted, and a `claude -p` or SDK session connects them without asking. `.mcp.json` expands `${VAR}` and `${VAR:-default}` in `command`, `args`, `env`, `url`, and `headers` — the credential indirection an emitted file uses; an unset variable with no default loads as literal text with a warning.

> **Open item of 2026-07-30, closed 2026-08-17.** The MCP reference places `.mcp.json` at the project root; the `.claude/` reading came from plugins, which carry their own `.mcp.json` at the plugin root. An audit may now treat a repo-level `.claude/.mcp.json` as misplaced.

**Emit rule.** A generated `.mcp.json` pins server versions rather than floating them, and carries no credential — env-var indirection only, with the variable named and the value never written into the file.

## Auto-memory

**[published]** Claude Code keeps its own memory separately from `CLAUDE.md`, per repository (shared across worktrees), at `~/.claude/projects/<project>/memory/`: a `MEMORY.md` index whose first 200 lines or 25 KB load at every session start, plus topic files read on demand. On by default; `/memory` toggles it (writing `autoMemoryEnabled` to user settings), a project can set `autoMemoryEnabled: false`, and `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` disables it outright. It does not load into subagents.

This layer is **not authored** by a build. It is included in the stack so an audit can spot the failure mode: a user hand-writing into the auto-memory file, or a `CLAUDE.md` restating what auto-memory already learned. Both are found and reported; neither is generated.

## Where this file stops — the agentwright line

Cowork tasks, Claude Code routines (cloud), and desktop scheduled tasks are **not documented here** and are not rigwright's to emit. Their fields, cadence presets, trigger types, missed-run semantics, and enforcement surfaces live in agentwright's `platform-notes.md`, which is the pack's single home for anything that runs unattended. A run that reaches for a scheduler here has crossed the seam and should hand off by name rather than duplicating the table.
