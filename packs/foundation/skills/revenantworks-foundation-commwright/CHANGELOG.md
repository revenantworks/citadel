# Changelog — revenantworks-foundation-commwright

> Renamed from `revenant-foundation-commwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.0.3] — 2026-08-08

- Case 4 fixture second-pass re-baseline (2026-08-08 estate audit): the
  greeting's recipient name — like the sender signature, never a frozen
  fact — now reads neutral. Its provenance against the original 2026-07-24
  run was unrecorded, so it is treated as potentially real rather than
  assumed synthetic; the fixture note records the adjudication. Frozen
  facts and the clause under test remain byte-identical to the baseline.
- This entry also lands the member-bump-on-shipped-change rule: the 2.2.3
  release changed this member's fixture and RESULTS provenance without a
  version bump, which left the claude.ai per-member re-upload with no
  signal that the name scrub needed shipping there.

## [1.0.2] — 2026-08-01

The skill's own framing prose used em dashes in the sentences that announce
its own no-dash rule (H1): SKILL.md's opening description of the humanized
default, two Turn-shape lines, and a Behavior-notes line, plus README.md's
opening differentiator sentence and its second-paragraph rule summary, all
used the dash H1 bans in every drafted message. Recast without em dashes
(colon, period-and-restart, or parentheses per case) so the pitch now
matches the policy. `references/humanize.md` was checked and already
self-applies H1 in its own prose, so no change was needed there.

No rule, gate, count, or entry point moved. No eval re-anchor is owed.

## [1.0.1] — 2026-08-01

Frozen-record marker added to the `evals/` files that cite predecessor-era
version numbers. Those designations predate the 2026-07-31 re-baseline, and
two of the tag names were later reused by unrelated releases, so a reader
could take a historical entry for a current one. The rows, verdicts, dates
and counts are untouched — only a header marker was added, so nothing about
what was executed or when has moved.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Channel-shaping core: resolves a channel profile from
  `channel-profiles.md` and drafts to that channel's register, length, and
  structure contract; a brand voice applies only via a handed-in brandwright
  voice-profile export — commwright stores no voice of its own.
- Humanized register enforced silently on every draft: rules H1–H9 (dash
  law, emoji law, sentence-variance floor, no preamble, no trailing
  help-offer, no recap paragraph, banned rhetorical constructions, one hedge
  per clause, name-the-actor) with frozen-content discipline and a stated
  precedence order; repairs never add or drop facts.
- Humanize entry: strips AI tells from handed-in text while preserving the
  original writer's quirks, closing with a one-line report of what was
  removed.
- Audit entry: report-only drift scoring across register, length, structure,
  subject/title rules, pre-publish hygiene, AI-tell density, and voice
  conformance, cataloged P0/P1/P2; rewrites land through Reshape on
  approval.
- Pre-publish redaction sweep on anything public-bound: names, internal
  URLs, filesystem paths, account IDs, and credentials flagged loudly, never
  echoed.
- Cadence sets for release comms and comms plans; strategy-labeled variants
  only when stakes genuinely compete; never sends — delivery stays with the
  surface's own tools.
