# Verdict Mode — Criteria → Verification → One Recommendation

Loaded on every verdict run. Mutually exclusive with playbook-mode.md.

## 1. Criteria intake

Mine the request and conversation for: the decision, the candidates (or "find them"), the constraints (budget, platform, deadline), and the stakes. Infer weights from context and state them as Assumed; ask one batch only when two readings produce different verdicts. Candidate discovery, when needed, checks the domain's registries and directories before generic search.

## 2. Live-source verification

Per candidate, per criterion: check the primary source this run — vendor docs, official listings, standards text, first-party changelogs. Date each check. Tag each cell:

| Tag | Cells that typically land here |
|---|---|
| [documented] | list price, plan quota, license term, supported platform, EOL date, standards text, official registry entry, an independent lab's own measurement — not a page repeating the vendor's |
| [vendor-reported] | "up to 30 h", "99.99% uptime", a vendor benchmark, any superlative — even read straight off the vendor's own spec page |
| [estimate] | arithmetic shown from tagged inputs |
| [unverified] | secondary source only, or check failed |

What each grade *means* lives in one place only — the body's Turn shape 2, loaded on every run of this file. This table adds examples, never a second definition: deliberately no Means column, so there is no wording here that can drift from the body's. When a vendor page is the source and two grades look live, the body's kind-of-fact test settles it; this table never overrides it, and a product's own tag legend copies the body's four glosses, not this column.

## 3. Comparison

One table — candidates × criteria, every cell tagged, a Sources row with dates. Disqualified candidates stay visible with the disqualifying cell bolded; silent drops are defects. A primary source that was attempted and could not be read is listed there too, with the reason and the date, alongside the reads that succeeded — the body's unreadable-source rule governs the grade it produces.

## 4. The recommendation

One pick, two-line why, and the **flip condition** — the single fact or weighting change that would move the verdict. Ties: name the breaking criterion, recommend under the likeliest weighting, and say so. Close with a confidence line derived from the tag mix **of the deciding cells** — the ones the pick and the flip condition actually rest on, not the whole table's average. If any deciding cell is [vendor-reported], [estimate] or [unverified], the line names that cell and does not claim high confidence (a line like "moderate, not high" is compliant; "high" or any stronger word such as "excellent" is not).
