# Changelog — revenantworks-foundation-tokenwright

> Renamed from `revenant-foundation-tokenwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.1.0] — 2026-08-05

Routing change (AUDIT-2026-08-05, seam resolution): the `description` gains
the rigwright boundary clause — "a config's layer placement or setup audit is
rigwright's — tokenwright only cuts its cost" (802 → 894 chars, measured per
`build.py`'s regex). Closes the previously undeclared rigwright ↔ tokenwright
seam over CLAUDE.md and other standing-config artifacts; the registry gains
the seam row (signal: one description — this one) and its naming note now
counts three CLAUDE.md descriptions. Minor bump: the description is the
routing surface. Trigger evals extended and re-anchored (Y11/N11, the new
seam's boundary pair); assertion suite re-anchored, no case moved — no body
rule changed. The cold re-judge of the trigger rows against the amended
listing is owed, not claimed.

## [1.0.2] — 2026-08-01

Completeness correction: SKILL.md's Preservation scan list named six of the
seven items the preservation contract already covers; `waste-taxonomy.md`
and this changelog both listed seven. "Dependency declarations and absence
behaviors" — already true and already stated in `waste-taxonomy.md` — is now
named in SKILL.md too, so all three sources agree. This is a correction, not
new behavior: nothing the contract protects has changed. Also a prose pass:
SKILL.md's cache-floor sentence, which restated `measurement.md`'s Cache
mechanics rule near-verbatim, now cross-references it instead, and a handful
of dash-joined clauses across SKILL.md, `measurement.md`, and
`waste-taxonomy.md` were re-punctuated for clarity. No rule, gate, or entry
point moved, so no eval re-anchor is owed.

## [1.0.1] — 2026-08-01

Frozen-record marker added to the `evals/` files that cite predecessor-era
version numbers. Those designations predate the 2026-07-31 re-baseline, and
two of the tag names were later reused by unrelated releases, so a reader
could take a historical entry for a current one. The rows, verdicts, dates
and counts are untouched — only a header marker was added, so nothing about
what was executed or when has moved.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Measurement discipline: every figure disclosed as exact (with the tool
  named) or estimate (with its ± band); no savings claim without a
  before/after pair.
- The ten-code waste taxonomy W1–W10: duplication, filler, over-
  specification, format overhead, example overrun, inline-what-should-load-
  on-demand, dead weight, cross-file boilerplate, cache-busting placement,
  resident-when-conditional.
- The nine-rung lossless→lossy ladder — cut dead weight → dedupe → tighten →
  de-specify → deformat → prune examples → offload to progressive disclosure
  → reorder for cache → semantic compression — with the lossy rung always
  gated.
- Preservation contract collected before any cut: safety rules, output
  contracts, routing and trigger text, license lines, stamped volatile
  facts, eval-anchored behaviors, declared dependencies.
- Net-cost accounting: always-on artifacts billed as size × turns in scope,
  formula-driven proceed/stop; cache mechanics with stable-first reordering
  and the minimum-cacheable-length floor check.
- Description-cap P0 rule keeping the platform cap, the listing budget, and
  the house ceiling single-homed and never conflated.
- Budget entry over a set: tier table (always-loaded / trigger-loaded /
  on-demand), ceilings, load order and cache plan, and a set-level
  tokens-per-task number. One calendar surface: `measurement.md` (60-day),
  re-synced by `tokenwright refresh`.
