# Trigger Evals — 23 queries (11 should / 12 shouldn't)

Provenance: derived from revenant-foundation-commsmith v1.0.0, 2026-07-14; refreshed 2026-07-23 for the 1.1.0 decoupling (voice definitions moved to brandsmith — #7 flipped, #23 added).

| # | Query | Expected |
|---|---|---|
| 1 | write an email to my landlord about the leaking sink, firm but polite | SHOULD |
| 2 | make this message sound more professional for Teams | SHOULD |
| 3 | draft the Discord announcement for the v2 launch | SHOULD |
| 4 | turn these commit notes into GitHub release notes | SHOULD |
| 5 | give me a YouTube title and description for this video about monitor setups | SHOULD |
| 6 | reshape this email into a two-line text to my brother | SHOULD |
| 7 | commsmith voice — save this as my work voice | SHOULD NOT (voice definition/storage — brandsmith) |
| 8 | I need a comms plan for the release next Friday | SHOULD |
| 9 | shorten this LinkedIn post and make it punchier | SHOULD |
| 10 | announce the downtime window to the team, not scary | SHOULD |
| 11 | send this email to bob@example.com | SHOULD NOT (delivery — surface tools) |
| 12 | write a 2,000-word guide on monitor calibration | SHOULD NOT (long-form — loresmith) |
| 13 | write a system prompt for my support bot | SHOULD NOT (prompts — promptsmith) |
| 14 | design our brand voice and taglines | SHOULD NOT (brand + voice ownership — brandsmith) |
| 15 | compare Slack vs Teams for our team and recommend one | SHOULD NOT (verdict — loresmith) |
| 16 | build me a skill that formats messages | SHOULD NOT (skill build — skillsmith) |
| 17 | what's the weather for the launch event | SHOULD NOT (off-topic) |
| 18 | summarize this 40-page PDF | SHOULD NOT (not message-shaping) |
| 19 | write mean replies to this guy's tweets | SHOULD NOT (restraint — harassment) |
| 20 | schedule this message for 9am | SHOULD NOT (delivery/scheduling — surface tools) |

Edge note: the sharpest pair is 3 vs 15 — announcing a decision is commsmith; making the decision is loresmith. Misses on 1–10 → push the channel nouns harder; fires on 11/20 → tighten the never-send boundary sentence.

## Audit additions

| # | Query | Expected |
|---|---|---|
| 21 | "commsmith audit — does this release note match our GitHub format?" | SHOULD — drift audit against a channel contract |
| 22 | "audit our Q3 marketing performance" | SHOULD NOT — analytics, not message form |

## 1.1.0 additions

| # | Query | Expected |
|---|---|---|
| 23 | "apply my brand voice to this email" (voice profile handed in / named) | SHOULD — voice *application* to a message; the profile comes from brandsmith's export, commsmith consumes it |

Edge pair: #7 vs #23 is the decoupling boundary — *defining or saving* a voice is brandsmith; *applying* a named or handed-in voice to a message is commsmith.
