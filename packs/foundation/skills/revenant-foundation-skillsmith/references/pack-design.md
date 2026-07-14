# Pack Design — Durable

> Loaded for every Entry — Pack run. The entry is a conductor: everything below is roster-design doctrine; the build machinery it drives lives in Build, Integrate, and Packaging, unchanged.

## Capability map

The output of domain research, before any skill is designed. One row per candidate capability:

| Tier | Candidate | Job (one line) | Incumbent scan |
|---|---|---|---|

Tier definitions — argue the tier, not the vibe:

- **must-have** — the role does this weekly or the workflow breaks without it, AND no strong incumbent owns it (or the incumbents are platform-bound where the user needs portable).
- **high-value** — real recurring need; either a partial incumbent exists or the need is less frequent. Build after must-haves.
- **nice-to-have** — plausible but unproven need. Default: record, don't build. A nice-to-have earns a build only when the user asks for it by name at the gate.
- **adopt** — a strong incumbent already owns the job. Name it, link it, record it in the spec's adopt register, leave it out of the roster. Building a worse copy of a good incumbent fails the niche verdict by definition.

The map is evidence-first: every tier call cites what the scan found (or found missing). "Nothing found" after checking the baseline's niche-research sources is a finding; "didn't check" is not.

## Trigger-partition table

Ten realistic requests someone in the domain would actually type, each mapped to exactly one roster member. Written at roster-design time — before the skills exist — so the descriptions are designed as a set instead of deconflicted after the fact. Rules:

- Every member appears at least once; no request plausibly routes to two members.
- Include at least two near-misses that should route OUTSIDE the pack (to an incumbent from the adopt register, or to nothing) — the set's boundary matters as much as its interior.
- At set finish, the same table re-runs against the real shipped descriptions. A request that now routes wrong is a P1 on whichever description drifted.

## The pack-spec baton

`<pack>-spec.md`, written immediately after the roster gate and handed back before the first build. Sections:

1. Header — pack name, profile, brand token, stamp, status line (`N of M built`).
2. Approved roster — the gated table plus a **Status** column: `QUEUED → BUILT → SHIPPED` (shipped = packaged and delivered).
3. Trigger-partition table — verbatim from the gate.
4. Adopt register — incumbents recorded instead of built.
5. Decisions log — dated, one line each (tier changes, renames, scope calls).
6. Session log — dated, which members each session touched.

The spec is the source of truth for resuming: a new session reads it, picks the next `QUEUED` member, and builds — no re-gating, no re-research of the roster (member-level niche verdicts still run fresh inside each Build). Update Status and the logs after every ship. When the user and the spec disagree, ask; when memory of the conversation and the spec disagree, trust the spec.

## Session staging

- Packs of **≤3** members may run one-shot when the user asks ("build the whole thing now").
- Above 3: default **one to two members per session**. The constraint is quality, not context arithmetic — later builds in a long run get measurably shallower research and looser suites. The spec makes stopping free, so stop while the work is still sharp.
- Always end a session by updating the spec and stating what's next ("3 of 6 built — next session: <member>").

## Set finish

When the last roster member ships, in order:

1. **Set discoverability test** — the partition table against the real descriptions (rules above).
2. **Entry — Integrate** for the whole roster — registry rows, manifests, packages per the pack's restamp policy, upload checklist.
3. **Plugin/marketplace prep** (offered, not automatic): `.claude-plugin/marketplace.json` + `plugin.json` per the current official schema, a validation step (`claude plugin validate .` where the CLI exists; by-eye checklist otherwise), and a submission checklist for the community marketplace flow recorded in the baseline sources. **Prep, never submit** — the submission PR/form is the user's action, and the checklist says exactly what they'll be asked for.

## Partial verdicts

A pack verdict is per-tier, not all-or-nothing. The normal healthy outcome: must-haves DEFENSIBLE, one or two candidates CROWDED and moved to the adopt register. A pack where *every* candidate comes back CROWDED is information too — report it, propose the one or two adjacent underserved niches the research surfaced, and let the user redirect before anything is built.

## Honesty rules

Size estimates (S/M/L) and session counts are estimates — label them so. The capability map cites its scan. The spec never claims a member is SHIPPED until its package was actually handed back. And the pack's one-gate promise is kept literally: after the roster gate, the user is never re-asked to approve something the gate already covered.
