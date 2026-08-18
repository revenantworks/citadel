# Platform Notes — Volatile Baseline *(single update surface)*

> **Last verified: 2026-08-17.** This is the **only** file "agentwright refresh" regenerates — what platforms offer for enforcement drifts with releases; the ten control areas in `design-checklist.md` do not. When the stamp is >60 days old, treat platform specifics here as possibly stale and say so; the checklist itself never goes stale.

The checklist decides *what* an agent's system must enforce; this file records what current platforms *provide* to enforce it. When an ops spec or audit names a concrete platform mechanism, the checklist decision comes first and the mechanism second. The mechanism comes from here. A run that stays at the decision level never opens this file; SKILL.md *Load budget* is the source of that rule.

**Per-row stamps, added 2026-07-30.** Non-Anthropic rows carry their own verified date. A refresh re-verifies what it can reach and **re-stamps only those rows**, leaving the others at their older date with the age visible, rather than blocking the whole file or silently restamping an unchecked row. A row more than one cadence behind the file header is quoted with its age stated.

## Contents

- Enforcement surfaces by platform
- Scheduling / cadence surfaces
- Emit targets — fields, enforcement, and missed runs
- Kill-switch & governance state
- Injection state of the art
- Checklist-area → platform-mechanism map

---

## Enforcement surfaces by platform

**Claude Code / Claude Agent SDK** — three deterministic gates, layered: (1) **permissions** — allow/ask/deny rules per tool, evaluated deny → ask → allow, first match wins; six permission modes (default, acceptEdits, plan, auto — a classifier reviews actions in place of the human — dontAsk, bypassPermissions); org-wide managed settings that can pin rules, hooks, and MCP servers to the managed layer alone (`allowManagedPermissionRulesOnly`, `allowManagedHooksOnly`, `strictPluginOnlyCustomization`); (2) **sandboxing** — OS-level filesystem + network boundaries on Bash and its subprocesses, domain allow/deny lists, documented to hold "even if a prompt injection bypasses Claude's decision-making"; (3) **hooks** — 31 lifecycle events, 5 handler types (command, http, mcp_tool, prompt, agent); PreToolUse receives the full tool call and can deny with a reason fed back to the model, force a prompt, rewrite the input, or let it proceed; PostToolUse closes the loop. Hooks are deterministic (they don't ask the model). **Hook decisions never bypass permission rules**: a matching deny rule blocks the call whatever a hook returns, and a blocking hook (exit 2) beats an allow rule — the older "a hook that exits 0 overrides deny" footgun is not what the docs describe (re-verified 2026-08-17). But hooks are also an attack surface: 2026 CVEs turned repo-supplied hooks into an RCE vector (a malicious `settings.json` executing on load — CVE-2025-59536 / CVE-2026-21852; npm and PyPI worms planting SessionStart hooks, still active 2026-08), and hooks in a repository's settings files run in `claude -p` and SDK sessions with no workspace-trust dialog. Treat any hook you didn't write as untrusted code; pin versions; open an unfamiliar repo with `--bare` or `--settings '{"disableAllHooks": true}'`. A skill marked `disable-model-invocation: true` reaches a scheduled fire as plain text and does not execute (v2.1.196+) — a spec whose prompt is a skill name confirms the flag is off, or the run silently does nothing.

**claude.ai / Cowork** — scheduled tasks (hourly / daily / weekly / weekdays / manual) that run remotely by default — only a task needing local files or apps runs on the machine — each with its own approval mode; connectors, skills, and plugins carry into the run; approval prompts are the human gate. No hook layer — guardrails live in the task prompt plus the platform's own action confirmations.

**OpenAI Agents SDK** — the recommended code path (Agent Builder and Prompt Objects shut down 2026-11-30, deprecation notice 2026-06-03): Agents / Runner / Tools / Handoffs / Guardrails / Sessions primitives; input, output, and tool guardrails, blocking or parallel; **resumable approval flows** — a tool marked `needs_approval` records an interruption, the run pauses, and resumes from saved state after human sign-off; built-in tracing; MCP tools first-class. The standalone guardrails library covers PII masking and jailbreak detection. *(verified 2026-08-17)*

**MCP (any host)** — approved-server allowlists are the control; real CVEs in popular servers (three in mcp-server-git, disclosed 2026-01-20, chainable to RCE through a prompt injection) make "which servers, pinned how" a protected-resource decision, not a convenience one. Tool descriptions are untrusted input to the host. A server can mark a tool `requiresUserInteraction`, which forces a human prompt on every call and refuses one-tap or scripted approval — the mechanism for a gate that must reach a person. *(verified 2026-08-17)*

## Scheduling / cadence surfaces

Native schedulers: Cowork scheduled tasks (hourly / daily / weekly / weekdays / manual; remote by default) and Claude Code desktop tasks (Manual / Hourly / Daily / Weekdays / Weekly presets, custom cron by asking, 1-minute floor); Claude Code cloud routines (schedule with a 1-hour floor, one-off, API, or GitHub event, combinable); the session-scoped `/loop` (1-minute floor, dies with the session, expires after seven days — a polling aid, not an unattended surface); CI cron (GitHub Actions et al., 5-minute floor) for repo-anchored agents; the Agents SDK runs on any external scheduler. Full per-target fields, gates, and missed-run behavior are in **Emit targets** below — single-homed there, not restated here. The checklist's cadence decision maps to whichever of these the agent lives on. A cadence the platform can't express (e.g. "every 61 days" on Cowork) becomes a nearest-cadence run plus an in-run date check.

## Emit targets — fields, enforcement, and missed runs

What `agentwright emit` renders into, and — the column that matters — what each target **cannot** enforce. The checklist decides the control; this table decides whether the platform can hold it or whether the prompt has to.

| Target | Triggers | Scope control | Gate | Kill switch | Untrusted-content isolation | Verified |
|---|---|---|---|---|---|---|
| Claude Code routine *(cloud)* | schedule — presets or cron, 1-hour floor, one-off · API POST with a per-routine bearer token (rotate / revoke) · GitHub pull-request and release events with filters; combinable; a daily run cap per account | repos cloned fresh per run, `claude/`-prefixed branches (pushes elsewhere refused when protected or another author's), environment network allowlist (Trusted default list), per-routine connectors — **all connected by default; remove the rest** | none — runs autonomously; every included connector tool, writes included, runs without asking | pause toggle · delete · revoke token · org-wide Routines toggle (Team / Enterprise) | fresh clone per run, no local filesystem; API and Run-now `text` arrives wrapped as untrusted `<routine-fire-payload>` that the saved prompt must opt into | 2026-08-17 |
| Claude Code desktop task | Manual · Hourly · Daily · Weekdays · Weekly presets; custom cron by asking (1-minute floor) | working folder, trusted before save; optional isolated git worktree; `~/.claude/settings.json` allow rules apply | per-task permission mode; Manual mode **stalls** until approved; org-`ask` connector tools stall every run | pause (Status toggle) · delete · revoke saved tool approvals — the task can rewrite its own schedule and prompt via `update_scheduled_task`, so pause and the approvals list are the human layers | worktree toggle only | 2026-08-17 |
| Cowork scheduled task | hourly · daily · weekly · weekdays · manual | optional folder; connectors, skills, plugins; runs remotely unless it needs local files or apps | per-task approval mode; approval prompts | pause · delete | folder scope only | 2026-08-17 |
| CI cron *(GitHub Actions et al.)* | schedule (5-minute floor, delayed under load; a public repo's schedule auto-disables after 60 idle days) · repo events · `workflow_dispatch` | repo + runner scope | branch protection, environments, required reviewers | disable workflow · revoke token | ephemeral runner | 2026-08-17 |
| Workflow runner *(n8n, Zapier, Make)* | schedule · webhook · app events | per-connection credentials | per-step, and you build it | disable workflow · revoke connection | you build it | 2026-08-17 |
| ChatGPT Tasks | schedule only; at most once per hour; 3–15 active by plan tier; unattended tasks auto-pause | none | **none** | pause · delete (Scheduled hub) | **none** — checks the web and connected apps and notifies rather than acts | 2026-08-17 |
| Gemini Scheduled Actions | schedule only (daily / weekly / monthly or once); 10 active cap | none | **none** | pause · delete | **none** — prepares content through connected Workspace apps and notifies | 2026-08-17 |

**The thin-scheduler finding, and why emit states a gap rather than a spec.** The two general-assistant surfaces are *prompt plus cadence* and nothing else — no permission model, no tool-grant scope, no isolation layer, and a kill switch that is only pause or deletion. Ten control areas cannot be enforced there; at most they can be *described* to a model that may or may not comply, which is the same probabilistic footing the checklist exists to avoid. An emit to one of these targets says so in plain terms, keeps the controls that survive as prompt-level instructions, and names the ones that do not survive at all. Where the spec's blast-radius decision depends on a control the target cannot hold, the honest emit is that the surface is wrong for this agent — SKILL.md *Entry — Emit* step 5 carries that as a Restraint condition.

**Missed-run semantics differ per target and change what a prompt must say.** Claude Code desktop checks on wake for runs missed in the last seven days and starts **exactly one** catch-up for the most recently missed time, discarding older ones; a run skipped because the machine slept, the prior run was still going, or other tasks were running is listed in the task's history with its reason. So a 9am task can fire at 11pm, and a spec that cares about timing puts its own clock check in the instruction. Cowork scheduled tasks run remotely by default and no longer depend on the machine; a task that must run locally still does, and the support article states no catch-up rule for it. Cloud routines and the general-assistant schedulers do not depend on the user's machine. A routine run's green status means the session exited without an infrastructure error, not that the task succeeded — the transcript is the only evidence, which is what the zero-signal line is for. Every emitted schedule states which of these applies; it is the field no scheduler's own form asks for.

**Stagger.** Anthropic-managed schedulers start a run a few minutes after the nominal time, deterministically — the same task or routine always takes the same offset; the session-scoped `/loop` adds up to 30 minutes for hourly-or-slower tasks. Specs that key on exact wall-clock boundaries are written against the *date*, not the minute.

## Kill-switch & governance state

A real kill-switch is **layered**, not one button: session termination → permission revocation → circuit breakers → rollback → full deactivation, with depth scaled to the agent's autonomy. The Five Eyes joint guidance *Careful Adoption of Agentic AI Services* (CISA with US and allied agencies, 2026-04-30) tells operators to assume unexpected behavior, grant minimum access, design for containment and reversibility, and keep the ability to intervene and deactivate once running *(verified 2026-08-17)*; EU and Singapore frameworks treat deactivation ability as a core requirement *(carried from the 2026-07-23 pass, not re-verified)*. The gap is real: only ~21% of enterprises report mature agent governance, and more than a third admit they could not shut down a rogue agent today *(industry-survey figures from the 2026-07-23 build-time research pass — vendor/analyst-reported, directional not audited)* — the reason the checklist makes kill-switch layers a first-class area rather than an ops afterthought.

## Injection state of the art

Prompt injection remains **unsolved** — current best practice is blast-radius limitation, not prevention: sandbox so a successful injection hits hard limits; deterministic hooks/guardrails on the actions that matter; untrusted content quarantined per the trust-tier rule. Claude Code's own docs now say the same in their own words: permission rules and the sandbox are enforced by the client and hold when an injection has already turned the model, while prompts and `CLAUDE.md` are context, not enforcement *(verified 2026-08-17)*. Two field notes worth carrying into specs: agent-authored commits leak credentials at roughly twice the human baseline (secret-blocking rules earn their keep) *(carried from the 2026-07-23 pass, not re-verified)*, and the guardrail mechanism itself is part of the attack surface (see the hook CVEs above) — audit the enforcement layer like any other dependency.

## Checklist-area → platform-mechanism map

| Checklist area | Current mechanism (by platform) |
|---|---|
| Hard guardrails | Claude Code deny rules (deny-first, not bypassable by a hook) + hooks + sandbox · Agents SDK guardrails (blocking or parallel) |
| Soft guardrails / HITL | ask-rules + approval prompts · MCP `requiresUserInteraction` and an org connector `ask` policy (prompt every call, no remember) · resumable approval flows |
| Kill-switch layers | permission revocation, sandbox teardown, scheduler pause or disable, token revocation — layered per above |
| Protected resources | sandbox scopes, domain allowlists, MCP server allowlists, routine environment allowlists |
| Cadence | Cowork + desktop native cadences · cloud routines (1h floor, one-off, API, GitHub events) · CI cron · external schedulers · assistant schedulers (schedule only, no enforcement) |
| Injection hygiene | sandbox blast-radius limits + trust tiers; hooks as deterministic filters; the routine fire-payload wrapper |
| Output contracts / handoffs | Agents SDK handoff + session primitives; schema validation at the boundary |

The seven rows above cover areas 1–6 and 9 — guardrail tiers (2) spans two rows, and output contracts (6) shares one with handoff schemas (5).

Three areas have no row. **Zero-signal (7)** and **failure & retry (8)** are decided by `design-checklist.md` and the SKILL body; no platform mechanism implements them. **Trust tiers (10)** has no row of its own because its enforcement is the mechanisms already listed above — read-only permission modes, tool allow/deny rules, approved-server allowlists (*Enforcement surfaces*), and schema validation at the boundary (*Output contracts / handoffs*) — and the injection-hygiene row names trust tiers outright. Blast radius is the pre-checklist sizing step (SKILL.md *Turn shape 3*), not one of the ten areas.
