# foundation — pack-spec baton

> Retro-fitted 2026-07-14 (self-audit finding P2-2): the roster predates the
> pack-spec doctrine, so this baton was reconstructed from the shipped pack and
> the 2026-07-14 self-audit rather than written at the original roster gate.
> From here it updates after every member ship or roster decision. When memory
> of a conversation and this spec disagree, trust the spec.

**Pack:** foundation · **Profile:** standalone · **Brand:** revenant ·
**Stamped:** 2026-07-14 · **Status:** 8 of 8 built — all SHIPPED ·
**Release:** Citadel 1.0 (pack 1.0.0 - tag `foundation-v1.0.0`)

## Approved roster

| Member | Job (one line) | Status | Version @ pack 1.0.0 |
|---|---|---|---|
| `revenant-foundation-skillsmith` | Builds, audits, brands, and ports Agent Skills and packs | SHIPPED | 1.0.0 |
| `revenant-foundation-promptsmith` | Builds, scores, and hardens prompts with model-tier routing | SHIPPED | 1.0.0 |
| `revenant-foundation-commsmith` | Shapes messages per channel, audience, and saved voice; audits drift | SHIPPED | 1.0.0 |
| `revenant-foundation-agentsmith` | Designs and audits autonomous agent systems | SHIPPED | 1.0.0 |
| `revenant-foundation-loresmith` | Research-verified verdicts and playbook reference docs | SHIPPED | 1.0.0 |
| `revenant-foundation-brandsmith` | Builds the brand definition; audits everything for drift (7 categories); exports payloads + HTML guide card | SHIPPED | 1.0.0 |
| `revenant-foundation-evalsmith` | Authors and audits eval suites — build-time, zero runtime deps | SHIPPED | 1.0.0 |
| `revenant-foundation-tokensmith` | Measures, budgets, and slims the token footprint of LLM-facing artifacts | SHIPPED | 1.0.0 |

## Trigger-partition table

Re-run 2026-07-14 against the real shipped descriptions — **12/12 route to
exactly one destination**; every member appears once; two near-misses exit the
pack correctly.

| # | Realistic request | Routes to |
|---|---|---|
| 1 | "Write a system prompt for my research agent" | promptsmith |
| 2 | "Score this SKILL.md against best practices" | skillsmith |
| 3 | "Rewrite this Slack update for the exec channel" | commsmith |
| 4 | "Add guardrails and a kill switch to my nightly scan agent" | agentsmith |
| 5 | "Which task app should I commit to — verdict with sources" | loresmith |
| 6 | "Check the repo for off-palette colors and stale taglines" | brandsmith |
| 7 | "Write trigger evals for the commsmith skill" | evalsmith |
| 8 | "My CLAUDE.md is 6k tokens — slim it, same behavior" | tokensmith |
| 9 | "Build an MCP server for my calendar API" | **outside** → mcp-builder (first-party) |
| 10 | "Review this PR for injection vulnerabilities" | **outside** → engineering plugins / security harness |
| 11 | "Is there a real niche for a meal-prep skill?" | skillsmith (loresmith defers skills to it by name) |
| 12 | "This prompt works — just make it cheaper to run" | tokensmith (promptsmith reciprocates the boundary) |

## Adopt register

Strong incumbents own these jobs — recorded, linked, left out of the roster.

| Job | Incumbent | Recorded |
|---|---|---|
| MCP server generation | `mcp-builder` — anthropics/skills, first-party | 2026-07-14 |
| Baseline skill drafting/review | `skill-creator` — built into claude.ai and Claude Code | 2026-07-14 |
| Code-level engineering (review, tests, debug, incidents) | Anthropic's open-sourced engineering plugins | 2026-07-14 |
| Document production (docx/pdf/pptx/xlsx) | first-party document skills | 2026-07-14 |
| Broad multi-source research reports | Claude Research feature (loresmith partitions this away) | 2026-07-14 |
| Code-level threat coverage | security harness / STRIDE-class skills (agentsmith partitions this away) | 2026-07-14 |

## Recorded, not built (nice-to-have)

- **contextsmith** — CLAUDE.md / project-instructions / memory-file
  architecture. Mostly decomposes into tokensmith (footprint) + promptsmith
  (instruction quality); a ninth member would blur two seams to cover one
  sliver. Earns a build only if asked for by name at a future gate.
- **runsmith** — runtime review of scheduled-agent runs (logs, behavior
  drift). No incumbent found 2026-07-14; partially covered by agentsmith
  audit; platform-bound. Record.

## Decisions log

- 2026-07-13 — Pack born at uniform 1.0.0 baseline (seven members); tokensmith
  added same day (roster of eight); conformance C-1/C-2 adopted pack-wide;
  restamp policy lazy (per-release flip allowed).
- 2026-07-14 — Pack self-audit (Phase 1.8 step 1), gated and approved:
  verdict **KEEP 8 / COMBINE 0 / BUILD 0**; partition test 12/12; findings
  P2-1 (promptsmith↔tokensmith boundary — applied, promptsmith 1.0.1) and
  P2-2 (this baton — applied). Combine analysis rejected all four candidate
  merges (evalsmith⇄skillsmith, tokensmith⇄promptsmith,
  brandsmith⇄skillsmith-configure, commsmith⇄loresmith).
- 2026-07-14 — Release bar adopted (closes OD12): release-solid = set
  discoverability pass with no open P0/P1 + repo/release/account parity +
  a current capstone card with one live run.
- 2026-07-14 — **Foundation 1.0** declared as pack release 1.2.0, tag
  `v1.2.0`; semver tags only going forward (date tags kept as history).
  Member versions stay independent per pack norm — skillsmith exempt from the
  1.0.x line (no semver regression from 1.2.x).
- 2026-07-14 — Capstone card restamped v1.2.1 (roster reconfirmed, no
  change); live run of the reconfirmed card still owed (Phase 1.8 step 3).

## Session log

- 2026-07-14 — Pack self-audit session: baseline research refresh, partition
  re-run, combine analysis, capability map, F1+F2 applied, Foundation 1.0
  release kit assembled (repo-sync bundle + eight member zips + card v1.2.1).
