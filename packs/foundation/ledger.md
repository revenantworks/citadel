# foundation — build & execution ledger

> Chronological record of the pack's build passes and eval-suite executions.
> Split out of `spec.md` 2026-07-25 (deferral-register item ⑥). The live baton is
> `spec.md`; durable decisions live in `decisions.md`. When memory of a conversation
> and this ledger disagree, trust the ledger.


---

## Cold trigger re-run — 2026-07-31, the wright re-baseline listing (97/97)

The rename invalidated every executed routing baseline, so the owed re-run was
paid the same day: three suites judged cold by independent blind judges holding
only the nine-member wright listing (names + descriptions at 1.0.0) and the
numbered queries — no bodies, no Expected column, no repo.

- **skillwright 43/43** — first perfect run in the suite's history (prior
  baseline 40/43 with #8/#26/#35 AMBIGUOUS; all three resolved on the shipped
  descriptions). The security partition held again (#38–#43).
- **agentwright 34/34** — rows #30–#34 (the 1.3.0 emit set) executed for the
  first time; both rigwright near-misses routed to rigwright; row 19 passes
  under its 1.2.2 SHOULD conversion. Prior baseline 28/29 on eight members.
- **rigwright 20/20** — the suite's first cold execution; all three birth
  seams held blind, as did the tokenwright cost-cue and brandwright apply
  splits.

Details in each member's `evals/RESULTS.md`. Judged against the descriptions
shipped at `foundation-v1.0.0` (the wright re-baseline release).

---

## Build pass — 1.3.0, the security release (opened and closed 2026-07-27)

Deferral item ⑧, then a release-gate audit that turned the new doctrine on the pack
itself. **CLOSED and tagged `foundation-v1.3.0`.**

**Item ⑧ — security-scan doctrine** ✅ DONE 2026-07-27 · commit `6a0c164` ·
**agentwright 1.2.0 · skillwright 1.4.0**
- [x] agentwright `Entry — Security-scan` + `references/security-scan-doctrine.md` — five
  runtime classes. Scans *against* SKILL.md's Trust-tiers section rather than restating it;
  reuses Entry — Audit's severity scale rather than inventing a second. Names no platform
  product and makes no threat-landscape claim, so no stamp and no `metadata.volatile` entry,
  and the file states why.
- [x] skillwright `Entry — Audit` security pass — S-1 to S-4 single-homed in `rubrics.md`,
  rows inside step 5's one catalog, tagged by class. Body budget 7500 → 7800.
- [x] Partitioned by **object**, not vocabulary — `injection` sits in both descriptions.
  Neither member loads a file in the other's directory (grep-verified); standalone holds.
- [x] Multi-host export half **dropped, not deferred** (`decisions.md` 2026-07-27).
- **Recorded at build time and honoured at release:** every new row and case authored,
  not executed; both descriptions moved; the `skillwright ↔ agentwright` seam row skipped
  because it regenerates all eight manifests.

**Release-gate pack audit** ✅ DONE 2026-07-27 — **the finding worth the pass.**
Running skillwright's brand-new security classes over all eight members caught two S-1
defects in members that had passed every prior review round. *The pack shipped a security
doctrine and immediately failed it in two places.* That is the correct outcome for a first
run, and it is the argument for the doctrine rather than against it — three rounds of
document review and 178 executed asserts had not surfaced either.
- [x] **lorewright → 1.1.6, S-1 P0.** Reads live third-party pages on every verdict and
  playbook, and consolidation reads handed-in docs; carried **no data-never-instructions
  statement anywhere** in the shipped package. Mechanically confirmed before the fix: zero
  hits for `untrusted` / `injection` / `never instructions` across `SKILL.md`,
  `verdict-mode.md`, `playbook-mode.md` — the folder's only hits were the generated
  `pack.md` and a historical line in `RESULTS.md`, neither of which is doctrine. Fixed with
  one paragraph single-homed in Verification doctrine, carrying an explicit
  no-restatement clause so it does not become the pack's next two-homes defect. Case 23 added.
- [x] **promptwright → 1.2.5, S-1 P1.** The member with the *most* untrusted-input doctrine
  in the pack — `prompt-hardening.md`, the Phase 6 hostile read, the Phase 7 `Hardened`
  check — had all of it aimed at the prompt it **builds** and none at the instruction-shaped
  text it **reads**. P1 not P0 on S-1's own anchor: the rule is stated, a specific step
  escapes it. Fixed at Phase 1 Intake, with the red-team branch named explicitly so the two
  rules cannot be confused. Case 36 added.
- [x] **`skillwright ↔ agentwright` seam row added**, all eight manifests regenerated. The
  seam notes record the mechanism gap rather than just the fix: `build.py`'s boundary-pair
  check validates the rows that are **declared** and has no way to notice one that is
  **missing**, so the clean `--check` at 1.2.0/`6a0c164` was never evidence the seam was
  covered. A boundary claimed in two descriptions and in no table is invisible to the tool
  built to police boundaries.
- [x] **Always-on router amended** — two security rows (agentwright runtime, skillwright
  package) plus a How-they-compose bullet stating the object split. **Same defect class as
  the router row caught at skillwright 1.3.1/1.3.2, recurring exactly one pass later:** a
  capability lands, and the pack-level surface no member owns is not swept. Worth a standing
  rule rather than a third catch — *a new entry point is not shipped until
  `packs/foundation/CLAUDE.md` names it.*
- [x] **agentwright → 1.2.1**, one accuracy fix against text shipped hours earlier: the Load
  budget declared one reference file as the standard security-scan load when three of the
  five classes cite a checklist area by number as a matter of course. Two standard, three
  the ceiling. An under-declared load in the section whose whole job is declaring load.
- [x] **Root `CHANGELOG.md` was three days stale** — the `[Unreleased]` block stopped at
  2026-07-25 and four member bumps of 07-26/27 had no line. Folded into the 1.3.0 entry and
  recorded as its own defect, since a root changelog that skips three days is the same class
  as a ledger that outruns its runs.
- [x] `build.py --check` **clean, zero warnings**; count integrity 8 = 8 = 8, nine seams.

**Debt open at the tag — the next pass opens here, not on new capability.** Every eval row
and case added across 1.3.0 is **authored, not executed**. agentwright (29 queries / 20 cases)
and skillwright (43 / 40) both moved descriptions and owe cold trigger re-runs; lorewright
Case 23, promptwright Case 36 and agentwright Cases 17–20 have never run. Last executed results
stand as last-executed and are **not restated as current** (agentwright 2026-07-24 · skillwright
37/37 2026-07-25 · promptwright v1.2.3 2026-07-25 · lorewright v1.1.5 2026-07-25). **No
pack-wide aggregate is quoted**, for the reason the 1.2.0 section below records. The register
is now empty but for ⑦, which is gated on pack #2 existing — so there is no capability item
competing with the executions, and adding one before they run would repeat precisely what
this release disclosed.

**Watch on the re-run:** skillwright #26 first (its description dropped
`Every build ships trigger evals.`, which that row rode) and #42 against #38 second (same
noun, opposite object, across the new `injection` collision). lorewright Case 23 and
promptwright Case 36 are both passable on assistant convention alone — a run that cannot
separate convention from loaded doctrine should say so rather than bank the pass, per the
agentwright row-19 and skillwright Case-37 precedents.

---

## Cold trigger re-run — 2026-07-27, post-tag — **DISCHARGED**

**Method first, because it is the result's warrant.** Three independent judges, each given
only the eight-member listing and a query slice — no SKILL.md body, no reference file, no
expected-answer column, no repo access, and no sight of each other's slice. **Every prior
"cold" run in this ledger was judged by a runner with the repo open.** This is the first that
was not, and the difference showed up immediately in what it caught.

**agentwright 28/29 · 1 FAIL · skillwright 40/43 clean · 0 FAIL · 3 AMBIGUOUS.** 43/43 was
never available and is not claimed anywhere.

- **skillwright #26 broke exactly as predicted, and the judge named the cause verbatim.** The
  1.4.0 trade note flagged #26 as *"the one to judge first"* because the description dropped
  `Every build ships trigger evals.` to pay for the security clause. A judge who had never seen
  that note wrote: *"the catalog listing of skillwright omits the sentence 'Every build ships
  trigger evals' that would have made this unambiguously a skillwright build."* **This is the
  first time in this pack's history that a predicted description cost has been independently
  measured rather than reasoned about**, and it is the argument for cold judges by itself — a
  contaminated runner would have supplied the missing clause from memory and passed the row.
- **agentwright row 19 is a defective ROW, not a description gap.** The judge fired agentwright on
  the harassment query and reasoned *"routing is by object; the harassment content is a
  downstream refusal question, not a routing one"* — reproducing the 2026-07-25 re-scope's
  prediction *and its reasoning*, blind. Restraint is a body behaviour, already proven to fire on
  two wordings. The row can only pass if the description spends characters advertising what
  agentwright won't build. Recommendation logged: convert to SHOULD, assert restraint in
  `test-cases.md`, the shape row 29 already uses.
- **#35 reopens a seam recorded closed.** The skillwright ↔ commwright close of 2026-07-25 was
  asymmetric by design and its own seam note called the judgement *authored, not instrumented*.
  Now instrumented: skillwright's file claim works, and **commwright's `humanize` verb was never
  scoped to a message**, so the verb half is unclosed. The fix belongs to commwright. #36, the
  CLAUDE.md twin, passed cleanly, which localises the defect to the shared verb.
- **#8 exposes a circular pair, unprompted.** brandwright disclaims toward skillwright; skillwright's
  reciprocal clause points back at brandwright. *"A router reading skillwright first gets pushed to
  brandwright; reading brandwright first gets pushed to skillwright."* The judge called it **the
  single worst structural defect in the catalog** — against a seam the 1.2.0 pass recorded as
  closed *non-circularly on both sides*. **The lesson generalises: two reciprocal boundary
  sentences can each be correct and jointly circular, and no single-member audit can see it.**
  A set-level check is the missing instrument.
- **The 1.4.0 security split HELD — the unambiguous good news.** All six new skillwright rows and
  all three agentwright security rows resolved cleanly and confidently. #41 and #42 fired
  agentwright with the judge citing skillwright's own boundary sentence as the reason it lost; #43
  returned NONE on the code-level harness line; #27 and #28 held from agentwright's side.
  **#42 against #38 — named the sharpest pair in the pack, same noun and opposite object —
  separated on the first cold judgement ever run against it.** The `injection` collision the new
  seam row was written for does not misroute.

**Over-claim observations, volunteered outside the scored rows and worth a future pass:**
agentwright's bare `cadence` pulls non-agent scheduling traffic (`run cadence` would fence it) ·
`audit` carries near-zero routing signal pack-wide, five members claiming the subcommand, so each
rests entirely on its object noun · skillwright's security clause is fenced roughly sixty words
after the claim and never says *of the skill package* · skillwright owns the noun `skill` while
claiming only build-side verbs, so "what are skills" and "install the PDF skill" fall through the
catalog entirely.

**Still owed: the assertion side.** agentwright 17-20, skillwright 38-40, lorewright 23,
promptwright 36 — authored, never executed. A trigger run judges a listing; it says nothing about
behaviour, and this ledger does not let one stand in for the other.

---

## Active build — 1.2.0 pass (opened 2026-07-24)

Works the deferral register one item at a time. **This section is the pass's
resume point** — continue from the first unchecked item.

**Bump rule (clarified 2026-07-24 after item ④ hit it):** a member bumps when its
own contract changes — a new entry point or capability — with a dated CHANGELOG
entry that rides to the tag, per the Forge Run 3 precedent. An item that only
edits existing text (item ②'s descriptions) bumps nothing. The **pack** bump and
the `foundation-v1.2.0` tag land once, at pass close.

**Item ② — description regime** ✅ DONE 2026-07-24
Orchestration: 21-agent draft+verify workflow (recon → draft ×8 → 3 adversarial
judges, one-catalog-one-gate) + 2-judge re-verify of the gate amendment + 16-agent
after-baseline run. Approval catalog + addendum archived outside the repo at
`Workspace/artifacts/citadel-120-description-regime-catalog.md`.
- [x] All 8 descriptions slimmed off the 1024 ceiling into the 600–800 band:
  **8089 → 6208 chars (−23.3%)** (714/764/798/785/784/777/791/795); the ≥1000-char
  build.py warns clear pack-wide.
- [x] Boundary-sentence rule enforced — negative-partition sentences kept only where
  a recorded false fire backs them (every kept sentence cites its eval row in the
  catalog); clean-pass handoffs (commwright's lorewright/promptwright tails, prophylactic
  seams) move to the item-① seam table, never the description.
- [x] `promptwright model` token now literal in the description; model language
  broadened to "a prompt or a live task" (5B finally in trigger language). The watched
  #25/#16 seam held by the explicit carve-out ("a sourced multi-model product
  comparison is lorewright's verdict, not a run-target pick").
- [x] **Both 1.1.1 routing findings CLOSED:** commwright trigger row 7 — name trigger
  scoped to "message or channel work" + explicit voice-definition reroute ("even as
  'commwright voice', routes there"); application twin #23 still passes · brandwright
  row 14 — owner-approved gate amendment: skillwright's port clause positively claims
  "porting, renaming, rebranding, or sanitizing for a new owner", so the seam is
  claimed on BOTH sides (non-circular); drift-audit stays brandwright.
- [x] After-baseline instrumentation run 2026-07-24: **187/187 pack-wide** (baseline
  185/187) — commwright 23/23, brandwright 22/22, all six others unchanged at full pass;
  before/after ledgered in each member's `evals/RESULTS.md`. 12-row partition re-test
  12/12 (table restamped below).
- Residual seam-table register (feeds item ①): full-pack reskin foregrounding
  palette/taglines straddles skillwright-port vs brandwright-apply · "sanitize" verb
  overload (skillwright/brandwright/commwright objects disambiguate) · sourced niche
  go/no-go pulls lorewright-ward (skillwright↔lorewright) · bare "tighten this prompt"
  resolves only via promptwright's trim disclaimer (promptwright↔tokenwright).
- No version bumps (per the bump rule above — descriptions are existing text); the
  description warn→fail flip stays a next-tag action and is now moot pack-wide anyway.

**Item ④ — commwright half** ✅ DONE 2026-07-24 · commit `016413b` · **commwright 1.2.0**
(promptwright half still open, see below). Orchestration: 3 adversarial rounds
(build → verify → repair → converge), 19 Opus agents. Findings archived at
`Workspace/artifacts/commwright-humanize-findings{,2,3}.json`.
- [x] **Humanize is the DEFAULT register**, not a mode: every draft is humanized
  silently, and a draft that needed humanizing afterward was a defective draft.
  Plus a new `## Entry — Humanize` for handed-in text, facts frozen as in Reshape.
- [x] **Hard rules H1–H9 live in the SKILL body** with counting units and thresholds
  inline. The architecture law this pass established: *a rule whose count lives in an
  unloaded file is not a rule*. `references/humanize.md` (new) is the tell catalog,
  detection, repair, worked example, lexicon procedure, residual risks — and states
  no rule. Load budget unchanged at one reference file per draft.
- [x] **Owner decisions:** em/en dashes banned in any role (hyphens in compounds stay,
  repair is recast not substitution); zero emoji by default on every channel, with a
  per-message human override that is never sticky or inferred; **H1/H2 absolute even on
  text a human hands in** — their pet words, comma habits and sign-off survive, their
  dashes and emoji do not. The ban governs commwright OUTPUT only, never this repo's docs.
- [x] `channel-profiles.md` emoji sweep + restamp (owner policy, not a platform shift);
  its release-note title template restamped off the em dash it was mandating.
- [x] Trigger suite **32/32** (was 23 rows), ledgered in `evals/RESULTS.md`. Row 7 and the
  two new seam guards hold; humanize never claims to define or store a voice.
- **Was carried to 1.2.1, CLOSED 2026-07-25 (`81b44ec`):** at the time, the humanize-vs-repo-file-prose
  seam held only because skillwright owned the literal token `SKILL.md`, no member positively claimed
  prose-style work on repo files, and "humanize the README / my CLAUDE.md" leaked to commwright. Closed by
  giving skillwright a real register-pass capability first and the description claim second, plus the
  matching amendment to the always-on router. Row 25 ("humanize this draft") now fires on the unrivalled verb rather than an
  object match; re-check it on any future humanize edit. The 26 assertion cases were executed 2026-07-24: 25 of 26 run, 23 pass, 2 fail, 1 honestly not run.
- **Cost, feeding item ③:** commwright's body is ≈5039 tokens at HEAD (≈5255 when first written), over the 5k gloss — a
  deliberate trade to put the additive repair guidance on the always-loaded path, since
  a purely subtractive rule set yields clean dead prose. Three members now carry that
  warn (commwright, promptwright, skillwright) where item ③ expected two.
**Item ④ — promptwright half** ✅ DONE 2026-07-24 · **promptwright 1.2.0** (patch 1.2.1 from ③).
- [x] Framework-name menu in Phase 3: a naming rule first, then CO-STAR, RISEN, TIDD-EC, BAB,
  RTF, APE and three non-acronym shapes, each with what it suits, plus a tie-break and an
  explicit never-invent-an-expansion clause. Every letter expansion was verified against the
  real framework during review; the unsupported RISE-lineage claim was dropped rather than kept.
- [x] Fast path: five gate conditions judged after Phase 3 names the structure, a literal
  trace-line format, six exits, and a restart procedure. A fast path with no exit condition is
  how a build gets skipped rather than shortened.
- [x] Hostile-interpreter pass in Phase 6: enumerate binding lines by a stated counting unit,
  write the cheapest literally-compliant output for each, fail it if the requester would reject
  it, classify into four named shapes, apply that shape's repair, then a collision pass and an
  instruction-boundary check. Executable from the body without opening the reference.
- New `references/frameworks.md` and `references/hostile-interpreter.md`. Suite 25 → 30 rows
  (15/15), cases 29 → 35. Rows 26-30 and all 35 cases were executed 2026-07-24 (39/40).
- **Was open, CLOSED 2026-07-25 (`81b44ec`):** the by-name red-team entry had no *red-team* /
  *adversarial* / *hostile* token in the description, so it was reachable by intent but not by name,
  and the run correctly reported that rather than slipping vocabulary past the item-② freeze. Closed
  at promptwright 1.2.2/1.2.3: the description now carries `red-teams` and `red-team`, both object-bound,
  paid for by dropping "(Claude by default)" — which also leaves zero `Claude` tokens in it, making the
  lorewright carve-out on Claude-vs-GPT strictly easier.
- **Cost:** promptwright's body is now ≈8038 tokens, up from ≈5760. The largest body in the pack
  and the biggest single footprint regression of the pass. Feeds item ③.

**Item ⑤ — release doctrine** ✅ DONE 2026-07-24 · skillwright `references/release-doctrine.md`,
worked against this pack's shipped 1.1.0 and 1.1.1 releases and the open 1.2.0 pass
(there is no 1.2.0 release; `git tag` shows v1.0.0, v1.1.0, v1.1.1 only).
- Verification caught the repair round asserting that `build.py` never opens `RESULTS.md`. It
  does: `validate_evals()` globs `evals/*.md`. Corrected by hand to state precisely what is
  mechanized (provenance freshness, orphan rows, both warns that flip at the next tag) and what
  is convention. **A doctrine about release integrity had a false claim about the release tool.**

**Item ① — routing-seam table** ✅ DONE 2026-07-24.
- [x] Eight seams authored ONCE in skillwright's `pack-registry.md` and generated into all eight
  `references/pack.md` by the existing registry pipeline. A seam is declared in one place and
  generated into N, never hand-copied.
- [x] `build.py` boundary-pair check added, stdlib-only, following the file's warn idiom.
- [x] **The eighth seam was recorded OPEN and warned on every build (closed 2026-07-25, see below):** prose-style work on repo
  files had no owner. `build.py` printed `seam skillwright ↔ commwright: cold-listing signal
  'none — table only' — no description carries the signal, so the listing cannot route this
  pair; recorded open, not closed`. That was the correct outcome AT THE TIME — the table records a boundary,
  but only a description can route one. **Closed 2026-07-25 (`81b44ec`):** skillwright 1.3.x took a real
  register-pass capability and a description claim carrying the signal, the seam row's cold-listing cell
  was updated, and `build.py --check` now emits ZERO warnings — the first time in the pass.
- [x] skillwright's own doctrine updated to match (Integrate steps 2 and 5, and Build step 6), since the member
  that owns what a `pack.md` contains had not been told the seam table is now part of it.

**Item ③ — hygiene, owner-scoped** ✅ DONE 2026-07-24 (safe half only).
- [x] Anti-pattern dedup, one-statement-per-law, body-versus-reference single-home across all 8.
- [x] **Deliberately NOT done, owner's call 2026-07-24:** no body was slimmed to a budget and the
  footprint warn was NOT flipped to a failure. tokenwright's own C-1 audit called that churn, and
  slimming bodies whose suites currently pass risks stranding eval anchors. Three warns stood.
- [x] **Footprint gate RESCOPED, owner's call 2026-07-25** — the remaining half of item ③, resolved
  rather than deferred again. The 1.1.1 release promised these warns would "flip to fail at the next
  tag"; a 1.2.0 proposal then proved promptwright cannot reach 5k without breaking the architecture law
  (gutting all four rule blocks still lands at ≈5064, and the realistic floor is ≈7000). Flipping as
  written would have failed the build on correct skills. **What changed:** the ≤500-line norm stays a
  hard fail — that is the ecosystem spec (agentskills.io via `rubrics.md`) and it is untouched. The
  5k token figure is this pack's OWN advisory, and the gate is no longer *how big* but *whether the
  size is declared and justified*: a member over the advisory carries `metadata.body_budget`
  {`tokens`, `why`}, undeclared overage warns now and **fails at the next tag** (so item ③'s promise
  lands, on the right defect), and exceeding your own declared budget warns as drift. This applies the
  pack's existing declared-dependencies doctrine to cost. Budgets declared: promptwright 8500,
  skillwright 7500, commwright 6000. Also corrected: `measurement.md` equated the ≤500-line norm with
  "≈5k tokens", the exact conflation that made a flat token gloss fire on a spec-compliant 265-line body.
- **Accepted downsides, recorded not hidden:** the pack loses a single comparable number across members
  (everyone is "at budget" by construction); budgets are self-policed and can ratchet upward, caught only
  by a diff reviewer; the real per-invocation cost of a ≈8k-token body is accepted rather than paid down;
  and muting a flat gate makes the pack's divergence from the progressive-disclosure *spirit* less visible
  to a future reader. The drift check and the 500-line hard fail are what stop those becoming unbounded.

**Item ⑥ — spec.md split** ✅ DONE 2026-07-25. The baton was split into `spec.md` (the live
resume point — identity, status, deferral register, roster), this `ledger.md` (build passes and
eval-suite execution registers), and `decisions.md` (decisions log, adopt register,
recorded-not-built). Done as the close-out of the week rather than deferred to the next Forge Run;
the pass was already closed, so splitting the resume point carried no open-pass risk.

**First execution of both assertion suites** 2026-07-24 (the suites had only ever been
authored; trigger runs judge a listing, these run the skill). **commwright 23/25 pass, 2 fail,
1 not run · promptwright 39/40.**
- **The finding worth the whole run: both commwright failures share one root cause.** H9 "name
  the actor" pressure caused fact changes inside a frozen-facts Reshape, twice, independently,
  and no other rule failed at all. Case 4 promoted a first-person actor the source never named;
  Case 26 shed a manner fact ("by hand") while recasting an agentless passive. Both pass a
  word-level check, which is why only execution caught them. H9 now carries an explicit
  loses-to-the-freeze guard naming both breaches and the diff to run before accepting a repair.
- promptwright's one failure was a defective TEST, not a defective feature: Case 30's input
  ("product URLs into a table with name, price, stock") fires the Phase 2 knowledge-vacuum
  check, itself a listed Fast-path exit, so the gate in Phase 3 is never reached. The control
  experiment proved the route sound — a simple input emitted `Fast path — APE · baseline
  3.0 → 8.6 · 15/15 checks` **without opening frameworks.md**, confirming the body-alone design
  claim. Case 30's input was replaced and the reason recorded in the case.
- commwright Case 20 T1 honestly NOT RUN: it needs a message-compose tool this environment
  lacks, and faking it would be the exact failure the case guards against.

**Hand-fix audit** 2026-07-24: the four fixes made by hand after the last verification pass were
themselves audited, and three were incomplete in the way this pass keeps catching. `release-doctrine.md`
was corrected at line 33 only, leaving its framing paragraph, its Contents annotation, and its
provenance bullet all still asserting the eval ledger has no mechanism. Worse, the seam-table
sentence added to Integrate step 2 was never propagated to Build step 6, whose enumeration is
what a chat-surface build actually follows — a build following it literally emits a pack.md with
no seam table and `build.py` HARD FAILS at `validate_seam_manifest`. All corrected, and the
unconditional "pack.md carries the seam table" claim narrowed to match `build.py`'s `if seams:`.

**PASS CLOSEABLE, NOT YET TAGGED — status corrected 2026-07-25.** The 2026-07-24 entry here listed
four blockers; all four have since cleared, and leaving the old text would have understated the state
at exactly the place a future session resumes from.
- Unexecuted suites → **all eight assertion suites were executed once, on 2026-07-24**, and that run is
  what the ledgers carry. The 1.2.1 fix loop then repaired every finding **by inspection**; those repairs
  were re-run inside the orchestration, but the results were never written into any `evals/RESULTS.md`,
  so the repo does not carry them and this file will not claim them. Several members say so themselves:
  brandwright records "the suite still has not been re-run", skillwright "no suite was executed in this
  pass" with 32/36 standing as its last executed result, tokenwright lists amended cases as unrun, and
  promptwright's newest entry heads "NO RUN PERFORMED". **A re-run of all eight, properly ledgered, is
  owed before the next tag** — this one ships on the 2026-07-24 execution plus inspected repairs, and
  that is the honest description of it.
  **No pack-wide aggregate is quoted here on purpose.** An earlier draft of this line scored
  "142/142 pack-wide", a number that appeared exactly once in the whole repo — in that sentence — and
  which no `evals/RESULTS.md` substantiated. Release doctrine forbids exactly that ("what may not be
  written: a row that was not run"), and a summary that outruns its ledgers is the same defect in
  aggregate form. The authoritative record is each member's own `evals/RESULTS.md`; read the per-member
  entries rather than a rolled-up figure, and roll one up only from ledgers that carry it.
- Unverified hand-fixes → **audited and corrected**, including a botched find/replace that had shipped
  ungrammatical text into brandwright's always-loaded body.
- promptwright's ≈8038-token body unreviewed → **resolved by the item-③ footprint rescope**, with a
  declared budget rather than a muted warn.
- Item ⑥ open → **does not gate this pass.** The register gates ⑥ on "before the next Forge Run", not
  on 1.2.0, so it carries forward rather than blocking the tag.

What remains is not a blocker but a decision: the pack version and the tag are the owner's act, per the
bump rule above. Everything is on main and `build.py --check` is clean **with zero warnings** — the last one
cleared on 2026-07-25 when the prose-on-repo-files seam closed. **Both items previously carried to
1.2.1 are now closed** (commit `81b44ec`): skillwright took a minor bump to 1.3.x for a real register-pass
capability plus the description claim that gives the seam a cold-listing signal, and promptwright took the
red-team vocabulary for the hostile-interpreter pass item ④ had already shipped but never named. The
always-on router in `packs/foundation/CLAUDE.md` was amended to match, since it is a pack-level surface
no member owns and the skillwright agent correctly declined to reach into it and disclosed the gap instead.

---

## Active build — Forge Run 3 → 1.1.0 (approved 2026-07-23)

Full pack-reopening pass: uniform structure across all 8, brand decoupled into
brandwright as the single brand home, two new capabilities, native-first
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
- [x] Split skillwright `brand-config.md`: brand styling → brandwright definition; structural roster → skillwright `pack-registry.md` (build.py derives from here)
- [x] Move cascade doctrine skillwright `brand-inheritance.md` → brandwright `application-doctrine.md` (reframed as on-invoke Apply)
- [x] Fold `voices.md` into brandwright's definition (Voice profile section); commwright sheds it
- [x] skillwright build path → neutral-default + structural-identity stamp only; `## Entry — Configure` removed
- [x] commwright → channel-correct + neutral-voice default; voice sourced from brandwright export on request; `## Entry — Voice` removed
- [x] brandwright → single home of brand + voice; new `## Entry — Apply`; Export voice profile now native
- [x] Point build.py at `pack-registry.md`; all 8 `pack.md` regenerated; `build.py --check` clean, count 8=8=8
- [x] 5F native-first Packaging (skillwright) — landed here early (validate-by-inspection default, optional shell hard-check, zip only as multi-file fallback); Phase 2's 5F box is satisfied
- [x] 3 changed skills bumped to 1.1.0 on main w/ dated CHANGELOG entries (ride to the Phase 6 tag)
- Swap masters now 2 surfaces {brandwright brand-definition (incl. voice profile), promptwright prompt-card} — commwright voices.md retired from the swap set
- **Deferred doc cleanup (named, not silent):** README ×3 (skillwright/commwright/brandwright — removed `configure`/`voice` commands + deleted-file tree lines) → Phase 2 U-6 full README rewrite. SOURCES ×2 volatile-file footnotes (brand-config/voices) → Phase 2. evals ×2 (skillwright `configure` test, commwright `voice` test) → Phase 6 evalwright refresh. None are runtime-loaded or build-validated; pack builds clean.

**Phase 2 — Uniformity layer** (all 8) ✅ DONE 2026-07-23
Staged in batches (SKILL.md work split from READMEs): **2A** skillwright+promptwright ✅ · **2B** commwright+agentwright+brandwright ✅ · **2C** lorewright+evalwright+tokenwright ✅ — **all 8 SKILL.md uniform** · **2D-1** README ×4 (skillwright, commwright, brandwright, agentwright) + SOURCES reconcile ✅ · **2D-2** README ×4 (promptwright, lorewright, evalwright, tokenwright) ⬜ NEXT. (README normalization split 4+4 — eight full rewrites too large for one pass.)
Volatile taxonomy (decided 2026-07-23): **calendar** (stamped, 60d) = skillwright rubrics.md, promptwright model-snapshot.md, tokenwright measurement.md · **event-driven** (restamp on trigger) = skillwright pack-registry.md, brandwright brand-definition.md, commwright channel-profiles.md · **none** = lorewright (re-verifies every run), evalwright (refresh is target-triggered), **agentwright TEMP** (platform-notes.md is genuine Phase 4 U-9 research; declared none now, Phase 4 upgrades it + adds its refresh path). metadata.volatile format = YAML list of {file, class, cadence_days?} or [] for none; last-verified date lives in each file's own header stamp (not duplicated in frontmatter); build.py U-7 (Phase 5) validates existence + stamp for calendar class only. NOTE for 2D: commwright SOURCES.md still calls channel-profiles.md "durable, no stamped baseline" — now declared event-driven; reconcile in the README/SOURCES pass.
- [x] U-1 `metadata.volatile:` frontmatter block ×8 — DONE (all 8; calendar ×3, event-driven ×3, none ×2 counting agentwright-temp)
- [x] U-2 uniform `## Volatile surfaces` block ×8 — DONE (lorewright/evalwright/agentwright declare none + why)
- [x] U-3 standardize Restraint-section position — DONE (6 moved: commwright/agentwright/brandwright/lorewright/evalwright/tokenwright; skillwright/promptwright were already canonical; every SKILL.md now Load budget → Volatile surfaces → Restraint → entries)
- [x] U-4 promptwright first-class `## Entry — Refresh` — DONE (promoted from Behavior-notes Maintenance; cross-refs fixed)
- [x] U-5 uniform `## Anti-patterns` section ×8 — DONE (all 8)
- [x] U-6 normalize README skeleton ×8 — DONE (all 8 on the canonical skeleton: tagline → Workflow → Package contents → Install → Entry points → Commands & switches → Staying current → Changelog). 2D-1 (skillwright/commwright/brandwright/agentwright) removed Phase 1 stale refs (configure/brand-config/brand-inheritance, voice/voices) + agentwright's stray owner note + reconciled skillwright/commwright SOURCES. 2D-2 (promptwright/lorewright/evalwright/tokenwright): promptwright compressed 116→~75 lines (Performance/Output/Pack/Renaming folded in); evalwright + tokenwright restructured from terse/hybrid; lorewright light-touch (already canonical). All Staying-current sections now match each skill's metadata.volatile. Each README's evals note = "in full folder-zips, excluded from .skill". (Minor non-issue left: skillwright uses "**Build workflow:**" vs others' "**Workflow:**" — defensible, not normalized.)
- **Brand centralization pass** ✅ DONE 2026-07-23 (user requested "all brand output centralized through brandwright" — extends Phase 1 decoupling to the remaining skills). Audited all 8 for brand-output: commwright/agentwright/lorewright/evalwright carry only the `brand: revenant` frontmatter *label* (structural, kept). Three real touchpoints fixed: (1) **tokenwright** — removed the per-run `brand:` report-flavor switch (SKILL + README); reports/sheets/rewrites always neutral. (2) **promptwright** — the HTML prompt card shipped a hardcoded `revenant-foundation-promptwright` wordmark lockup + `<title>`; now fully neutral ("Prompt Card" label). (3) **skillwright** — removed a stale "brand cascade" reference in `build-templates.md` (Phase 1 leftover). **brandwright** `application-doctrine.md` now names sibling artifacts (prompt cards, tokenwright reports, any skill's HTML) as canonical Apply targets. Result: brandwright is the single door for ALL brand application; every other skill outputs neutral. skillwright/promptwright/tokenwright/brandwright 1.1.0 changelogs updated (no version change; 1.1.0 unreleased). Verified: zero non-label brand-output remains pack-wide.
- [x] 5F native-first Packaging rework (skillwright) — DONE in Phase 1 (landed with the skillwright rewrite)

**Phase 3 — New capabilities** ✅ DONE 2026-07-23
Batches: **3A** skillwright Entry — Upkeep (5A) ✅ · **3B** promptwright Entry — Model (5B) + tier hints (5E) ✅ · **3C** foundation CLAUDE.md (5C) ⬜ NEXT.
- [x] 5A skillwright `## Entry — Upkeep` — DONE. Pack-wide staleness sweep: reads every member's metadata.volatile, reports calendar-surface status vs cadence (report-only default), runs the mapped refresh verb per overdue surface on approval (rubrics→skillwright refresh · model-snapshot→promptwright refresh · measurement→tokenwright refresh), degrades by environment (read-stamps portable; run-refresh needs search+file tools; never auto-commit). New reference `upkeep-doctrine.md`; `upkeep` in description + bare-invocation + README. skillwright desc now 1022/1024 chars.
- [x] 5B promptwright `## Entry — Model` — DONE. Standalone tier + model recommendation for a live task (no prompt built); reuses the Phase 5 tier taxonomy (durable S/A/B/C) with names from `model-snapshot.md` (tier-name fallback past the stamp); delivers tier + model + effort + flip condition. Boundary: the Model line stays Phase 5's (attached to a build); a sourced multi-model comparison is lorewright. `promptwright model` added to bare-invocation + README (description already covered the trigger, left at 1004/1024).
- [x] 5E durable tier hints — DONE. promptwright: the tier taxonomy is the durable, snapshot-free layer both Entry — Model and the Model line draw on. tokenwright: model-tier questions now route to promptwright `Entry — Model` specifically, plus a durable tier→cost note (tokenwright reasons in tiers, never names a model).
- [x] 5C foundation `CLAUDE.md` — DONE. Always-on router + conventions at `packs/foundation/CLAUDE.md` (pack-scoped, not repo-root — foundation is one pack in a multi-pack marketplace). Not a skill — standing context. Sections: reaching for the right wright (task→wright table), how they compose (neutral→brandwright apply; skillwright→evalwright; promptwright model owns model data; skillwright upkeep sweeps freshness; lorewright decides), conventions (neutral default, one-gate, audits report-only, declared deps, stamped+swept volatile surfaces). Repo README updated: CLAUDE.md discoverability line + 3 stale wright rows fixed (skillwright no "brands", commwright no "saved voice", brandwright now brand+voice). **Phase 3 COMPLETE.**

**Phase 4 — Baseline refreshes** (restamp 2026-07-23) ✅ DONE 2026-07-23
Batches: **4A** promptwright model-snapshot ✅ · **4B** skillwright rubrics + tokenwright measurement ✅ · **4C** agentwright platform-notes (U-9) + commwright channel-profiles stamp (U-10) ✅.
- [x] skillwright `rubrics.md` — DONE (restamped 2026-07-23). Format stable: agentskills.io canonical, anthropics/skills carries an explicit spec pointer file, ≤500-line + progressive-disclosure guidance unchanged, standard adopted by Codex/Copilot. ClawHub added as a cited-not-verified niche-source candidate next to Skillstore (~490K-skill ecosystem per 07-23 cross-checks); per-source live-check dates kept honest (07-12/07-13).
- [x] promptwright `model-snapshot.md` — DONE (restamped 2026-07-23, genuine re-research vs vendor docs + registries). Real drift caught since the 07-06 stamp: OpenAI → **GPT-5.6 family** (Sol/Terra/Luna, GA 07-09, 1M ctx ×3; 5.5 Pro stays S); Gemini → **3.6 Flash** (07-21 workhorse, −17% output tokens) + **3.5 Flash-Lite** (C), with **3.5 Pro flagged partner-only/never-recommend** (Gemini S slot empty; 3.1 Pro = top GA); Grok → **4.5** (07-08, A-tier, 500K-ctx caveat vs 4.3's 1M / 4.1 Fast's 2M; >200K surcharge on 4.5/4.3); DeepSeek → V4-Flash at C, **V4 Pro promo expired 05-31** (standard rate now). Claude column CONFIRMED correct as stamped (Sonnet 5 GA 06-30; Sonnet 4.6 legacy; intro pricing to 08-31; effort xhigh Sonnet 5+, max Fable 5). Also fixed the file's stale refresh pointer (Behavior notes → Maintenance ⇒ Entry — Refresh). Rides in unreleased 1.1.0 (no patch bump).
- [x] tokenwright `measurement.md` — DONE (restamped 2026-07-23). REAL STALE FIX: OpenAI cached reads were listed ~50% of input — current families (5.4+) bill ~0.10× (the 50% is gpt-4o-era legacy); GPT-5.6 cache writes 1.25× w/ 30-min minimum added. Anthropic sharpened: ≤4 breakpoints, 1.25×/2× write (5-min/1-hr), 0.10× reads, TTL refresh-on-read, reads excluded from input rate limits. Skill-metadata discovery cost → measured median ~80 tok/skill (~55–235). Ratios durable, unchanged.
- [x] U-9 agentwright `platform-notes.md` — DONE (new stamped baseline, verified 2026-07-23, real research). Contents: enforcement surfaces per platform (Claude Code 3-gate permissions/sandbox/hooks incl. hook-CVE attack-surface notes + exit-0 footgun; Cowork native cadences hourly/daily/weekly/weekdays; OpenAI Agents SDK guardrails/resumable approvals, Agent Builder EOL 2026-11-30; MCP allowlists + server CVEs), scheduling surfaces, layered kill-switch doctrine (CISA/NSA 2026-04 guidance, EU/SG regs, governance-gap stats), injection state (unsolved — blast-radius limitation; agent commits leak credentials ~2× baseline), checklist-area→mechanism map. agentwright volatile [] → calendar 60d; Volatile surfaces + Load budget rewritten; new `## Entry — Refresh`; description 1019/1024; README updated. skillwright upkeep-doctrine verb map + example gained the 4th calendar row.
- [x] U-10 commwright `channel-profiles.md` — DONE: event-driven header stamp added (Last restamped 2026-07-23) so the declaration, file, and upkeep read one dated surface; SKILL volatile section points at it. **Phase 4 COMPLETE.**

**Phase 5 — Toolchain + validation** ✅ DONE 2026-07-23
- [x] U-7 build.py `validate_volatile()` — DONE. Stdlib parse (no yaml dep); rules: block required on all 8 (`[]` for none) · class ∈ {calendar, event-driven} · declared file exists · calendar needs sane cadence_days 7–365 + dated header stamp (`Last verified/restamped/stamped: YYYY-MM-DD`, not future) · event-driven must not carry cadence_days. Wired into validate_skill, runs in --check and full modes; docstring updated; root CHANGELOG gained an Unreleased note. **Two real bugs the 8-case negative-test matrix caught before shipping:** (1) the `[]` regex had optional brackets, so the bare `volatile:` line of every LIST also matched and the validator early-returned — passed clean trees, validated nothing; fixed to require literal `[]`. (2) stamp search window was 6 lines — rubrics.md legitimately stamps its volatile *section* (~line 18, only that section is volatile), previously masked by bug 1; widened to 40 lines with a comment. All 7 failure modes proven firing on exactly the mutated member; clean trees pass.
- [x] Run build.py full — DONE (sandbox): 8/8 dist zips at 1.1.0, 0 manifests synced (no registry drift), all validation incl. U-7 green. dist/ is gitignored (release artifacts; CI attaches on tag).

**Phase 6 — Eval + release integrity** ✅ DONE 2026-07-23
Batches: **6A** eval refresh ×8 ✅ · **6B** partition re-test + release metadata + tag ✅.
- [x] evalwright event-driven refresh ×8 — DONE (2026-07-23, diff-scoped, touched cases only). **skillwright**: trigger #7 → upkeep, #8 flipped to brandwright boundary (34 rows, 17/17); cases 11–12 → Upkeep (sweep report-only + refresh-on-approval/degradation), 15–16 → neutral build + brandwright routing; brand-config→pack-registry rename in 17, brand:-switch removed from 18; header/contents/provenance updated. **commwright**: #7 flipped (definition→brandwright) + #23 added as the application-side pair (23 q, 11/12); firewall cases re-anchored to handed-in profiles; Case 19 → definition-routes/application-stays two-turn. **brandwright**: #12 FLIPPED to SHOULD (Entry — Apply is its own; 22 q, 13/9); Case 9 → structural-payload export; Case 10 names apply; Case 12 → T2 runs Apply per application-doctrine. **promptwright**: #25 added (Entry — Model, live task no prompt; 25 q, 12/13); prompt-in-play edge note corrected; Case 29 added (standalone rec contract + lorewright boundary). **agentwright**: #23 added (refresh; 23 q, 12/11); Case 16 added (refresh scope). **tokenwright**: Case 15 → always-neutral + brandwright routing, retired brand: switch purged. **lorewright + evalwright**: swept clean, zero stale, entries unchanged — no edits. Count integrity verified per file (declared = actual everywhere); pack-wide stale sweep zero. Changelog notes ×6.
- [x] 12-row trigger-partition re-test — DONE 2026-07-23, 12/12 single-destination against live descriptions; sharp pairs verified on-disk; the four new 1.1.0 claims partition cleanly (results recorded in the Trigger-partition table section below).
- [x] Release metadata — DONE: all 8 CHANGELOGs already head `## [1.1.0] - 2026-07-23` (created release-dated); marketplace.json foundation plugin 1.0.0 → 1.1.0; root CHANGELOG's Unreleased converted to the dated `[foundation-v1.1.0] - 2026-07-23` entry. Tag `foundation-v1.1.0` is the user's push step (CI attaches the 8 member zips on tag). **Phase 6 COMPLETE.**

**Brand-carriage law** (owner decision 2026-07-23, post-run — supersedes the 2-swap state where they differ): **the only brand carrier anywhere, repo or installs, is the locally configured brandwright.** All other members are brandless everywhere; branded artifacts — prompt cards included — are produced at need via `brandwright apply` and never stored. Consequence: the prompt-card swap retired; swap set 2→1 {brand-definition}; apply-install-swaps.py, RUNBOOK, and upkeep-task.md updated (script ignores a stray prompt-card.md with a retirement note). Verified same day: applied-brand sweep across all 8 skill folders clean — zero house strings, zero palette hexes, "Revenant" only as structural tokens (names, metadata.brand label, canonical-repo URL). No member files touched → no version bumps. Non-skill brand surfaces, owner's call made same day: **repo `brand/` folder REMOVED** (git rm; the public house-only definition v1.3.1 + HTML brand guide leave the repo — the locally configured brandwright is the definition's only home; git history retains the files if ever needed) · **structural `revenant-` naming + marketplace token KEPT** (name segments are structure per the shipped doctrine; renaming would break registry, marketplace, installs, and tag history for zero brand-carriage gain). Same sweep extended to root docs caught the house tagline signing off the root README — removed under the law; a branded README is a `brandwright apply` product at need, never the repo copy.

**Phase 7 — Audit + capstone + final optimization** ✅ DONE 2026-07-23
Batches: **7A** final Fable audit (user-added) ✅ · **7B** tokenwright C-1 audit + capstone restamp ✅ · **7C** delivery + Cowork upkeep task (60d) ✅. **ALL PHASES COMPLETE.**
- [x] 7A FINAL AUDIT — DONE 2026-07-23 against the tagged release (main == foundation-v1.1.0 == bddde22). **Part A, intended changes: all verified landed** — decoupling files (3 gone, 4 new), uniformity ×8 (volatile block, Volatile-surfaces, Anti-patterns, Restraint position), 4 calendar stamps + commwright event stamp at 2026-07-23, U-7 defined+wired, release metadata, --check clean, desc/body limits ×8 green. **Part B, logic gaps — 4 real finds, all FIXED (F1–F4):** F1 brandwright `audit-doctrine.md` export shape still titled "skillwright configure payload" → "Structural payload (skillwright consumes it)". F2 RUNBOOK still carried the 3-row swap table (commwright voices.md) + a now-past "coming in 1.1.0" note → 2-row table {brand-definition (identity+voice), prompt-card}, note resolved; build.py's documented validation list gained the U-7 clause. F3 marketplace description "brandwright (brand & drift)" → "(brand & voice)". F4 **genuine divergence:** skillwright SKILL.md's Entry — Upkeep inline verb map had only 3 surfaces while upkeep-doctrine had 4 — platform-notes row added; entry and doctrine agree again. False positives confirmed by-design: commwright eval negative-inputs; cross-member mentions (evalwright fallback line, skillwright verb map, Behavior-notes brand-definition). **Versioning:** skillwright + brandwright → 1.1.1 with dated entries per the 1.0.1 post-launch-audit precedent; fixes ride main (installed copies behaviorally unaffected; next tag picks them up, or re-tag if wanted). **Part C, recommendations register:** (1) watch the promptwright-Model vs lorewright-comparison boundary in real usage (eval pair #25/#16 covers the seam). (2) Owner to-do outside this run: `agentwright audit` the two live trading specs (Research Agent, Entry Scan) against the new platform-notes baseline — the standing-targets note left the public README in 2D-1 but the job remains. (3) Optional hardening: extend U-7 to require stamps on event-driven files too (all three carry them; low value — calendar-only per spec). (4) Confirm CI attached 8 zips to the foundation-v1.1.0 release (user-side check). (5) First upkeep due ~2026-09-21 — the 7C Cowork task encodes it.
- [x] tokenwright pass — DONE 2026-07-23 as a **C-1 score-only audit** (tokenwright's own churn-restraint + already-lean doctrine governed the verdict). Measured (estimate, chars÷4 prose ratio, ±15%): bodies agentwright 1.7k · brandwright 2.4k · commwright 1.8k · evalwright 1.5k · lorewright 1.4k · promptwright 5.8k · skillwright 6.4k · tokenwright 2.6k ≈ **23.4k total trigger-loaded**; discovery layer (8 near-max descriptions) ≈ **2.5k tok/session always-on**. Findings: (W-dense, P2) skillwright + promptwright exceed the ≈5k-token gloss while well under the 500-line norm — flagged as **opportunistic-slim candidates on their next content touch** (recoverable est ~10–15% each via table/phrasing compression), NOT worth standalone churn one commit after a release: 8 version bumps + re-uploads + eval-anchor regression risk against ~1–2k tok recovered on files that load one-at-a-time. (Discovery, noted-no-action) descriptions run ~3× the ecosystem median ~80 tok/skill because they're routing-maxed near 1024 chars — the "routing wins, then trim" tradeoff, made deliberately and re-proven by the 12/12 partition. **Verdict: already lean — no rung clears the net-cost bar; pack built under tokenwright's rules from the start.**
- [x] Forge Run 3 capstone — DONE 2026-07-23. The 1.1.0 rebuild itself is the live run (all eight doctrines exercised in anger); registry capstone line restamped with the run record; build.py propagated the fresh capstone to all 8 `references/pack.md` manifests. No separate demo theater — the build is the proof.
- [x] Delivery assembled — DONE 2026-07-23. Repo synced through per-phase bundles (main at 7B close); tag `foundation-v1.1.0` pushed, CI attached the 8 member zips. **`tools/apply-install-swaps.py` written** — the RUNBOOK referenced it but it never existed in the public repo (a 7A doc-claim miss: the claim was checked, the file wasn't); contract implemented + tested (hard-fail on neutral input · builds `dist/install/<member>-<ver>+install.zip` on a real swap · skips absent swaps · repo untouched). Upload checklist delivered in-chat: local build → swap script for {brand-definition, prompt-card} → delete-and-re-upload ×8 on claude.ai. Release-asset note: the tag predates the 1.1.1 audit fixes + capstone manifests — local dist builds are the upload source of truth; optional `foundation-v1.1.1` re-tag documented for asset parity.
- [x] Cowork upkeep task — DONE at **60-day cadence (owner decision, replacing the 61-day draft)**: `packs/foundation/upkeep-task.md` — weekly-Monday wrapper (Cowork native cadences only), stamp check against the four calendar surfaces via canonical-repo raw reads, zero-signal one-liner under 53d, due-soon note 53–59d, full upkeep flow at ≥60d (refresh per owner verb, files + paste-ready commit line, never commits itself); first actionable fire lands exactly on the due date, Monday 2026-09-21. **Phase 7 COMPLETE — FORGE RUN 3 CLOSED.**

**After the build:** stand up a Cowork scheduled task (weekly cadence, the tightest
native option) that runs `skillwright upkeep` and refreshes anything past its
per-surface staleness window. First upkeep due ~2026-09-21 (all stamps reset 07-23).

---

## 1.2.1 register — findings from the first full suite execution (2026-07-24)

All eight assertion suites have now been EXECUTED (they run the skill; trigger runs only judge a
cold listing). Pack-wide **109/116 across the six run last**, plus commwright 23/25 and promptwright
39/40 earlier the same day. Execution found structural defects that three rounds of document review
did not, in members whose suites had never failed. Full findings:
`Workspace/artifacts/foundation-suite-execution-findings.json`.

**The pattern, stated once because it recurs in five of eight members:** a rule collides with another
rule under pressure, and the eval assert — not the doctrine — picks the winner. commwright's H9 versus
frozen-facts was the first instance; it is not special.

- **brandwright 14/16, the only member with a live contradiction.** Its two export shapes are defined
  twice and the definitions disagree: SKILL.md says a structural payload is `brand token · naming
  template · license default`, `audit-doctrine.md` says `token · identity map · palette roles · voice
  line · license · wordmark`. **No output can satisfy both.** Worse, the Load budget contains the word
  "export" zero times, so an export-only run never loads the file holding the shapes. Fix: one home for
  each shape, and route export runs to it.
- **agentwright 15/15 but its invocation surface is undocumented in the load path.** Bare invocation and
  area spot-check exist only in `README.md`, which the Load budget never opens and which is not injected
  when a skill runs. Two cases pass on assistant convention alone. The skill already knows the fix:
  `design-checklist.md` areas 7 and 10 delegate upward with "they bind whether or not this file is open".
  Apply that pattern in the body. The runner also disclosed it had grepped README before answering, so
  the passes cannot be read as the loaded doctrine producing the behavior.
- **agentwright row 19 CORRECTED, a standing finding was wrong.** The recorded claim was that the harassment
  row "passes only on assistant-level restraint, not on the text". Executed live in two wordings including
  a laundered one, the **body's own Restraint clause caught both** and offered the legitimate alternative.
  Re-scope the finding: the description carries no restraint cue, so a cold listing judge sees only
  "design an agent" — but the body fires on execution. A description gap, not a body gap.
- **tokenwright 17/18, and its flagship P0 is unenforceable.** The Audit entry defines P0 as "a description
  past its platform cap" and never names the cap; grep of the entire declared load path returns no
  description character cap at all. The one `1,024` in the load path is OpenAI's cache-prefix threshold in
  **tokens** (`measurement.md`), a units false-friend sitting exactly where a model reaching for "the cap"
  will find it. Claude Code's real listing cap is `skillListingMaxDescChars`, default **1536 characters**,
  so a model falling back on memory is wrong by 512. Note `build.py` hard-fails at 1024 chars — that is a
  deliberate house ceiling, not the platform cap, and no doctrine should call it one.
- **skillwright 32/36, two shared causes.** (a) FAILs 14 and 17: version passes swept renamed entry points
  but not asserts whose ground moved underneath them — the bare-invocation reply grew to 4 sentences
  against a `<=3` assert, and the 1.1.0 decoupling moved registry writes into Integrate so Build can no
  longer produce the manifest Case 17 asserts. Rule to adopt: when a pass edits mandated verbatim text or
  moves a write between entry points, re-run every case asserting on that text or artifact. (b) FAILs 19
  and 20: `PORT-REPORT.md` is a required output carrying the old→new name map, so the port's own audit
  artifact necessarily contains the source brand token the residue asserts forbid. Scope the assert to
  shipped skill files, or the doctrine forbids its own deliverable.
- **evalwright 13/13 but five non-production states share one rule.** SKILL.md names one flag
  (`<no-suite>`); the suite exercises five distinct cannot-produce states and demands mutually exclusive
  shapes for three of them. Nothing distinguishes a bare keyword from a named-but-absent target except the
  assert text. `<no-build>` appears zero times in SKILL.md.
- **lorewright 18/18 but its two evidence tags collide on ~90% of real cells.** `[documented]` is earned by
  "primary source read this run" and `[vendor-reported]` by "vendor's own page" — a vendor-published price
  satisfies both and they return different tags. Since the closing confidence line is derived from the tag
  mix, the same verdict can honestly close "high" or "medium". The suite encodes both readings.
- **commwright H9 guard: holds, but insufficient.** Cases 4 and 26 re-run and PASS on identical sources. But
  a repair was constructed that clears both prescribed diffs with zero novel tokens and still invents an
  actor: the guard closes repair step 1 and adverbial loss, then redirects pressure into step 2 ("recast so
  the sentence needs no actor"), which is unguarded. Also flagged: the worked breach names first person
  only, so an invented bare third person ("They'll validate parking") slips the example; and event-to-state
  recasting ("has been notified" → "knows") is unnamed doctrine-wide and shipped unflagged in the very run
  the guard was written from. Cases 4 and 26 ship no fixture, so both turn on sources that live only in a
  temp file — add fixtures.

---

## 1.2.1 register — the ledgered re-run (2026-07-25, post-tag)

The debt `foundation-v1.2.0` shipped with is **paid**: all eight assertion suites executed against the
released text and written into each `evals/RESULTS.md`. **177/178 executed-and-passed · 1 FAIL · 2 NOT RUN**
(agentwright 15/15 · brandwright 16/16 · commwright 25/25 · evalwright 13/13 · lorewright 19/19 · promptwright 35/35 ·
skillwright 37/37 · tokenwright 17/18). Measurement only — nothing was fixed, so the ledgers describe the text
that actually shipped. Raw: `Workspace/artifacts/foundation-v120-ledgered-rerun.json`.

**The theme, in six of eight members: a green suite is weaker evidence than it looks.** The defects are no
longer contradictions — those were closed in the 1.2.1 fix loop — they are asserts that check the SHAPE of an
artifact rather than the PROPERTY the doctrine governs. brandwright's runner put it best: *"a 16/16 here is
weaker evidence than the 14/16 was."*

- **tokenwright — A STAMPED PLATFORM FIGURE IS WRONG, and it is the second time a disposition overruled a
  correct runner.** `measurement.md` states Anthropic's minimum cacheable length as "per-model and currently
  runs **1,024–4,096 tokens**". The runner fetched the primary source twice on 2026-07-25 and reports the low
  end is **512**, not 1,024. Worse: the v1.1.2 runner originally recorded 512–4,096 correctly, and the **v1.1.4
  disposition overruled it as "model memory"** and wrote 1,024 into both `measurement.md` and `SOURCES.md`,
  with CHANGELOG 1.1.4 calling the wrong number "the sourced range". That is precisely the failure mode v1.1.6
  retracted for the description counting unit — still live, in the file next door, uncaught. **Owner check
  before acting:** the runner cites a model name this session cannot independently confirm, and this member
  has now been wrong in both directions, so verify against the live doctrine page before writing anything.
  Consequence today: Case 6's cache advice is computed off the wrong floor.
- **tokenwright Case 13 T2 — the only FAIL, and an honest one.** The run claimed "`1,536` occurs in SKILL.md
  exactly once" without running the grep; it occurs **twice** on line 68, and a refresh syncing only the
  "Platform cap" occurrence leaves "can bite far below 1,536" stale — body and stamp disagreeing, which is
  exactly what the assert forbids. The runner caught its own false completeness claim and recorded it verbatim
  rather than softening it.
- **skillwright — A FALSE HOME the suite is blind to by construction.** SKILL.md line 108 cites "one statement
  made twice, so neither copy is authoritative" to `rubrics.md` § progressive disclosure. **The rule is not
  there** (mechanical scan: `twice` 0, `duplicat` 0, `authoritative` 0, `single source` 0). Case 37's assert
  repeats the citation verbatim, so a run that cites the empty home **passes**. The case validates the pointer,
  not the rule — the same shape as the H9/frozen-facts collision.
- **brandwright — the failure mode changed class, from contradictions to SILENCES.** Every prior FAIL and every
  stated-twice collision is genuinely closed, verified mechanically against released text. What survives is
  under-specification: four cases pass only because the runner supplied a missing rule by inference. **The
  sharpest instance is self-referential:** nine of sixteen cases require "a definition stored", the suite ships
  no fixture, and Entry — Export has no handed-in path, so executing them required **inventing a brand identity
  — the single thing the neutral-core law exists to prevent**. It also makes those nine rows non-reproducible,
  since each executor invents a different fixture. Ship a fixture definition before comparing two runs again.
- **agentwright — the suite tests shape, never sizing.** Every assert across all sixteen cases is an existence,
  count, string-presence or range check. Nothing tests whether a number is calibrated to the blast radius the
  same spec declared: a `$50,000,000` per-trade cap satisfies Case 3 exactly as well as `$2,500`. The standing
  "Never pad has no test" finding is one symptom of this, not a standalone gap.
- **evalwright — literal-absence asserts have no surface scope.** "no `<no-build>`" and "no gate question
  appears" both break a strict grep because the string occurs inside the negation itself, or inside a generated
  case's own absence assertion. SKILL.md line 37 already diagnosed this exact double-use problem for flags and
  closed it there; the fix was never generalized to assert text.
- **lorewright — string-shaped asserts at the point the doctrine got nuanced.** Case 19's "does not read 'high'"
  false-fires on the doctrine-correct "Confidence: moderate, not high", and would happily **pass** "Confidence:
  excellent", which breaks verdict-mode §4 outright. Two prior findings did not recur only by luck of phrasing.
- **promptwright — one artifact's shape stated twice, differently, in the released body.** Entry — Model step 4
  and the Phase 7 footer specify different separators for the same model line; the follow-up path and the Phase 7
  pre-flight disagree on where the diff sits. Both are load-bearing for a case, and the runner slipped on the
  first before self-correcting.
- **commwright — the one unambiguous good-news result.** The H9-versus-frozen-facts collision found on
  2026-07-24 is **caught rather than shipped**: two fact-move near-misses were rejected in flight against the
  1.2.3/1.2.4 fact-integrity text, including one that clears the two-item diff and is only stopped by the
  enumerated class list. The fix works, and it works for the reason it was written.

**Disposition:** none of this is a v1.2.0 hotfix — the release is out, CI is green, and every finding is
recorded rather than patched. The tokenwright cache floor is the one worth checking first, because it is a
factual error that produces wrong advice and its correction history has been wrong twice.

---

## Trigger-partition table

**Re-run 2026-07-24 against the item-② slimmed descriptions (600–800 band) — 12/12 route to exactly one destination.** Two independent cold-listing judges (partition + findings lenses) verified the amended set: all 12 rows unchanged in destination; row 6 fires brandwright on drift vocabulary alone, row 11 holds via lorewright's by-name deferral, row 12 via promptwright's reciprocal trim boundary. Six fresh seam attacks on skillwright's amended port clause: five unambiguous, one recorded edge (full-pack reskin foregrounding palette/taglines — logged to the item-① seam-table register). The commwright #7 / brandwright #14 closures verified at set level, non-circular on both sides.

**Re-run 2026-07-23 against the live descriptions at the 1.1.0 release bar — 12/12 route to exactly one destination.** The three Phase-1 description changes sharpened the boundaries as predicted; the four new 1.1.0 claims (skillwright upkeep, promptwright Entry — Model, brandwright Entry — Apply, agentwright refresh) partition cleanly — verified per sharp pair against on-disk text: row 7 (evalwright claims suite-authoring for existing targets; skillwright only ships suites with builds), row 11 (skillwright's explicit niche clause vs lorewright's no-skill verdict framing), row 12 (reciprocal promptwright↔tokenwright boundary sentences intact), row 10 (agentwright's security-harness partition line intact), and the Model claim (promptwright owns run-target picks incl. live tasks; lorewright owns sourced product comparisons — the one boundary worth watching in real usage; eval pair #25 vs #16 covers it). Per-skill trigger evals (6A) cover the new entries individually; this set test confirms no new overlap. *(Original 2026-07-14 run: same 12/12 result against the 1.0.0 descriptions.)*

| # | Realistic request | Routes to |
|---|---|---|
| 1 | "Write a system prompt for my research agent" | promptwright |
| 2 | "Score this SKILL.md against best practices" | skillwright |
| 3 | "Rewrite this Slack update for the exec channel" | commwright |
| 4 | "Add guardrails and a kill switch to my nightly scan agent" | agentwright |
| 5 | "Which task app should I commit to — verdict with sources" | lorewright |
| 6 | "Check the repo for off-palette colors and stale taglines" | brandwright |
| 7 | "Write trigger evals for the commwright skill" | evalwright |
| 8 | "My CLAUDE.md is 6k tokens — slim it, same behavior" | tokenwright |
| 9 | "Build an MCP server for my calendar API" | **outside** → mcp-builder (first-party) |
| 10 | "Review this PR for injection vulnerabilities" | **outside** → engineering plugins / security harness |
| 11 | "Is there a real niche for a meal-prep skill?" | skillwright (lorewright defers skills to it by name) |
| 12 | "This prompt works — just make it cheaper to run" | tokenwright (promptwright reciprocates the boundary) |

---

## Session log

- 2026-07-14 — Pack self-audit session: baseline research refresh, partition
  re-run, combine analysis, capability map, F1+F2 applied, release kit assembled.
- 2026-07-23 — Forge Run 3 approved; full 1.1.0 plan written into this baton;
  Phase 0 (repo hygiene) executed (homepage, doc removals, version
  reconciliation, RUNBOOK swap correction).
- 2026-07-23 — **Phase 1 (brand decoupling) executed** in sandbox, verified
  `build.py --check` clean (count 8=8=8). brandwright = single home of brand+voice;
  skillwright + commwright build neutral by default; registry split to
  `pack-registry.md`; 3 skills → 1.1.0. Delivered as repo-sync bundle + git
  commands (3 `git rm` deletions). Doc cleanup for READMEs/SOURCES/evals deferred
  to Phase 2/6 (listed under Phase 1). Next: Phase 2 uniformity layer.
