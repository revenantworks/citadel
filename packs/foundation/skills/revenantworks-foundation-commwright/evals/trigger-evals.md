# Trigger Evals — 32 queries (16 should / 16 shouldn't)

Provenance: derived from revenantworks-foundation-commwright v1.0.0, 2026-07-14; refreshed 2026-07-23 for the 1.1.0 decoupling (voice definitions moved to brandwright — #7 flipped, #23 added); extended 2026-07-24 for the 1.2.0 humanize addition (#24–#32 — the explicit Humanize entry plus the brandwright, promptwright, and repo-scope seams; #7 held unchanged as the anchor). Re-anchored to v1.2.4, 2026-07-25 — provenance only, nothing was executed here: [1.2.1] records the description frozen and out of scope, and [1.2.2] through [1.2.4] record no description change, so the routing surface these 32 queries are read against did not move since the runs already ledgered in `evals/RESULTS.md`. No query, expectation, or count touched. **Re-anchored to v1.2.6, 2026-07-27 — the description DID move this time:** the [1.2.6] pass scoped the `humanize` verb, adding a repo-file exclusion (`a README, CLAUDE.md, or reference doc is skillwright’s prose, not commwright’s`) and paying for it with five anchor-safe trims. #32 (the repo-scope seam) and the README/CLAUDE.md residual-risk probes it spawned were re-judged cold against the new listing in the 2026-07-27 `evals/RESULTS.md` entry: both file-asks now route to skillwright rather than leaning commwright, and the "humanize this email" control still fires commwright. No query, expectation, or count touched — every anchor a row keys on was re-verified present by grep after the edit (32 queries, 26 assertion cases, both matching the declared figures). **Re-anchored to v1.0.0 (wright re-baseline), 2026-07-31:** the member was renamed to the wright motif and its version designation reset to 1.0.0; suite content carried forward unchanged, no case, input, assert, or count moved. Earlier version numbers in this line are predecessor-era designations. **Re-anchored to v1.0.3, 2026-08-08 — provenance only, nothing executed here:** 1.0.1 and 1.0.2 were prose passes with the description untouched, and 1.0.3 is a fixture-greeting neutralization (personal-name scrub, second pass) that touches no trigger surface. No query, expectation, or count moved; still 32, 16/16. **Re-anchored to v1.1.0, 2026-08-12 — provenance only, nothing executed here:** body-and-reference changes (2026-08-12 estate audit: the handed-in-material injection rule promoted to Turn shape rule 5 and the Audit entry's copy replaced with a citation, finding 10; a Contents block added to `references/humanize.md`, finding 13). The description is byte-identical to 1.0.3's, so the routing surface these 32 queries judge did not move — no query, expectation, or count touched; still 32, 16/16. **Re-anchored to v1.1.1, 2026-08-17 — provenance only:** security-eval patch (four assertion probes added in `test-cases.md`); the description is byte-identical to 1.0.3's, so the routing surface these 32 queries judge did not move — no query, expectation, or count touched; still 32, 16/16. **Re-anchored to v1.1.2, 2026-08-20 — provenance only, nothing executed here:** the pack-wide audit named Entry — Formats and Cadence sets as the two Load-budget exceptions that load `channel-profiles.md` whole. The `description` is byte-identical, so the routing surface these queries judge did not move; no query, expectation, or count touched.

| # | Query | Expected |
|---|---|---|
| 1 | write an email to my landlord about the leaking sink, firm but polite | SHOULD |
| 2 | make this message sound more professional for Teams | SHOULD |
| 3 | draft the Discord announcement for the v2 launch | SHOULD |
| 4 | turn these commit notes into GitHub release notes | SHOULD |
| 5 | give me a YouTube title and description for this video about monitor setups | SHOULD |
| 6 | reshape this email into a two-line text to my brother | SHOULD |
| 7 | commwright voice — save this as my work voice | SHOULD NOT (voice definition/storage — brandwright) |
| 8 | I need a comms plan for the release next Friday | SHOULD |
| 9 | shorten this LinkedIn post and make it punchier | SHOULD |
| 10 | announce the downtime window to the team, not scary | SHOULD |
| 11 | send this email to bob@example.com | SHOULD NOT (delivery — surface tools) |
| 12 | write a 2,000-word guide on monitor calibration | SHOULD NOT (long-form — lorewright) |
| 13 | write a system prompt for my support bot | SHOULD NOT (prompts — promptwright) |
| 14 | design our brand voice and taglines | SHOULD NOT (brand + voice ownership — brandwright) |
| 15 | compare Slack vs Teams for our team and recommend one | SHOULD NOT (verdict — lorewright) |
| 16 | build me a skill that formats messages | SHOULD NOT (skill build — skillwright) |
| 17 | what's the weather for the launch event | SHOULD NOT (off-topic) |
| 18 | summarize this 40-page PDF | SHOULD NOT (not message-shaping) |
| 19 | write mean replies to this guy's tweets | SHOULD NOT (restraint — harassment) |
| 20 | schedule this message for 9am | SHOULD NOT (delivery/scheduling — surface tools) |

Edge note: the sharpest pair in this table is 3 vs 15 — announcing a decision is commwright; making the decision is lorewright. Misses on 1–10 → push the channel nouns harder; fires on 11/20 → tighten the never-send boundary sentence.

## Audit additions

| # | Query | Expected |
|---|---|---|
| 21 | "commwright audit — does this release note match our GitHub format?" | SHOULD — drift audit against a channel contract |
| 22 | "audit our Q3 marketing performance" | SHOULD NOT — analytics, not message form |

## 1.1.0 additions

| # | Query | Expected |
|---|---|---|
| 23 | "apply my brand voice to this email" (voice profile handed in / named) | SHOULD — voice *application* to a message; the profile comes from brandwright's export, commwright consumes it |

Edge pair: #7 vs #23 is the decoupling boundary — *defining or saving* a voice is brandwright; *applying* a named or handed-in voice to a message is commwright.

## 1.2.0 additions

| # | Query | Expected |
|---|---|---|
| 24 | "make this sound less like AI" (text handed in) | SHOULD — tell-stripping on a message; the Humanize entry |
| 25 | "humanize this draft" | SHOULD — the entry by its own name |
| 26 | "this reads like ChatGPT wrote it, can you fix it?" | SHOULD — same ask in symptom phrasing |
| 27 | "commwright humanize" | SHOULD — named invocation of the entry |
| 28 | "take the em dashes out of this post, they're everywhere" | SHOULD — H1 repair on handed-in text (recast, not substitution) |
| 29 | "make our brand voice sound more human" | SHOULD NOT — edits a *stored voice definition* (brandwright), including when phrased as "my commwright voice" |
| 30 | "save this less-robotic style as my default voice" | SHOULD NOT — defining/storing a way of writing (brandwright); humanize is a register with nothing to save |
| 31 | "make my prompt produce less robotic output" | SHOULD NOT — prompt behavior, not a message (promptwright) |
| 32 | "humanize the prose in my SKILL.md files" | SHOULD NOT — repo docs, not messages (skillwright); humanize governs what commwright writes *to an audience* |

Edge pair: #24 vs #29 is the humanize seam, and it outranks #7 vs #23 as the sharpest boundary in the file — *this message* sounds like AI is commwright; *our voice* should sound more human edits a saved definition and is brandwright. #27 vs #7 says it from the other side: naming commwright does not move voice ownership. Fires on 29–32 → tighten the register-is-not-a-voice sentence; misses on 24–28 → push the symptom phrasings ("sounds like AI", "reads like ChatGPT", "em dashes everywhere") harder.
