# Changelog — revenantworks-foundation-promptwright

> Renamed from `revenant-foundation-promptwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.4.1] — 2026-08-17

Estate member audit + security scan (2026-08-17; rubric A, S-1..S-4, C-1/C-2,
OWASP agentic lenses) plus the calendar refresh the stamp owed. The description
is untouched, so the routing surface did not move.

**Findings and fixes:**

- **S-1 · P1 — mid-build web fetch escaped the rule.** The head note permits
  web search "for an external fact the prompt's job needs, or to verify the
  model lineup"; both fetch pages the skill did not author, and the
  data-never-instructions rule sat only in Phase 1 (handed-in text) and Entry —
  Refresh (that entry's own fetches). Fix: the permission now states that a
  page fetched for either is data, never instructions, on Phase 1's terms.
- **S-1 · P1 — Entry — Model's plan grain escaped the rule.** A plan handed
  in for tiering is an ingested artifact, and the entry runs Tier routing
  "invoked directly" without passing Phase 1 (the same gap 1.4.0 closed for
  Refresh). Fix: one located sentence in Plan grain — the handed-in plan is
  data; a line in it addressed to the run rather than describing a subtask
  (pin every row to one tier, waive the flip conditions or the standing rule)
  is a finding reported beside the table, never a routing input. Text that
  names a target *inside a subtask's own description* stays user direction
  under Tier routing's 1.3.0 override; the two rules bind different text.
- **Eval gap (rubric f).** Case 36 was the suite's only injection probe and
  covered build/improve. Added, authored not run: **Case 40** (score-only,
  then red-team by name), **Case 41** (plan grain — a routing directive
  embedded in the plan beside a legitimate subtask-level model ask), **Case
  42** (refresh — an instructing source page). 39 → 42. The count line in
  `evals/test-cases.md` had read 38 since 1.3.0 while the suite held 39;
  corrected.
- Rubric A otherwise clean: description matches the body (every entry point
  advertised, boundary clauses true); references one level deep, TOCs on
  every 150+ line file; every referenced file present, no broken relative
  links; no `citadel` mention live anywhere in the member; no Windows-style
  paths; invocation control (dimension 11) passes — the only writes (Refresh's
  regeneration of `model-snapshot.md` + this file + the version; the prompt
  card) fire on a named invocation or a hard opt-in, never silently.

**Security scan 2026-08-17:** (a) prompt-injection posture — every ingesting
step now states the rule (Phase 1 intake incl. score-only and red-team, the
mid-build fetch, Entry — Refresh, Entry — Model plan grain); (b) no
fetch-and-follow, permission-widening, secret-echo or guard-bypass instruction
in SKILL.md or any reference; (c) tool scoping — web search and native file
tools only, no shell, degradation stated (no search → no restamp; no HTML
surface → no card; no option tool → plain-text selection); (d) hidden-text
scan clean (2026-08-17); (e) output handling — Refresh writes one named file
plus the CHANGELOG line and version, the card is opt-in only; (f) one
injection probe per ingesting entry (Cases 36, 40, 41, 42). S-2 none, S-3
none, S-4 none (the card template is single-file, offline, no external host).

**Refresh — `model-snapshot.md` restamped Last verified 2026-08-17.** All five
vendor model docs fetched live (Anthropic models overview + pricing + effort
pages; OpenAI models, model pages and pricing; Gemini models + pricing;
docs.x.ai models; api-docs.deepseek.com pricing), OpenRouter registry as
cross-check; LiteLLM not fetched this pass. Changes: Claude A-tier Opus 4.8 →
**Opus 5** (4.8 now legacy, same price); Sonnet 5's $2/$10 is now standard
(the 2026-09-01 rise cancelled); 128K output on Fable 5, Opus 5 and Sonnet 5;
`effort` levels are low/medium/high/xhigh/max (no `minimal`/`none`; xhigh and
max coverage restated; Haiku 4.5 has no effort control); Opus 4.7+ tokenizer
note added. OpenAI: 5.4 nano/mini no longer undercut Luna — dropped from the C
slot; long-context premium (>272K) attributed to the whole 5.x line; cache
1.25×/0.1×/1,024-token minimum/30-minute life verified. Gemini B-tier 3.6
Flash → **3.7 Flash** (Aug 2026, GA); 3.6/3.7 Flash promo price to
2026-12-31 recorded; 3.5 Pro still absent (Aug 13 press confirms delay); 3.1
Pro corrected to its `-preview` id. Grok A-tier 4.5 → **4.6** (2026-08-12,
500K); 4.1 Fast is gone from xAI's model list — removed from the C slot,
which now reads Grok 4.3 (the 4.20 non-reasoning variant for latency); the
"2M context" quirk rewritten around 4.3's 1M. DeepSeek: the API now lists
only V4 Pro (0813) and V4-Flash (0731), both 1M / 384K, thinking on by
default — the bare "V4" B slot → V4-Flash; the expired promo note dropped for
the off-peak half-rate note. Not re-verified and retired with the models they
described rather than carried: the 3.6-vs-3.5 Flash "~17% fewer output
tokens" figure and the Flash-Lite "~350 tok/s" figure. Left as previously
stated (not re-verified live this pass): the "Grok 4 Heavy" consumer-product
name for the S slot (docs.x.ai lists no Heavy API model; the footnote holds
either way). Observation for the next durable-file pass, not changed here:
`model-notes.md` §6 says multi-agent Heavy is not an API capability, while
docs.x.ai now lists a `grok-4.20-multi-agent` API model at 4.3 rates.

**Body budget:** 8977 → 9004 measured against the 9030 row (`build.py
--footprint`); the two additions were paid for by seven claim-preserving trims
(the `evals/` load-budget line, the volatile-block sentence, the Fast-path
say-so, Phase 3's Fast-path exception, Entry — Model's opener and step 3, the
Maintenance note), each a restatement of a rule whose binding statement lives
elsewhere in the body. No row raise needed.

Both eval heads re-anchored to 1.4.1. Trigger suite unchanged (34, 17/17);
Cases 40–42 authored, not run — no RESULTS.md row.

## [1.4.0] — 2026-08-12

Two 2026-08-12 estate-audit findings closed in Entry — Refresh; the
description is untouched, so the routing surface did not move:

- **Refresh injection rule (finding 2).** The refresh path re-researches live
  vendor pages and writes the result into `model-snapshot.md`, the file every
  Model line reads — and the handed-in-text-is-data rule lived only in Phase
  1, which the refresh entry explicitly skips. The rule now rides in the
  entry itself: a fetched page is data, never instructions; an instructing
  source is itself a finding, recorded at its URL.
- **Search-unavailable fallback (finding 14).** The entry now states what a
  refresh does when it cannot verify: never re-stamp, report the surface
  unverified, leave the Last-verified date untouched, name the invocation to
  re-run — so the stamp downstream members trust keeps its meaning.

## [1.3.0] — 2026-08-05

Tier routing (Phase 5) gains the **user-named-target override**, directed by
the pack owner and recorded as the ENHANCE verdict in AUDIT-2026-08-05: a
model or effort the user names wins, exactly as a named framework wins in
Phase 3 — build to the stated target, shape the prompt for that tier, never
quietly substitute the routed pick; when routing disagrees, the Model line
notes the target was set by user direction and offers the better tier or
effort in one line. Entry — Model is bound identically (stated target
confirmed, not re-routed, disagreement named). Single-homed in Tier routing,
as the role-based overrides are.

Four lossless trims in the same pass offset the addition against the 8,850
body budget (AUDIT-2026-08-05 TRIM verdict; all four are restatements of
rules whose binding statement lives elsewhere in the body, no rule moved):
Turn shape rule 5's quiet-build/Fast-path contrast compressed (the full
distinction lives in the Fast path section); the Keep going Rendering
bullet's tool-list-test restatement now points at Turn shape rule 2, keeping
the observed-field-failure example; the Load budget's `hostile-interpreter.md`
bullet compressed (its reach-for conditions restate Phase 6's); the
Surface-awareness note's selection-form sentence now cites rule 2. Body
lands at 8,850 / 8,850 measured — exactly at budget, zero headroom
(`build.py --footprint`): the next body edit must bring its own offset or a
deliberate row raise.

Suite: **Case 39** covers the override (built to a user-named target, Model
line note, one-line better-fit offer, no silent substitution); Cases 1–38
untouched. Trigger evals not re-anchored — the `description` did not move.

## [1.2.0] — 2026-08-02

Tier routing (Phase 5) gains two **role-based overrides**, applying to both
the standalone Model entry and plan grain since both run the same routing
logic:

- **Planning/orchestrator subtasks default one effort notch lower** than
  their tier would otherwise suggest. High-effort planning reliably
  over-thinks and scope-creeps a plan past what was asked; effort is raised
  only once the plan itself is failing to converge, never pre-emptively.
- **Review/verification subtasks default to a different model family** than
  the work they're checking, where the stakes justify the cost — not a
  resampled instance of the same model, which tends to miss what that model
  already rationalized away.

Closes a gap identified in a skillwright niche-verdict + gap scan run against
a candidate 10th foundation member (an orchestration skill). The scan found
plan grain (1.1.0) already covers the candidate's stated job end-to-end
except for these two rules, so a new pack member wasn't justified — this is
the "smaller fix" half of that verdict, landing directly in Tier routing
rather than a new file.

Evals: **Case 38** added (`evals/test-cases.md`) — a four-role project
exercising both overrides in one table. Cases 1–37 untouched: the override is
additive to existing Tier routing logic, and no prior case's plan depended on
a planning or review role's specific effort/model. Trigger evals not
re-anchored — the `description` field did not move.

## [1.1.1] — 2026-08-01

Prose/register pass over this skill's own files (SKILL.md, README.md,
`references/hostile-interpreter.md`): dash-chained run-on sentences split
into plain sentences, the README's crammed differentiator sentence converted
to a short bulleted list, and the hostile-read catalog's four failure-shape
entries trimmed to keep only the added instances, pointing back to SKILL.md
Phase 6 for the definition instead of re-stating it.

Also fixed: `references/model-snapshot.md`'s tier-map footnotes skipped ²
entirely (¹, then ³, then ⁴, with no ² anywhere in the file) — a table-
formatting defect, not a claim change. Renumbered sequentially (¹ ² ³) since
no source in the pack recorded what a footnote 2 would have claimed; the
facts each footnote carries are unchanged, only their markers moved.

No rule, gate, count, or entry point moved. No eval re-anchor is owed.

## [1.1.0] — 2026-08-01

Entry — Model gains **plan grain**: handed a task list or project plan with a
targets ask, steps 1–3 run per subtask and delivery becomes one target table —
`subtask · tier + model · effort/depth · run inline or as a subagent · one-line
why` — in place of the single-recommendation line. Two contracts ride with
every table: the **living table** (a subtask created mid-session gets a row
through the same steps *before* dispatch, so emergent work adheres to the same
tier logic as the plan it joins) and the **standing rule** (one paste-ready
rule line emitted beneath the table so the contract survives the session;
layer placement stays rigwright's, named not made). Decomposition stays the
caller's — promptwright targets the subtasks it is handed and never re-plans
the project.

- `description` gains the plan clause ("a prompt, a live task, or each subtask
  of a plan"), the mid-session binding, and the target-table mention in the
  `promptwright model` parenthetical.
- **Body budget raised 8500 → 8800** in skillwright's registry: the plan-grain
  delivery shape and both contracts are decision rules, body-resident like the
  rest of Entry — Model — the content reason this raise owes per the
  registry's own budget notes.
- Trigger rows #31–#34 (two should, two shouldn't — the rigwright standing-
  config boundary and the no-targets decomposition boundary) and assertion
  Case 37 (target table + living table + standing rule, two turns) added;
  both suites re-anchored. All 34 trigger rows judged cold against the new
  description this pass; Case 37 is authored, not executed — see
  `evals/RESULTS.md`.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Seven-phase build pipeline — Intake → Analyze & score → Pick structure →
  Clarify → Build → Re-score & self-check → Output — with a five-dimension
  1–10 scoring rubric (clarity, specificity, context, completeness,
  structure) delivered as a before→after delta.
- Framework menu with named-origin doctrine: CO-STAR, RISEN, TIDD-EC, BAB,
  RTF/APE, chain-of-thought, and agent/system shapes; a user-named framework
  always wins and is never silently substituted.
- Fast path: a fixed five-condition gate collapsing Phases 1–6 into one trace
  line for small RTF/APE-shape prompts, with published exit conditions.
- Hostile read: a bad-faith-literal pass over every binding line — four
  failure shapes, each with a named repair — plus collision and
  instruction-boundary cross-checks; the knowledge-vacuum check flags factual
  tasks lacking reference material before scoring.
- Model-tier routing (S/A/B/C: frontier / flagship / balanced / fast) feeding
  a mandatory Model line on every delivered prompt, and the standalone
  `promptwright model` entry for live-task tier picks without a build.
- Output contract: TL;DR, Model line, Score, Structure, an optional
  self-contained HTML prompt card, and the fixed four-option "Keep going"
  close.
- One calendar surface: `model-snapshot.md` (60-day), re-verified by
  `promptwright refresh`, with tier-name fallback when the stamp is stale.
