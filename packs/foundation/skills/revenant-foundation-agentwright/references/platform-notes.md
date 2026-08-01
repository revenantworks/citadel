# Platform Notes — Volatile Baseline *(single update surface)*

> **Last verified: 2026-07-30.** This is the **only** file "agentwright refresh" regenerates — what platforms offer for enforcement drifts with releases; the ten control areas in `design-checklist.md` do not. When the stamp is >60 days old, treat platform specifics here as possibly stale and say so; the checklist itself never goes stale.

The checklist decides *what* an agent's system must enforce; this file records what current platforms *provide* to enforce it. When an ops spec or audit names a concrete platform mechanism, the checklist decision comes first and the mechanism second — and the mechanism comes from here. A run that stays at the decision level never opens this file; SKILL.md *Load budget* is the source of that rule.

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

**Claude Code / Claude Agent SDK** — three deterministic gates, layered: (1) **permissions** — allow/ask/deny rules per tool, four permission modes including a structurally read-only plan mode, org-wide managed settings; (2) **sandboxing** — filesystem + network boundaries on Bash and subprocesses, domain allowlists; (3) **hooks** — 12 lifecycle events, 4 handler types; PreToolUse receives the full tool call and can allow, deny with a reason fed back to the model, escalate to a human, or rewrite the input; PostToolUse closes the loop. Hooks are deterministic (they don't ask the model) — but they are also an attack surface: 2026 CVEs turned repo-supplied hooks into an RCE vector (malicious `settings.json` executing on load; a PyPI worm planting SessionStart hooks). Treat any hook you didn't write as untrusted code; pin versions; a PreToolUse hook that exits 0 *overrides* deny rules — a known footgun.

**claude.ai / Cowork** — scheduled tasks (native cadences: hourly / daily / weekly / weekdays), connectors, and skills; approval prompts are the human gate. No hook layer — guardrails live in the task prompt plus the platform's own action confirmations.

**OpenAI Agents SDK** — the recommended code path (Agent Builder and Evals are EOL 2026-11-30): Agents / Runner / Tools / Handoffs / Guardrails / Sessions primitives; input and output guardrails run in parallel and fail fast; **resumable approval flows** — the runner pauses on a flagged action and resumes after human sign-off; built-in tracing; MCP tools first-class. The standalone guardrails library covers PII masking and jailbreak detection.

**MCP (any host)** — approved-server allowlists are the control; real CVEs in popular servers (e.g. mcp-server-git) make "which servers, pinned how" a protected-resource decision, not a convenience one. Tool descriptions are untrusted input to the host.

## Scheduling / cadence surfaces

Native schedulers: Cowork scheduled tasks and Claude Code desktop tasks (hourly / daily / weekly / weekdays — no cron grammar); Claude Code cloud routines (schedule, API, or GitHub event, combinable, 1-hour floor); CI cron (GitHub Actions et al.) for repo-anchored agents; the Agents SDK runs on any external scheduler. Full per-target fields, gates, and missed-run behavior are in **Emit targets** below — single-homed there, not restated here. The checklist's cadence decision maps to whichever of these the agent lives on — and a cadence the platform can't express (e.g. "every 61 days" on Cowork) becomes a nearest-cadence run plus an in-run date check.

## Emit targets — fields, enforcement, and missed runs

What `agentwright emit` renders into, and — the column that matters — what each target **cannot** enforce. The checklist decides the control; this table decides whether the platform can hold it or whether the prompt has to.

| Target | Triggers | Scope control | Gate | Kill switch | Untrusted-content isolation | Verified |
|---|---|---|---|---|---|---|
| Claude Code routine *(cloud)* | schedule (1-hour floor) · API POST with per-routine bearer token · GitHub events; combinable | repos cloned fresh per run, `claude/`-prefixed branches, environment network allowlist, per-routine connectors | none — runs autonomously, no prompts | disable trigger · revoke token · teardown environment | fresh clone per run; no local filesystem | 2026-07-30 |
| Claude Code desktop task | Manual · Hourly · Daily · Weekdays · Weekly (1-minute floor) | working folder; optional isolated git worktree | per-task permission mode; Manual mode **stalls** until approved | pause · delete · revoke saved tool approvals | worktree toggle only | 2026-07-30 |
| Cowork scheduled task | hourly · daily · weekly · weekdays · manual | folder choice; connectors | approval prompts | pause · delete | folder scope only | 2026-07-30 |
| CI cron *(GitHub Actions et al.)* | schedule · repo events | repo + runner scope | branch protection, environments, required reviewers | disable workflow · revoke token | ephemeral runner | 2026-07-30 |
| Workflow runner *(n8n, Zapier, Make)* | schedule · webhook · app events | per-connection credentials | per-step, and you build it | disable workflow · revoke connection | you build it | 2026-07-30 |
| ChatGPT Tasks | schedule only; ~10 active cap | none | **none** | delete the task | **none** | 2026-07-30 |
| Gemini Scheduled Actions | schedule only; ~10 active cap | none | **none** | delete the action | **none** | 2026-07-30 |

**The thin-scheduler finding, and why emit states a gap rather than a spec.** The two general-assistant surfaces are *prompt plus cadence* and nothing else — no permission model, no tool-grant scope, no isolation layer, and a kill switch that is only deletion. Ten control areas cannot be enforced there; at most they can be *described* to a model that may or may not comply, which is the same probabilistic footing the checklist exists to avoid. An emit to one of these targets says so in plain terms, keeps the controls that survive as prompt-level instructions, and names the ones that do not survive at all. Where the spec's blast-radius decision depends on a control the target cannot hold, the honest emit is that the surface is wrong for this agent — SKILL.md *Entry — Emit* step 5 carries that as a Restraint condition.

**Missed-run semantics differ per target and change what a prompt must say.** Claude Code desktop checks on wake for runs missed in the last seven days and starts **exactly one** catch-up for the most recently missed time, discarding older ones — so a 9am task can fire at 11pm, and a spec that cares about timing puts its own clock check in the instruction. Cowork local tasks likewise depend on the machine being awake and skip otherwise. Cloud routines and the general-assistant schedulers do not depend on the user's machine. Every emitted schedule states which of these applies; it is the field no scheduler's own form asks for.

**Stagger.** Anthropic-managed schedulers start a run a few minutes after the nominal time, deterministically — the same task always takes the same offset. Specs that key on exact wall-clock boundaries are written against the *date*, not the minute.

## Kill-switch & governance state

A real kill-switch is **layered**, not one button: session termination → permission revocation → circuit breakers → rollback → full deactivation, with depth scaled to the agent's autonomy. Joint CISA/NSA guidance (2026-04) tells operators to assess failure scenarios before deploying agentic AI and keep intervene/deactivate ability once running; EU and Singapore frameworks treat deactivation ability as a core requirement. The gap is real: only ~21% of enterprises report mature agent governance, and more than a third admit they could not shut down a rogue agent today *(industry-survey figures from the 2026-07-23 build-time research pass — vendor/analyst-reported, directional not audited)* — the reason the checklist makes kill-switch layers a first-class area rather than an ops afterthought.

## Injection state of the art

Prompt injection remains **unsolved** — current best practice is blast-radius limitation, not prevention: sandbox so a successful injection hits hard limits; deterministic hooks/guardrails on the actions that matter; untrusted content quarantined per the trust-tier rule. Two field notes worth carrying into specs: agent-authored commits leak credentials at roughly twice the human baseline (secret-blocking rules earn their keep), and the guardrail mechanism itself is part of the attack surface (see the hook CVEs above) — audit the enforcement layer like any other dependency.

## Checklist-area → platform-mechanism map

| Checklist area | Current mechanism (by platform) |
|---|---|
| Hard guardrails | Claude Code deny rules + hooks · Agents SDK guardrails (fail-fast) |
| Soft guardrails / HITL | ask-rules + approval prompts · resumable approval flows |
| Kill-switch layers | permission revocation, sandbox teardown, scheduler disable — layered per above |
| Protected resources | sandbox scopes, domain allowlists, MCP server allowlists |
| Cadence | Cowork + desktop native cadences · cloud routines (1h floor) · CI cron · external schedulers · assistant schedulers (schedule only, no enforcement) |
| Injection hygiene | sandbox blast-radius limits + trust tiers; hooks as deterministic filters |
| Output contracts / handoffs | Agents SDK handoff + session primitives; schema validation at the boundary |

The seven rows above cover areas 1–6 and 9 — guardrail tiers (2) spans two rows, and output contracts (6) shares one with handoff schemas (5).

Three areas have no row. **Zero-signal (7)** and **failure & retry (8)** are decided by `design-checklist.md` and the SKILL body; no platform mechanism implements them. **Trust tiers (10)** has no row of its own because its enforcement is the mechanisms already listed above — read-only permission modes, tool allow/deny rules, approved-server allowlists (*Enforcement surfaces*), and schema validation at the boundary (*Output contracts / handoffs*) — and the injection-hygiene row names trust tiers outright. Blast radius is the pre-checklist sizing step (SKILL.md *Turn shape 3*), not one of the ten areas.
