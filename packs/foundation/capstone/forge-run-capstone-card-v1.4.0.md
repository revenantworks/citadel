FORGE RUN v1.4.0 — foundation capstone: ship one skill, end to end

TRIGGER + INPUTS
Run this when a new skill (or a major rework) should ship through the full
foundation pipeline. Inputs: {{skill_intent}} — one line on what the skill
does and for whom · {{pack}} — destination pack + profile (default
foundation / standalone) · {{constraints}} — optional. Fill at run time;
the VALIDATION RUN LADDER below defines the intent class for proof runs.

Precondition: the six active-leg smiths are installed (promptsmith,
skillsmith, commsmith, loresmith, agentsmith, tokensmith); brandsmith and
evalsmith are consulted inside Leg 4 rather than driven as their own legs —
except in RUN 3, where brandsmith takes Leg 0 and evalsmith's audit line
ships in <release>. Name any that are missing, recommend them by name, and
apply that leg's (or Leg 4's consult's) skip clause rather than failing
the run.

LEG 1 — promptsmith (standing)
promptsmith authors and maintains this prompt and any prompts the new skill
carries inside it. No action unless an inner prompt is needed; when one is,
build it per promptsmith's workflow and hand the finished text to Leg 4 as
<inner_prompts>…</inner_prompts>.

LEG 2 — loresmith · verdict mode
Niche research for {{skill_intent}}: check the registries and plugin
directories in skillsmith's baseline plus the domain's own incumbents; tag
every claim by evidence quality; end in a go / no-go with the flip
condition. HANDOFF → <verdict>go or no-go · incumbents · the distinct
angle · requirements the build must honor</verdict>.
ON NO-GO: stop the run and report the verdict — a clean no-go is a
successful Forge Run, not a failure.

LEG 3 — agentsmith (conditional)
If the skill is or contains an agent — acts on a schedule or trigger, or
touches external resources on its own — produce the ops spec: blast
radius, guardrail tiers, kill switches, protected resources, trust tiers.
HANDOFF → <ops_spec>…</ops_spec>.
SKIP CLAUSE: if nothing acts autonomously, state "Leg 3 skipped — no
agentic surface" and continue. Never skip silently.

LEG 4 — skillsmith · build (consults brandsmith + evalsmith)
Run the Build entry with the <verdict> requirements (plus <ops_spec> and
<inner_prompts> when present) as the intent: fresh research → design
catalog → one gate → build (**spec-clean neutral per the brand-carriage
law** — structural identity stamped from pack-registry.md; brand and voice
are applied only at need via `brandsmith apply`, never stored) → evals/
authored under evalsmith's doctrine when evalsmith is installed
(eval-authoring.md is the stated fallback — its absence never fails the
build) → self-audit
(lean-body + quiet-mode norms) → package .skill + full zip → model-matrix
probe list (balanced + fast tier minimum) → pack.md restamps and the
registry row. HANDOFF →
<release>package files · eval results · probe list</release>.
Close the leg with the canonical-repo reminder: push the archive; zips are
artifacts, the repo is the source of truth; CI gate runs on push.

LEG 5 — tokensmith
Budget pass over the pack's always-on surface using <release> from Leg 4,
then an Audit of the shipped member as the efficiency gate: score-only
findings (W-codes, recoverable estimate, LEAN/TRIMMABLE/BLOATED verdict) —
never a rewrite inside this run. A BLOATED verdict does not block the
release; it's reported alongside SHIPPED for a follow-up slim pass.
HANDOFF → <budget_sheet>tier sheet, set-level tokens-per-task</budget_sheet>
and <efficiency_verdict>LEAN|TRIMMABLE|BLOATED + findings</efficiency_verdict>.

LEG 6 — commsmith
Sanitize hygiene pass on everything public-bound, then the release set:
GitHub release notes from the CHANGELOG · per-channel announcements ·
a dated cadence (build-log → release-day → follow-up). Marketplace-publish
comms only on request.

OUTPUT CONTRACT
The installable .skill + versioned archive (pushed) · eval and CI results ·
release notes · the scheduled comms set · the verdict and ops spec on file ·
the token budget sheet and efficiency verdict. Close with three lines:
SHIPPED · MY CHECKLIST · NEXT RUN.

VALIDATION RUN LADDER
One-time proof runs. Each is a normal Forge Run with the stated intent
class and success test; the ladder proves the pipeline once and is
separate from the RE-RUN CONDITION below. Log each completion in place.

RUN 1 — gate proof (front half: precondition → Leg 2 gate → stop clause)
Intent class: disposable, thin-niche by design.
Success test: an honest Leg-2 verdict; a no-go stop is a valid completion.
STATUS: COMPLETE 2026-07-14 — timestamp-conversion intent, no-go at
Leg 2, verdict memo on file. The gate gates.

RUN 2 — ship proof (back half: Legs 3–6 through the full output contract)
Intent class: go-viable and real — pull from the recorded candidates in
foundation-spec.md (contextsmith, runsmith) or any roadmap-real need.
Leg 2 still adjudicates honestly: a no-go is recorded and the next
candidate re-enters; pre-screening the verdict would defeat Run 1's proof.
Success test: completes only when a package ships — the .skill + pushed
archive, eval results, budget sheet, efficiency verdict, and comms set
all land. No brand dependency; may run before or parallel to Phase 2.
STATUS: PENDING

RUN 3 — full-set proof (all eight members active in one run)
For this run only, the two consults become visible checkpoints:
· LEG 0 (Run 3 only) — brandsmith: verify the locally configured
  brand definition is current before anything builds; refresh if stale.
  HANDOFF → <brand_check>definition version · verified date</brand_check>.
· LEG 4 ADDENDUM (Run 3 only) — evalsmith authors the suite AND issues
  its own audit line on it; the audit score ships inside <release>.
Historical predicate note: the original v1.3.0 predicate required shipping
"under the registered brand, not neutral" — that line predates the
2026-07-23 brand-carriage law, under which every ship is neutral and
branded artifacts are produced at need, never stored. Leg 0's definition
check is the law-era equivalent.
STATUS: COMPLETE 2026-07-23 — credited per the registry capstone line and
spec.md Phase 7: the Forge Run 3 / 1.1.0 pack rebuild itself was the live
run — all eight doctrines exercised in anger on a real full-pack ship; no
separate demo theater. (Recorded in pack-registry.md's capstone line;
build.py propagated it to all 8 references/pack.md manifests.)

RE-RUN CONDITION
Re-run after any foundation member's major version bump. Adding a new pack
member updates this card's roster only — it does not itself trigger a
re-run. Ladder runs are proof work, not re-run triggers. v1.3.0 changes no
leg machinery (additive ladder only), so Run 1 retains this card's
live-run credit against the OD12 release bar — recorded as OD13, ratify or
flip. Run log: brandsmith 2026-07-13 · Run 1 complete 2026-07-14 (v1.2.1
legs, unchanged here) · Roster reconfirmed 2026-07-14 (pack self-audit —
no change) · Run 3 credited 2026-07-23 (the 1.1.0 rebuild as the live run;
registry capstone line). v1.4.0 (2026-07-24, foundation-v1.1.1): brand-
carriage-law alignment — brand-config references removed, Leg 4 builds
neutral, Run-3 status reconciled to the registry; the stored branded HTML
twin deleted (a stored branded artifact violates the law — regenerate at
need via `brandsmith apply`). No leg machinery changed; Run 2 remains the
open ladder item.
