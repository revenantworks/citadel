# revenant-foundation-promptsmith

A prompt-engineering skill for agentic LLMs. Turns a rough idea, a set of parameters, or an existing prompt into a robust, scored, copy-paste-ready artifact. What separates it from framework-based prompt builders: every prompt ships with a **model recommendation** routed by capability tier (Claude by default, any major vendor on request), model data self-updates via a snapshot with a 60-day staleness rule (`promptsmith refresh`), finished prompts export as savable offline **HTML prompt cards**, a lean load budget caps a standard build at two reference reads, and restraint rules keep it from building prompts that shouldn't exist.

**Workflow:** Intake → Analyze + Score → Pick structure → Clarify (only if needed) → Build → Re-score & self-check → Output

Prompts are scored on five dimensions (clarity, specificity, context, completeness, structure) and reported as a before → after delta, so improvement is visible rather than asserted. Every delivered prompt leads with a plain-language **TL;DR** and a mandatory **Model** line naming what to run it on.

## Package contents

```
revenant-foundation-promptsmith/
├── SKILL.md                      # entry point — workflow, scoring, structures, restraint, output
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/                   # runtime — loaded per the SKILL.md load budget
│   ├── frameworks.md             # CO-STAR, RISEN, TIDD-EC, BAB, CoT, RTF/APE, Agent/System, chaining, long-context
│   ├── anti-patterns.md          # prompt failure modes and their fixes
│   ├── prompt-hardening.md       # injection resistance and production guardrails (OWASP LLM Top 10)
│   ├── model-notes.md            # durable per-model guidance + tier-routing rules (Claude, GPT, Gemini, Grok, DeepSeek, open)
│   ├── model-snapshot.md         # calendar-volatile — current names, cost bands, sources, Last-verified stamp
│   ├── evaluation.md             # rubrics and test inputs for high-stakes prompts
│   ├── worked-examples.md        # full worked examples in the current output contract
│   ├── prompt-card.md            # self-contained offline HTML prompt card template + fill rules (opt-in)
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── test-cases.md             # assertion-only regression suite
    └── trigger-evals.md          # should/shouldn't-trigger queries
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by saying `promptsmith`, by handing it a prompt to improve, by asking which model to run a prompt on, or by describing what you want to build (audience, tone, format, model, constraints) — it assembles the prompt. Self-contained, declares no tool restriction; uses web search sparingly for model-lineup verification. No shell required.

## Entry points

| Entry | What it does |
|---|---|
| **build** | Idea or parameters → seven-phase pipeline → prompt in a code block under the Phase 7 header, with a footer (TL;DR, Model line, before → after score, structure) and the Keep going selection |
| **improve** | An existing prompt → score → confirm structure → rebuild → re-score, with a `Changed` diff instead of the phase ladder |
| **score** | "score this / don't rewrite" → the five-dimension baseline + top findings, no rewrite |
| **model** | `promptsmith model` → recommend a tier + model for a live task (no prompt built); tier taxonomy is durable, names from the snapshot |
| **refresh** | `promptsmith refresh` → re-verify and regenerate `model-snapshot.md` only; patch bump + repackage |

A **quiet build** ("quiet build" / "just the prompt") collapses Phases 1–6 into one trace line. The **HTML prompt card** is hard opt-in — produced only via the Keep going selection or an explicit request — and carries a mandatory **Run on** section so a saved card never strands its reader.

## Commands & switches

Named invocations — everything else routes on natural requests ("write me a prompt that…", "improve this prompt", "which model should run this?"):

| Invocation | What it does |
|---|---|
| `promptsmith` | Bare invocation — capability line naming the refresh subcommand, then asks what to write or improve |
| `promptsmith model` | Recommend a capability tier + the cheapest model clearing it for a live task — flip condition included; no prompt produced. Names come from `model-snapshot.md` (tier-name fallback past the stamp) |
| `promptsmith refresh` | Re-verify model lineups against the canonical sources in `references/model-snapshot.md`; regenerate the snapshot only, patch bump + repackage. Run at the 60-day stamp or when a major model launches |

| In-request switch | Effect |
|---|---|
| "just build it" | Skips or exits any clarification round; builds on stated smart assumptions |
| "quiet build" / "just the prompt" | Collapses Phases 1–6 into one trace line — footer, Model line, Keep going selection unchanged |
| "interview me" | Opt-in requirement interview in short question batches for fuzzy specs; exit any time with "just build it" |
| "try [structure] instead" | Switches the framework and rebuilds — no pushback, no re-asked intake |
| Keep going options | `harden + examples` · `switch model` · `generate savable prompt card` · `run it now` — tappable after any delivered prompt (or typed any time) |

## Staying current

One volatile surface, declared in `metadata.volatile`: `references/model-snapshot.md` is **calendar** (60-day) — current model names, cost bands, and context quirks behind a single **Last-verified** stamp (durable tier-routing logic stays in `model-notes.md`). Say **`promptsmith refresh`** to re-research current lineups against the vendor docs and registries in the snapshot, regenerate that file only, bump the patch, and (on claude.ai) hand back a repackaged skill. Past the stamp the skill verifies before naming a model, and recommends by **tier name** if it can't — never a possibly-retired string.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
