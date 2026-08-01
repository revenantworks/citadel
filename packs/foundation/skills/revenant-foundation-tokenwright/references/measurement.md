# Measurement — Volatile Baseline *(stamped update surface)*

> **Last verified: 2026-07-27.** `tokenwright refresh` restamps this file: ratios, cache mechanics, and platform reference points drift with models and pricing; the taxonomy and doctrine in `waste-taxonomy.md` do not. Refresh's full scope — including the three platform values the SKILL body mirrors from here: cap, counting unit, listing budget — is stated in SKILL.md — Entry — Refresh. When the stamp is >60 days old, treat every number here as possibly stale and say so in reports.

## Contents

- Method ladder
- Estimation ratios
- Net-cost accounting
- Cache mechanics
- Platform reference points
- Honesty rules

---

## Method ladder

Highest available method wins; the report names which was used.

1. **Exact** — a real tokenizer or counting endpoint on the current surface (a code-execution surface with a tokenizer library installed; an API token-count endpoint). Label: `exact (<tool>)`. Different model families tokenize differently — an exact count is exact *for the named tokenizer*.
2. **Estimate** — character- or word-ratio arithmetic from the table below. The character/word count feeding that arithmetic must itself come from a **named counting method** — a language runtime's length function, a shell count, a script — stated alongside the number; never eyeballed, approximated, or recalled from a prior report. Label: `estimate (±15%, chars via <tool>)`. Show the arithmetic once per report (`chars ÷ ratio`), not per line item.
3. **Never** — word counts presented as token counts, counts with no stated method, or a character/word input with no named counting source (an eyeballed, approximated, or remembered figure dressed as `estimate (±15%)`). All three are report defects, and the last one is invisible to the ±15% band — a wrong count that happens to land inside the band still ships as fact unless the source is checked.

## Estimation ratios

| Content type | Ratio | Notes |
|---|---|---|
| English prose | ~4 chars/token · ~0.75 tokens/word | The default for docs, prompts, instructions |
| Source code | ~3–3.5 chars/token | Identifiers and symbols tokenize denser than prose |
| Dense markup (tables, JSON, YAML) | prose ratio, then add structural overhead | Pipes, braces, fences, and indentation are tokens too — a markdown table can cost 30–50% more than the same facts as terse lines |
| Non-Latin scripts | measure, don't assume | Chars/token runs materially lower; the prose ratio misleads |

Estimates carry a ±15% band. When a decision sits inside the band (an artifact "just fits" a budget on the estimate), say so and prefer an exact count before calling it fit.

## Net-cost accounting

- **Always-on text bills per turn.** Cost = size × turns in scope. A 300-token rule that trims 150 tokens of output per turn is profit; the same rule saving 20 is a loss by turn three. Every recommendation that *adds* instruction text states this arithmetic.
- **Tokens-per-task is the target, not tokens-per-request.** A larger one-shot that finishes beats a lean loop that retries — savings are counted across the whole task, including the re-prompts a too-aggressive cut causes.
- **A slim that costs behavior isn't a saving.** Re-prompting, corrections, and broken evals are token costs; the preservation contract exists because they usually exceed what the cut recovered.

## Cache mechanics *(rates verified 2026-07-23; minimum cacheable length per-model table re-verified live 2026-07-27)*

*Units: every number in this section is in **tokens**. Character limits — the description caps — live in Platform reference points below, and no threshold here is one.*

- **Caches hit on prefixes.** Stable content first, variable content last; anything ordered after a variable element does not cache. The high-hit order: system prompt → tool definitions → long static context → slow-changing context → the live request.
- **Anthropic:** explicit `cache_control` breakpoints (≤4 per prompt); cache writes bill ~1.25× the input rate for the 5-minute TTL, ~2× for the 1-hour TTL; reads ~0.10× (a ~90% discount); the TTL refreshes on each read. *(A further claim that cache reads do not count toward input-rate limits is **unsourced here** — it is absent from the prompt-caching page and belongs to the rate-limits docs; re-verify or drop it at the next refresh.)* **Minimum cacheable length**: a prefix shorter than the model's floor never caches — `cache_control` is accepted and **silently ignored**, with no error. **Diagnose it on BOTH counters:** a prompt was not cached only when `cache_creation_input_tokens` **and** `cache_read_input_tokens` are both 0 — on a successful cache *read* the creation counter is also 0, so the one-field test misreads a working hit as "never cached".

  **The floor is per-model, not a single number or a smooth range — read the row for the model in scope** *(https://platform.claude.com/docs/en/build-with-claude/prompt-caching, fetched and verified twice on 2026-07-27; applies on the Claude API, Claude Platform on AWS, Google Cloud, and Microsoft Foundry)*:

  | Minimum tokens | Models |
  |---|---|
  | 512 | Claude Opus 5, Claude Fable 5, Claude Mythos 5 |
  | 1,024 | Claude Opus 4.8, Claude Sonnet 5, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Opus 4.1 (deprecated), Claude Opus 4 (retired except Google Cloud), Claude Sonnet 4 (retired except Bedrock and Google Cloud) |
  | 2,048 | Claude Mythos Preview, Claude Opus 4.7, Claude Haiku 3.5 (retired except Bedrock and Google Cloud) |
  | 4,096 | Claude Opus 4.6, Claude Opus 4.5, Claude Haiku 4.5 |

  It does not track capability tier or release recency: the newest Opus tier (Opus 5) sits at the *lowest* floor (512) while the previous Opus generation (4.6/4.5) sits at the *highest* (4,096), and Haiku 4.5 shares that same 4,096 ceiling with them. So tier, generation, or "it's the flagship/fast one" is never a proxy for the floor — name the model in scope and read its row; a single flat range invites assuming the low end applies pack-wide, which it does not. **OpenAI:** automatic caching on stable prefixes past ~1,024 **tokens** — a token threshold, not a character count, and not a cap on description length; on the current families (GPT-5.4 onward) reads bill ~0.10× of input — the old ~50% discount applies only to legacy gpt-4o-era models — and the GPT-5.6 family bills cache *writes* at ~1.25× with a 30-minute minimum cache life. Confirm live pricing before architecting around either — that's what Refresh is for.
- **The cache-safety corollary:** editing a cached artifact invalidates its prefix and forces one re-write. A slim is cache-positive when `(tokens saved × reads × read rate) > (rewrite cost)` — for hot prefixes that's almost always (a 5-minute Anthropic write breaks even inside one read), for rarely-read ones it may not be. Reordering *within* the stable block is free at the next write; interleaving anything volatile into it is the expensive mistake.
- **The floor gates that arithmetic.** Check the prefix against the minimum cacheable length before running it. Under the floor there is no cache to hit: the read saving is zero however hot the prefix looks, so the payback never lands. Report "below the minimum cacheable length — this prefix cannot cache" and name what it would take to clear the floor; never project a saving for a prefix that cannot cache.
- **Volatile facts belong in stamped, isolated files** — which is also what keeps the big stable body cacheable.

## Platform reference points

- **Skill metadata** (name + description) is always-on — measured discovery cost runs a median of ~80 tokens per installed skill (range ~55–235 across Anthropic's official skills), every session. The description is the one surface where thrift and routing compete; routing wins, then trim.
- **Description cap — 1,536 characters, per listing entry** *(added 2026-07-24; re-sourced to Anthropic's own docs 2026-07-25)*. Counted in **characters, not tokens**: the skill listing sent to the model truncates each entry's routing text at Claude Code's `skillListingMaxDescChars`, whose default is 1,536. **Counting unit — `description` and `when_to_use` concatenated.** Anthropic's Claude Code skills documentation states this three times: the `description` row ("the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing"), the `when_to_use` row ("Appended to `description` in the skill listing and counts toward the 1,536-character cap"), and troubleshooting ("each entry's combined text is capped at 1,536 characters regardless of budget") — SOURCES.md — Description cap. No member of this pack declares `when_to_use`, so for them the combined text is the description. The setting is user-configurable, so the figure drifts: this stamp is its source of truth, SKILL.md's Description cap rule mirrors it, and Refresh re-verifies the unit as well as the number (sync scope: SKILL.md — Entry — Refresh).
- **Skill-listing budget — 1% of the model's context window** *(added 2026-07-25)*. A second, separate mechanism on the same surface, not a per-entry cap. The listing always carries every skill *name*; the descriptions are held to a budget that "scales at 1% of the model's context window" (`skillListingBudgetFraction`, or the `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable). On overflow Claude Code shortens descriptions to fit and then drops them starting with the least-invoked skills. Being window-relative and shared across every installed skill, it moves with the window size and the installed count — so it can bite far below the 1,536 per-entry cap, which is why that cap applies "regardless of budget". Stamped here, mirrored in SKILL.md's Description cap rule.
- **Skill bodies** load on trigger, not always-on, so their cost is per-invocation rather than a standing tax; the discovery layer is the always-on surface. Two separate measures, and conflating them is a real error: the **≤500-line norm** is the ecosystem spec (agentskills.io), while **token weight** is the truer cost and does not track line count — a dense 265-line body can outweigh a sparse 500-line one, which is why a flat token gloss fires on spec-compliant skills. Measure both, and where a body earns extra weight by carrying enforceable rules inline, declare the budget rather than mute the signal. References load on demand one level deep; that progressive-disclosure shape is still the reference architecture for any artifact set.
- **Tool/MCP schemas load whole and always** in most harnesses — documented sessions show five-figure always-on schema costs versus double-digit costs for an equivalent trigger-loaded skill. The strongest standing argument for conditional surfaces over resident ones.
- **Session floors are real:** agent CLIs commonly start tens of thousands of tokens deep (system prompt + instruction files + schemas + skill metadata) before the first user word. Budget sheets treat that floor as spent, not available.

## Honesty rules

Before → after pairs on every slim; method named on every count; the ± band shown on every estimate; net-cost arithmetic shown whenever text is added; "verified as of" language on anything from this file when the stamp is aging.
