# Trigger Evals — 22 queries (13 should / 9 shouldn't)

Read each cold against name + description only. Provenance: derived from revenant-foundation-brandsmith v1.0.0, 2026-07-14; refreshed 2026-07-23 for 1.1.0 — #12 flipped to SHOULD (Entry — Apply is brandsmith's own now).

| # | Query | Expected |
|---|---|---|
| 1 | "brandsmith build — here's my brand guide PDF" | SHOULD |
| 2 | "help me define a brand for my studio" | SHOULD |
| 3 | "brandsmith audit this repo for drift" | SHOULD |
| 4 | "check my skill pack for old handles and off-palette colors" | SHOULD |
| 5 | "is this doc on-brand?" | SHOULD |
| 6 | "export a voice profile for commsmith" | SHOULD |
| 7 | "consolidate these three style guides into one" | SHOULD |
| 8 | "our repos use three different naming schemes — standardize the convention" | SHOULD |
| 9 | "did the persona voice leak into any work docs?" | SHOULD — firewall audit |
| 10 | "brandsmith" | SHOULD — bare invocation |
| 11 | "make this email sound on-brand" | SHOULD NOT — commsmith applies voice to messages |
| 12 | "apply the brand to the skill you're building" | SHOULD — Entry — Apply brands a built skill or artifact on invoke |
| 13 | "design me a logo" | SHOULD NOT — asset production |
| 14 | "rebrand this whole skill set for work" | SHOULD NOT — skillsmith port |
| 15 | "write our brand story for the About page" | SHOULD NOT — content production |
| 16 | "which brand of monitor should I buy?" | SHOULD NOT — loresmith |
| 17 | "pick brand colors that convert better" | SHOULD NOT — marketing optimization |
| 18 | "audit this agent's guardrails" | SHOULD NOT — agentsmith |
| 19 | "trademark search for my company name" | SHOULD NOT — legal research |
| 20 | "make my slides look nicer" | SHOULD NOT — no brand standard invoked |

**Edge note.** Sharpest pairs: 5 vs 11 — "is this on-brand" (judge against the standard) routes here; "make it on-brand" for a *message* is commsmith consuming the exported voice. 11 vs 12 marks the decoupling boundary — voice on a message stays with commsmith; branding a built skill or artifact is Entry — Apply, here. Tuning rule: misses on 1–10/12 → push apply/audit/define triggers; fires on 11 or 13–20 → tighten the consumer boundary in the closing sentence.
| 21 | "give me an HTML brand guide card from my definition" | SHOULD — guide-card export |
| 22 | "add typography and logo usage rules to my brand definition" | SHOULD — build/rebuild covers the extended groups |
