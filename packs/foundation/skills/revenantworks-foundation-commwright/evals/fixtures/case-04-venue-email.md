# Fixture — Case 4 source email (reshape freezes facts)

The source Case 4 reshapes to a text. Committed 2026-07-24 so the case is reproducible: it turns on exact wording (the two frozen facts, and the actorless clause that produced the 2026-07-24 H9 breach), and until now the only copy lived in a run-local temp file. The fenced block below was reproduced byte-for-byte from that run and is pure ASCII, with no dashes of any kind; the prose around it is ordinary pack doc and is not part of the fixture. **Re-baselined 2026-08-08 (owner-approved personal-name scrub): the sender signature — never one of the frozen facts — now reads a neutral name; every frozen fact and the clause under test are byte-identical to the 2026-07-24 baseline.**

The clause under test is the last one: **"the venue releases the booking if it is not paid by then"** supplies its own actor, so H9 repair step one is available and no invention is needed. The recorded failure reached past it for "we".

```
Hi Sam,

Following up on the venue deposit. The balance of $450 is due by March 3, and the venue releases the booking if it is not paid by then.

Can you send it this week?

Thanks,
Jordan
```

Frozen facts a repair may not move: `$450`, `March 3`, and the conditional (non-payment releases the booking, and it is the venue that releases it).
