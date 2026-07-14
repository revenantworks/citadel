# Model Snapshot — Volatile Data *(single update surface)*

> **Last verified: 2026-07-06.** This is the **only** file to edit when model lineups change — durable routing logic lives in `model-notes.md` §2 and never needs touching for a lineup update. If today is more than 60 days past this stamp and the output names a specific model, verify against the canonical sources below first (one or two searches). If verification isn't possible, recommend by tier name ("current Claude balanced tier"), never a possibly-retired model string. To regenerate this file, say **"promptsmith refresh"** (procedure in SKILL.md → Behavior notes → Maintenance).

---

## Current tier map *(verified 2026-07-06)*

| Tier | Claude *(default)* | OpenAI | Gemini | Grok (xAI) | DeepSeek |
|---|---|---|---|---|---|
| **S — frontier** | Fable 5 | GPT-5.5 Pro | Gemini 3.5 Pro | Grok 4 Heavy¹ | V4 Pro |
| **A — flagship** | Opus 4.8 | GPT-5.5 | Gemini 3.1 Pro | Grok 4.3 | V4 |
| **B — balanced** | Sonnet 5 | GPT-5.4 | Gemini 3.5 Flash | Grok 4.3² | V4 |
| **C — fast** | Haiku 4.5 | GPT-5.4 nano (mini for coding subagents) | Gemini 3.1 Flash-Lite | Grok 4.1 Fast | V3.x |

¹ Consumer product only — not available on the API. Never recommend gated or limited-availability models (e.g. Claude Mythos 5) as defaults.
² xAI compresses tiers — Grok 4.3 serves both flagship and balanced roles at balanced-tier pricing.

---

## Relative cost bands *(within vendor, cheapest → priciest)*

| Vendor | C | B | A | S |
|---|---|---|---|---|
| Claude | ¢ Haiku | $ Sonnet | $$ Opus | $$$ Fable |
| OpenAI | ¢ nano/mini | $ 5.4 | $$ 5.5 | $$$ 5.5 Pro |
| Gemini | ¢ Flash-Lite | ¢–$ 3.5 Flash | $ 3.1 Pro | $$ 3.5 Pro |
| Grok | ¢ 4.1 Fast | ¢–$ 4.3 | ¢–$ 4.3 | consumer sub |
| DeepSeek | ¢ | ¢ | ¢ | ¢–$ |

**Pricing quirks worth flagging:** Claude Sonnet 5 carries introductory pricing until 2026-08-31. Gemini 3.1 Pro doubles its per-token rate on prompts over 200K tokens. OpenAI GPT-5.5 charges a premium on sessions whose prompts exceed ~272K tokens. Gemini 3.5 Flash, Grok 4.3, and the whole DeepSeek line deliver near-flagship capability at budget prices — the reason routing goes by required capability, not by price.

---

## Context / output quirks *(verified 2026-07-06)*

- Claude: 1M context on Fable/Opus/Sonnet; **Haiku 200K**. 64K output standard (larger via batch beta).
- OpenAI: GPT-5.5 ≈1.05M context / 128K output.
- Gemini: **all current tiers carry 1M context** — the only vendor whose fast tier keeps full context.
- Grok: **4.1 Fast has 2M context — larger than the 1M flagship.** Check before assuming newest = biggest.
- DeepSeek: V4 line ≈1M context.

---

## Reasoning-depth parameter names

| Vendor | Parameter |
|---|---|
| Claude | `effort` (minimal / low / medium / high / xhigh / max; `none` off) |
| OpenAI | `reasoning_effort` (none → xhigh) |
| Gemini | `thinking_level` (low / medium / high) |
| Grok | reasoning on by default on current flagships |
| DeepSeek | family choice: V-line = chat, R-line = reasoning |

---

## Canonical sources *(verify here, in this order)*

**Primary — vendor model docs** (URLs are durable even as contents change):

| Vendor | URL |
|---|---|
| Anthropic | https://platform.claude.com/docs/en/about-claude/models/overview |
| OpenAI | https://developers.openai.com/api/docs/models |
| Google | https://ai.google.dev/gemini-api/docs/models |
| xAI | https://docs.x.ai/ |
| DeepSeek | https://api-docs.deepseek.com/ |

**Cross-check — machine-readable registries** (community-maintained; may lag brand-new launches — vendor docs win conflicts):

- LiteLLM model/price/context registry: https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
- OpenRouter live model availability: https://openrouter.ai/api/v1/models

---

## Refresh procedure *(summary — full procedure in SKILL.md Behavior notes)*

Say **"promptsmith refresh"** → the skill re-verifies the tier map, cost bands, and quirks against the sources above, regenerates **this file only** with a new Last-verified stamp, adds a dated CHANGELOG line, bumps the patch version, and (on claude.ai) hands back a repackaged skill to reinstall. Cadence: on the 60-day stamp, or whenever a major model launches.
