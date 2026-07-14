# Trigger Evals — revenant-foundation-tokensmith

> **Provenance:** target `revenant-foundation-tokensmith` v1.0.0 · suite derived 2026-07-13 (evalsmith doctrine; runnable cold, no tooling). Twenty queries — ten should fire the description, ten shouldn't. Read each cold against **name + description only** and compare to the expected column.

## Should trigger (10)

| # | Query | Expected |
|---|---|---|
| Y1 | "Slim this system prompt — it's 6k tokens and I need it under 3k." | Fire (Slim, budgeted) |
| Y2 | "Why does my CLAUDE.md cost so many tokens every session?" | Fire (cost question on an instruction file) |
| Y3 | "tokensmith audit my pack's skill descriptions." | Fire (Audit, keyword) |
| Y4 | "This agent spec has to fit an 8k context budget with room left for tool output — make it fit." | Fire (Slim, budget/context fit) |
| Y5 | "Set token budgets for the seven instruction files in this project." | Fire (Budget) |
| Y6 | "My skill's always-on surface is eating context at session start — trim what loads every turn." | Fire (Slim, always-on role) |
| Y7 | "Compress this reference doc without losing any of the rules in it." | Fire (Slim, preservation) |
| Y8 | "tokensmith refresh." | Fire (Refresh, keyword) |
| Y9 | "Estimate what this prompt costs per call and whether caching it would pay off." | Fire (measurement + cache accounting) |
| Y10 | "Get this SKILL.md under 300 lines without changing what it does." | Fire (Slim, behavior-preserving) |

## Should NOT trigger (10)

| # | Query | Expected | Routes to |
|---|---|---|---|
| N1 | "Make this prompt more persuasive and improve its examples." | No fire | promptsmith (near-miss — quality, not cost) |
| N2 | "Audit my skill against current best practices." | No fire | skillsmith (near-miss — conformance, not footprint) |
| N3 | "Shorten this email to a client to three sentences." | No fire | commsmith (near-miss — audience-facing length) |
| N4 | "My session keeps compacting mid-task — manage my live context." | No fire | runtime/platform tools (near-miss — session, not artifact) |
| N5 | "Write the assertion suite for my slimmed skill." | No fire | evalsmith (near-miss) |
| N6 | "Which model tier should this prompt run on?" | No fire | promptsmith |
| N7 | "Build me a skill that makes responses terse." | No fire | skillsmith (near-miss — a build ask; terse output is a runtime style) |
| N8 | "What's a token and how does tokenization work?" | No fire | plain explanation |
| N9 | "Summarize this article for me." | No fire | ordinary summarization |
| N10 | "Cut our cloud spend on this AWS bill." | No fire | not an LLM text artifact |

## Edge notes

**Sharpest boundary pair:** N1 vs Y1 — "make this prompt *better*" is promptsmith; "make this prompt *cheaper / fit a budget*" is tokensmith. Second sharpest: N2 vs Y3 — "audit my skill" (best practices) is skillsmith; "audit my skill's *token footprint*" is tokensmith.

**Tuning rule:** misses on the yes-set → make the description's triggers pushier (add the cost/fit/footprint vocabulary users actually type); fires on the no-set → tighten the boundary sentence naming promptsmith, skillsmith, and commsmith.
