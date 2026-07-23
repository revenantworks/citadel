# Model Snapshot — Volatile Data *(single update surface)*

> **Last verified: 2026-07-23.** This is the **only** file to edit when model lineups change — durable routing logic lives in `model-notes.md` §2 and never needs touching for a lineup update. If today is more than 60 days past this stamp and the output names a specific model, verify against the canonical sources below first (one or two searches). If verification isn't possible, recommend by tier name ("current Claude balanced tier"), never a possibly-retired model string. To regenerate this file, say **"promptsmith refresh"** (procedure in SKILL.md → Entry — Refresh).

---

## Current tier map *(verified 2026-07-23)*

| Tier | Claude *(default)* | OpenAI | Gemini | Grok (xAI) | DeepSeek |
|---|---|---|---|---|---|
| **S — frontier** | Fable 5 | GPT-5.5 Pro | —³ | Grok 4 Heavy¹ | V4 Pro |
| **A — flagship** | Opus 4.8 | GPT-5.6 Sol | Gemini 3.1 Pro³ | Grok 4.5⁴ | V4 Pro |
| **B — balanced** | Sonnet 5 | GPT-5.6 Terra | Gemini 3.6 Flash | Grok 4.3 | V4 |
| **C — fast** | Haiku 4.5 | GPT-5.6 Luna (5.4 nano/mini for the cheapest routing) | Gemini 3.5 Flash-Lite | Grok 4.1 Fast | V4-Flash |

¹ Consumer product only — not available on the API. Never recommend gated or limited-availability models (e.g. Claude Mythos 5, Gemini 3.5 Flash Cyber) as defaults.
³ **Gemini 3.5 Pro is not broadly available** (partner testing only, delayed past its announced June window; last GA Pro is 3.1, Feb 2026) — never recommend it until it ships. Gemini's S slot is effectively empty; 3.1 Pro is their top recommendable model.
⁴ Grok 4.5 (July 8) carries a **500K context — smaller than Grok 4.3's 1M and 4.1 Fast's 2M**; pick 4.3 or 4.1 Fast when the window matters more than the newest weights.

---

## Relative cost bands *(within vendor, cheapest → priciest)*

| Vendor | C | B | A | S |
|---|---|---|---|---|
| Claude | ¢ Haiku | $ Sonnet | $$ Opus | $$$ Fable |
| OpenAI | ¢ Luna / 5.4 nano | $ Terra | $$ Sol | $$$ 5.5 Pro |
| Gemini | ¢ Flash-Lite | ¢–$ 3.6 Flash | $ 3.1 Pro | — |
| Grok | ¢ 4.1 Fast | ¢–$ 4.3 | $ 4.5 | consumer sub |
| DeepSeek | ¢ V4-Flash | ¢ V4 | ¢–$ V4 Pro | ¢–$ V4 Pro |

**Pricing quirks worth flagging:** Claude Sonnet 5 carries introductory pricing until 2026-08-31 (standard rate from Sept 1). DeepSeek V4 Pro's launch promo **expired 2026-05-31** — it now bills at its standard rate (still the cheapest flagship-class option by a wide margin). Gemini 3.1 Pro doubles its per-token rate on prompts over 200K tokens. OpenAI GPT-5.5 charges a long-context premium (≈2× input / 1.5× output) on sessions whose prompts exceed ~272K tokens; the GPT-5.6 family bills cache *writes* at 1.25× with a 30-minute minimum cache life. Grok 4.5 and 4.3 double their rates above 200K tokens. Gemini 3.6 Flash, Grok 4.3, and the whole DeepSeek line deliver near-flagship capability at budget prices — the reason routing goes by required capability, not by price.

---

## Context / output quirks *(verified 2026-07-23)*

- Claude: 1M context on Fable/Opus/Sonnet; **Haiku 200K**. 64K output standard; Fable 5 carries a 128K output ceiling.
- OpenAI: the GPT-5.6 family (Sol/Terra/Luna, GA 2026-07-09) is **1M context on all three tiers**; GPT-5.5 ≈1.05M context / 128K output.
- Gemini: current line is ~1M context; **3.6 Flash** (2026-07-21) is the workhorse — ~17% fewer output tokens than 3.5 Flash; **3.5 Flash-Lite** is the speed floor (~350 tok/s).
- Grok: **4.1 Fast has 2M context — larger than every newer Grok, including the 4.5 flagship (500K).** Check before assuming newest = biggest.
- DeepSeek: V4 line ≈1M context; the old R-line reasoning models are folded into V4's thinking mode.

---

## Reasoning-depth parameter names

| Vendor | Parameter |
|---|---|
| Claude | `effort` (minimal / low / medium / high / xhigh / max; `none` off — xhigh on Sonnet 5 up; max on Fable 5) |
| OpenAI | `reasoning_effort` (none → xhigh) |
| Gemini | `thinking_level` (low / medium / high) |
| Grok | reasoning on by default on current flagships |
| DeepSeek | family choice: V-line = chat, thinking mode = the old R-line |

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

## Refresh procedure *(summary — full procedure in SKILL.md → Entry — Refresh)*

Say **"promptsmith refresh"** → the skill re-verifies the tier map, cost bands, and quirks against the sources above, regenerates **this file only** with a new Last-verified stamp, adds a dated CHANGELOG line, bumps the patch version, and (on claude.ai) hands back a repackaged skill to reinstall. Cadence: on the 60-day stamp, or whenever a major model launches.
