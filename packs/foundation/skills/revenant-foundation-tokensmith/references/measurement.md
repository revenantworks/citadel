# Measurement — Volatile Baseline *(single update surface)*

> **Last verified: 2026-07-23.** This file is the **only** one "tokensmith refresh" regenerates — ratios, cache mechanics, and platform reference points drift with models and pricing; the taxonomy and doctrine in `waste-taxonomy.md` do not. When the stamp is >60 days old, treat every number here as possibly stale and say so in reports.

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
2. **Estimate** — character- or word-ratio arithmetic from the table below. Label: `estimate (±15%)`. Show the arithmetic once per report (`chars ÷ ratio`), not per line item.
3. **Never** — word counts presented as token counts, or counts with no stated method. Both are report defects.

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

## Cache mechanics *(verified 2026-07-23)*

- **Caches hit on prefixes.** Stable content first, variable content last; anything ordered after a variable element does not cache. The high-hit order: system prompt → tool definitions → long static context → slow-changing context → the live request.
- **Anthropic:** explicit `cache_control` breakpoints (≤4 per prompt); cache writes bill ~1.25× the input rate for the 5-minute TTL, ~2× for the 1-hour TTL; reads ~0.10× (a ~90% discount); the TTL refreshes on each read, and cache reads don't count toward input-rate limits on current models. **OpenAI:** automatic caching on stable prefixes past ~1,024 tokens; on the current families (GPT-5.4 onward) reads bill ~0.10× of input — the old ~50% discount applies only to legacy gpt-4o-era models — and the GPT-5.6 family bills cache *writes* at ~1.25× with a 30-minute minimum cache life. Confirm live pricing before architecting around either — that's what Refresh is for.
- **The cache-safety corollary:** editing a cached artifact invalidates its prefix and forces one re-write. A slim is cache-positive when `(tokens saved × reads × read rate) > (rewrite cost)` — for hot prefixes that's almost always (a 5-minute Anthropic write breaks even inside one read), for rarely-read ones it may not be. Reordering *within* the stable block is free at the next write; interleaving anything volatile into it is the expensive mistake.
- **Volatile facts belong in stamped, isolated files** — which is also what keeps the big stable body cacheable.

## Platform reference points

- **Skill metadata** (name + description) is always-on — measured discovery cost runs a median of ~80 tokens per installed skill (range ~55–235 across Anthropic's official skills), every session. The description is the one surface where thrift and routing compete; routing wins, then trim.
- **Skill bodies** load on trigger — the ≤500-line norm (≈5k tokens) is the ceiling, not the target; references load on demand one level deep. This progressive-disclosure shape is the reference architecture for any artifact set.
- **Tool/MCP schemas load whole and always** in most harnesses — documented sessions show five-figure always-on schema costs versus double-digit costs for an equivalent trigger-loaded skill. The strongest standing argument for conditional surfaces over resident ones.
- **Session floors are real:** agent CLIs commonly start tens of thousands of tokens deep (system prompt + instruction files + schemas + skill metadata) before the first user word. Budget sheets treat that floor as spent, not available.

## Honesty rules

Before → after pairs on every slim; method named on every count; the ± band shown on every estimate; net-cost arithmetic shown whenever text is added; "verified as of" language on anything from this file when the stamp is aging.
