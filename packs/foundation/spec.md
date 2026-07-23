# foundation — pack-spec baton

> Retro-fitted 2026-07-14 (self-audit finding P2-2): the roster predates the
> pack-spec doctrine, so this baton was reconstructed from the shipped pack and
> the 2026-07-14 self-audit rather than written at the original roster gate.
> From here it updates after every member ship or roster decision. When memory
> of a conversation and this spec disagree, trust the spec.

**Pack:** foundation · **Profile:** standalone · **Brand:** revenant ·
**Stamped:** 2026-07-23 · **Shipped release:** Citadel 1.0 — pack **1.0.0**,
tag `foundation-v1.0.0` (Releases: "Foundation 1.0.0 — Citadel launch") ·
**Current status:** 1.1.0 uniformity + brand-decoupling build **IN PROGRESS**
(Forge Run 3 — see below).

---

## Active build — Forge Run 3 → 1.1.0 (approved 2026-07-23)

Full pack-reopening pass: uniform structure across all 8, brand decoupled into
brandsmith as the single brand home, two new capabilities, native-first
packaging, baselines refreshed. Approved in full ("approve all"). Runs as the
capstone Forge Run (owed since launch). **This section is the resume point** —
a new session or Cowork run continues from the first unchecked phase.

Target: all 8 members → **1.1.0**, pack tag `foundation-v1.1.0`.

**Phase 0 — Repo hygiene** ✅ DONE 2026-07-23
- [x] D-1 · GitHub About homepage `revenantworks.dev` removed (unregistered domain, was live)
- [x] D-5 · `SYNC-NOTES.md` + `AUDIT-FIX-NOTES.md` removed (spent delivery docs; history retains)
- [x] D-3 · this baton's version contradiction reconciled to the shipped 1.0.0 state
- [x] D-4 · RUNBOOK claude.ai/swap section corrected (config-carrying surfaces named)

**Phase 1 — Brand decoupling** ⬜ NEXT
- [ ] Split skillsmith `brand-config.md`: brand half → brandsmith; pack-registry half → skillsmith `pack-registry.md` (build.py derives from here)
- [ ] Move `brand-inheritance.md` (cascade doctrine) skillsmith → brandsmith
- [ ] Fold `voices.md` into brandsmith's definition; commsmith sheds it
- [ ] skillsmith build path → neutral-default + thin brand-token stamp only
- [ ] commsmith → channel-correct + neutral-default; voice sourced from brandsmith on request
- [ ] Point build.py at `pack-registry.md`'s new location
- [ ] Swap masters → 2 surfaces {brand-definition (incl. voices), prompt-card}

**Phase 2 — Uniformity layer** (all 8) ⬜
- [ ] U-1 `metadata.volatile:` frontmatter block ×8
- [ ] U-2 uniform `## Volatile surfaces` block (loresmith/evalsmith declare class:none + why)
- [ ] U-3 standardize Restraint-section position (6 move it before entries)
- [ ] U-4 promptsmith first-class `## Entry — Refresh`
- [ ] U-5 uniform `## Anti-patterns` section ×8
- [ ] U-6 normalize README skeleton ×8
- [ ] 5F native-first Packaging rework (skillsmith): no mandatory shell; validate by inspection, shell one-liner optional; zip = multi-file-in-shell fallback only

**Phase 3 — New capabilities** ⬜
- [ ] 5A skillsmith `## Entry — Upkeep` (pack-wide stamp check via metadata.volatile; report-only default; runs refresh verbs on approval; degrades per surface)
- [ ] 5B promptsmith `## Entry — Model` (recommend tier+model for a live task/conversation; sole home of model data)
- [ ] 5E durable tier hints in tokensmith + promptsmith (snapshot-free; point to promptsmith Entry — Model for specific names)
- [ ] 5C foundation `CLAUDE.md` (always-on router + preferences) — not a skill

**Phase 4 — Baseline refreshes** (restamp 2026-07-23) ⬜
- [ ] skillsmith `rubrics.md` re-verify + restamp
- [ ] promptsmith `model-snapshot.md` — genuine lineup re-research (Fable 5 / Opus 4.8 / Sonnet 5 / Haiku 4.5 / effort) + restamp
- [ ] tokensmith `measurement.md` re-verify + restamp
- [ ] U-9 agentsmith `platform-notes.md` new stamped baseline
- [ ] U-10 commsmith `channel-profiles.md` → stamped baseline

**Phase 5 — Toolchain + validation** ⬜
- [ ] U-7 extend build.py: validate every declared volatile surface exists, is stamped, sane cadence
- [ ] Run build.py — regenerate pack.md ×8, validate, build dist zips

**Phase 6 — Eval + release integrity** ⬜
- [ ] evalsmith event-driven refresh across all 8 (structure changed) — touched cases only
- [ ] Re-run the 12-row trigger-partition test as a set (release bar)
- [ ] All 8 → 1.1.0, dated CHANGELOG ×8, pack tag `foundation-v1.1.0`

**Phase 7 — Capstone + final optimization** ⬜
- [ ] tokensmith optimization pass over all 8 final SKILL.mds
- [ ] Forge Run 3 — run the capstone orchestration as build proof; restamp capstone card with a real live run
- [ ] Assemble delivery (repo-sync bundle + 8 zips + commit/tag lines + swap diffs + upload checklist)
- [ ] promptsmith writes the Cowork upkeep task prompt (61-day cadence)

**After the build:** stand up a Cowork scheduled task (weekly cadence, the tightest
native option) that runs `skillsmith upkeep` and refreshes anything past its
per-surface staleness window. First upkeep due ~2026-09-21 (all stamps reset 07-23).

---

## Approved roster

| Member | Job (one line) | Status | Version @ pack 1.0.0 |
|---|---|---|---|
| `revenant-foundation-skillsmith` | Builds, audits, brands, and ports Agent Skills and packs | SHIPPED | 1.0.0 ¹ |
| `revenant-foundation-promptsmith` | Builds, scores, and hardens prompts with model-tier routing | SHIPPED | 1.0.0 ¹ |
| `revenant-foundation-commsmith` | Shapes messages per channel, audience, and saved voice; audits drift | SHIPPED | 1.0.0 |
| `revenant-foundation-agentsmith` | Designs and audits autonomous agent systems | SHIPPED | 1.0.0 |
| `revenant-foundation-loresmith` | Research-verified verdicts and playbook reference docs | SHIPPED | 1.0.0 |
| `revenant-foundation-brandsmith` | Builds the brand definition; audits everything for drift (7 categories); exports payloads + HTML guide card | SHIPPED | 1.0.0 |
| `revenant-foundation-evalsmith` | Authors and audits eval suites — build-time, zero runtime deps | SHIPPED | 1.0.0 |
| `revenant-foundation-tokensmith` | Measures, budgets, and slims the token footprint of LLM-facing artifacts | SHIPPED | 1.0.0 |

¹ Now 1.0.1 — 2026-07-14 post-launch pack audit, P2 doc fixes; column preserves the pack-1.0.0 snapshot. All eight move to 1.1.0 at the Forge Run 3 release.

## Trigger-partition table

Re-run 2026-07-14 against the real shipped descriptions — **12/12 route to
exactly one destination**; every member appears once; two near-misses exit the
pack correctly. Re-run again as a set at Phase 6 (descriptions untouched by the
1.1.0 build, so expected to hold).

| # | Realistic request | Routes to |
|---|---|---|
| 1 | "Write a system prompt for my research agent" | promptsmith |
| 2 | "Score this SKILL.md against best practices" | skillsmith |
| 3 | "Rewrite this Slack update for the exec channel" | commsmith |
| 4 | "Add guardrails and a kill switch to my nightly scan agent" | agentsmith |
| 5 | "Which task app should I commit to — verdict with sources" | loresmith |
| 6 | "Check the repo for off-palette colors and stale taglines" | brandsmith |
| 7 | "Write trigger evals for the commsmith skill" | evalsmith |
| 8 | "My CLAUDE.md is 6k tokens — slim it, same behavior" | tokensmith |
| 9 | "Build an MCP server for my calendar API" | **outside** → mcp-builder (first-party) |
| 10 | "Review this PR for injection vulnerabilities" | **outside** → engineering plugins / security harness |
| 11 | "Is there a real niche for a meal-prep skill?" | skillsmith (loresmith defers skills to it by name) |
| 12 | "This prompt works — just make it cheaper to run" | tokensmith (promptsmith reciprocates the boundary) |

## Adopt register

Strong incumbents own these jobs — recorded, linked, left out of the roster.

| Job | Incumbent | Recorded |
|---|---|---|
| MCP server generation | `mcp-builder` — anthropics/skills, first-party | 2026-07-14 |
| Baseline skill drafting/review | `skill-creator` — built into claude.ai and Claude Code | 2026-07-14 |
| Code-level engineering (review, tests, debug, incidents) | Anthropic's open-sourced engineering plugins | 2026-07-14 |
| Document production (docx/pdf/pptx/xlsx) | first-party document skills | 2026-07-14 |
| Broad multi-source research reports | Claude Research feature (loresmith partitions this away) | 2026-07-14 |
| Code-level threat coverage | security harness / STRIDE-class skills (agentsmith partitions this away) | 2026-07-14 |
| Model selection (standalone) | multiple community skills (Claude Model Selector, model-selection ×N) — 5B folds the need into promptsmith instead | 2026-07-23 |

## Recorded, not built (nice-to-have)

- **contextsmith** — CLAUDE.md / project-instructions / memory-file
  architecture. Mostly decomposes into tokensmith (footprint) + promptsmith
  (instruction quality); a ninth member would blur two seams to cover one
  sliver. Earns a build only if asked for by name at a future gate.
  (2026-07-23: the foundation `CLAUDE.md` in Phase 3 covers the always-on
  routing sliver without a skill.)
- **runsmith** — runtime review of scheduled-agent runs (logs, behavior
  drift). No incumbent found 2026-07-14; partially covered by agentsmith
  audit; platform-bound (needs run logs → breaks standalone profile). Natural
  home is the future trading-pack quarterly audits. Record.
- **session-helper / model-picker (standalone)** — rejected 2026-07-23 as
  members: model-picking is CROWDED standalone and folds into promptsmith (5B);
  always-on session help is CLAUDE.md territory, not a skill (5C).

## Decisions log

- 2026-07-13 — Pack born at uniform 1.0.0 baseline (seven members); tokensmith
  added same day (roster of eight); conformance C-1/C-2 adopted pack-wide;
  restamp policy lazy (per-release flip allowed).
- 2026-07-14 — Pack self-audit (Phase 1.8 step 1), gated and approved:
  verdict **KEEP 8 / COMBINE 0 / BUILD 0**; partition test 12/12; findings
  P2-1 (promptsmith↔tokensmith boundary — applied, promptsmith 1.0.1) and
  P2-2 (this baton — applied). Combine analysis rejected all four candidate
  merges (evalsmith⇄skillsmith, tokensmith⇄promptsmith,
  brandsmith⇄skillsmith-configure, commsmith⇄loresmith).
- 2026-07-14 — Release bar adopted (closes OD12): release-solid = set
  discoverability pass with no open P0/P1 + repo/release/account parity +
  a current capstone card with one live run.
- 2026-07-23 — **CORRECTION (D-3):** earlier 2026-07-14 lines here declared
  "Foundation 1.0 as pack release 1.2.0, tag v1.2.0" and a capstone "v1.2.1".
  The shipped artifacts — the live Release, `.claude-plugin` manifests, and
  every member's frontmatter — are **1.0.0 / tag `foundation-v1.0.0`**. Those
  1.2.x lines were predecessor-era numbering that never shipped and are
  superseded; the shipped state is authoritative. Semver tags going forward
  (date tags kept as history); member versions independent per pack norm.
- 2026-07-23 — **Forge Run 3 approved in full** ("approve all"): 1.1.0
  uniformity + brand-decoupling build. Brand decoupled into brandsmith as the
  single brand home; skillsmith `upkeep` + promptsmith `model` entries added;
  native-first packaging; uniform volatility/anti-patterns/README structure;
  build.py extended to validate volatility metadata. Plan + status tracked in
  the Active build section above. Cowork 61-day upkeep cadence to follow.

## Session log

- 2026-07-14 — Pack self-audit session: baseline research refresh, partition
  re-run, combine analysis, capability map, F1+F2 applied, release kit assembled.
- 2026-07-23 — Forge Run 3 approved; full 1.1.0 plan written into this baton;
  Phase 0 (repo hygiene) executed (homepage, doc removals, version
  reconciliation, RUNBOOK swap correction). Next: Phase 1 brand decoupling.
