# revenant-foundation-promptsmith

A prompt-engineering skill for agentic LLMs. Turns a rough idea, a set of parameters, or an existing prompt into a robust, scored, copy-paste-ready artifact. What separates it from framework-based prompt builders: every prompt ships with a model recommendation routed by capability tier (Claude by default, any major vendor on request), model data self-updates via a snapshot with a 60-day staleness rule ("promptsmith refresh"), finished prompts export as savable offline HTML prompt cards, and restraint rules keep it from building prompts that shouldn't exist.

**Workflow:** Intake → Analyze + Score → Pick structure → Clarify (only if needed) → Build → Re-score & self-check → Output

Prompts are scored on five dimensions (clarity, specificity, context, completeness, structure) and reported as a before → after delta, so improvement is visible rather than asserted. Every delivered prompt leads with a plain-language **TL;DR** so a non-author understands what it does at a glance.

See `SOURCES.md` for the public material the skill's guidance draws on.

---

## Package contents

```
revenant-foundation-promptsmith/
├── SKILL.md                      # entry point — workflow, scoring, structures, restraint, output
├── README.md                     # this file
├── LICENSE                       # MIT license
├── CHANGELOG.md                  # version history
├── SOURCES.md                    # maps guidance to public origins
├── references/                   # runtime references — loaded per the SKILL.md load budget
│   ├── frameworks.md             # CO-STAR, RISEN, TIDD-EC, BAB, CoT, RTF/APE, Agent/System, chaining, long-context
│   ├── anti-patterns.md          # 11 prompt failure modes and their fixes
│   ├── prompt-hardening.md       # injection resistance and production guardrails (OWASP LLM Top 10)
│   ├── model-notes.md            # durable per-model guidance + tier-routing rules (Claude, GPT, Gemini, Grok, DeepSeek, open)
│   ├── model-snapshot.md         # volatile model data: current names, cost bands, sources, Last-verified stamp
│   ├── evaluation.md             # rubrics and test inputs for high-stakes prompts
│   ├── worked-examples.md        # three full worked examples in the current output contract
│   ├── pack.md                   # foundation-pack roster — stamped, advisory; consulted on boundary doubt only
│   └── prompt-card.md            # self-contained offline HTML prompt card template and fill rules (opt-in)
└── evals/                        # maintenance / QA — full archive only; excluded from .skill installs
    ├── test-cases.md             # 28-case regression suite, assertion-only mechanical checks
    └── trigger-evals.md          # 24 should/shouldn't-trigger queries for description tuning
```

---

## Install

This skill follows the [Agent Skills](https://agentskills.io/) open standard: a folder containing a `SKILL.md` with YAML frontmatter, plus Markdown and reference files.

1. Drop the `revenant-foundation-promptsmith/` folder into the skills directory your agent platform reads.
2. The agent loads the `description` from the frontmatter; the body and `references/` files are pulled in progressively as needed.
3. Trigger it by saying `promptsmith`, by handing it a prompt to improve, by asking which model to run a prompt on, or by describing what you want to build — audience, tone, format, model, constraints — and it will assemble the prompt.

The skill is self-contained and declares no `allowed-tools` restriction — it inherits the session's tools, so it can always read its own `references/` files on any surface. It uses web search sparingly (external fact-checking, model-lineup verification); the Keep going options render as a native tappable selection where the session's tool list has an option/question tool, and a plain-text fallback line elsewhere — no inline widget or visualization tooling is needed either way. No shell access required for normal use.

---

## Commands & switches

Named invocations — everything else routes on natural requests ("write me a prompt that…", "improve this prompt", "which model should run this?"):

| Invocation | What it does |
|---|---|
| `promptsmith` | Bare invocation — capability line naming the refresh subcommand, then asks what to write or improve |
| `promptsmith refresh` | Re-verifies model lineups against the canonical sources in `references/model-snapshot.md`; regenerates the snapshot only, patch bump + repackage. Run at the 60-day stamp or when a major model launches |

| In-request switch | Effect |
|---|---|
| "just build it" | Skips or exits any clarification round; the build proceeds immediately on stated smart assumptions |
| "quiet build" / "just the prompt" | Collapses Phases 1–6 into one trace line above the output — footer, Model line, and Keep going selection unchanged |
| "interview me" | Opt-in requirement interview in short question batches for fuzzy specs; exit any time with "just build it" |
| "try [structure] instead" | Switches the framework (e.g. RISEN for CO-STAR) and rebuilds — no pushback, no re-asked intake |
| "harden it" / "add examples" | Runs that half of the harden + examples path alone |
| Keep going options | `harden + examples` · `switch model` · `generate savable prompt card` · `run it now` — tappable after any delivered prompt, or typed any time (see Output) |

---

## Performance

The entry file is kept lean and a **load budget** caps a standard build at two reference loads: the chosen section of `frameworks.md` plus `model-snapshot.md`. Core tier routing is inlined in `SKILL.md`, and the Keep going options close the response as a native tappable selection where supported, or a plain-text fallback line — no inline-widget render calls — so typical builds involve far fewer file reads and render faster. The remaining references load only when their trigger condition fires (hardening, non-Claude targets, cards, evals).

---

## Output

The deliverable is the prompt itself, led by a fenced code block under the `── Phase 7 / 7 — Output ──` header (all seven phase headers appear on a full build). An opt-in **quiet build** ("quiet build" / "just the prompt") collapses Phases 1–6 into a single trace line above the output instead — footer, Model line, and Keep going selection unchanged. Beneath it sits a compact footer in this order: a plain-language **TL;DR**, a mandatory **Model** line (tier + recommended model + reasoning-depth setting — every delivered prompt names what to run it on), the before → after score, the chosen structure, then variables, assumptions, and one test suggestion. The **Keep going** selection closes the response as its final element — a tappable single-select where an option/question tool exists in the session's tool list (Claude app / claude.ai web), else a plain-text fallback line (API, Claude Code, exported text) — with four options:

| Option | What it does |
|---|---|
| `harden + examples` | Apply production / injection-resistance hardening and generate few-shot examples together |
| `switch model` | Re-target the prompt to a different model/vendor or tier and adapt its syntax |
| `generate savable prompt card` | Produce a self-contained offline HTML artifact |
| `run it now` | Execute the prompt directly in chat |

Typing `harden it` or `add examples` on its own still triggers that half alone.

The HTML prompt card is **hard opt-in**: it is produced only when the user selects "generate savable prompt card" from the Keep going options, or explicitly requests it. It is a fully offline artifact — no API calls, no network dependency — and carries a mandatory **Run on** section mirroring the chat Model line, so a saved card never strands its reader without a run target. On Chat/Cowork surfaces the skill does not deliver the prompt as a Markdown file.

---

## Model recommendations & staying current

The skill recommends a **capability tier** (frontier / flagship / balanced / fast) and then the cheapest model in the target vendor's lineup that clears that bar — defaulting to Claude. The durable routing logic lives in `references/model-notes.md` §2; the volatile facts (current model names, cost bands, context quirks) are isolated in `references/model-snapshot.md` behind a single **Last-verified** stamp.

**Keeping it current is one phrase.** Model lineups move fast, so the skill degrades gracefully — past the 60-day stamp it verifies against canonical sources before naming a model, and recommends by tier name if it can't. To fully refresh, say **"promptsmith refresh"**: the skill re-researches the current lineups against the vendor docs and registries listed in the snapshot, regenerates `model-snapshot.md` only, bumps the patch version, writes a CHANGELOG line, and (on claude.ai) hands back a repackaged skill to reinstall. Recommended cadence: on the 60-day stamp, or whenever a major model launches.

*Optional (self-hosted repos):* a scheduled CI job diffing the LiteLLM registry monthly and opening an issue on drift is a heavier alternative to the manual refresh — see the sources in `model-snapshot.md`.

---

## Pack

promptsmith is part of the **foundation** pack (standalone profile), declared in frontmatter metadata. `references/pack.md` carries a stamped roster of pack siblings for mid-task handoffs — advisory only: an uninstalled sibling is recommended by name, never a failure, and initial routing stays at the name + description level. The canonical roster lives in skillsmith's registry, which re-stamps the copy whenever it builds, audits, or refreshes this skill.

## Renaming

The skill's identity is set in two places that must stay in sync: the folder name and the `name:` field in `SKILL.md` frontmatter. To rename, change both to the same kebab-case value (lowercase letters, numbers, and hyphens). The wordmark on the HTML prompt card lives in `references/prompt-card.md` if you want to update it to match.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
