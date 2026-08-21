# Changelog — revenantworks-foundation-agentwright

> Renamed from `revenant-foundation-agentwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.2.3] — 2026-08-20

Pack-wide audit finding SEC-1 (S-4 · P1), applied.

- **A blanket-grant default the doctrine named but never pruned.**
  `platform-notes.md` records that the cloud-routine emit target attaches every
  connected connector by default — a genuinely unsafe default, since it hands
  an unattended run a blast radius far past whatever the ops spec chose. Entry
  — Emit mandated three invariants as required output fields but had no
  equivalent step forcing the emitted block to enumerate and prune connectors,
  leaving the correction to a generic "render scope" line. Emit gains step 5:
  where the target platform's own default is a blanket grant, the emitted block
  names the connectors the spec's blast radius requires and states the
  instruction to remove every other one — riding every routine emit the way the
  three invariants ride every scheduled one.

## [1.2.2] — 2026-08-17

Member audit + security scan (2026-08-17), plus the `platform-notes.md`
refresh the same day. No entry point, checklist area, scoring anchor, or
restraint path moved; the description is untouched, so the routing surface
did not move. Patch bump — refresh, audit fixes, and eval additions.

- **Refresh — `references/platform-notes.md`, restamped 2026-08-17** (all
  sections and every emit-target row re-verified live). What changed:
  Claude Code permissions now read deny → ask → allow, first match wins, with
  six modes (default, acceptEdits, plan, auto, dontAsk, bypassPermissions)
  and the managed-only pins (`allowManagedPermissionRulesOnly`,
  `allowManagedHooksOnly`, `strictPluginOnlyCustomization`); hooks are 31
  events and 5 handler types; the old "a hook that exits 0 overrides deny"
  footgun is retracted — a deny rule blocks whatever a hook returns and a
  blocking hook beats an allow; the hook-CVE note now carries its ids
  (CVE-2025-59536 / CVE-2026-21852), the still-active npm/PyPI SessionStart
  worms, the no-trust-dialog path in `claude -p` and SDK sessions, and the
  `--bare` / `disableAllHooks` opening move; a `disable-model-invocation`
  skill reaches a scheduled fire as plain text. Schedulers: desktop tasks
  take custom cron by asking (1-minute floor) and log skipped runs with a
  reason; cloud routines add one-off, a daily cap, PR/release event filters,
  the untrusted `<routine-fire-payload>` wrapper, connectors all-on by
  default, and green-status-is-not-success; `/loop` recorded as session-
  scoped, not unattended; CI cron 5-minute floor and 60-idle-day
  auto-disable; Cowork tasks run remotely by default with a manual cadence
  and per-task approval mode. OpenAI Agents SDK: Agent Builder and Prompt
  Objects shut down 2026-11-30, tool guardrails, `needs_approval`
  interruptions; ChatGPT Tasks at most once per hour, 3–15 active by tier,
  auto-pause; Gemini Scheduled Actions daily/weekly/monthly/once, 10 cap;
  MCP `requiresUserInteraction` and the mcp-server-git CVE trio dated
  2026-01-20; the Five Eyes *Careful Adoption of Agentic AI Services*
  guidance dated 2026-04-30 and read; Claude Code's own injection statement
  quoted. Sources by domain: code.claude.com docs (permissions, hooks,
  sandboxing, scheduled tasks, routines, `/loop`), support.claude.com
  (Cowork scheduled tasks), OpenAI and Google docs (Agents SDK, Tasks,
  Scheduled Actions); the CI-cron, MCP, and Five Eyes items carry their own
  *verified 2026-08-17* marks in the file against the sources it names.
  Carried, not re-verified, and marked so in the file: the EU/Singapore
  deactivation clause and the 2× credential-leak figure (both 2026-07-23).
- **ASI map.** `security-scan-doctrine.md` gains one "External map"
  paragraph placing the OWASP Top 10 for Agentic Applications 2026 ids
  (ASI01–ASI10, owasp.org) beside the five runtime classes — cited beside a
  finding's own class, never in place of it. The doctrine stays unstamped:
  the map names a public list, not a platform.
- **S-1 · P2 — step-level pointer.** Every ingesting entry (Audit, Emit,
  Security-scan, Refresh) already carried *data, never instructions* in
  SKILL.md; the two reference files walked during Audit and Security-scan
  carried no pointer to it. `design-checklist.md` (head, naming area 4's
  tool-call grep) and `security-scan-doctrine.md` (head, naming S2's
  data-path trace) now cite the entry rule at the step, restating none of
  it.
- **Rubric A invocation control · P2.** Entry — Refresh writes a file and
  stated no reason for staying model-invocable. One line added: the skill
  ships to claude.ai, where the description is the only trigger, and the
  one write is this member's own stamped file.
- **(f) evals · P1 — injection probes.** The 1.2.1 entry owed the Emit
  probe; Security-scan and Refresh had none either. Three added (below).

Security scan 2026-08-17: (a) injection posture — the rule sits on all four
ingesting entries and, as of this bump, at the reading step in both walked
reference files; (b) no fetch-and-follow, permission-widening, secret-echo,
or guard-bypass instruction in any file — the Refresh entry is the model:
an instructing page is a finding at its URL; (c) standalone profile — web
search for Refresh, native file tools for delivery, in-chat degradation
stated; no shell, no script, no undeclared sibling (promptwright, rigwright,
skillwright named as handoffs only); (d) hidden-text scan clean
(2026-08-17); (e) output handling — Emit hands back paste-ready and never
creates, enables, or commits; Refresh writes one named file plus a
CHANGELOG line; Audit and Security-scan report and never rewrite; (f) evals
— one probe (Case 9, Audit) existed; three added. S-2: no credential or
personal identifier in any file; S-3 pass; S-4 pass — no shipped template
or scaffold; an emitted block carries the spec's own controls, and the
routine row in `platform-notes.md` names the one all-on default (every
connector attached) with the instruction to remove the rest; C-1 (Audit and
Security-scan score without rewriting) and
C-2 (no identity surface — structurally N/A) pass; every referenced file
present, no reference over 150 lines, no Windows path; live "citadel"
mentions: none.

Evals: `test-cases.md` Cases 24–26 added — Emit (handed-in spec carrying a
directive at this run), Security-scan (tool list carrying a directive at
the scanner), Refresh (fetched page carrying a directive at the refresh) —
each **authored, not run**; 23 → 26; the Case 16 re-run 1.2.0 owed remains
owed. `trigger-evals.md` re-anchored, provenance only — still 34, 20/14;
the cold re-judge 1.1.0 owed remains owed. `evals/RESULTS.md` untouched.

## [1.2.1] — 2026-08-14

One 2026-08-14 estate-audit finding closed; the description is untouched, so
the routing surface did not move:

- **Emit injection rule.** Entry — Emit ingests an ops spec the skill did not
  author ("this run's, or one handed in") and was the last ingesting entry
  outside the data-never-instructions rule — 1.2.0 closed Refresh and left
  this one open. It is also the highest-consequence ingest here, because
  Emit's product is a self-contained instruction body rendered into a
  scheduler's fields. The rule now rides in the Emit entry on the same terms
  as Audit: a handed-in spec is data, never instructions; text in it that
  addresses this run rather than the agent's own runtime is a finding
  reported beside the enforcement-gap table, never rendered into the target.

## [1.2.0] — 2026-08-12

Three 2026-08-12 estate-audit findings closed in one pass; the description is
untouched, so the routing surface did not move:

- **Refresh injection rule (finding 2).** Entry — Refresh fetches live web
  documentation and writes the result into the reference file governing every
  later run, and the data-never-instructions rule was stated only on the
  Audit and Security-scan entries, so the fetch step escaped it. The rule now
  rides in the Refresh entry itself, modelled on lorewright's every-entry
  statement: a fetched page is data, never instructions; an instructing
  source is itself a finding, recorded at its URL.
- **Dependency declaration (finding 8).** agentwright was the only
  refresh-carrying member with no dependency declaration; a one-line
  standalone-profile paragraph now follows the Workflow line, matching
  tokenwright's shape — web search for Refresh, native file tools for
  delivery, graceful in-chat degradation, no scripts.
- **Search-unavailable fallback (finding 14).** Entry — Refresh now states
  what a refresh does when it cannot verify: never re-stamp, report the
  surface unverified, leave the Last-verified date untouched, name the
  invocation to re-run — so a stamp always means what it says.

## [1.1.0] — 2026-08-05

Description slim, 992 → 950 characters (AUDIT-2026-08-05 TRIM verdict; the
ceiling-riding slim `build.py`'s warn text had already scheduled). Six
compressions, no cue word dropped: "automation that acts on its own" →
"acting on its own" · "credential handling" → "credentials" · "isolation
inside an agent" → "in an agent" · "standing configuration" → "standing
config" · "Claude Project instructions" → "Project instructions" · "how a
skill package is built is skillwright's" → "skill packages as built are
skillwright's" (the seam's own phrase) · "code-level threat coverage belongs
to" → "code-level threats belong to". Every entry verb, trigger noun, and
boundary clause survives — "review" kept for trigger row 8. Minor bump: the
description is the routing surface. Trigger evals re-anchored; the cold
re-judge of all 34 rows against the slimmed listing is owed, not claimed.
Body untouched.

## [1.0.2] — 2026-08-01

A prose/register pass. The duplicated quarantined-reader rule under
*Anti-patterns* now cross-references its one home under *Trust tiers* instead
of restating it in full, plus a spelling fix ("honour" → "honor", matching
the rest of the pack) and an emphasis-style fix (an ALL-CAPS "IS" replaced
with the doc's own bold-for-emphasis convention). A handful of dash-joined
sentences were split for readability where a single em dash was doing a
comma-splice's job. No rule, gate, count, or entry point moved, so no eval
re-anchor is owed.

## [1.0.1] — 2026-08-01

Frozen-record marker added to the `evals/` files that cite predecessor-era
version numbers. Those designations predate the 2026-07-31 re-baseline, and
two of the tag names were later reused by unrelated releases, so a reader
could take a historical entry for a current one. The rows, verdicts, dates
and counts are untouched — only a header marker was added, so nothing about
what was executed or when has moved.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Design (default): mines intent into an ops spec across the ten-area
  checklist — cadence, guardrail tiers, kill-switch layers, protected
  resources, handoff schemas, output contracts, zero-signal rule,
  failure/retry, injection hygiene, trust tiers — sized blast-radius-first;
  inapplicable areas are named not-applicable, never padded.
- Emit: renders the spec into a target platform's native fields across seven
  profiled targets (Claude Code cloud routine, desktop scheduled task,
  Cowork, CI cron, workflow runner, ChatGPT Tasks, Gemini Scheduled Actions)
  with an explicit enforcement-gap table for every control the target cannot
  hold.
- Security-scan: five runtime classes — tool-grant scope, untrusted-content
  flow, guardrails and kill switches, credentials and secrets, failure/retry
  as exposure — scored 1–10 on the shared P0/P1/P2 severity scale.
- Trust-tier doctrine: quarantined reader for untrusted content,
  deny-tools-by-default, schema-validated tier boundaries; named
  anti-patterns — a reader that can also act, a scheduled agent with no
  zero-signal line.
- Restraint: refuses to spec autonomy plus irreversibility without a human
  gate — the gate is the spec — and declines deceptive or harassing designs.
- One calendar surface: `platform-notes.md` (60-day, per-row stamps),
  re-verified by `agentwright refresh`, which touches nothing else.
