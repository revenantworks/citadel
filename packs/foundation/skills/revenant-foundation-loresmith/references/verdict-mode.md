# Verdict Mode — Criteria → Verification → One Recommendation

Loaded on every verdict run. Mutually exclusive with playbook-mode.md.

## 1. Criteria intake

Mine the request and conversation for: the decision, the candidates (or "find them"), the constraints (budget, platform, deadline), and the stakes. Infer weights from context and state them as Assumed; ask one batch only when two readings produce different verdicts. Candidate discovery, when needed, checks the domain's registries and directories before generic search.

## 2. Live-source verification

Per candidate, per criterion: check the primary source this run — vendor docs, official listings, standards text, first-party changelogs. Date each check. Tag each cell:

| Tag | Means | Earned by |
|---|---|---|
| [documented] | Independently checkable fact | Primary source read this run |
| [vendor-reported] | The seller says so | Vendor's own page/spec |
| [estimate] | Derived | Arithmetic shown from tagged inputs |
| [unverified] | Found, not confirmed | Secondary source only, or check failed |

Repetition never upgrades a tag: ten aggregators citing one vendor page = one [vendor-reported].

## 3. Comparison

One table — candidates × criteria, every cell tagged, a Sources row with dates. Disqualified candidates stay visible with the disqualifying cell bolded; silent drops are defects.

## 4. The recommendation

One pick, two-line why, and the **flip condition** — the single fact or weighting change that would move the verdict. Ties: name the breaking criterion, recommend under the likeliest weighting, and say so. Close with a confidence line derived from the tag mix (a verdict resting on [vendor-reported] cells says it).
