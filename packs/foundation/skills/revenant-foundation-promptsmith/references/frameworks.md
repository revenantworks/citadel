# Prompt Structures Reference

Read only the section for the structure you picked in Phase 3. Each is a proven scaffold matched to a task type — scaffolding, not a word-count target. Use the parts that earn their place and cut the rest.

---

## Contents

- Selection at a glance
- CO-STAR — content / writing
- RISEN — multi-step process
- TIDD-EC — high-precision / compliance
- BAB — rewrite / refactor / convert
- Chain of Thought — reasoning / debugging / math
- RTF / APE — simple, well-defined tasks
- Agent / System structure — tool-using agents and system prompts
- Advanced / critique set — Self-Refine, Red-team, RCoT, Chain of Density
- Prompt chaining — when to split a task across multiple prompts
- Long-context structuring — where to place data and instructions
- Note on research backing

---

## Selection at a glance

| Task type | Structure |
|---|---|
| Content / writing (audience + tone matter) | CO-STAR |
| Multi-step process or procedure | RISEN |
| High-precision / compliance (explicit dos & don'ts) | TIDD-EC |
| Rewrite / refactor / convert existing content | BAB |
| Reasoning / debugging / math | Chain of Thought |
| Simple, well-defined task | RTF (APE if ultra-minimal) |
| Agentic / tool-using / system prompt | Agent / System structure |
| Stress-test or verify a prompt | Advanced / critique set |
| Multi-step task where output of A feeds input of B | Prompt chaining |

When two fit, pick the simpler one. When requirements are unclear, use Interview mode (Phase 4 of SKILL.md) before choosing.

---

## CO-STAR — Context, Objective, Style, Tone, Audience, Response

**Best for:** blog posts, emails, marketing copy, docs, presentations — anything where audience and tone drive quality.

| Component | What it carries |
|---|---|
| Context | Background and situation the writing serves |
| Objective | The specific goal of the piece |
| Style | Structural / format approach (narrative, bullets, subheads every N words) |
| Tone | Voice and emotional quality |
| Audience | Who reads it, what they know, what they value |
| Response | Exact output format and length |

**Skeleton:**

```
CONTEXT:   Business blog for C-level execs exploring AI; readers know strategy, not ML.
OBJECTIVE: Help them grasp practical ML applications and tangible business value.
STYLE:     Professional blog, narrative + bullets, subheads every 150–200 words, 2–3 cases.
TONE:      Authoritative but approachable; practical, not theoretical.
AUDIENCE:  Senior managers who weigh ROI and have limited technical ML knowledge.
RESPONSE:  800-word article — headline (≤10 words), hook, 3–4 sections, CTA close.
```

CO-STAR's distinctive move is splitting **Style** (the writing approach) from **Tone** (the emotional register) — most frameworks merge them. That separation is what makes it strong for voice-sensitive content.

*Origin: Sheila Teo, winner of Singapore's first GPT-4 Prompt Engineering competition, 2023.*

---

## RISEN — Role, Instructions, Steps, End goal, Narrowing

**Best for:** multi-step processes, systematic procedures, workflows, structured analysis.

| Component | What it carries |
|---|---|
| Role | The expertise / perspective needed |
| Instructions | High-level guidance on the task |
| Steps | The explicit methodology, in order |
| End goal | What success looks like |
| Narrowing | Constraints and boundaries |

**Skeleton:**

```
ROLE:       You are a senior data engineer.
INSTRUCTIONS: Process a CSV of user registrations into a clean PostgreSQL table.
STEPS:
  1. Validate email format; reject malformed rows to an error log.
  2. Normalize names (trim, title-case).
  3. Deduplicate on email.
  4. Insert valid rows; report counts.
END GOAL:   A clean table plus a summary of inserted / rejected counts.
NARROWING:  Python + psycopg2 only; never drop existing rows; handle bad data gracefully.
```

RISEN separates the *what* (Instructions), the *how* (Steps), the *why* (End goal), and the *boundaries* (Narrowing). It maps to how you'd brief a skilled colleague.

*Origin: Kyle Balmer — an evolution of the earlier RISE framework, adding explicit Narrowing.*

---

## TIDD-EC — Task, Instructions, Do, Don't, Examples, Context

**Best for:** high-precision or compliance work where boundaries must be explicit — secure code generation, regulated content, quality-critical output.

| Component | What it carries |
|---|---|
| Task | Nature of the work |
| Instructions | What to accomplish |
| Do | Explicit positive guidance |
| Don't | Explicit things to avoid |
| Examples | Reference samples showing the bar |
| Context | Background |

**Skeleton:**

```
TASK:         Generate a user-facing error message for a failed payment.
INSTRUCTIONS: One clear sentence the user can act on.
DO:           Name the likely cause; give one next step; stay calm and plain.
DON'T:        Blame the user; expose stack traces, codes, or PII; use jargon.
EXAMPLES:
  Good: "Your card was declined. Check the number and expiry, then try again."
  Bad:  "Error 402: txn_auth_fail at gateway node 7."
CONTEXT:      Shown in a checkout modal to non-technical shoppers.
```

The explicit Do / Don't pair is what sets TIDD-EC apart — it tells the model directly which characteristics must and must not appear. Keep the Don't list short and specific; long prohibition stacks backfire (see `anti-patterns.md` #3).

---

## BAB — Before, After, Bridge

**Best for:** transforming existing content — refactors, rewrites, tone changes, migrations. You have a current state and a target state.

| Component | What it carries |
|---|---|
| Before | The current state and what's wrong with it |
| After | The desired end state |
| Bridge | The transformation rules and constraints |

**Skeleton:**

```
BEFORE: <paste current code/copy>. Problems: nested callbacks, no error handling.
AFTER:  Same behavior, async/await, errors surfaced to the caller, unit-testable.
BRIDGE: Preserve the public API; don't add dependencies; keep it under 60 lines;
        add a one-line comment only where logic isn't self-evident.
```

BAB frames the task as a current → target transition with the Bridge carrying the rules. It's a clean fit whenever you already hold the input and want a controlled transformation rather than fresh generation.

*Origin: a community prompt pattern adapted from the classic Before-After-Bridge copywriting structure.*

---

## Chain of Thought (CoT)

**Best for:** reasoning, debugging, math, decision analysis — anything with a path to work through.

Instruct the model to reason in explicit steps, separated from the final answer, and to self-verify before concluding.

**Skeleton:**

```
You are a debugging assistant. A function returns the wrong total for some inputs.

<code>{{code}}</code>
<failing_case>{{input_and_expected}}</failing_case>

Work through this step by step in <reasoning> tags: trace the inputs, find where
the value diverges, and identify the root cause. Then in <answer> tags give the
fix and a one-line explanation. Before finishing, check the fix against the
failing case.
```

> **Target model note:** a native-reasoning model (the current flagship and frontier tiers across major vendors — live lineup in `model-snapshot.md`) already thinks before answering. On those models, explicit "think step by step" framing is redundant or harmful. Reserve CoT scaffolding for non-reasoning / chat models or thinking-off deployments. See `model-notes.md`.

*Research: Wei et al., 2022 — "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models."*

---

## RTF — Role, Task, Format (and APE for the ultra-minimal case)

**Best for:** simple, well-defined tasks where a little expertise framing is enough.

| Component | What it carries |
|---|---|
| Role | The expertise required |
| Task | What to do |
| Format | Output structure |

**Skeleton:**

```
You are a technical editor. Rewrite the paragraph below to be clearer and 20%
shorter, preserving all facts. Return only the revised paragraph.

<paragraph>{{text}}</paragraph>
```

**APE — Action, Purpose, Expectation** — for one-off, throwaway prompts where even RTF is too much:

```
Summarize the text below in 3 bullets (Action) so a busy manager gets the gist
(Purpose); each bullet ≤15 words, lead with the decision (Expectation).

<text>{{text}}</text>
```

RTF is the lightest structured option — three components, short prompt, fast output. Reach for it (or APE) before anything heavier when the task is unambiguous.

---

## Agent / System structure — tool-using agents and system prompts

**Best for:** prompts that drive an agent with tools, or system prompts that set persistent behavior across a session. The failure modes here are different from a single-shot prompt: the model has to decide *when to act*, *which tool to call*, and *when to stop*.

Cover these components; drop the ones a given task doesn't need:

| Component | What it carries |
|---|---|
| Role + available tools | Who the agent is and exactly what tools it has, each with a one-line "use it when…" trigger |
| Act vs. ask | The default: proactive ("infer the most useful action and proceed") or conservative ("gather information and recommend rather than act") |
| Tool-use discipline | Prefer small, targeted calls over one broad call; define what to do on a tool error (retry once with a narrower input, then report) |
| Parallel tool calls | When multiple calls are independent, run them simultaneously — significant latency win |
| Stop / exit conditions | What "done" looks like; what to do if it cannot finish (report blockers, don't loop) |
| Output contract | What the agent returns at the end, in exactly what shape |

**Skeleton:**

```
You are a release assistant with these tools:
  - run_tests(): use before any tagging step.
  - read_file(path) / write_file(path, content): use to edit changelog entries.

By default, take the next release step rather than asking; if a step is ambiguous,
infer the most useful action and proceed, using read_file to confirm rather than
guessing. Make small, targeted tool calls. If a tool errors, retry once with a
narrower input, then report and stop.

Stop when the changelog is updated and tests pass, OR report the blocker if tests
fail. Return a two-line summary: what changed and the test result.
```

The "right altitude" for a system prompt sits between hardcoding brittle if-then logic and vague hand-waving. Bloated tool sets with overlapping triggers are a common failure mode — curate a minimal viable set.

---

## Advanced / critique set — stress-testing and verifying

Reach for these when the goal is to *harden or check* a prompt or an answer, not to draft fresh content. Keep them compact; they are tools, not a checklist to run every time.

| Technique | When to use |
|---|---|
| **Self-Refine** | Generate, then critique the draft against criteria, then revise. One pass usually suffices; it catches sloppy first drafts cheaply. |
| **Red-team (Devil's Advocate / Pre-Mortem)** | Argue the strongest case *against* the prompt or plan, or imagine it has already failed and explain why. Surfaces failure modes a forward pass misses. |
| **RCoT (Reverse Chain of Thought)** | Have the model restate the requirements from its own draft and check that none were dropped or contradicted. Good for multi-constraint tasks where a requirement quietly gets lost. |
| **Chain of Density** | For summarization: produce an initial summary, then iterate — each round adds missing entities while keeping length fixed. Yields a dense, information-rich summary. |

**Self-Refine skeleton:**

```
Draft a response to {{input}}. Then, in <critique> tags, judge it against these
criteria: {{criteria}}. List concrete weaknesses. Then in <final> tags, output a
revised version that fixes them. Show only the <final> block to the user.
```

*Research: Self-Refine — Madaan et al., 2023. Chain of Density — Adams et al., 2023.*

---

## Prompt chaining — when to split a task across multiple prompts

A single prompt is the right default. Chain only when one prompt genuinely can't hold the whole task.

**Chain when:**
- The output of step A is the input of step B and can't be known upfront.
- The context window can't hold the full input + instructions + expected output at once.
- Different steps need different models, temperatures, or tools.
- Reliability matters: checkpointed steps make failures easier to isolate and retry.

**Don't chain when:**
- The task fits in one prompt and the model can hold all context comfortably.
- Latency matters more than reliability (each link adds round-trip time).
- The steps aren't truly sequential — parallel calls are faster.

**Handoff format:** pass only what the next step needs, not the full conversation history. Wrap the handoff in a clear tag: `<step1_output>…</step1_output>`. State in the next prompt what the block contains and what to do with it.

**Context hygiene:** summarize or compress intermediate outputs before passing them forward. A chain that accumulates full outputs at every step will hit the context limit faster than one that passes lean summaries.

---

## Long-context structuring — where to place data and instructions

When a prompt carries large inputs (20k+ tokens), placement matters as much as wording.

| Rule | Why it works |
|---|---|
| **Data at the top, question at the end.** Put long documents and inputs above the query, instructions, and examples. | For Claude, this ordering can lift quality by up to ~30% on complex, multi-document inputs. |
| **Avoid the middle for anything critical.** | Models attend least to the middle of a long context ("lost in the middle"). Put the most important instructions at the start or the end. |
| **Ground in quotes.** Ask the model to first quote the relevant passages, then answer. | Cuts through surrounding noise and reduces hallucination. |
| **Tag the structure.** Wrap each document in clear tags with source/metadata (e.g. `<document index="1">`). | Lets the model tell documents apart and cite which one it used. |

*Source: Anthropic prompt-engineering guidance.*

---

## Note on research backing

The acronym frameworks (CO-STAR, RISEN, TIDD-EC, BAB, RTF/APE) are widely-used community patterns with named originators where known. The reasoning and critique loops are research-backed:

- Chain of Thought — Wei et al., 2022
- Self-Refine — Madaan et al., 2023
- Chain of Density — Adams et al., 2023
- Constitutional AI (critique-revise) — Bai et al., Anthropic, 2022

The placement, example, and prefill guidance follows Anthropic's published prompting best practices. Full citations and links are in `SOURCES.md`.
