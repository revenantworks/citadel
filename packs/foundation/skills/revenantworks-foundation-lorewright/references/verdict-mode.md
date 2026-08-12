# Verdict Mode — Criteria → Verification → One Recommendation

Loaded on every verdict run. Mutually exclusive with playbook-mode.md.

## Contents

- 0. Verdict class — decide this first
- 1. Criteria intake
- 2. Live-source verification
- 3. Comparison
- 4a. The recommendation — Selection class
- 4b. The recommendation — Decision class

## 0. Verdict class — decide this first

Two shapes, one mode. The class sets the recommendation form in §4 and nothing else;
criteria intake, verification, and tagging are identical either way.

| Class | What it is | Recommendation form |
|---|---|---|
| **Selection** | Picking a thing to acquire from a field of comparable options — a product, a plan, a vendor, a tier | Four slots (§4a) |
| **Decision** | A go/no-go, an A-vs-B with no field to shop, a worth-it check on something already in hand | One pick (§4b) |

"Which blender should I buy" is Selection. "Should we standardize on Postgres" is
Decision. When both readings survive, ask in the §1 batch — do not ship both forms.

## 1. Criteria intake

Mine the request and conversation for: the decision, the candidates (or "find them"),
the constraints (budget, platform, deadline), and the stakes. Infer weights from context
and state them as Assumed; ask one batch only when two readings produce different
verdicts. Candidate discovery, when needed, checks the domain's registries and
directories before generic search.

**The must-have question — Selection class, in the same batch.** A Selection verdict
gates once before verification, and that batch carries a features question alongside the
budget/scope ones: *which of these are must-haves?* Ask it as multi-select and **seed it
with 4–6 concrete, domain-typical examples** — a bare "what features matter?" makes the
user do the recall work and reliably surfaces the deciding constraint three turns too
late, after a table has already been built against the wrong criteria.

Draw the examples from the domain's real differentiators, not generic virtues:

| Domain | Seed examples |
|---|---|
| Blenders / kitchen | personal to-go cups · food processor attachment · handles ice & frozen fruit · dishwasher-safe removable blade · quiet operation |
| Dehumidifiers | built-in pump vs gravity drain · continuous drain hose · smart/app control · Energy Star · quiet for bedroom |
| Laptops | battery life · discrete GPU · port selection · screen color accuracy · repairability · weight |
| Hosting / SaaS | SSO · data residency · SLA tier · API rate limits · seat vs usage pricing · export/portability |
| Cameras | in-body stabilization · weather sealing · lens ecosystem · video specs · size/weight |

No domain in the table is a licence to skip the question — derive 4–6 for whatever the
domain is. **Where an option-presenting tool caps the choices below that, the cap governs
the tappable list and the remaining examples go in the question's framing line** — the
requirement is that the user sees 4–6 concrete options somewhere in the gate, not that a
particular widget holds them all.

The user's answer becomes a **hard filter**, not a weighting: a candidate missing a stated
must-have is disqualified in §3 with that cell bolded, never quietly ranked lower. The
gate stays **one batch** — the features question rides inside it, never as a second
round.

Skip the question only when the request already names the must-haves, or the field is
small enough that every candidate has every feature. Say which applies in one clause.

**Score only what was asked.** A criterion the user did not raise never costs a candidate
its place. Where a candidate is weak on an axis outside the stated set, that belongs in
the flaws line (§4a) or nowhere — not in the ranking. A verdict that quietly penalises a
product for lacking something its buyer does not want has invented a criterion.

## 2. Live-source verification

Per candidate, per criterion: check the primary source this run — vendor docs, official
listings, standards text, first-party changelogs. Date each check. Tag each cell:

| Tag | Cells that typically land here |
|---|---|
| [documented] | list price, plan quota, license term, supported platform, EOL date, standards text, official registry entry, an independent lab's own measurement — not a page repeating the vendor's |
| [vendor-reported] | "up to 30 h", "99.99% uptime", a vendor benchmark, any superlative — even read straight off the vendor's own spec page |
| [estimate] | arithmetic shown from tagged inputs |
| [unverified] | secondary source only, or check failed |

What each grade *means* lives in one place only — the body's Turn shape 2, loaded on
every run of this file. This table adds examples, never a second definition: deliberately
no Means column, so there is no wording here that can drift from the body's. When a
vendor page is the source and two grades look live, the body's kind-of-fact test settles
it; this table never overrides it, and a product's own tag legend copies the body's four
glosses, not this column.

**Independent evidence first — search order, not just tag order.** The tag ladder grades
what was found; this rule governs what to look for. For any criterion a vendor could
measure about itself — performance, capacity, durability, noise, efficiency — check for an
**independent measurement before settling for the vendor's**: standards bodies and
regulators, certification programs, a testing lab's own published result, an independent
review outlet's measured figure. Only after that search comes up empty does the vendor's
own number become the best available cell.

**State the attempt, not just the result.** The search is only auditable if the output
records it: name the independent source used, or say that one was looked for and not
found. A verdict whose cells are correctly tagged but which never shows whether an
independent measurement was sought is indistinguishable from one that never looked.

**Disclose the absence.** Where no independent testing exists for a candidate or a whole
category, say so once, plainly: *"no independent test data found for any candidate on this
axis — every performance figure below is the manufacturer's own."* An entire comparison
resting on vendor self-measurement is a real and common state; the failure is letting the
reader assume otherwise. If that axis is the deciding one, the confidence line says so.

## 3. Comparison

One table — candidates × criteria, every cell tagged, a Sources row with dates.
Disqualified candidates stay visible with the disqualifying cell bolded; silent drops are
defects. A primary source that was attempted and could not be read is listed there too,
with the reason and the date — the body's unreadable-source rule governs the grade it
produces.

**Coverage disclosure — Selection class, immediately after the table.** State the field
that was actually swept, in three short lines. Without it the user cannot tell a
market-wide scan from four vendors that happened to rank well in one search.

- **Brands scanned:** every brand whose current line was checked live this run.
- **Excluded, with reason:** brand → one-clause reason — *over budget · discontinued ·
  no product in this category · missing a stated must-have · price unverifiable*.
  "No product in this category" is a real and useful finding: report it plainly rather
  than substituting the brand's nearest different product.
- **Not reached:** brands a complete sweep would cover that this run did not, and what
  it would take. Never imply completeness the search did not earn.

**Screened out is not the same as beaten.** Two different findings, two different
sentences. A candidate **screened out** failed a filter — budget, a must-have, availability
— and its disqualifying cell is bolded. A candidate that **qualified and lost** cleared
every filter and was beaten on a named axis; say which axis and by how much, in one
clause. Collapsing the second into the first tells the reader a real contender was never
in the running, which is false and costs them the option.

**Re-check on constraint change.** When the user moves a constraint mid-thread — raises a
budget, drops or adds a must-have — re-screen the **already-excluded** list against the
new constraint *before* searching for new candidates, restate the criteria set as it now
stands, and say what re-qualified. A candidate excluded on the old ceiling is the single
likeliest winner under the new one; searching fresh instead of re-screening is how a
previously-seen, now-qualifying option gets missed.

## 4a. The recommendation — Selection class

Four labelled slots, then flaws, flip condition, confidence, and one follow-up. **The Top
Pick is the recommendation; the other three are reference points, not a menu.** Frame them
that way — this mode ends in one answer, and a four-slot table that reads as "you choose"
is the hedge this skill exists to prevent.

| Slot | Rule |
|---|---|
| **Top pick** | Best against the user's stated criteria, must-haves included, within budget. Two-line why. The answer. |
| **Runner-up** | Next-best qualifier. One line on the single axis where it beats or loses to the pick — never a general re-description. |
| **Budget pick** | Cheapest option still meeting every must-have. Name what is given up versus the top pick, concretely. |
| **Top overall** | Best in the field ignoring budget, must-haves still met, ceiling stated. Give the delta in money and in capability so the user can price the upgrade. |

**Every slot names its buyer.** One clause per slot on *who it is for* — the use case that
makes it the right call, not its rank. *"Budget pick — for one person making a single
smoothie a day who will never batch."* A slot labelled only by position makes the reader
re-derive the fit the verdict already worked out.

**Collapse, never pad.** Slots merge when the field says so, and the merge is stated in
one clause: *"the top pick is also the cheapest qualifier — no separate budget pick"* ·
*"nothing above this ceiling beats it; top pick is top overall."* Four entries invented to
fill four rows is padding, and padding is a defect. A field with two qualifiers yields two
slots.

**Flaws, not dealbreakers.** After the slots, one short line naming the top pick's known
weakness — the thing a buyer will notice and that did *not* change the verdict — and why
it didn't. A pick presented without a downside reads as marketing, and the reader has no
way to tell a genuinely clean win from an unexamined one. Where the flaw sits on an axis
outside the stated criteria, it lives here rather than in the ranking (§1, score only what
was asked). If nothing qualifies, say the search found no notable flaw — never invent one
for symmetry.

**Purchase link — top pick only.** Give one link for the Top Pick, **Amazon preferred**;
the vendor's own product page where no retail listing was retrieved. Two hard rules:

- **Only a URL retrieved this run.** Links come from search or fetch results in this
  session. Never construct one from a remembered ASIN, SKU, or URL pattern — a fabricated
  product link is a wrong answer that looks authoritative.
- **Carry the volatility caveat** where price or seller varied across the run: say the
  observed range and tell the user to confirm before buying. Listings for one model
  routinely duplicate across sellers, bundles, and renewed units.

Link the other slots only if asked. One link keeps the pick unambiguous.

**Then the flip condition** — the single fact or weighting change that would move the
verdict — **and the confidence line**, derived from the tag mix **of the deciding cells**:
the ones the pick and the flip condition actually rest on, not the whole table's average.
If any deciding cell is [vendor-reported], [estimate] or [unverified], the line names that
cell and does not claim high confidence ("moderate, not high" is compliant; "high" or
anything stronger is not).

**Close with one drill-down offer.** A single question naming the sharpest real axis
between the slots — the one the table shows is genuinely close or genuinely uncertain, not
a generic "want more detail?". *"Want me to break down the pick vs the runner-up on
cleanup and noise?"* · *"Want me to chase the unverified price on the budget pick?"* One
offer, one axis, then stop.

## 4b. The recommendation — Decision class

One pick, two-line why, and the **flip condition**. Ties: name the breaking criterion,
recommend under the likeliest weighting, and say so. Close with the same confidence line
as 4a. No slots, no purchase link — there is nothing to shop. The flaws line and a single
drill-down offer both still apply where a real weakness or open axis exists.
