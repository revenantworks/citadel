# Changelog — revenant-foundation-agentwright

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
