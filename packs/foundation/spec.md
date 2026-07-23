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

**Phase 1 — Brand decoupling** ✅ DONE 2026-07-23
- [x] Split skillsmith `brand-config.md`: brand styling → brandsmith definition; structural roster → skillsmith `pack-registry.md` (build.py derives from here)
- [x] Move cascade doctrine skillsmith `brand-inheritance.md` → brandsmith `application-doctrine.md` (reframed as on-invoke Apply)
- [x] Fold `voices.md` into brandsmith's definition (Voice profile section); commsmith sheds it
- [x] skillsmith build path → neutral-default + structural-identity stamp only; `## Entry — Configure` removed
- [x] commsmith → channel-correct + neutral-voice default; voice sourced from brandsmith export on request; `## Entry — Voice` removed
- [x] brandsmith → single home of brand + voice; new `## Entry — Apply`; Export voice profile now native
- [x] Point build.py at `pack-registry.md`; all 8 `pack.md` regenerated; `build.py --check` clean, count 8=8=8
- [x] 5F native-first Packaging (skillsmith) — landed here early (validate-by-inspection default, optional shell hard-check, zip only as multi-file fallback); Phase 2's 5F box is satisfied
- [x] 3 changed skills bumped to 1.1.0 on main w/ dated CHANGELOG entries (ride to the Phase 6 tag)
- Swap masters now 2 surfaces {brandsmith brand-definition (incl. voice profile), promptsmith prompt-card} — commsmith voices.md retired from the swap set
- **Deferred doc cleanup (named, not silent):** README ×3 (skillsmith/commsmith/brandsmith — removed `configure`/`voice` commands + deleted-file tree lines) → Phase 2 U-6 full README rewrite. SOURCES ×2 volatile-file footnotes (brand-config/voices) → Phase 2. evals ×2 (skillsmith `configure` test, commsmith `voice` test) → Phase 6 evalsmith refresh. None are runtime-loaded or build-validated; pack builds clean.

**Phase 2 — Uniformity layer** (all 8) ✅ DONE 2026-07-23
Staged in batches (SKILL.md work split from READMEs): **2A** skillsmith+promptsmith ✅ · **2B** commsmith+agentsmith+brandsmith ✅ · **2C** loresmith+evalsmith+tokensmith ✅ — **all 8 SKILL.md uniform** · **2D-1** README ×4 (skillsmith, commsmith, brandsmith, agentsmith) + SOURCES reconcile ✅ · **2D-2** README ×4 (promptsmith, loresmith, evalsmith, tokensmith) ⬜ NEXT. (README normalization split 4+4 — eight full rewrites too large for one pass.)
Volatile taxonomy (decided 2026-07-23): **calendar** (stamped, 60d) = skillsmith rubrics.md, promptsmith model-snapshot.md, tokensmith measurement.md · **event-driven** (restamp on trigger) = skillsmith pack-registry.md, brandsmith brand-definition.md, commsmith channel-profiles.md · **none** = loresmith (re-verifies every run), evalsmith (refresh is target-triggered), **agentsmith TEMP** (platform-notes.md is genuine Phase 4 U-9 research; declared none now, Phase 4 upgrades it + adds its refresh path). metadata.volatile format = YAML list of {file, class, cadence_days?} or [] for none; last-verified date lives in each file's own header stamp (not duplicated in frontmatter); build.py U-7 (Phase 5) validates existence + stamp for calendar class only. NOTE for 2D: commsmith SOURCES.md still calls channel-profiles.md "durable, no stamped baseline" — now declared event-driven; reconcile in the README/SOURCES pass.
- [x] U-1 `metadata.volatile:` frontmatter block ×8 — DONE (all 8; calendar ×3, event-driven ×3, none ×2 counting agentsmith-temp)
- [x] U-2 uniform `## Volatile surfaces` block ×8 — DONE (loresmith/evalsmith/agentsmith declare none + why)
- [x] U-3 standardize Restraint-section position — DONE (6 moved: commsmith/agentsmith/brandsmith/loresmith/evalsmith/tokensmith; skillsmith/promptsmith were already canonical; every SKILL.md now Load budget → Volatile surfaces → Restraint → entries)
- [x] U-4 promptsmith first-class `## Entry — Refresh` — DONE (promoted from Behavior-notes Maintenance; cross-refs fixed)
- [x] U-5 uniform `## Anti-patterns` section ×8 — DONE (all 8)
- [x] U-6 normalize README skeleton ×8 — DONE (all 8 on the canonical skeleton: tagline → Workflow → Package contents → Install → Entry points → Commands & switches → Staying current → Changelog). 2D-1 (skillsmith/commsmith/brandsmith/agentsmith) removed Phase 1 stale refs (configure/brand-config/brand-inheritance, voice/voices) + agentsmith's stray owner note + reconciled skillsmith/commsmith SOURCES. 2D-2 (promptsmith/loresmith/evalsmith/tokensmith): promptsmith compressed 116→~75 lines (Performance/Output/Pack/Renaming folded in); evalsmith + tokensmith restructured from terse/hybrid; loresmith light-touch (already canonical). All Staying-current sections now match each skill's metadata.volatile. Each README's evals note = "in full folder-zips, excluded from .skill". (Minor non-issue left: skillsmith uses "**Build workflow:**" vs others' "**Workflow:**" — defensible, not normalized.)
- **Brand centralization pass** ✅ DONE 2026-07-23 (user requested "all brand output centralized through brandsmith" — extends Phase 1 decoupling to the remaining skills). Audited all 8 for brand-output: commsmith/agentsmith/loresmith/evalsmith carry only the `brand: revenant` frontmatter *label* (structural, kept). Three real touchpoints fixed: (1) **tokensmith** — removed the per-run `brand:` report-flavor switch (SKILL + README); reports/sheets/rewrites always neutral. (2) **promptsmith** — the HTML prompt card shipped a hardcoded `revenant-foundation-promptsmith` wordmark lockup + `<title>`; now fully neutral ("Prompt Card" label). (3) **skillsmith** — removed a stale "brand cascade" reference in `build-templates.md` (Phase 1 leftover). **brandsmith** `application-doctrine.md` now names sibling artifacts (prompt cards, tokensmith reports, any skill's HTML) as canonical Apply targets. Result: brandsmith is the single door for ALL brand application; every other skill outputs neutral. skillsmith/promptsmith/tokensmith/brandsmith 1.1.0 changelogs updated (no version change; 1.1.0 unreleased). Verified: zero non-label brand-output remains pack-wide.
- [x] 5F native-first Packaging rework (skillsmith) — DONE in Phase 1 (landed with the skillsmith rewrite)

**Phase 3 — New capabilities** ✅ DONE 2026-07-23
Batches: **3A** skillsmith Entry — Upkeep (5A) ✅ · **3B** promptsmith Entry — Model (5B) + tier hints (5E) ✅ · **3C** foundation CLAUDE.md (5C) ⬜ NEXT.
- [x] 5A skillsmith `## Entry — Upkeep` — DONE. Pack-wide staleness sweep: reads every member's metadata.volatile, reports calendar-surface status vs cadence (report-only default), runs the mapped refresh verb per overdue surface on approval (rubrics→skillsmith refresh · model-snapshot→promptsmith refresh · measurement→tokensmith refresh), degrades by environment (read-stamps portable; run-refresh needs search+file tools; never auto-commit). New reference `upkeep-doctrine.md`; `upkeep` in description + bare-invocation + README. skillsmith desc now 1022/1024 chars.
- [x] 5B promptsmith `## Entry — Model` — DONE. Standalone tier + model recommendation for a live task (no prompt built); reuses the Phase 5 tier taxonomy (durable S/A/B/C) with names from `model-snapshot.md` (tier-name fallback past the stamp); delivers tier + model + effort + flip condition. Boundary: the Model line stays Phase 5's (attached to a build); a sourced multi-model comparison is loresmith. `promptsmith model` added to bare-invocation + README (description already covered the trigger, left at 1004/1024).
- [x] 5E durable tier hints — DONE. promptsmith: the tier taxonomy is the durable, snapshot-free layer both Entry — Model and the Model line draw on. tokensmith: model-tier questions now route to promptsmith `Entry — Model` specifically, plus a durable tier→cost note (tokensmith reasons in tiers, never names a model).
- [x] 5C foundation `CLAUDE.md` — DONE. Always-on router + conventions at `packs/foundation/CLAUDE.md` (pack-scoped, not repo-root — foundation is one pack in a multi-pack marketplace). Not a skill — standing context. Sections: reaching for the right smith (task→smith table), how they compose (neutral→brandsmith apply; skillsmith→evalsmith; promptsmith model owns model data; skillsmith upkeep sweeps freshness; loresmith decides), conventions (neutral default, one-gate, audits report-only, declared deps, stamped+swept volatile surfaces). Repo README updated: CLAUDE.md discoverability line + 3 stale smith rows fixed (skillsmith no "brands", commsmith no "saved voice", brandsmith now brand+voice). **Phase 3 COMPLETE.**

**Phase 4 — Baseline refreshes** (restamp 2026-07-23) ✅ DONE 2026-07-23
Batches: **4A** promptsmith model-snapshot ✅ · **4B** skillsmith rubrics + tokensmith measurement ✅ · **4C** agentsmith platform-notes (U-9) + commsmith channel-profiles stamp (U-10) ✅.
- [x] skillsmith `rubrics.md` — DONE (restamped 2026-07-23). Format stable: agentskills.io canonical, anthropics/skills carries an explicit spec pointer file, ≤500-line + progressive-disclosure guidance unchanged, standard adopted by Codex/Copilot. ClawHub added as a cited-not-verified niche-source candidate next to Skillstore (~490K-skill ecosystem per 07-23 cross-checks); per-source live-check dates kept honest (07-12/07-13).
- [x] promptsmith `model-snapshot.md` — DONE (restamped 2026-07-23, genuine re-research vs vendor docs + registries). Real drift caught since the 07-06 stamp: OpenAI → **GPT-5.6 family** (Sol/Terra/Luna, GA 07-09, 1M ctx ×3; 5.5 Pro stays S); Gemini → **3.6 Flash** (07-21 workhorse, −17% output tokens) + **3.5 Flash-Lite** (C), with **3.5 Pro flagged partner-only/never-recommend** (Gemini S slot empty; 3.1 Pro = top GA); Grok → **4.5** (07-08, A-tier, 500K-ctx caveat vs 4.3's 1M / 4.1 Fast's 2M; >200K surcharge on 4.5/4.3); DeepSeek → V4-Flash at C, **V4 Pro promo expired 05-31** (standard rate now). Claude column CONFIRMED correct as stamped (Sonnet 5 GA 06-30; Sonnet 4.6 legacy; intro pricing to 08-31; effort xhigh Sonnet 5+, max Fable 5). Also fixed the file's stale refresh pointer (Behavior notes → Maintenance ⇒ Entry — Refresh). Rides in unreleased 1.1.0 (no patch bump).
- [x] tokensmith `measurement.md` — DONE (restamped 2026-07-23). REAL STALE FIX: OpenAI cached reads were listed ~50% of input — current families (5.4+) bill ~0.10× (the 50% is gpt-4o-era legacy); GPT-5.6 cache writes 1.25× w/ 30-min minimum added. Anthropic sharpened: ≤4 breakpoints, 1.25×/2× write (5-min/1-hr), 0.10× reads, TTL refresh-on-read, reads excluded from input rate limits. Skill-metadata discovery cost → measured median ~80 tok/skill (~55–235). Ratios durable, unchanged.
- [x] U-9 agentsmith `platform-notes.md` — DONE (new stamped baseline, verified 2026-07-23, real research). Contents: enforcement surfaces per platform (Claude Code 3-gate permissions/sandbox/hooks incl. hook-CVE attack-surface notes + exit-0 footgun; Cowork native cadences hourly/daily/weekly/weekdays; OpenAI Agents SDK guardrails/resumable approvals, Agent Builder EOL 2026-11-30; MCP allowlists + server CVEs), scheduling surfaces, layered kill-switch doctrine (CISA/NSA 2026-04 guidance, EU/SG regs, governance-gap stats), injection state (unsolved — blast-radius limitation; agent commits leak credentials ~2× baseline), checklist-area→mechanism map. agentsmith volatile [] → calendar 60d; Volatile surfaces + Load budget rewritten; new `## Entry — Refresh`; description 1019/1024; README updated. skillsmith upkeep-doctrine verb map + example gained the 4th calendar row.
- [x] U-10 commsmith `channel-profiles.md` — DONE: event-driven header stamp added (Last restamped 2026-07-23) so the declaration, file, and upkeep read one dated surface; SKILL volatile section points at it. **Phase 4 COMPLETE.**

**Phase 5 — Toolchain + validation** ✅ DONE 2026-07-23
- [x] U-7 build.py `validate_volatile()` — DONE. Stdlib parse (no yaml dep); rules: block required on all 8 (`[]` for none) · class ∈ {calendar, event-driven} · declared file exists · calendar needs sane cadence_days 7–365 + dated header stamp (`Last verified/restamped/stamped: YYYY-MM-DD`, not future) · event-driven must not carry cadence_days. Wired into validate_skill, runs in --check and full modes; docstring updated; root CHANGELOG gained an Unreleased note. **Two real bugs the 8-case negative-test matrix caught before shipping:** (1) the `[]` regex had optional brackets, so the bare `volatile:` line of every LIST also matched and the validator early-returned — passed clean trees, validated nothing; fixed to require literal `[]`. (2) stamp search window was 6 lines — rubrics.md legitimately stamps its volatile *section* (~line 18, only that section is volatile), previously masked by bug 1; widened to 40 lines with a comment. All 7 failure modes proven firing on exactly the mutated member; clean trees pass.
- [x] Run build.py full — DONE (sandbox): 8/8 dist zips at 1.1.0, 0 manifests synced (no registry drift), all validation incl. U-7 green. dist/ is gitignored (release artifacts; CI attaches on tag).

**Phase 6 — Eval + release integrity** ✅ DONE 2026-07-23
Batches: **6A** eval refresh ×8 ✅ · **6B** partition re-test + release metadata + tag ✅.
- [x] evalsmith event-driven refresh ×8 — DONE (2026-07-23, diff-scoped, touched cases only). **skillsmith**: trigger #7 → upkeep, #8 flipped to brandsmith boundary (34 rows, 17/17); cases 11–12 → Upkeep (sweep report-only + refresh-on-approval/degradation), 15–16 → neutral build + brandsmith routing; brand-config→pack-registry rename in 17, brand:-switch removed from 18; header/contents/provenance updated. **commsmith**: #7 flipped (definition→brandsmith) + #23 added as the application-side pair (23 q, 11/12); firewall cases re-anchored to handed-in profiles; Case 19 → definition-routes/application-stays two-turn. **brandsmith**: #12 FLIPPED to SHOULD (Entry — Apply is its own; 22 q, 13/9); Case 9 → structural-payload export; Case 10 names apply; Case 12 → T2 runs Apply per application-doctrine. **promptsmith**: #25 added (Entry — Model, live task no prompt; 25 q, 12/13); prompt-in-play edge note corrected; Case 29 added (standalone rec contract + loresmith boundary). **agentsmith**: #23 added (refresh; 23 q, 12/11); Case 16 added (refresh scope). **tokensmith**: Case 15 → always-neutral + brandsmith routing, retired brand: switch purged. **loresmith + evalsmith**: swept clean, zero stale, entries unchanged — no edits. Count integrity verified per file (declared = actual everywhere); pack-wide stale sweep zero. Changelog notes ×6.
- [x] 12-row trigger-partition re-test — DONE 2026-07-23, 12/12 single-destination against live descriptions; sharp pairs verified on-disk; the four new 1.1.0 claims partition cleanly (results recorded in the Trigger-partition table section below).
- [x] Release metadata — DONE: all 8 CHANGELOGs already head `## [1.1.0] - 2026-07-23` (created release-dated); marketplace.json foundation plugin 1.0.0 → 1.1.0; root CHANGELOG's Unreleased converted to the dated `[foundation-v1.1.0] - 2026-07-23` entry. Tag `foundation-v1.1.0` is the user's push step (CI attaches the 8 member zips on tag). **Phase 6 COMPLETE.**

**Phase 7 — Audit + capstone + final optimization** 🔶 IN PROGRESS
Batches: **7A** final Fable audit (user-added) ✅ · **7B** tokensmith pass + capstone + card restamp ⬜ NEXT · **7C** delivery assembly + Cowork upkeep task ⬜.
- [x] 7A FINAL AUDIT — DONE 2026-07-23 against the tagged release (main == foundation-v1.1.0 == bddde22). **Part A, intended changes: all verified landed** — decoupling files (3 gone, 4 new), uniformity ×8 (volatile block, Volatile-surfaces, Anti-patterns, Restraint position), 4 calendar stamps + commsmith event stamp at 2026-07-23, U-7 defined+wired, release metadata, --check clean, desc/body limits ×8 green. **Part B, logic gaps — 4 real finds, all FIXED (F1–F4):** F1 brandsmith `audit-doctrine.md` export shape still titled "skillsmith configure payload" → "Structural payload (skillsmith consumes it)". F2 RUNBOOK still carried the 3-row swap table (commsmith voices.md) + a now-past "coming in 1.1.0" note → 2-row table {brand-definition (identity+voice), prompt-card}, note resolved; build.py's documented validation list gained the U-7 clause. F3 marketplace description "brandsmith (brand & drift)" → "(brand & voice)". F4 **genuine divergence:** skillsmith SKILL.md's Entry — Upkeep inline verb map had only 3 surfaces while upkeep-doctrine had 4 — platform-notes row added; entry and doctrine agree again. False positives confirmed by-design: commsmith eval negative-inputs; cross-member mentions (evalsmith fallback line, skillsmith verb map, Behavior-notes brand-definition). **Versioning:** skillsmith + brandsmith → 1.1.1 with dated entries per the 1.0.1 post-launch-audit precedent; fixes ride main (installed copies behaviorally unaffected; next tag picks them up, or re-tag if wanted). **Part C, recommendations register:** (1) watch the promptsmith-Model vs loresmith-comparison boundary in real usage (eval pair #25/#16 covers the seam). (2) Owner to-do outside this run: `agentsmith audit` the two live trading specs (Research Agent, Entry Scan) against the new platform-notes baseline — the standing-targets note left the public README in 2D-1 but the job remains. (3) Optional hardening: extend U-7 to require stamps on event-driven files too (all three carry them; low value — calendar-only per spec). (4) Confirm CI attached 8 zips to the foundation-v1.1.0 release (user-side check). (5) First upkeep due ~2026-09-21 — the 7C Cowork task encodes it.
- [ ] tokensmith optimization pass over all 8 final SKILL.mds — 7B
- [ ] Forge Run 3 — run the capstone orchestration as build proof; restamp capstone card with a real live run — 7B
- [ ] Assemble delivery (repo-sync bundle + 8 zips + commit/tag lines + swap diffs + upload checklist) — 7C
- [ ] promptsmith writes the Cowork upkeep task prompt (61-day cadence) — 7C

**After the build:** stand up a Cowork scheduled task (weekly cadence, the tightest
native option) that runs `skillsmith upkeep` and refreshes anything past its
per-surface staleness window. First upkeep due ~2026-09-21 (all stamps reset 07-23).

---

## Approved roster

| Member | Job (one line) | Status | Version @ pack 1.0.0 |
|---|---|---|---|
| `revenant-foundation-skillsmith` | Builds, audits, and ports Agent Skills and packs (neutral by default) | SHIPPED | 1.0.0 ¹ |
| `revenant-foundation-promptsmith` | Builds, scores, and hardens prompts with model-tier routing | SHIPPED | 1.0.0 ¹ |
| `revenant-foundation-commsmith` | Shapes messages per channel and audience; neutral-voice default; audits drift | SHIPPED | 1.0.0 |
| `revenant-foundation-agentsmith` | Designs and audits autonomous agent systems | SHIPPED | 1.0.0 |
| `revenant-foundation-loresmith` | Research-verified verdicts and playbook reference docs | SHIPPED | 1.0.0 |
| `revenant-foundation-brandsmith` | Single home of brand + voice; defines, applies on invoke, audits for drift, exports payloads + HTML guide card | SHIPPED | 1.0.0 |
| `revenant-foundation-evalsmith` | Authors and audits eval suites — build-time, zero runtime deps | SHIPPED | 1.0.0 |
| `revenant-foundation-tokensmith` | Measures, budgets, and slims the token footprint of LLM-facing artifacts | SHIPPED | 1.0.0 |

¹ Now 1.0.1 — 2026-07-14 post-launch pack audit, P2 doc fixes; column preserves the pack-1.0.0 snapshot. All eight move to 1.1.0 at the Forge Run 3 release.

## Trigger-partition table

**Re-run 2026-07-23 against the live descriptions at the 1.1.0 release bar — 12/12 route to exactly one destination.** The three Phase-1 description changes sharpened the boundaries as predicted; the four new 1.1.0 claims (skillsmith upkeep, promptsmith Entry — Model, brandsmith Entry — Apply, agentsmith refresh) partition cleanly — verified per sharp pair against on-disk text: row 7 (evalsmith claims suite-authoring for existing targets; skillsmith only ships suites with builds), row 11 (skillsmith's explicit niche clause vs loresmith's no-skill verdict framing), row 12 (reciprocal promptsmith↔tokensmith boundary sentences intact), row 10 (agentsmith's security-harness partition line intact), and the Model claim (promptsmith owns run-target picks incl. live tasks; loresmith owns sourced product comparisons — the one boundary worth watching in real usage; eval pair #25 vs #16 covers it). Per-skill trigger evals (6A) cover the new entries individually; this set test confirms no new overlap. *(Original 2026-07-14 run: same 12/12 result against the 1.0.0 descriptions.)*

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
  reconciliation, RUNBOOK swap correction).
- 2026-07-23 — **Phase 1 (brand decoupling) executed** in sandbox, verified
  `build.py --check` clean (count 8=8=8). brandsmith = single home of brand+voice;
  skillsmith + commsmith build neutral by default; registry split to
  `pack-registry.md`; 3 skills → 1.1.0. Delivered as repo-sync bundle + git
  commands (3 `git rm` deletions). Doc cleanup for READMEs/SOURCES/evals deferred
  to Phase 2/6 (listed under Phase 1). Next: Phase 2 uniformity layer.
