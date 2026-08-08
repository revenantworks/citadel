# foundation — pack-spec baton

> Retro-fitted 2026-07-14 (self-audit finding P2-2): the roster predates the
> pack-spec doctrine, so this baton was reconstructed from the shipped pack and
> the 2026-07-14 self-audit rather than written at the original roster gate.
> From here it updates after every member ship or roster decision. When memory
> of a conversation and this spec disagree, trust the spec.

**Pack:** foundation · **Profile:** standalone · **Brand:** revenantworks ·
**Stamped:** 2026-08-07 ·
**Current status:** **SHIPPED** — pack **2.0.0**, tag `foundation-v2.0.0`
(2026-08-07): the `revenant` → `revenantworks` migration (brand definition
v2.1.0). Breaking rename, content otherwise unchanged: marketplace
`revenant` → `revenantworks`, all nine members
`revenant-foundation-*` → `revenantworks-foundation-*` (directories,
frontmatter, evals, every cross-reference), brand token and `metadata.brand`
label moved, LICENSE now carries both founding names. No member version
bumps, no eval re-anchors owed. The platform has no marketplace-rename
mechanism (COLLISION.md C3/C4, supersession noted there): the owner
adjudicated execute-anyway, and the single-consumer estate migrates by local
remove-and-re-add — until that lands, `--parity` cannot see the old-name
install and skips. Root `CHANGELOG.md` carries the full account. Interim
releases between the stamp below and this one — **1.1.4** (parity widened),
**1.1.5** (lorewright 1.1.2, promptwright 1.2.0), **1.2.0**
(AUDIT-2026-08-05 apply pass; promptwright 1.3.0, 13 seams) — are in the
root CHANGELOG; this baton was not restamped for them, a recorded drift.

Prior shipped state — pack **1.1.3**, tag `foundation-v1.1.3`
(2026-08-01): a pack-wide prose pass — every member's own files plus the
root/pack-level docs rewritten for register (connector cleanup, cross-
referenced rule duplication), tokenwright's Preservation-contract list
gained a missing item, promptwright's model-snapshot footnotes renumbered.
No rule, gate, count, or entry point moved; see the root `CHANGELOG.md` for
the full member-by-member account. All nine members carry a version bump
(see Approved roster, below).

Preceded the same day by pack **1.1.2** (`foundation-v1.1.2`): every
frozen-record `evals/` file across the pack gained a header naming its
version numbers as predecessor-era, and `dist/` prunes superseded zips.
Delivery release, no capability change; rows, verdicts, dates, and counts in
those files are untouched.

Prior releases the same day: pack **1.1.1** (`foundation-v1.1.1`), the
install-parity fix delivering **skillwright 1.0.1** to the copies that load —
cut because the pack version is the plugin cache key, so a member patch alone
is undeliverable (`ledger.md`); and pack **1.1.0** (`foundation-v1.1.0`),
**promptwright 1.1.0** (Entry — Model gains plan grain: per-subtask target
tables, the living-table and standing-rule contracts), pack version bumped in
the same stroke per release-doctrine's Two clocks. Roster and seams unchanged
across all three (9 members, 12 seams).

Preceded by the 2026-07-31 wright baseline: all nine members baselined under
the wright motif and reset to **1.0.0** (pack, plugin manifest, marketplace
entry, members), content carried forward unchanged. Version references in the
history sections below are predecessor-era designations, frozen as written.
Full parity reached 2026-08-01 at the 1.0.0 baseline: release assets live
(nine zips), Claude Code plugin installed at 1.0.0, cold trigger baselines
re-measured on the wright listing (97/97, `ledger.md`), and all nine claude.ai
copies re-uploaded by the owner. **Parity since 1.1.0 is partial and since
2.0.0 is broken by design pending the local re-add**: release assets track
each release, the local Claude Code install still points at the retired
`revenant` marketplace name until the remove-and-re-add lands, and **all nine
claude.ai copies still serve their 1.0.0 bodies under the retired
`revenant-foundation-*` names — which now lack shipped doctrine, not just
prose** (see register ⑨). The prior shipped state before 1.0.0 was pack
**1.4.0** (roster 8 → 9).

**The 1.3.2 pass is CLOSED** (pre-rebaseline pass; the register's current state is below, past the history section) **— at the time, the register was empty but for the gated ⑦.** Every
routing/doctrine item the 1.3.1 executions and cold re-runs surfaced is closed at
the doctrine level in its owning member, one member per worker under the standalone
law: agentwright's **S1/S5 severity contradiction** (irreversible accumulation is the
sole retry-P0 trigger; the worked example is now consistent) and **row 19 → SHOULD**
(17/12); the **#8 brandwright↔skillwright circular seam** (brandwright claims the
identity-definition half, plus a CLAUDE.md compose bullet as the router-level gate);
commwright's **#35 unscoped `humanize`** (repo files excluded by name, both descriptions
now carry the boundary); skillwright's **#26** (`Every build ships trigger evals.`
restored). brandwright findings 2/3 + fixture 4(c) and evalwright findings 3/4/5/6 were
verified **already closed** and not re-touched. All patches — agentwright 1.2.2,
brandwright 1.1.9, commwright 1.2.6, skillwright 1.4.2 — no new capability. `build.py
--check` clean, 8 = 8 = 8, 9 seams.

**The 1.3.0 pass is CLOSED.** Deferral item ⑧'s security-scan half is built and split
across two members that share no files (agentwright `Entry — Security-scan` + its own
doctrine reference; skillwright `Entry — Audit` + a named security pass in `rubrics.md`);
its multi-host export half is **dropped, not deferred**. The pack's own security classes
were then run over the pack itself for the first time and **found two members failing
them** — lorewright at S-1 **P0** (reads live third-party pages every run, no
data-never-instructions statement anywhere in its package) and promptwright at S-1 **P1**
(all its untrusted-input doctrine aimed at the prompt it builds, none at the
instruction-shaped text it reads). Both closed, each with the case it should have arrived
with. The `skillwright ↔ agentwright` seam row is added and all eight manifests regenerated,
closing a boundary that shipped claimed from one side only — and recording that
`build.py`'s boundary-pair check validates declared rows and **cannot detect a missing
one**, so the clean `--check` that pass was never evidence of coverage. The always-on
router gained the two security rows and the compose bullet it was missing.

**Trigger debt DISCHARGED 2026-07-27, post-tag.** Both owed cold re-runs are executed and
ledgered, judged by independent judges holding only the eight-member listing and the query
list — no body, no expected column, no repo. **agentwright 28/29, one FAIL (row 19).
skillwright 40/43 clean, 0 FAIL, 3 AMBIGUOUS (#8, #26, #35).** 43/43 was never available
and is not claimed. Three findings came out of it, none a hotfix: **#26 broke exactly as
the 1.4.0 trade note predicted** — a blind judge named the removed `Every build ships
trigger evals.` string verbatim, so the cost of that trade is now measured rather than
reasoned · **#35 reopens the skillwright ↔ commwright seam** recorded closed 2026-07-25, on
commwright's `humanize` verb never being scoped to a message, which is commwright's fix and
not skillwright's · **#8 exposes a circular pair** — brandwright and skillwright's reciprocal
boundary sentences point at each other, individually correct and jointly circular, which
no single-member audit can see. **The 1.4.0 security clause held**: all six new skillwright
rows and all three agentwright security rows resolved cleanly, #42 against #38 included, so
the `injection` collision the new seam row was written for does not misroute. Row 19 fails
on a restraint expectation no listing can test and carries a recommendation to convert it
to a SHOULD; not applied, the expectation is owner-owned.

**Assertion debt DISCHARGED 2026-07-27, at pack 1.3.1.** Every case added across 1.3.0 —
agentwright Cases 17-20, skillwright Cases 38-40, lorewright Case 23, promptwright Case 36 —
was **executed against released text**, one member per worker under the standalone law:
**9 executed / 9 passed / 0 failed / 0 not-run**. lorewright's S-1 P0 and promptwright's
1.2.5 input-boundary paragraph are now closed **and demonstrated**, not only authored.
The executed assertion baselines now read: agentwright 17-20 pass at v1.2.1 · skillwright
40/40 at v1.4.x · lorewright Case 23 at v1.1.6 · promptwright Case 36 at v1.2.6. One
**non-failing doctrine gap** came out of it, logged not fixed: agentwright's S1 lists
`send` as destructive while S5's worked example scores an unbounded send-retry P1 against
a rule reading P0 — Case 17 passes under either, so it is a gated severity-policy call,
not a hotfix. **That gap was closed at 1.3.2** (agentwright 1.2.2): irreversible
accumulation is the sole retry-P0 trigger, the worked example is now consistent, and S1↔S5
cross-reference so they can't drift again.
**The two P2 budget headrooms are decided, not left riding:** the ceilings hold as-is —
skillwright 7800 (body ≈43 under) and promptwright 8500 (≈96 under) — and the standing rule
governs the next body edit: trim to fit or state a content reason for a raise in the
member's CHANGELOG. No open action; the 1.3.2 edits were description-only (skillwright) or
in other members, so neither thin body moved.

Prior pass — the 1.2.0 pass is **CLOSED**: register items ①②③④⑤ plus both deferred
1.2.1 closures shipped, all eight assertion suites were executed for the first time,
the pack's last open routing seam is closed, and `build.py --check` emits zero
warnings. Item ⑥ (spec.md split) is **DONE 2026-07-25** — this baton is now split into
`spec.md` (live), `ledger.md`, and `decisions.md`; ⑦/⑧ remained owner calls at the time
(⑧ shipped 2026-07-27, ⑦ resolved 2026-08-07 — see the register above).
**Debt cleared 2026-07-25 (week close-out).** The owed re-run of all eight assertion
suites is **paid** — executed against released text and written into each
`evals/RESULTS.md` (178/178 executed-and-passed · 0 FAIL · 2 NOT RUN; see `ledger.md`
→ *the ledgered re-run*). The eight eval-suite quality findings that re-run surfaced are
now **fixed** (tokenwright's cache floor at `281649c`; the other seven — agentwright,
brandwright, commwright, evalwright, lorewright, promptwright, skillwright — one each,
in-place at current versions, `build.py --check` clean). tokenwright's Case 13 T2 —
the pack's last open FAIL — was closed at `50a05f7` (2026-07-25/26). skillwright's owed
37-query cold trigger re-run is discharged (37/37, all watch rows held). No member version bumped —
each fix is a suite or doctrine correction against unchanged behavior, so every ledger's
version still describes the code under test.
Prior release: the 2026-07-24 hygiene release, predecessor-era (next
upkeep due ~2026-09-21 via the Cowork task in `upkeep-task.md`).

**Deferral register (opens the 1.2.0 pass — touch each member once when it runs):**
① machine-readable routing-seam table generated into each member's `references/pack.md`
via the registry pipeline + a build.py boundary-pair check · ② description regime
(600–800 chars, headroom rule, `promptwright model` token, boundary sentences only where
evals prove false fires) with the new build.py warns as instrumentation and the
evals/RESULTS.md baselines as before/after — **✅ DONE 2026-07-24, see the
1.2.0-pass section in `ledger.md`** · ③ anti-patterns dedup + one-statement-
per-law + body↔reference single-home; footprint warn→fail flip · ④ promptwright
framework-name menu (CO-STAR/RISEN) + fast path + hostile-interpreter pass; commwright
Humanize entry · ⑤ skillwright release-doctrine reference (this release is its worked
example) · ⑥ spec.md split (spec/ledger/decisions) — **✅ DONE 2026-07-25** ·
⑦ pack-registry relocation out of skillwright when pack #2 becomes real (owner call) —
**gate FIRED 2026-08-06** (the vault pack shipped: two members, `-picker` motif, canonical
repo `longshot`; registry row added 2026-08-07, renamed to `ossuary` the same day), and
**✅ RESOLVED 2026-08-07 — the other way**. The owner call landed as *the skills move to the
citadel, not the registry out of skillwright*: `revenantworks-ossuary-linecaller` and
`revenantworks-ossuary-cardcaller` were relocated into `packs/ossuary/skills/` with a pack
`plugin.json` at 1.0.0, a marketplace catalog entry, a pack router, and full registry
tables (members, budgets, seams), so both packs now derive from one registry inside one
repo. The registry therefore stays in skillwright, and the reason it was ever a question
is gone: the item existed because a second pack living in another repo would have made
skillwright's `references/` a cross-repo source of truth. Nothing is cross-repo now.
`MickMacPW/longshot` keeps a declared downstream mirror at `skills/` — its cloud routine
clones only that repo — recorded as a mirror in its `CLAUDE.md` file map, source of truth
named, must-not-drift stated. What the resolution does **not** claim: a registry file at
270+ lines serving nine members plus two is still shipped inside one member's zip, so the
size argument survives its trigger. If that becomes a real cost it opens as a *token*
item measured by tokenwright, not as this structural one ·
⑧ security-scan doctrine — **✅ DONE 2026-07-27, shipped at pack 1.3.0** (agentwright
`Entry — Security-scan` with its own doctrine reference; skillwright's `Entry — Audit`
gains its own security pass; each self-contained per the standalone profile, partitioned
by reciprocal boundary sentences **and now by the `skillwright ↔ agentwright` seam row**,
which the build pass deliberately skipped and the release pass added). Item ⑧'s
**multi-host export half is dropped** — see the 2026-07-27 line in `decisions.md`.

**⑨ claude.ai re-uploads owed — all nine members, and the risk statement has
CHANGED.** Opened at pack 1.1.0 (2026-08-01) for promptwright alone; widened
to the whole roster at pack 1.1.3; **re-scoped 2026-08-07 at 2.0.0**. The
claude.ai custom-skill copies are personal-account uploads that only move on
delete-and-re-upload (release-doctrine — Install parity), and all nine still
serve their **1.0.0 bodies under the retired `revenant-foundation-*` names**.
The old "out of date, not wrong" framing no longer holds: since 1.0.0 the
pack has shipped **doctrine, not just prose** — promptwright's tier-routing
role overrides (1.2.0) and the user-named-target override (1.3.0),
lorewright's Selection/Decision doctrine (1.1.x), tokenwright's rigwright
boundary clause (1.1.0) — so a claude.ai copy now **lacks shipped doctrine
and misroutes against the current seam table**, and after 2.0.0 it also
carries a retired name. The refresh is delete-and-re-upload of every member
under its `revenantworks-foundation-*` name from the 2.0.0 release zips.
Still owed to the owner's hand; recorded here rather than claimed done.

**The register is now empty except ⑨.** ⑦ (pack-registry relocation out of skillwright) was
the last structural item; its gate fired 2026-08-06 when the second pack shipped, and it
**closed 2026-08-07 by owner decision resolving it the other way** — the pack moved into
this repo instead of the registry moving out of skillwright, which dissolved the cross-repo
source-of-truth problem the item was opened against. Full account in the register entry
above. Structurally this is the first pass where count integrity spans two packs, and the
second pack immediately found a latent parser bug the first could not expose: `pack_lines`
read conformance checks from the *Profile* cell, never matched, and fell through to a
whole-document search that returns the **first** pack's line — so ossuary's generated
manifest was stamped with foundation's checks and adoption date. Fixed in `tools/build.py`
(`registry_pack_notes`, per-pack notes, no whole-document fallback) with two unit tests,
one on the fixture and one on the live registry. Recorded because it is the class this
repo keeps re-learning: a gate that passes on N=1 is not evidence, and `--check` was clean
throughout. The assertion side that once
opened the next pass (agentwright 17-20, skillwright 38-40, lorewright 23, promptwright 36) is
**discharged at 1.3.1** (9/9), and the routing findings behind it are **closed at 1.3.2**.

**All three routing findings are CLOSED at 1.3.2**, each in its owning member and none a
hotfix: agentwright **row 19 → SHOULD** (restraint asserted in Case 11, not a routing
property) · skillwright **#26** (`Every build ships trigger evals.` restored, −37 traded
from decoration no row rides) · commwright's **unscoped `humanize`** (#35 — repo files now
excluded by name in the description; the first item closed in a member other than the one
whose suite found it). The **#8** brandwright↔skillwright circularity got the gate of its own
it needed: brandwright's description now claims the identity-definition half, and the
always-on router carries a `Rebranding a whole skill set is a two-step handoff` compose
bullet so the split holds on the surface that loads first, not only at description level.

---

## Approved roster

*Re-baselined 2026-07-31: all nine members reset to 1.0.0 under the wright
motif, content carried forward; earlier designations frozen as written.*

| Member | Job (one line) | Status | Version |
|---|---|---|---|
| `revenantworks-foundation-skillwright` | Builds, audits, and ports Agent Skills and packs (neutral by default) | SHIPPED | 1.0.6 |
| `revenantworks-foundation-promptwright` | Builds, scores, and hardens prompts with model-tier routing | SHIPPED | 1.3.0 |
| `revenantworks-foundation-commwright` | Shapes messages per channel and audience; neutral-voice default; audits drift | SHIPPED | 1.0.2 |
| `revenantworks-foundation-agentwright` | Designs and audits autonomous agent systems | SHIPPED | 1.1.0 |
| `revenantworks-foundation-lorewright` | Research-verified verdicts and playbook reference docs | SHIPPED | 1.1.2 |
| `revenantworks-foundation-brandwright` | Single home of brand + voice; defines, applies on invoke, audits for drift, exports payloads + HTML guide card | SHIPPED | 1.0.2 |
| `revenantworks-foundation-evalwright` | Authors and audits eval suites — build-time, zero runtime deps | SHIPPED | 1.0.2 |
| `revenantworks-foundation-tokenwright` | Measures, budgets, and slims the token footprint of LLM-facing artifacts | SHIPPED | 1.1.0 |
| `revenantworks-foundation-rigwright` | Builds the standing configuration Claude reads before work | SHIPPED | 1.0.2 |

---

## Companion files

The baton was split 2026-07-25 (deferral-register item ⑥ — done):
- **`ledger.md`** — the build passes (Forge Run 3 → 1.1.0, the 1.2.0 pass) and every
  eval-suite execution register, plus the trigger-partition table and the session log.
- **`decisions.md`** — the decisions log, the adopt register, and recorded-not-built candidates.

This file (`spec.md`) stays the live baton: identity, current status, the deferral register,
and the approved roster. When memory and the spec disagree, trust the spec.

