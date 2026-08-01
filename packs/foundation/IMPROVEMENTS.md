# foundation — what improved (1.0.0 → 1.3.2)

*A narrative companion to the per-member `CHANGELOG.md` files and the root
`CHANGELOG.md`. The changelogs record every edit; this records what the edits
add up to. Stamped 2026-07-27, pack **1.3.2** (`foundation-v1.3.2`).*

The pack went from a uniform launch baseline to eight wrights that are
neutral-by-default, single-homed, security-scanned inside and out,
**execution-verified rather than authored-and-hoped**, and routed cleanly
against each other. The arc, by theme:

## New capabilities
- **agentwright** gained a fourth entry point, `security-scan` (1.2.0) — a
  runtime-permission audit of tool grants, credentials, blast radius, and
  retry-as-attack-surface, scored on the existing Audit scale.
- **skillwright** gained a named **security pass inside every audit** (1.4.0) —
  injection surface, secrets, undeclared tools, unsafe defaults — turning a
  one-line rubric that had existed unspecified since 1.0.0 into a real catalog;
  and wrote down its **release doctrine** (1.2.0) it had practised but never
  documented.
- **promptwright** added a steerable **framework menu (CO-STAR/RISEN), a Fast
  path, and a by-name red-team / hostile-interpreter pass** (1.2.0).
- **commwright** made **humanize its default register** (1.2.0) — every draft
  obeys it silently, instead of it being an opt-in flavour.

## Architecture
- **Brand fully decoupled (1.1.0).** brandwright is the single home of brand and
  voice; skillwright and commwright went neutral-by-default and consume brand only
  through `brandwright apply` / export. No wright styles its own output.
- **One-statement-per-law, single-home everywhere.** Every rule lives in exactly
  one place and is referenced elsewhere — closing the "defined twice, copies
  disagree" defect that kept recurring across members.
- **Footprint budgets moved out of frontmatter into the registry (1.3.1).**
  Saved ~50–95 tokens *per invocation* per member by not shipping a build-time
  number on every run.
- **Volatile-surface stamping + a 60-day calendar sweep** added pack-wide (1.1.0).

## Correctness — driven by actually running the suites
For the first time, every member's **assertion suite was executed** rather than
only authored, and execution surfaced real failures a green-on-paper suite had
hidden: skillwright 32/36, brandwright 14/16, tokenwright's flagship P0 that was
unenforceable from its own load path, lorewright's two evidence tags firing on
the same source, evalwright's five states sharing one wrong rule. Each was fixed
**at the doctrine level, not by weakening the assert** — and a lasting discipline
emerged: distrust a clean sweep, and audit every repair for restating the defect
it was closing.

## Security
- The pack **ran its own security classes on itself** for the first time and
  found **two of its own members failing** — lorewright S-1 **P0** (read live web
  pages with no data-never-instructions rule) and promptwright S-1 **P1**
  (hardening aimed at its output, not its input). Both closed with the test case
  each should have shipped with.
- agentwright's **S1/S5 severity contradiction** reconciled (1.3.2): irreversible
  *accumulation*, not mere external visibility, is the P0 retry trigger.

## Routing precision
Closed the last open routing seam, then the subtler cross-member ones: the
**skillwright ↔ agentwright** security boundary, the **skillwright ↔ commwright**
prose-vs-message split (both `humanize` sides now scoped), and the
**brandwright ↔ skillwright** circular rebrand seam — plus a router-level compose
bullet in the always-on `CLAUDE.md` so the splits hold on the surface that loads
first, not only in descriptions.

## Where it stands
The open register is **empty but for one item** — relocating the pack-registry
out of skillwright — which is gated on a *second pack existing* and cannot be
closed by editing code. Every other doctrine, suite, and routing finding raised
across two weeks of execution passes is closed, each in its owning member, each
with a ledger entry backing the claim.
