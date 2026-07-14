# Waste Taxonomy, Technique Ladder & Report Formats *(durable doctrine)*

Read on every slim, audit, and budget run. W-codes name the waste; the ladder orders the fixes; the contract names what never gets cut; the formats keep reports uniform.

## Contents

- W-codes — the waste taxonomy
- Technique ladder — safety-ordered
- Preservation contract
- The legibility floor
- Report formats (slim report · audit catalog · budget sheet)

---

## W-codes — the waste taxonomy

| Code | Waste | Detection cue | Fix (ladder rung) |
|---|---|---|---|
| W1 | Duplication | The same rule or fact stated twice, anywhere in the set | Dedupe — one owner per rule (2) |
| W2 | Filler & hedging | Throat-clearing, pleasantries, "it's worth noting", restated intent | Tighten (3) |
| W3 | Over-specification | Instructions restating what the model does by default | De-specify, with disclosure (4) |
| W4 | Format overhead | Tables, bold, and headers where structure isn't doing work | Deformat (5) |
| W5 | Example overrun | Examples past the contrastive minimum, or redundant variants | Prune (6) |
| W6 | Inline-what-should-load-on-demand | Heavy material in an always-on or trigger surface that a reference could carry | Offload (7) |
| W7 | Dead weight | Stale, superseded, or unreachable content; commented-out corpses | Cut (1) |
| W8 | Cross-file boilerplate | The same preamble or block repeated across a set | Dedupe to one owner + pointer (2) |
| W9 | Cache-busting placement | Volatile content interleaved into a stable prefix; unstable ordering | Reorder stable-first; isolate volatiles in stamped files (8) |
| W10 | Resident-when-conditional | Always-on cost that only some sessions use (schemas, modes, personas) | Move behind a trigger-loaded surface (7) |

Audit findings cite W-codes; severity (P0/P1/P2) is assigned per the Audit entry in SKILL.md — the code says *what kind* of waste, the P-level says *how much it matters here*.

## Technique ladder — safety-ordered

Rungs apply in order on every slim; each rung logs what it removed. Rungs 1–8 are lossless — the artifact's stated behavior is unchanged. Rung 9 is lossy and always gates.

1. **Cut dead weight** (W7) — stale facts, superseded sections, unreachable branches.
2. **Dedupe** (W1, W8) — one owner per rule; second statements become nothing, not pointers, unless files genuinely load separately.
3. **Tighten** (W2) — meaning-preserving compression: filler out, hedges out, one verb where three stood. The constraint's shortest faithful wording.
4. **De-specify** (W3) — remove instructions that restate model defaults. Lossless in behavior, visible in text — every removed default goes on a disclosure line so the owner can veto.
5. **Deformat** (W4) — tables to terse lines where alignment isn't information; emphasis diet; "some things include x, y, z" over three bullets. Structure stays wherever it *is* the information.
6. **Prune examples** (W5) — down to the contrastive minimum, usually one good + one boundary case. Gates like a lossy cut when it would drop below two, or when any pruned example anchors an eval.
7. **Offload** (W6, W10) — progressive disclosure: heavy or conditional material to references loaded on demand, one level deep; the body keeps a one-line pointer. Same content, cheaper residence.
8. **Reorder for cache** (W9) — stable → volatile; volatile facts into stamped single-update-surface files; breakpoint-friendly boundaries. Same content, cheaper reads.
9. **Semantic compression** *(lossy — always gates)* — summarizing, dropping behaviors, collapsing constraints. Each candidate is named with the behavior it drops and the tokens it buys; "just slim it" never pre-approves this rung.

## Preservation contract

Collected before any cut; every item survives the slim or appears as a gated lossy finding — never a silent casualty:

- Safety rules and refusal boundaries
- Output contracts and schemas the artifact promises
- Routing and trigger text (names, descriptions, invocation keywords)
- License, legal, copyright, and ownership lines
- Stamped volatile facts and their stamps
- Eval-anchored behaviors — anything the artifact's suite asserts
- Dependency declarations and absence behaviors

The slim report lists the contract explicitly, so "preserved" is checkable, not claimed.

## The legibility floor

An instruction artifact must survive a cold read: a reader with no context follows it or the compression failed. Symbol registers, telegraphic grammar, and stripped-connective "caveman" styles are runtime *output* tactics — applied to instruction artifacts they trade reliability for tokens, and re-prompting eats the difference. The floor: past rung 5, re-read the artifact cold; if any step now requires guessing, back up one rung.

## Report formats

**Slim report** — six lines before the artifact:
`Before → After` (both with method) · `Δ tokens / Δ%` · `Rungs applied` (numbered, with per-rung recovery where notable) · `Preserved` (the contract, listed) · `Disclosures` (defaults removed, examples pruned — or "none") · `Cache impact` (role, re-write cost vs read savings — or "n/a"). Then the rewritten artifact, whole, never a diff the user must apply.

**Audit catalog** — inventory (2–3 lines), then one row per finding:
`ID · W-code · where · finding · est. recoverable · P0/P1/P2`, closing with the efficiency score and the one-line verdict (LEAN / TRIMMABLE ~n% / BLOATED ~n%). No rewritten text anywhere in an audit.

**Budget sheet** — the tier table (always-loaded / trigger-loaded / on-demand; per artifact: current, ceiling, headroom), the set-level always-on total against the tokens-per-task target, load order, and the cache plan. Ceilings cite `measurement.md`'s reference points and the set's real turn count.
