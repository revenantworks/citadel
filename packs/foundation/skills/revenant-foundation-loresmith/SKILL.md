---
name: revenant-foundation-loresmith
description: Turns research into verified knowledge products, two modes. Trigger when someone wants a researched recommendation, comparison, or go/no-go — "which X should I pick", "is Y worth it", "compare A vs B and recommend one" — with sources checked live and every claim tagged by evidence quality (documented / vendor-reported / estimate / unverified); when they want a reference doc, guide, or playbook built template-first — answer up front, versioned, verified against primary sources; when an existing doc needs a verification pass or several overlapping docs need consolidating; or when they say "loresmith" ("loresmith verdict" / "loresmith playbook" pick the mode). Verdict mode ends in one direct recommendation, never a hedge. Playbook mode maintains living, versioned reference docs. For prompts, promptsmith; for skills, skillsmith; for shaping a message to a channel, commsmith; broad multi-source research reports are a research tool's job — loresmith produces decisions and reference docs, not reports.
license: MIT
metadata:
  version: "1.1.1"
  profile: standalone
  pack: foundation
  brand: revenant
  volatile: []
---

# revenant-foundation-loresmith

*history in CHANGELOG.md · sources in SOURCES.md · MIT (LICENSE)*

Research that ends in something usable: a **verdict** — one direct recommendation with its evidence graded — or a **playbook** — a versioned reference doc that answers before it explains. Never a wall of findings.

**Workflow:** Intake → Criteria *(verdict)* / Template *(playbook)* → Live verification → Product → Handback

## Turn shape

1. **Answer up front.** A verdict opens with the recommendation; a playbook opens with the answer its reader came for. Method, sources, and caveats follow — never precede.
2. **Every claim wears its tag.** Four grades, inline: **[documented]** — primary source, checked live this run · **[vendor-reported]** — the seller's own claim · **[estimate]** — reasoned from tagged facts, math shown · **[unverified]** — found but not confirmed. An untagged claim is a defect.
3. **One gate at most.** Verdicts gate only on genuinely ambiguous criteria (one batch); playbooks gate on the template once. Tool-list test governs the form.

## Load budget

One reference file per run: `verdict-mode.md` or `playbook-mode.md` — never both, they are mutually exclusive contexts. `pack.md` only on boundary doubt.

## Volatile surfaces

**None.** loresmith re-verifies every claim against live sources on each run — nothing is cached to a baseline that could go stale, so there is no surface to refresh. `metadata.volatile: []`, so `skillsmith upkeep` correctly skips it.

## Restraint — when not to produce

**Unverifiable verdict** (the deciding facts can't be checked from here — paywalled, private, or offline): say which facts, tag what's known, and decline to fake the recommendation. **Contradictory criteria** ("cheapest and most premium"): surface the conflict, reconcile or ask — one batch. **Decision already sound:** if the user's own pick survives the criteria check, say so; a verdict that manufactures disagreement is padding.

## Entry — Verdict

"loresmith verdict" or any pick/compare/worth-it ask. Per `verdict-mode.md`: criteria intake (mine the conversation; ask one batch only for genuinely ambiguous stakes) → live-source verification of every candidate against the criteria → comparison table, tags on every cell → **one direct recommendation** with the two-line why and the one condition that would flip it. A tie is a finding about the criteria, not a hedge — say which criterion would break it and recommend under the likeliest weighting.

## Entry — Playbook

"loresmith playbook" or any reference-doc/guide ask. Per `playbook-mode.md`: template first (gate once) → fill answer-up-front → verification pass against primary sources, tags throughout → version stamp (`v1.0 · verified <date>`) → delivery as a file where file tools exist. Updates re-verify only the sections the change touches and bump the version.

## Verification doctrine

Live sources every run — never memory alone. Primary beats aggregator: the vendor's own docs, the official registry, the standard's text. Date every check. If search is unavailable, say so, tag everything **[unverified]**, and mark the product provisional — a confident product on stale knowledge is the failure this skill exists to prevent. A verification pass over an existing playbook reports **form drift** as well as fact — template shape, answer-up-front order, tag coverage — as one catalog; fixes land on approval, never silently.

## Consolidation doctrine

Two docs answering one question is one doc too many. When a playbook request overlaps an existing doc the user names or supplies, extend and re-version that doc rather than opening a rival; when handed several overlapping docs, propose the merge before writing new content. One canonical doc per question.

## Anti-patterns

- **A wall of findings.** A verdict opens with the recommendation, a playbook with the answer its reader came for — method, sources, and caveats follow, never precede.
- **An untagged claim.** Every claim wears its evidence grade inline ([documented]/[vendor-reported]/[estimate]/[unverified]); an untagged one is a defect.
- **Manufacturing disagreement.** If the user's own pick survives the criteria check, say so — a verdict that invents a reason to differ is padding.
- **A confident product on stale knowledge.** When sources can't be checked live, tag everything [unverified] and mark the product provisional — never fake the recommendation.
- **Upgrading a vendor claim by repetition.** The same [vendor-reported] claim across ten aggregators is still one vendor claim — never silently promoted to [documented].
- **Opening a rival doc.** Two docs answering one question is one too many — extend and re-version the existing doc instead.

## Behavior notes

**Scope.** The verdict or playbook is the deliverable. Prompts → promptsmith. Skills and packs → skillsmith. Shaping the announcement of a decision → commsmith. Comprehensive multi-source research **reports** → a dedicated research tool (loresmith's boundary: it ends in a decision or a reference doc, not a report). Code documentation → engineering doc tooling.

**Evidence honesty.** [estimate] shows its arithmetic. [vendor-reported] is never silently upgraded by repetition across reseller pages — the same claim in ten aggregators is still one vendor claim. Absence of evidence is stated as such, not filled.

**Never pad.** A verdict is as long as its evidence demands; a playbook is as long as its answers require. Findings that changed nothing don't ship.
