# Platform Notes — Volatile Baseline *(single update surface)*

> **Last verified: 2026-07-23.** This is the **only** file "agentsmith refresh" regenerates — what platforms offer for enforcement drifts with releases; the ten control areas in `design-checklist.md` do not. When the stamp is >60 days old, treat platform specifics here as possibly stale and say so; the checklist itself never goes stale.

The checklist decides *what* an agent's system must enforce; this file records what current platforms *provide* to enforce it. An ops spec names the checklist decision first, then the platform mechanism that implements it — from here.

## Contents

- Enforcement surfaces by platform
- Scheduling / cadence surfaces
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

Native schedulers: Cowork scheduled tasks (hourly / daily / weekly / weekdays — no cron grammar); CI cron (GitHub Actions et al.) for repo-anchored agents; the Agents SDK runs on any external scheduler. The checklist's cadence decision maps to whichever of these the agent lives on — and a cadence the platform can't express (e.g. "every 61 days" on Cowork) becomes a nearest-cadence run plus an in-run date check.

## Kill-switch & governance state

A real kill-switch is **layered**, not one button: session termination → permission revocation → circuit breakers → rollback → full deactivation, with depth scaled to the agent's autonomy. Joint CISA/NSA guidance (2026-04) tells operators to assess failure scenarios before deploying agentic AI and keep intervene/deactivate ability once running; EU and Singapore frameworks treat deactivation ability as a core requirement. The gap is real: only ~21% of enterprises report mature agent governance, and more than a third admit they could not shut down a rogue agent today — the reason the checklist makes kill-switch layers a first-class area rather than an ops afterthought.

## Injection state of the art

Prompt injection remains **unsolved** — current best practice is blast-radius limitation, not prevention: sandbox so a successful injection hits hard limits; deterministic hooks/guardrails on the actions that matter; untrusted content quarantined per the trust-tier rule. Two field notes worth carrying into specs: agent-authored commits leak credentials at roughly twice the human baseline (secret-blocking rules earn their keep), and the guardrail mechanism itself is part of the attack surface (see the hook CVEs above) — audit the enforcement layer like any other dependency.

## Checklist-area → platform-mechanism map

| Checklist area | Current mechanism (by platform) |
|---|---|
| Hard guardrails | Claude Code deny rules + hooks · Agents SDK guardrails (fail-fast) |
| Soft guardrails / HITL | ask-rules + approval prompts · resumable approval flows |
| Kill-switch layers | permission revocation, sandbox teardown, scheduler disable — layered per above |
| Protected resources | sandbox scopes, domain allowlists, MCP server allowlists |
| Cadence | Cowork native cadences · CI cron · external schedulers |
| Injection hygiene | sandbox blast-radius limits + trust tiers; hooks as deterministic filters |
| Output contracts / handoffs | Agents SDK handoff + session primitives; schema validation at the boundary |

Areas not listed (zero-signal, failure/retry, blast radius) are spec logic, not platform features — the checklist owns them outright.
