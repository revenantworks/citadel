# Security-Scan Doctrine — the Five Runtime Classes *(durable doctrine)*

Loaded on `agentwright security-scan` and on nothing else. `design-checklist.md` asks whether an agent's spec is *complete*; the five classes here ask whether what the agent is **allowed to do when it runs** is safe. Durable by construction: no platform product names and no threat-landscape claims live in this file — a finding that needs a concrete enforcement mechanism takes it from `platform-notes.md`, which is the stamped surface, so nothing here ages.

## Contents

Severity · S1 Tool-grant scope · S2 Untrusted-content flow · S3 Guardrails & kill switches · S4 Credentials & secrets · S5 Failure & retry as a security surface · Worked example

---

## Severity — the existing scale, applied per class

There is one scale in this skill and this file adds none. Scores are Entry — Audit's 1–10 with its anchors (7+ operable · 4–6 runs but leaks risk · 1–3 unguarded), **one score per class — five, not ten**; a class the agent's blast radius cannot reach is marked n/a with the one-line why and excluded from the composite, never scored zero (SKILL.md *Behavior notes*, "Never pad"). Findings carry Entry — Audit's row shape verbatim: `ID (P0/P1/P2) · what's exposed · the exact control to add · Apply / Optional / Skip`.

**P0 keeps the definition Entry — Audit already states** — uncontrolled blast radius, missing kill switch, or untrusted content reaching privileged tools. Each class below names which of its own defects meets that bar rather than restating it. **P1** — a real exposure the agent's stated bounds still cap (over-broad grant on reversible tools, per-run credential hygiene missing where a breach stays recoverable). **P2** — hygiene that costs nothing to fix and buys margin (unstated-but-narrow scope, log verbosity short of secret leakage).

## S1 — Tool-grant scope

What the agent may call, versus what its job needs. Three questions, in order:

- **Is scope stated at all?** An agent whose grant is "whatever the connector exposes" has no scope. Unstated grant on a surface that reaches any destructive tool is **P0** by the standing definition — the blast radius is uncontrolled because nobody has bounded it. Unstated but demonstrably read-only is **P2**.
- **Is it wider than the job?** Compare the granted set against the actions the ops spec's own sections require. Every tool granted and never used by any stated action is over-grant — **P1**, or **P0** when the surplus tool is destructive.
- **Is any destructive tool ungated?** Delete, send, publish, pay, deploy — irreversible or externally visible in one call. Each needs a gate named at the hard tier (review-before-execute, human confirmation per action, allowlisted destination) or the spec's reason why hard enforcement is unavailable on that surface (`design-checklist.md` area 2). A destructive tool granted with soft-tier rules only is **P0**; the agent argues its way past prompt text on the run that matters.

Deny-by-default is the standard the scan measures against: unlisted is denied. A grant expressed as an exclusion list ("everything except X") is a finding of its own — the set it permits changes whenever the platform ships a tool.

## S2 — Untrusted-content flow

The rule this class scans against is **SKILL.md, *Trust tiers — the untrusted-content rule*** — quarantined reader, deny-by-default toolset, validated boundaries. It is stated there, it binds whether or not this file is open, and this file does not restate it. The scan's job is to walk the agent's real data path against it and report where the path departs:

- Trace every input the agent does not author — fetched pages, received messages, attachments, tool output that embeds third-party text, and prior-run state written from any of those — to the first tier that can act on it. That trace is the finding's evidence.
- Untrusted content reaching a tier holding a write, send, or spend tool is **P0** by name in the standing P0 definition.
- A boundary crossed by free-form text with no schema and no length cap is **P1** — the tier separation exists on paper and is unenforced in the one place it is load-bearing.
- Destinations (recipients, URLs, account identifiers) taken from untrusted content are **P0** regardless of tier, because the guardrail the agent still has is aimed at the wrong target.

## S3 — Guardrails and kill switches — presence and adequacy

Entry — Design and Entry — Audit already cover *specifying* these; the scan does not re-teach them and does not rewrite them. It asks three narrow questions and answers each with a yes plus the evidence, or a finding:

- **Is there a stop condition?** Something the run reaches that ends it — a cap hit, an error class, a phrase honored. An agent whose only terminal state is "task complete" cannot stop when the task is the problem: **P0**.
- **Is the blast radius bounded numerically?** Caps are numbers with units (`design-checklist.md` area 2) and the scan checks proportion, not just presence — a cap that cannot bind in any plausible run is a cap in name only, **P1**, and the finding states the radius it fails to bound.
- **Can a running agent be halted?** Both layers, per checklist area 3, with the puller named for each. Missing hard layer is **P0** — it is the standing P0's second clause. Present but pullable only by the agent's own machinery (a flag the agent itself writes, a schedule it can re-enable) is a hard layer that isn't one: **P0**.

## S4 — Credentials and secrets

- **Secrets in prompts.** A key, token, password, or account number pasted into instruction text is exposed to every tier that reads that text and to every log that captures it — **P0** when the credential grants a destructive or spending capability, **P1** otherwise. The control named is always the same shape: a reference the runtime resolves, never the value.
- **Secrets in logs and outputs.** Scan what the run *emits* — the output contract's fields, error text, retry diagnostics, and any handoff payload — for anything that carries a credential, a session token, or a full account identifier. Verbose error paths are where this lands, because they were written for a debugging turn and never re-read as an output surface. **P0** where the emission destination is shared, external, or untrusted-readable; **P1** where it stays owner-private.
- **Scoping per run.** Credentials are scoped to the narrowest capability and the shortest life the surface supports, and the spec names which credential each tier holds. One long-lived all-scopes credential shared across every tier collapses the tier separation S2 depends on, whatever the trust tiers say — **P1**, and **P0** when the shared credential reaches an untrusted-content tier.
- **Revocation is the hard kill switch's substrate** (area 3). A credential nobody can revoke without taking down unrelated systems is a kill switch that will not be pulled: **P1**, with the fix stated as a dedicated per-agent credential.

## S5 — Failure and retry behavior as a security surface

Failure handling is specified in `design-checklist.md` area 8 as correctness; this class re-reads the same decisions as exposure.

- **Unbounded retry against an external service.** No retry ceiling, or a ceiling that resets on each new run of a fast cadence, is an availability attack the owner is running against their own dependency — and the fastest route to a revoked credential or a ban. **P1** by default. It is **P0** only when a retry *accumulates unrecoverable effect* — a spend, a delete, a deploy, or a send that fans out to fresh recipients per run with no dedupe — because each attempt lands a new irreversible action and the ceiling is the only thing bounding the total. The discriminator is accumulation, not external visibility: a **bounded resend to the same destination**, controlled by dedupe or suppression rather than a retry count (the worked example below — a bounced address retried, fixed by *retry once narrower, then suppress that recipient*), collapses to one delivery however many attempts it makes and stays **P1**. The destructive inventory here is S1's — delete, send, publish, pay, deploy — read against this class's accumulation test and single-homed in S1 so the rule and the worked example cannot drift apart again; note that `send` splits by shape, per-run fan-out is P0 and a bounded resend to one recipient is P1.
- **Silent failure.** A failure path that emits nothing is indistinguishable from a breach that emits nothing. Every failure class terminates at a stated emission to the same destination as findings — the zero-signal rule (SKILL.md *Anti-patterns*) covers the empty-result case and binds here unchanged; this scan covers the *errored* case. Silent swallow on a path that touches money, sends, or protected resources is **P0**.
- **Unbounded fan-out.** A run that spawns work per input item — one message per sender, one sub-run per row — with no ceiling on item count converts a large or attacker-influenced input into proportional action. The control is a per-run item cap plus an overflow behavior (report and stop, never truncate silently): **P0** where the fanned-out action is destructive or externally visible, **P1** otherwise.
- **Degrading a cap on failure.** A retry path that widens scope, drops a check, or falls back to a broader credential to get through is a guardrail with a documented bypass: **P0**.

## Worked example

*Input: an ops spec for a support-inbox agent — reads incoming email, drafts and sends replies, files tickets, runs every 15 minutes on the owner's mailbox credential.*

Scoreline: **S1 3 · S2 2 · S3 5 · S4 4 · S5 6 — composite 4.0.**

| ID | P | What's exposed | The exact control to add | Disposition |
|---|---|---|---|---|
| S1-1 | P0 | One tier holds `messages.read`, `messages.send` and `messages.delete`; no stated action deletes anything | Drop `messages.delete` from the grant; deny-by-default the remainder | Apply |
| S2-1 | P0 | The tier that reads sender text is the tier that sends — untrusted content reaches a send tool, against SKILL.md's trust-tier rule | Split into a quarantined reader emitting a `ReplyDraft` schema (typed, length-capped) and a sender tier that reads only that schema | Apply |
| S2-2 | P0 | Reply recipient is taken from the inbound message's `Reply-To` | Route replies to the original `From` only, checked against an allowlist of prior correspondents | Apply |
| S3-1 | P0 | Soft phrase "STOP" honored in-prompt; no hard layer named | Name the hard layer (revoke the mailbox credential) and its puller; state both in the drill | Apply |
| S4-1 | P1 | One long-lived full-mailbox credential held by every tier, including the reader | Per-tier credentials: read-only scope for the reader, send scope for the sender, both per-run | Apply |
| S5-1 | P1 | Send failures retry each 15-minute run with no ceiling; a bounced address retries indefinitely | Retry once narrower, then report to the findings destination and suppress that recipient for the day | Apply |
| S4-2 | P2 | Error text echoes the full message-id and header block into the run log | Truncate diagnostics to the fields the output contract names | Optional |

Verdict: three P0s on one data path — the reader-that-sends is the root, and S1-1, S2-2 and S3-1 are what it costs. The spec is not runnable as written; S2-1 is the fix the other findings are sized against.
