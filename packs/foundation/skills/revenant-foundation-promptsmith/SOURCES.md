# Sources

This skill is assembled from public, citable material: Anthropic's prompt- and context-engineering documentation, the named originators of each prompt framework, peer-reviewed research, the OWASP security guidance for LLM applications, and the Agent Skills open standard. This file maps each part of the skill to where its ideas come from, so the guidance can be checked and updated against primary sources.

> Everything below was verified against the listed sources as of **2026-07-06**. Model facts and product details change quickly — durable routing guidance lives in `references/model-notes.md`, and volatile facts (names, prices, context windows) are isolated in `references/model-snapshot.md` behind a Last-verified stamp. Re-check the snapshot against the vendor docs before relying on specifics, or run "promptsmith refresh".

---

## Foundations — Anthropic prompt & context engineering

*Applies to: `SKILL.md` (workflow, restraint, long-context ordering), `references/frameworks.md` (long-context and agent/system patterns), `references/model-notes.md`, `references/evaluation.md`.*

| Source | Key guidance |
|---|---|
| Anthropic — Prompt engineering overview and best practices. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview | Be clear and direct; give the model a role; use XML tags to separate instructions from data; show 3–5 diverse examples rather than exhaustively enumerating edge cases. |
| Anthropic — Use XML tags / long context tips. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips | For long inputs, place documents / context at the **top** of the prompt and put the question or instruction **after** them. This ordering can materially improve answer quality on long-context tasks. |
| Anthropic — "Effective context engineering for AI agents." https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Aim for the smallest set of high-signal tokens; find the "right altitude" for system prompts (specific enough to steer, general enough to leave room); curate a minimal, well-described tool set rather than exposing everything. |
| Anthropic — Interactive prompt-engineering tutorial. https://github.com/anthropics/prompt-eng-interactive-tutorial | Source for the staged "intake → structure → refine" mental model and for the principle that more capable models need *less* prescriptive scaffolding. |

---

## Prompt frameworks — named origins

*Applies to: `references/frameworks.md`.*

| Framework | Origin | Signature contribution |
|---|---|---|
| **CO-STAR** (Context, Objective, Style, Tone, Audience, Response) | Sheila Teo, winner of Singapore's first GPT-4 Prompt Engineering Competition (2023). Popularized in Maximilian Vogel's "Prompt Engineering Cheat Sheet." | The Style / Tone split — most frameworks merge them. |
| **RISEN** (Role, Instructions, Steps, End goal, Narrowing) | Kyle Balmer — an evolution of the earlier RISE pattern. | Explicit Narrowing (constraints) added to the earlier RISE structure. |
| **RTF** (Role, Task, Format) | Widely-used community pattern. | Minimal three-part scaffold for simple, well-defined tasks. |
| **BAB** (Before, After, Bridge) | Community pattern derived from the Before–After–Bridge copywriting structure. | Frames the task as a current → target transition with the Bridge carrying the rules. |
| **TIDD-EC** (Task, Instructions, Do, Don't, Examples, Context) | Community framework. | Explicit Do / Don't pairing — tells the model directly which characteristics must and must not appear. |
| **Chain of Thought** ("think step by step") | See Research section below. | — |

---

## Research papers

*Applies to: `references/frameworks.md` (CoT, Chain of Density), `references/evaluation.md` (self-refinement loop), `references/prompt-hardening.md` (constitutional framing).*

| Paper | Citation | Application |
|---|---|---|
| Chain-of-Thought prompting | Wei et al., 2022 — "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." arXiv:2201.11903. | Basis for the explicit step-by-step reasoning instruction on non-reasoning / chat models. |
| Self-Refine | Madaan et al., 2023 — "Self-Refine: Iterative Refinement with Self-Feedback." arXiv:2303.17651 (NeurIPS 2023). | Basis for the score → critique → revise loop and for the skill's re-scoring phase. |
| Chain of Density | Adams et al., 2023 — "From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting." arXiv:2309.04269. | Basis for the iterative summarization guidance in the Advanced / critique set. |
| Constitutional AI | Bai et al. (Anthropic), 2022 — "Constitutional AI: Harmlessness from AI Feedback." arXiv:2212.08073. | Background for principle-based self-critique in hardening. |

---

## Security & hardening

*Applies to: `references/prompt-hardening.md`.*

**OWASP Top 10 for LLM Applications (2025)** — https://genai.owasp.org/

| Risk | ID | How it's reflected in the skill |
|---|---|---|
| Prompt Injection (direct and indirect) | LLM01 | Treated as the top risk. The guidance that you cannot fully "patch" injection and must design around it comes from here. Mitigations: separate instructions from untrusted data, segregate and label external content, constrain output formats, apply defense-in-depth. |
| Sensitive Information Disclosure | LLM02 | Least-exposure guidance in the sensitive data section. |
| Excessive Agency | LLM06 | Least-privilege tooling and human-in-the-loop guidance for agentic prompts. |
| System Prompt Leakage | LLM07 | Don't put secrets in the system prompt; instruct the model not to reveal its instructions. |

---

## Skill format — the Agent Skills open standard

*Applies to: the packaging of this skill itself (`SKILL.md` frontmatter, `references/` layout, progressive disclosure).*

**Agent Skills open standard** — https://agentskills.io/ · reference repository: https://github.com/anthropics/skills

| Principle | How it's applied |
|---|---|
| A skill is a folder with a `SKILL.md` containing YAML frontmatter (`name` and `description` required) plus Markdown instructions, with optional `references/`, scripts, and assets. | Package structure follows this exactly. |
| **Progressive disclosure:** the model first sees the frontmatter, then the body, then pulls in reference files only as needed. | Heavy material lives in `references/` rather than in `SKILL.md`. |
| Descriptions should be explicit and "pushy" about when to trigger. | Reflected in the skill's `description` field. |
| **Conciseness:** the context window is a public good — once loaded, every SKILL.md token competes with the conversation. Keep the entry file lean; split mutually-exclusive contexts into separate files. (Anthropic — Skill authoring best practices, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices · "Equipping agents for the real world with Agent Skills," https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Drives the load budget, the lean SKILL.md, and the situational (rather than mandatory) reference loads. |
| `allowed-tools` restricts tool access while a skill is active on surfaces that enforce it. | The field is omitted so the skill can always read its own references. |

*Standard provenance: released as an open standard in December 2025. Specification code under Apache-2.0; documentation under CC BY 4.0.*

---

## Model-specific notes

*Applies to: `references/model-notes.md`, and model-tagged guidance throughout.*

These reflect vendor documentation and product facts current as of **2026-07-06** and will drift. The tier-routing model (`model-notes.md` §2) is durable; the specific names, prices, and context windows in `model-snapshot.md` are the parts that rot. Primary sources (vendor model docs, verify in this order):

- Anthropic — https://platform.claude.com/docs/en/about-claude/models/overview
- OpenAI — https://developers.openai.com/api/docs/models
- Google — https://ai.google.dev/gemini-api/docs/models
- xAI (Grok) — https://docs.x.ai/
- DeepSeek — https://api-docs.deepseek.com/

Cross-check registries (community-maintained, machine-readable; may lag brand-new launches — vendor docs win conflicts):

- LiteLLM model/price/context registry — https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
- OpenRouter live model list — https://openrouter.ai/api/v1/models

The single-update-surface pattern (isolating volatile facts in one stamped file) and the fetch-first / verify-against-canonical-source approach follow Anthropic's own `product-self-knowledge` skill, which handles the same drift problem by keeping stable pointer URLs instead of baked-in facts.
