# Model Notes — Durable Per-Model Prompting Guidance + Tier Routing

> This file holds the **durable** guidance: routing rules and prompting behavior that survive model releases. **Volatile facts — current model names, cost bands, context quirks — live only in `model-snapshot.md`** under a Last-verified stamp. When naming a specific model, load the snapshot alongside this file. If the snapshot is stale (>60 days) and unverifiable, recommend by tier name, never a possibly-retired model string.

This skill is Claude-first but model-agnostic. The structures in `frameworks.md` are universal; this file holds the model-specific differences. When a prompt targets a non-Claude model, keep the structure and swap in the notes below.

---

## Contents

1. The reasoning-model split *(read first)*
2. Tier routing *(reference — the core routing lives inline in SKILL.md Phase 5)*
3. Claude
4. GPT (OpenAI)
5. Gemini (Google)
6. Grok (xAI)
7. DeepSeek
8. Open-weight / local models
9. Cross-model rule

---

## 1. The reasoning-model split *(read first)*

Every major vendor now ships in two modes, and the prompt changes with the mode — this distinction matters more than which vendor you target.

| Mode | Examples | How to prompt |
|---|---|---|
| **Reasoning / "thinking" models** | Claude with adaptive thinking, GPT-5.x series, Gemini 3.x with thinking, Grok 4.x, DeepSeek R-line | Give the objective, the constraints, and what "done" looks like, then get out of the way. Do **not** add "think step by step" or a prescribed reasoning outline — it's redundant and can degrade quality or inflate cost. Control depth with the model's API parameter, not prompt language. |
| **Non-reasoning / chat models** | Most fast-tier models, any model with thinking off or effort `none`, DeepSeek V-line in chat mode, most smaller open models | Explicit chain-of-thought framing and few-shot examples still earn their keep. Spell out the steps and show examples. |

Before engineering an elaborate CoT prompt, check whether the target has a reasoning mode you can switch on with a parameter — you get better results with less prompt complexity.

> **Recurring trap:** legacy "booster" instructions written for older models (e.g. "ALWAYS use the search tool before answering," heavy step-by-step scaffolding) now backfire on newer, more capable models, causing over-triggering and overthinking. Newer models usually need *less* prompt, not more. Strip boosters when you move up a generation.

---

## 2. Tier routing *(reference — core routing is inlined in SKILL.md Phase 5)*

**Route by the capability tier the task requires, then choose the cheapest model in the target vendor's lineup that clears that bar.** Tier no longer tracks price — several vendors ship near-flagship quality in budget tiers, so "hard task → expensive model" is the wrong rule; "required capability → cheapest model that clears it" is the durable one.

**Default vendor: Claude**, unless the user names another vendor, the deployment stack implies one, or a vendor override applies:

- Real-time X / social-pulse data → Grok
- Self-hosting / data sovereignty / no-cloud → DeepSeek open weights or other open models
- Deep Google Workspace / Search-grounding integration → Gemini

**Routing inputs:** hardest-step complexity · cost of a wrong answer · volume + latency · context length needed · output length · structured-output and tool needs.

**The tiers** (current names per vendor: `model-snapshot.md`):

| Tier | Route here when |
|---|---|
| **S — frontier** | Failure is very costly; the hardest reasoning, longest-horizon agentic work; stakes justify premium pricing |
| **A — flagship** | Hard multi-step reasoning, complex agents, large multi-file refactors, dense analysis where mistakes are expensive |
| **B — balanced** *(default)* | Most writing, coding, analysis, summarization, and agent work |
| **C — fast** | Classification, extraction, routing, tagging, high-volume pipelines, latency-sensitive interactive products |

Never recommend gated or limited-availability models as defaults.

**Escalation heuristic:** start at Tier B. Before moving up a tier, try raising the reasoning-depth parameter on the current tier (see the snapshot for each vendor's parameter) — often cheaper than a tier jump. Move to A when failure is expensive or evals show B falling short; S only when stakes justify the premium. Drop to C when the task is simple, high-volume, or latency-bound.

**Tier changes the prompt, not just the price:** Tier C models usually behave as chat models (section 1) — explicit steps and few-shot examples earn their keep. Tier A/S models reason natively — strip scaffolding. Re-check section 1 after any tier change, including via the "switch model" path.

**Staleness rule:** `model-snapshot.md` carries the Last-verified stamp and canonical sources. If today is >60 days past the stamp and the output names a specific model, verify the lineup against those sources first (one or two searches); otherwise recommend by tier ("current Claude balanced tier").

---

## 3. Claude

*(Current lineup, context windows, and pricing: `model-snapshot.md`.)*

| Behavior | Guidance |
|---|---|
| **Literal instruction following** | Current Claude does what you say precisely. Be exact, remove contradictory rules, and request "above and beyond" behavior explicitly. Give the reason behind a constraint ("no ellipses — read by text-to-speech") and the model honors it more reliably. |
| **Adaptive thinking** | Recommended mode; default on current flagship tiers. The model decides per turn whether and how much to think — don't add CoT framing when it's on. Set depth with the `effort` parameter, not with prompt text. On the newest frontier tier, thinking is always on and cannot be disabled. Manual token budgets are deprecated. |
| **Mid-task instruction updates** | The Messages API accepts `system` entries inside the `messages` array, so an agent harness can update instructions, permissions, or context mid-run without breaking the prompt cache. |
| **No assistant prefill** | Current Claude models reject a prefilled final assistant turn. Steer format with explicit output-format instructions, structured outputs, or strict tool use. |
| **XML tags** | Claude respects hierarchical tags for separating instructions, context, examples, and input. A terse, clean prompt yields terse, clean output. |
| **Structured output** | Prefer a native structured-output feature or strict tool use when you need a guaranteed shape. For free-form JSON: specify the exact schema and require only that structure with no preamble and no code fences. |
| **Tool use** | Don't over-force. Aggressive "always call X" language causes over-triggering on newer Claude models. State when a tool is appropriate and let the model judge. |
| **Long-context placement** | Put the data at the top and the question after it. See `frameworks.md` — long-context structuring. |
| **Caching** | Split into a stable prefix (instructions, tool definitions, background) and a dynamic suffix (the query and injected data). Cache hits need an exact prefix match. |

**Effort starting points:** medium for coding, agentic, tool-heavy, and frontend work; low for chat, content, search, and classification. Raise only when evals show it pays.

---

## 4. GPT (OpenAI)

*(Current lineup: `model-snapshot.md`. The GPT-5.x series are reasoning models.)*

| Behavior | Guidance |
|---|---|
| **Reasoning depth** | Control with `reasoning_effort`. Effort `none` makes the model behave like a non-reasoning model — prompt it chat-style (few-shot, explicit steps, high-quality tool descriptions). |
| **Verbosity** | Control final-answer length with `verbosity`. Both are API knobs — reach for them before padding the prompt. |
| **Prompting style** | Outcome-oriented prompts win. Describe what good looks like, the constraints, and the evidence available, then let the model pick the path. Don't port every line from an older prompt stack — over-specifying process adds noise and can trigger overthinking. |
| **Roles** | System and developer messages hold durable role and rules (`role: "developer"` is the system-message equivalent). |
| **Structured output** | JSON schema and function calling are first-class — prefer them over free-form JSON instructions. |
| **Agentic / tool use** | Use the Responses API where available — it carries reasoning state across turns and measurably improves agentic performance. |
| **Version pinning** | Defaults shift between versions. Pin `reasoning_effort` explicitly and change one thing at a time when migrating. |

---

## 5. Gemini (Google)

*(Current lineup: `model-snapshot.md`.)*

| Behavior | Guidance |
|---|---|
| **Prompting style** | Gemini 3.x reasons natively and rewards simple, clear prompts. It is good at inferring intent — long chained instructions and over-explaining reduce quality rather than add to it. |
| **Reasoning depth** | Set with `thinking_level`. Don't mix it with legacy `thinking_budget`. For low latency, pair a low thinking level with a "think silently" system instruction. |
| **Constraints** | Avoid broad negative constraints like "do not infer" or "do not guess" — they make the model over-index and drop basic logic. Instead, tell it explicitly to base deductions on the provided context. |
| **Structured output** | Response schema is supported — prefer it over prompt-only JSON instructions. |
| **Multi-turn tool use** | Relies on "thought signatures" — encrypted reasoning state that must be returned on subsequent calls. The official SDK handles this automatically; dropping them degrades quality or errors out. |
| **Knowledge cutoff** | Trails the calendar — ground with search for current facts. |

---

## 6. Grok (xAI)

*(Current lineup: `model-snapshot.md`.)*

| Behavior | Guidance |
|---|---|
| **Real-time data** | Grok's structural advantage is native, real-time access to X and live web/X search server-side tools. If the prompt's job depends on what's happening *right now*, this is the vendor-override case in §2. |
| **API compatibility** | The API mirrors the OpenAI schema — streaming, tool calls, and structured JSON output work as expected. Prompt it like a reasoning-mode GPT target. |
| **Reasoning** | Current Grok flagships are reasoning models — apply the section-1 reasoning rules; no CoT scaffolding. |
| **Multi-agent "Heavy" mode** | The parallel multi-agent configuration is a consumer-product feature, not an API capability — don't design prompts assuming it. |
| **Context quirk** | The fast tier has historically carried a *larger* context window than the flagship — check the snapshot before assuming newest = biggest. |
| **Verification** | Persona runs looser than other vendors; for high-stakes factual output, build in a self-check or grounding step. |

---

## 7. DeepSeek

Two families with opposite prompting needs — identify which one before building. *(Current lineup: `model-snapshot.md`.)*

**V-line (chat/flagship — current mainline, open-weights MoE):**
- Conventional behavior — supports system prompts, personas, few-shot, function calling, and JSON mode.
- Prompt it like GPT or Claude. Strong at structured output and long-document analysis.

**R-line (dedicated reasoning models):**
- No system prompt — put every instruction in the user turn. A system persona fights the trained reasoning and degrades it.
- No few-shot — examples make it mimic the pattern instead of reasoning. Describe the task and output format in detail instead.
- Don't add "think step by step" — built in; forcing it can cause repetition loops.
- Keep prompts concise and give a high-level objective.
- Weaker at strict JSON and format-bound work — use the V-line for those, or constrain only the final answer, not the reasoning.

**Both:** the API is stateless — resend conversation history each turn, and send only assistant content, not `reasoning_content`. Built-in safety is lighter than some competitors', so add your own guardrails around untrusted input.

---

## 8. Open-weight / local models

*(Llama, Qwen, Gemma, Mistral, DeepSeek open weights, and similar)*

| Consideration | Guidance |
|---|---|
| **Scaffolding** | Smaller or older instruction-tuned models need more explicit, simpler instructions and more examples than frontier models. What one line buys on a frontier model may take three here. |
| **Reasoning variants** | Many open families ship thinking variants. When thinking is on, apply the reasoning-model rules from section 1. |
| **Context windows** | Often shorter than frontier models — keep inputs tight and put the critical instruction at the start or end. |
| **Testing** | Behavior varies widely by checkpoint and quantization. Test on the exact model and quant; don't port a frontier-model prompt unchanged. |

---

## 9. Cross-model rule

Keep the universal scaffold — role, context, examples, explicit output format — for any model. Then:

1. Pick the capability tier first (section 2), before any vendor-specific syntax.
2. Decide whether the target is a reasoning or a chat model and prompt accordingly (section 1).
3. Control reasoning depth with the model's API parameter, not with prompt padding.
4. Drop Claude-specific conventions (XML-as-preferred, adaptive-thinking phrasing, prefill warnings) for non-Claude targets.
5. Re-test on every model switch and version bump — newer models often need less prompt, and legacy booster instructions that once helped can quietly hurt.

Vendors not detailed here still fall on one side of the reasoning / chat split and into one of the four tiers — identify which and apply the matching rules.
