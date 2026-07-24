# Sources — revenant-foundation-tokensmith

Where the doctrine comes from. **Verified as of 2026-07-13** (build-day research, fresh web pass). `tokensmith refresh` re-checks the Measurement rows; taxonomy and boundary rows are durable design decisions cross-checked at build.

## Doctrine → source

| Guidance area | Claim(s) | Primary source(s) | Re-check |
|---|---|---|---|
| Governing principle | "Smallest possible set of high-signal tokens"; context engineering as curation of everything in the window | Anthropic engineering — *Effective context engineering for AI agents* (anthropic.com/engineering) | On refresh |
| Progressive disclosure & platform points | Skill metadata always-on at ~dozens of tokens; body ≤500-line norm loads on trigger; references on demand, one level deep | Anthropic Agent Skills best-practices + overview docs; Agent Skills open standard (agentskills.io); anthropics/skills | On refresh |
| Cache mechanics | Prefix hits; stable-first ordering; nothing after a variable element caches; Anthropic ~1.25× write / ~0.10× read, ~5-min TTL; OpenAI auto ≥1,024 tokens, ~0.10× reads on current families (the oft-quoted ~50% is gpt-4o-era legacy — measurement.md is authoritative) | Anthropic prompt-caching docs (canonical); cross-checked via 2026 provider comparisons and practitioner write-ups | On refresh — pricing drifts |
| Estimation ratios | ~4 chars/token English prose, ~0.75 tokens/word; code denser; markup overhead; non-Latin lower | Provider tokenizer documentation + practitioner measurement posts; tokenizers differ per family — treated as estimates with ±15% band by design | On refresh |
| Net-cost accounting | Always-on rules bill per turn and can cost more than they save; tokens-per-task over tokens-per-request | drona23/claude-token-efficient (per-turn caveat, stated in-repo); bm629 token-optimization skill (tokens-per-task framing); Superpowers benchmark write-ups (clarify-first is net-cheaper) | Durable |
| Resident-vs-conditional (W10) | MCP/tool schemas load whole and always; documented five-figure always-on costs vs double-digit trigger-loaded skills | Practitioner measurements (LangSmith-CLI skills-vs-MCP post: ~16.1k always-on vs 91 activated); Claude Code session-floor reports | Durable pattern, numbers on refresh |
| Session floors | Agent CLIs start tens of thousands of tokens deep before the first user word | Firecrawl *12 Ways to Cut Token Consumption in Claude Code* (2026) + linked GH issue; /context, /usage introspection | On refresh |
| Trigger routing over resident docs | Routing triggers beat verbose always-loaded documentation; measured ~54% initial-context cut | johnlindquist context-optimization write-up (gist, 2025-12) | Durable pattern |
| Legibility floor | Telegraphic/symbol registers are runtime output tactics; instruction artifacts must survive a cold read | Contrast case — Caveman-style terseness skills (output lane); Anthropic instruction-style guidance (explain-the-why) | Durable |
| Formatting sensitivity | Cosmetic format changes shift tokenization and can move behavior — deformat carefully, measure after | arXiv literature on LLM format sensitivity (Sclar et al. 2023 et seq., surveyed in 2026 control-plane paper) | Durable |

## Niche research — incumbents named (checked 2026-07-13)

Session/setup lane: alexgreensh/token-optimizer (hooks, dashboards; Claude Code/Codex) · egorfedorov/claude-context-optimizer (plugin telemetry) · nadimtuhin/claude-token-optimizer (CLI + hooks restructuring docs) · mksglu/context-mode, RTK/Headroom (shell-output compression). Output lane: Caveman, valorisa rescue-tokens, KINGSTAR-OMEGA protocols. Delegation lane: crichalchemist/token-saver-skill (routes work to free models via OpenCode MCP — the r/claudeskills thread's namesake; the thread itself was fetch-blocked at build time, its subject located by name). Curriculum lane: muratcankoylan/Agent-Skills-for-Context-Engineering (8-skill agent-architecture pack) · bm629 token-optimization triage map. Nearest single-type neighbor: "Claude Skill Optimizer" (mcpmarket — SKILL.md-only restructuring). Directories checked via the skillsmith niche-source list: skills.sh, anthropics/skills, claude-plugins-official/community, VoltAgent/awesome-agent-skills, skillsmp.com, agentskill.sh, awesomeskill.ai/awesomeskills.dev, mcpmarket — no artifact-class slimmer with a preservation contract, score-only audit, and budget sheets found under any name, `tokensmith` unclaimed.

**Verdict recorded at build: DEFENSIBLE** — the build-time artifact lane (measure → slim → budget → audit, portable, zero-runtime-dep) is open; every incumbent is session-scoped, output-styled, delegation-based, curricular, or single-artifact-type.
