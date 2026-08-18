# Model Snapshot — Volatile Data *(single update surface)*

> **Last verified: 2026-08-17.** This is the **only** file to edit when model lineups change — durable routing logic lives in `model-notes.md` §2 and never needs touching for a lineup update. If today is more than 60 days past this stamp and the output names a specific model, verify against the canonical sources below first (one or two searches). If verification isn't possible, recommend by tier name ("current Claude balanced tier"), never a possibly-retired model string. To regenerate this file, say **"promptwright refresh"** (procedure in SKILL.md → Entry — Refresh).

---

## Current tier map *(verified 2026-08-17)*

| Tier | Claude *(default)* | OpenAI | Gemini | Grok (xAI) | DeepSeek |
|---|---|---|---|---|---|
| **S — frontier** | Fable 5 | GPT-5.5 Pro | —² | Grok 4 Heavy¹ | V4 Pro |
| **A — flagship** | Opus 5 | GPT-5.6 Sol | Gemini 3.1 Pro² | Grok 4.6³ | V4 Pro |
| **B — balanced** | Sonnet 5 | GPT-5.6 Terra | Gemini 3.7 Flash | Grok 4.3 | V4-Flash |
| **C — fast** | Haiku 4.5 | GPT-5.6 Luna | Gemini 3.5 Flash-Lite | Grok 4.3 (the 4.20 non-reasoning variant, same rate, when latency rules) | V4-Flash (non-thinking mode) |

¹ Consumer product only (the SuperGrok Heavy subscription) — not an API model; xAI's own API guidance points at Grok 4.6 for everything. Never recommend gated or limited-availability models (e.g. Claude Mythos 5 and Mythos Preview, both invitation-only) as defaults.
² **Gemini 3.5 Pro is still not available** (announced at I/O May 2026; June and July targets missed; absent from the Gemini API model list on 2026-08-17) — never recommend it until it ships. Gemini's S slot is effectively empty; 3.1 Pro (Feb 2026, still served under the `-preview` id) is their top recommendable model.
³ Grok 4.6 (2026-08-12) and 4.5 carry a **500K context — smaller than Grok 4.3's 1M**; pick 4.3 when the window matters more than the newest weights. Grok 4.1 Fast no longer appears on xAI's model list — do not recommend it.

---

## Relative cost bands *(within vendor, cheapest → priciest)*

| Vendor | C | B | A | S |
|---|---|---|---|---|
| Claude | ¢ Haiku | $ Sonnet | $$ Opus | $$$ Fable |
| OpenAI | ¢ Luna | $ Terra | $$ Sol | $$$ 5.5 Pro (6× Sol — try Sol at `xhigh`/`max` first) |
| Gemini | ¢ Flash-Lite | ¢–$ 3.7 Flash | $ 3.1 Pro | — |
| Grok | ¢–$ 4.3 | ¢–$ 4.3 | $ 4.6 | consumer sub |
| DeepSeek | ¢ V4-Flash | ¢ V4-Flash | ¢–$ V4 Pro | ¢–$ V4 Pro |

**Pricing quirks worth flagging:** Claude Sonnet 5's $2/$10 launch price is now the standard price — the increase to $3/$15 scheduled for 2026-09-01 was cancelled (Anthropic pricing page, 2026-08-17). Opus 5 bills the same as Opus 4.8 ($5/$25); Fable 5 is $10/$50. Gemini 3.7 Flash and 3.6 Flash bill $0.75/$3.75 through 2026-12-31 and double on 2027-01-01; Gemini 3.1 Pro doubles input and lifts output ×1.5 on prompts over 200K tokens. OpenAI's whole 5.x line (5.6 Sol/Terra/Luna, 5.5, 5.5 Pro, 5.4) charges a long-context premium on requests whose prompts exceed ~272K tokens (≈2× input / 1.5× output for the full request); the GPT-5.6 family bills cache *writes* at 1.25× and reads at 0.1×, with a strict 1,024-token minimum and a 30-minute cache life. Grok 4.6, 4.5 and 4.3 double their rates at 200K tokens and above. DeepSeek halves its rates in off-peak windows (hours on its pricing page) — V4-Flash is the cheapest capable model anywhere. Gemini 3.7 Flash, Grok 4.3, and the whole DeepSeek line deliver near-flagship capability at budget prices — the reason routing goes by required capability, not by price.

---

## Context / output quirks *(verified 2026-08-17)*

- Claude: 1M context on Fable 5, Opus 5, Sonnet 5 (and the Opus 4.6–4.8 / Sonnet 4.6 legacy tier); **Haiku 4.5 200K**. **128K output** on Fable 5, Opus 5 and Sonnet 5 (300K on the Batch API via a beta header); Haiku 64K. Fable 5 and the Opus 4.7-onward tokenizer bill ~30% more tokens for the same text than Sonnet 4.6-era models — budget for it. Fable 5's adaptive thinking is always on and cannot be disabled.
- OpenAI: the GPT-5.6 family (Sol/Terra/Luna) is **1.05M context / 128K output on all three tiers**; GPT-5.5 Pro shares that window; the older 5.4 mini/nano sit at 400K and no longer undercut Luna on price.
- Gemini: 1,048,576-token input / 65,536-token output across 3.7 Flash, 3.6 Flash and 3.1 Pro; **3.7 Flash** (Aug 2026, GA) is the workhorse; **3.5 Flash-Lite** is the speed and price floor.
- Grok: **the flagships (4.6, 4.5) carry 500K; the cheaper 4.3 and 4.20 variants carry 1M** — the smaller model has the bigger window. Check before assuming newest = biggest.
- DeepSeek: V4 Pro (0813) and V4-Flash (0731) are both 1M context / 384K output, thinking on by default with a non-thinking mode; the old R-line reasoning models are folded into thinking mode.

---

## Reasoning-depth parameter names

| Vendor | Parameter |
|---|---|
| Claude | `effort` (low / medium / high / xhigh / max; default high — xhigh on Fable 5, Opus 5, Opus 4.8/4.7 and Sonnet 5; max on the 4.6 generation and later; Haiku 4.5 has no effort control) |
| OpenAI | `reasoning_effort` (none / low / medium / high / xhigh / max on the 5.6 family) |
| Gemini | `thinking_level` (low / medium / high) |
| Grok | reasoning on by default on current flagships; 4.20 ships reasoning and non-reasoning variants |
| DeepSeek | thinking mode on by default (the old R-line), non-thinking mode for chat-style work — both on V4 Pro and V4-Flash |

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

Say **"promptwright refresh"** → the skill re-verifies the tier map, cost bands, and quirks against the sources above, regenerates **this file only** with a new Last-verified stamp, adds a dated CHANGELOG line, bumps the patch version, and (on claude.ai) hands back a repackaged skill to reinstall. Cadence: on the 60-day stamp, or whenever a major model launches.
