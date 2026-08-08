# Pack — ossuary *(standalone profile)*

> Advisory only — consulted on boundary doubt; initial routing stays at the name + description level. **Last stamped: 2026-08-08** (two-member roster + canonical repo; generated from the registry in skillwright's `pack-registry.md`).

| Member | Job | Route there when |
|---|---|---|
| `revenantworks-ossuary-linecaller` | Runs one pass of the Project Longshot daily NFL bet-card pipeline and writes the card | The deliverable is a card that does not exist yet — a pipeline run, in Claude Code, against the longshot repo |
| `revenantworks-ossuary-bonecaller` | Reads the card on claude.ai and answers back — shows it, explains its picks, reports bankroll and dashboard state, logs what was actually bet, captures coaching notes | The card already exists and the deliverable is understanding it, a status answer, or a write-back into the repo |

**Routing seams** — one row per boundary pair: what each side owns, and the signal that decides. Same advisory standing as the roster; a row reading *none — table only* is a seam the cold listing cannot decide, recorded here rather than claimed.

| Seam | Left owns | Right owns | Router keys on | Cold-listing signal |
|---|---|---|---|---|
| linecaller ↔ bonecaller | Producing the card — one pipeline pass in the longshot repo from Claude Code: sync, fetch, reconcile and postmortem tagging, preseason intel, build, driver enrichment, verify, commit | Consuming it and answering back on claude.ai — showing today's card as an Artifact, explaining picks in plain language, bankroll and dashboard state, logging what was actually placed, capturing coaching notes | Whether the card is being made or being read. No card for today and a run is wanted → linecaller; the card exists and the ask is to see it, understand it, or write something back against it → bonecaller. The surface corroborates and never decides: linecaller needs a clone and a shell, bonecaller needs only connector read access | both descriptions |

**ossuary seam notes:**

- **linecaller ↔ bonecaller** (declared 2026-08-07, under the pair's then-names linecaller ↔ cardcaller, with the pack's relocation into this repo — the pack shipped 2026-08-06 with no seam table at all, since it had no registry section to hold one): the boundary is carried on **cardcaller's side only**, which is why the signal reads *one description* rather than *both*. cardcaller's `description` states the exclusion outright — it never runs the daily pipeline, and it names the cloud routine as the owner — while linecaller's negative clause covers model-building, general sports chat, and work outside the repo, and says nothing about a card that already exists. The overlap is real and recorded rather than papered over: linecaller's trigger tokens include "daily bet card" and "today's bets" against cardcaller's "today's card", so a cold listing reading only linecaller's row has no clause telling it to defer. Same asymmetric shape foundation records for promptwright ↔ lorewright and rigwright ↔ tokenwright, and the same discipline applies — the close is one boundary clause in linecaller's `description`, and the cold re-judge that would prove it is **owed, not claimed**. Until then the practical guard is capability, not routing: cardcaller is a claude.ai upload with no shell and no clone, so a false fire degrades to "I cannot run that, the routine owns it" rather than to a wrong card. **Closed 2026-08-08 (linecaller 1.2.0):** linecaller's `description` gained the owed boundary clause — "not for reading an existing card and ledger/bankroll questions — the claude.ai companion revenantworks-ossuary-cardcaller owns those" — so the signal column above now reads *both descriptions*. The cold re-judge of both members' trigger suites was executed the same day and is recorded in each member's `evals/RESULTS.md`; the capability guard remains as defense in depth, no longer the only guard. **Renamed 2026-08-08 (ossuary 2.0.0):** the right member is now `revenantworks-ossuary-bonecaller` and linecaller's clause follows the new name (linecaller 1.3.0); both trigger suites were re-judged cold again with the renamed pair, results in each member's `evals/RESULTS.md`. The narrative above quotes the clause as first released, under the old name — frozen record.

**Pack conformance checks** (adopted 2026-08-07, scored on every member audit): **O-1 decision-support only** · **O-2 never fabricate a number**.

**Canonical repo:** `github.com/revenantworks/citadel` — pack source of truth for drift audits (registered in skillwright's `pack-registry.md`; subject to relocation — the registry row is authoritative).

**Capstone:** none, deliberately — a two-member pack whose members already compose end to end in production every day (the cloud routine runs linecaller at 13:00 UTC; bonecaller reads what it wrote), so an orchestration prompt would only re-describe a live system. Revisit if the pack takes a third member.

**Absence rule:** recommend an uninstalled sibling by name — never fail the task over it.
