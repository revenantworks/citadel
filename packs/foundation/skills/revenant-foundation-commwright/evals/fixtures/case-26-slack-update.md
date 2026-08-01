# Fixture — Case 26 source Slack update (channel contract outranks humanize)

The handed-in text Case 26 humanizes. Committed 2026-07-24 so the case is reproducible: it turns on exact wording (the manner fact "by hand", whose loss was the 2026-07-24 H9 breach), and until now the only copy lived in a run-local temp file. The fenced block below is reproduced byte-for-byte from that run and is pure ASCII, with no dashes of any kind; the prose around it is ordinary pack doc and is not part of the fixture.

Carries what the case asserts on: the Slack profile's required bold lead line, six facts, and a nested one-line sub-bullet, plus the tells a humanize pass has to remove (a recap opener, "Moreover", "it's worth noting that", "comprehensive", a trailing help offer).

```
**Q3 billing migration is done.**

We are pleased to report that the migration was completed successfully.
- All 42,000 accounts were migrated on 12 September.
- Invoice generation moved to the new pipeline.
  - The old pipeline is now read-only.
- Two accounts failed validation and were fixed by hand.
- Support has been notified and will handle any billing questions.
- The finance close is unaffected; the October close runs on schedule.
- A full reconciliation report will be provided by 19 September.

Moreover, it's worth noting that this represents a comprehensive overhaul of our billing infrastructure. Let us know if you have any questions!
```

The six facts, in bullet order: the migration count and date (42,000 accounts, 12 September); invoice generation on the new pipeline, with the old one read-only; two validation failures fixed **by hand**; support notified and handling billing questions; the finance close unaffected and October on schedule; the reconciliation report due 19 September.

Four of them sit on agentless passives, which is what makes this the H9 pressure case. "were fixed by hand" is the one to watch: its manner word is the fact the recorded failure shed, and its completion is the fact a step-two recast to "needed a manual fix" would shed instead.
