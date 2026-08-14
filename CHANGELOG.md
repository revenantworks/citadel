# Changelog — citadel

Pack releases tag as `<pack>-vX.Y.Z`; member versions are independent semver.
This log starts at the foundation 1.0.0 baseline.

> **Predecessor-era version numbers do not resolve.** The pack re-baselined to
> 1.0.0 on 2026-07-31 and the pre-1.0 history was destroyed with no archive, so
> tag names from before that date (`foundation-v1.1.x` through `v1.4.x`,
> 2026-07-14 → 2026-07-27) name releases that no longer exist anywhere, as do
> the commit SHAs recorded beside them. **Two of those names have since been
> reused:** today's `foundation-v1.1.0` and `foundation-v1.1.1` are new
> releases unrelated to the predecessor tags of the same name. Where a
> pre-2026-07-31 designation appears in a frozen record — the eval `RESULTS.md`
> ledgers, `spec.md`'s history sections, `IMPROVEMENTS.md` — it is left verbatim
> because it records what was true when written; read it as a date, not a tag.
> Live code and runbooks cite dates instead, for exactly this reason.

## [ossuary-v2.2.5] - 2026-08-14

A 2026-08-14 estate-audit finding: bonecaller implements a fifth job the
description never named, so nothing routed to it.

- bonecaller 1.3.4: `description` gains the Pause/resume job in its
  capability clause and "pause the betting" in its trigger list, 791 → 890
  chars. The body has carried the job since 1.0.0 and `test-cases.md`
  asserts it at B5; the pack router lists it too, but that router ships as a
  Claude Code `CLAUDE.md` and bonecaller's declared surface is claude.ai,
  which never loads it — so the description was the only routing text and it
  was silent on pause. Trigger suite 8 rows → 9 (row 9 authored, not run);
  the cold re-judge of all 9 is owed, not claimed.
- **The longshot `skills/revenantworks-ossuary-bonecaller` mirror is owed a
  re-sync** (separate session, per the downstream-mirror rule). It is still
  at 1.3.0 — three releases behind before this one — and that copy carries
  the 533-char `compatibility` the live upload form is confirmed to reject.

## [foundation-v2.3.1] - 2026-08-14

Six 2026-08-14 estate-audit findings closed across four members. No
description moved, so no routing surface changed and every trigger suite
keeps its counts; three of the six extend the same
data-never-instructions rule to entry points that were ingesting without it.

- **agentwright 1.2.0 → 1.2.1** — Entry — Emit carries the rule. It ingests a
  handed-in ops spec and renders it into a scheduler's fields, which makes it
  the highest-consequence ingest in that member; 1.2.0 closed Refresh and
  left it open.
- **skillwright 1.2.0 → 1.2.1** — Entry — Upkeep step 1 carries the rule. It
  reads other skills' frontmatter and stamp headers, from a registered
  canonical repo where no workspace copy exists, and step 4 acts on what it
  read. `upkeep-doctrine.md` points at that single home instead of copying
  it. Body budget raised 8080 → 8180 with the reason on the registry row.
- **tokenwright 1.2.0 → 1.2.1** — the rule is promoted from Entry — Slim to a
  fifth Turn shape item, so Audit and Budget are bound by it too; they ingest
  the same instruction-shaped artifacts. Two single-homing repairs ride along:
  the audit inventory's length threshold now lives only in
  `waste-taxonomy.md`, and the refresh sync sweep names `SOURCES.md`, the
  third site of a platform figure it was not reaching.
- **lorewright 1.1.3 → 1.1.4** — eval provenance only: the 1.1.3 re-anchor
  clause was inserted mid-paragraph rather than appended, so the chain
  terminated at the older v1.1.2 anchor. Moved to the end, wording unchanged.

Each member's eval provenance is re-anchored in this commit, and the suites
record what is now asserted nowhere: no case covers an injected directive on
agentwright's Emit, skillwright's Upkeep, or tokenwright's Audit and Budget.
Those cases are owed, not claimed.

## [ossuary-v2.2.4] - 2026-08-14

Caught during the 2026-08-14 hygiene sweep's mirror re-sync: citadel's copy
of `references/card-contract.md` (linecaller) had drifted stale against two
real fixes that landed only on the longshot production mirror and were
never ported back — `2713461` (weather driver, today's-risk KPI, bets-first
game ordering) and `e7e43e6` (corrected spread-pick sign, unambiguous bet
instructions). A routine full-directory mirror sync would have silently
clobbered both; caught before it shipped.

- linecaller 1.5.4: `references/card-contract.md` re-synced from the
  longshot mirror — citadel is the canonical source again, both copies
  byte-identical. No trigger token, `name`, `description`, or
  `compatibility` field touched; cold re-judge held 10/10. R1 and R9 in the
  assertion suite sit nearest the changed ground and are owed a live
  re-run before the next release claims full coverage.

## [ossuary-v2.2.3] - 2026-08-14 (correction)

The 2.2.1 fix assumed `description`'s 500-char rejection shared
`compatibility`'s cause. It never did: two real upload attempts at the
trimmed description length never errored on `description`, only on
`compatibility` (2.2.2). skillwright's own rubric caps `description` at
1024 chars and Anthropic's help-center page separately states 200 — neither
number is confirmed live by this product, so guessing further wasn't the
right move. Reverted `description` to its full pre-trim text on both
members.

- bonecaller 1.3.3: description reverted 496 → 791 chars (original text,
  byte-identical to the version already cold-judged 8/8).
- linecaller 1.5.3: description reverted 495 → 742 chars (original text,
  byte-identical to the version already cold-judged 10/10).
- `compatibility` stays at its 2.2.2 trimmed length on both — that field's
  500-char rejection is the one actually confirmed live.

## [ossuary-v2.2.2] - 2026-08-14

The 500-char claude.ai upload ceiling turned out to apply to more than
`description` — the owner's actual upload attempt on ossuary-v2.2.1 was
rejected on `compatibility` (bonecaller 533 chars, linecaller 667 chars).

- bonecaller 1.3.2: `compatibility` trimmed 533 → 312 chars, every
  dependency and degradation fact preserved.
- linecaller 1.5.2: `compatibility` trimmed 667 → 463 chars, every
  dependency and degradation fact preserved.
- Pack bump only — no trigger token, hard rule, or reference file changed;
  cold re-judge not owed (compatibility carries no routing).

## [ossuary-v2.2.1] - 2026-08-13

Both members' claude.ai skill upload was failing: the live upload form
rejects a `description` over 500 characters, a stricter ceiling than the
1024-char spec limit this pack's `rubrics.md` baseline carries (flagged there
for the next `skillwright refresh`).

- bonecaller 1.3.1: description trimmed 791 → 496 chars, every trigger token
  and both boundary clauses preserved; cold re-judge 8/8, unchanged.
- linecaller 1.5.1: description trimmed 742 → 495 chars, every trigger token
  and both boundary clauses preserved; cold re-judge 10/10, unchanged.
- Pack bump only — no member body, hard rule, or reference file changed.
  Longshot `skills/revenantworks-ossuary-linecaller` mirror re-synced
  byte-identical.

## [ossuary-v2.2.0] - 2026-08-12

The 2026-08-12 estate-audit remediation pass, ossuary half (findings 3, 6, 7,
11, 12, 19, 20 of `estate-audit/findings/audit-2026-08-12.json`):

- linecaller 1.5.0: coaching notes bounded to model guidance (never the Hard
  rules, the identity gate, the staging list, or any command); step 7 gains
  the delivery proof (fetch, confirm origin/main holds HEAD, retry once, else
  DELIVERY FAILED — ported from the live routine prompt so the skill is the
  procedure's single home); `compatibility` declares step 3's web-search and
  network dependency and drops the Windows-only path and interpreter forms
  for per-surface ones.
- bonecaller 1.3.0: the graded-bet ROI threshold is re-homed to a pointer at
  `longshot-bankroll-rules.md` (one number, one home); the connector
  dependency names the fully-qualified tools (`github:get_file_contents`,
  `github:create_or_update_file`); hard rule 3 extends to the verbatim-HTML
  render path.
- **The longshot `skills/` mirror is owed a re-sync** for both members
  (separate session, per the downstream-mirror rule), and the live Longshot
  routine prompt is owed its thinning to point at the skill (finding 6's
  other half).

## [foundation-v2.3.0] - 2026-08-12

The 2026-08-12 estate-audit remediation pass, foundation half (findings 2, 5,
8, 9, 10, 13, 14, 15, 16, 17 of the same audit):

- All five refresh-carrying members (agentwright 1.2.0, promptwright 1.4.0,
  tokenwright 1.2.0, rigwright 1.1.0, skillwright 1.2.0) carry the
  fetched-page injection rule on their fetch-and-stamp steps, and the four
  without one gain the search-unavailable no-restamp fallback.
- The handed-in-material injection rule is promoted to a file-level Turn
  shape rule in commwright 1.1.0, brandwright 1.3.0, evalwright 1.1.0, and
  rigwright 1.1.0 — single-homed, binding every entry.
- Boundary closes: rigwright ↔ tokenwright shut from both sides (both
  descriptions moved; seam row updated); skillwright's description gains the
  tokenwright and evalwright negative triggers.
- skillwright: packaging caps re-homed to Rubric A; shell/python3 packaging
  dependency declared; rubrics.md records the ~150-line TOC threshold as a
  deliberate house variance from Anthropic's ~100.
- TOCs: lorewright 1.1.3 (verdict-mode.md) and commwright (humanize.md) gain
  Contents blocks.
- agentwright gains its missing dependency declaration.
- upkeep-task.md scope item 2 now derives member surfaces from
  `metadata.volatile` and fails loud; the live routine's STEP 2 is owed the
  matching edit by hand.
- Registry budget rows raised for the audit additions (promptwright 9030,
  skillwright 8080, linecaller 1560), reasons per row.

## [ossuary-v2.1.0] - 2026-08-08

- linecaller 1.4.0: the daily run stages **by path**
  (`reports ledger models docs data/intel data/odds`) instead of `git add -A`,
  with `data/nflverse/` excluded by name. Closes the two remaining open
  findings against this member from the 2026-08-08 assessment: the
  unbounded-history risk (a 37 MB depth-chart CSV plus games.csv were
  recommitted on every refresh — in-season churn would have ballooned the
  repo, which is what the LFS question was really about) and the observation
  that `-A` ships any stray working-tree file unreviewed. Chosen over Git LFS
  deliberately: LFS would add a binary dependency the daily cloud runner does
  not have, while the CSVs are re-fetchable cache governed by their own
  `.stamp` files. They stay tracked at their current revision so a fresh clone
  still boots warm, so run reliability is unchanged. New assertion case R12
  covers it (11 → 12).

## [foundation-v2.2.4] - 2026-08-08

- skillwright 1.1.1: pack-registry records the ossuary member rename
  (`cardcaller` → `bonecaller`, see ossuary-v2.0.0 below) across the members,
  budgets, and seams tables; the Entry — Pack eval scenario's role moved to
  "a customer-support engineer" (2026-08-08 estate audit, owner judgment —
  the old role was a near-description of a firewalled identity's own
  product).
- commwright 1.0.3: case-04 fixture second-pass re-baseline — the greeting's
  recipient name (never a frozen fact, provenance unrecorded) is neutralized
  like the sender signature was in 2.2.3.
- Forge Run capstone card: rigwright joins the Leg-4 consult roster
  (brandwright + evalwright + rigwright) — the registry's 2026-07-30
  nine-member claim finally reaches the card it claimed to have updated.
- RUNBOOK: member-bump-on-shipped-change rule codified — any change to a
  member's shipped files (evals and fixtures included) bumps that member in
  the same commit, because the claude.ai lazy re-upload is keyed on the
  member zip's version. 2.2.3 shipped three members' eval changes with no
  version signal; for commwright the stranded change was the name scrub.
- build.py: eval-provenance freshness now requires the head to name the
  CURRENT member version (a dated re-anchor to an old version used to pass —
  how linecaller's assertion suite sat at v1.1.0 through two releases);
  parity compares an installed peer brand definition against its declared
  home-repo source instead of skipping it (northstar mapped); clone parity
  lines are labeled per pack.
- NEXT.md refreshed (item 2 → confirm the 2026-08-07 branded `+install` zip
  actually reached claude.ai).

## [ossuary-v2.0.0] - 2026-08-08

- **Member renamed: `revenantworks-ossuary-cardcaller` →
  `revenantworks-ossuary-bonecaller`** (owner-directed, motif conserved —
  the ossuary claims `-caller`, and bones are the oldest dice). Major pack
  bump: a member's invocation name is a breaking surface. Collision-checked
  before the claim (`audit/COLLISION.md`, 2026-08-08 supersession): zero
  GitHub namesakes, unclaimed on npm/PyPI/crates.io; runner-up `shotcaller`
  rejected on the same bar. Directory, frontmatter `name:`, description
  trigger token, router, registry rows, root README, and both manifests
  moved; member history continuous.
- bonecaller 1.2.0: eval coverage completed to the house standard —
  first assertion suite (`evals/test-cases.md`, 7 cases), first
  `SOURCES.md`, and `evals/RESULTS.md` now exists, making the four surfaces
  that already pointed at it true (the 1.1.1 re-judge record previously
  lived only in trigger-evals' provenance note). Post-rename cold re-judge
  of the trigger suite recorded there.
- linecaller 1.3.0: description and compatibility follow the companion's
  new name; step 5 hardened — enrichment bullets are plain text,
  HTML-escaped before landing in the rendered card's drivers list (audit
  finding: a planted "quote" could smuggle markup into the artifact the
  companion renders verbatim); assertion-suite provenance re-anchored (the
  missed 1.2.0 re-anchor the old gate accepted).
- Pack CLAUDE.md: the stale "open asymmetry" seam paragraph replaced with
  the closure the registry and both descriptions have recorded since
  ossuary-v1.1.0 (the router asserted the opposite of the surface it
  governs).

## [foundation-v2.2.3] - 2026-08-08

- brandwright evals: the 1.2.0 roster/peer-selection mechanism finally has
  coverage — trigger suite 22 → 30 (17/13), assertion suite 16 → 23 (Cases
  17–23: named/scoped/ask selection, never-blend, peer-scoped audit with the
  cross-brand P0, absent-roster refusal, build-writes-peers), and a new peer
  fixture `brand-definition-saltmere.md` beside the primary (bumped 2.0.0 →
  2.1.0 with a roster table). Extended AND executed the same day: two
  independent blind judges 27/30 each (identical misses — the known #15/#17
  borderline pair, plus new #27, an authoring defect reworded in-pass with
  its single re-judge owed); Cases 17–23 first execution 7/7 PASS. Full
  record in brandwright `evals/RESULTS.md`.
- Owner-approved personal-identifier scrub on public eval surfaces:
  commwright's `case-04` fixture re-signed with a neutral name (re-baselined,
  not silently edited — frozen facts byte-identical; provenance updated in
  `RESULTS.md`), and local run paths in commwright's and agentwright's
  `RESULTS.md` ledgers redacted to `%TEMP%` (entries otherwise verbatim).
- skillwright pack-registry: the ossuary seam row moves from *one
  description* to *both descriptions* — the owed linecaller boundary clause
  landed (ossuary 1.1.0) and the cold re-judge is executed, so the seam note
  records the closure instead of the debt.

## [ossuary-v1.1.0] - 2026-08-08

- linecaller 1.2.0: the description gains the owed seam-closing clause —
  "not for reading an existing card and ledger/bankroll questions — the
  claude.ai companion revenantworks-ossuary-cardcaller owns those." Full
  10-row cold re-judge executed: 10/10, and row 9's old JUDGE tag retires
  (the exclusion is now stated text). `references/card-contract.md` also
  stops naming live brand palette tokens on this public surface — it points
  at the private repo's `style.py` as the single token source
  (brand-carriage hygiene).
- cardcaller 1.1.1 + linecaller 1.2.0: owner-approved personal-name scrub —
  the owner is no longer named by first name anywhere in either member
  (descriptions, bodies, contracts, README, eval prose). No trigger token
  moved; cardcaller's 8-row suite was re-judged cold anyway: 8/8. Both
  members' provenance re-anchored in the same commit.
- cardcaller README: the cloud routine is named by its full canonical name
  ("Project Longshot - Daily Card"), closing a stale short form.

## [ossuary-v1.0.1] - 2026-08-07

- linecaller evals: discharge the row-3 trigger debt owed since the
  `vault`→`ossuary` / `-picker`→`-caller` rename — re-read cold against the
  shipped `linecaller` token, PASS. R11 (a live idempotency assertion, not a
  cold-trigger read) stays open until a real pipeline run exercises it; noted
  in `RESULTS.md` rather than closed by assertion.

## [foundation-v2.2.2] - 2026-08-07

Ships content that had already landed on 2.2.1 without a bump — and the pack version
is the cache key, so an install could never receive it. That is the gotcha this repo
documents; this release is it happening for real.

- `LICENSE` x10 now read `Copyright (c) 2026 Revenantworks` (brand definition v2.1.14
  made the copyright line a naming class: the house, never a person).
- `pack-registry.md` carries the ossuary pack tables; `spec.md` records register 7 as
  resolved.
- `tools/build.py`: per-pack conformance notes (a latent bug the second pack exposed —
  every pack resolved to the FIRST pack's conformance line), and `--parity` no longer
  reports an installed **peer** brand definition as drift. A peer is installed from a
  private repo by design and absent from HEAD, so flagging it made parity a gate that
  could never pass — the inverse of one that never fails, and no more useful.

## [ossuary-v1.0.0] - 2026-08-07

**Second pack, first release from this repo — the citadel is now the canonical home
for every skill** (owner decision, 2026-08-07). `revenantworks-ossuary-linecaller`
and `revenantworks-ossuary-cardcaller`, both at member version 1.1.0, moved from
`MickMacPW/longshot`'s `skills/` into `packs/ossuary/skills/`. Names unchanged; no
member behavior changed.

New in this repo: `packs/ossuary/.claude-plugin/plugin.json` at 1.0.0, an `ossuary`
marketplace catalog entry, a pack router at `packs/ossuary/CLAUDE.md`, and the pack's
registry section — `ossuary` members, budgets, and seams — so `references/pack.md` is
generated for both members like foundation's nine. Measured bodies: linecaller 1145
tokens against a 1400 ceiling, cardcaller 805 against 1100, both far under the 5k
advisory and declared anyway so the pack starts with one comparable number per member.
The single boundary pair (linecaller ↔ cardcaller) is declared with its cold-listing
signal recorded honestly as **one description**: cardcaller's description excludes
running the pipeline, linecaller's says nothing about reading a card that already
exists, and the cold re-judge that would close it is owed, not claimed. Pack
conformance checks adopted: **O-1 decision-support only · O-2 never fabricate a
number** — both verbatim hard rules in both bodies.

**longshot keeps a working copy, by requirement.** The "Project Longshot - Daily Card"
cloud routine clones only that repo and reads linecaller's `SKILL.md` and two of its
`references/` files out of the fresh clone, and a user-scope junction points into it.
That copy is now a declared **downstream mirror** — same convention the repo already
uses for `docs/routine-prompt.md`: citadel is source of truth, the two must not drift,
and the mirror is byte-identical so `diff -r` is the drift check. Recorded in longshot's
`skills/README.md` and in its `CLAUDE.md` file map.

**Deferral-register item ⑦ is closed** (`packs/foundation/spec.md`) — resolved the
other way round: the pack moved in rather than the registry moving out of skillwright,
which dissolves the cross-repo source-of-truth problem the item was opened against.

**`tools/build.py` — a latent parser bug the second pack exposed.** `pack_lines()` read
conformance checks from the registry row's *Profile* cell, never matched, and fell
through to a whole-document search that returns the **first** pack's line — so ossuary's
generated manifest was stamped with foundation's checks and its 2026-07-13 adoption date,
with `--check` clean throughout. Fixed: new `registry_pack_notes()` reads each pack's own
Notes cell, and the whole-document fallback is gone in favour of a stated default. Two
unit tests added (one on the synthetic fixture, one asserting the live registry's two
packs cannot resolve to the same pair), plus number words 2–6 for the manifest's roster
line. Foundation's nine manifests are byte-unchanged by the fix.

Count integrity now spans two packs: registry 11 = folders 11 = manifests 11.

## [foundation-v2.2.1] - 2026-08-07

brandwright 1.2.1 — the neutral definition's palette storage shape now has slots for
everything 1.1.0's derivation rules produce: the computed neutral ladder, accent
base/ink pairs, per-mode light, shared accents, and the separation floor. Without them
the rules had nowhere to land on a new brand, and the absence read as compliance.

## [foundation-v2.2.0] - 2026-08-07

**brandwright holds several brands now.** It could carry exactly one active
definition, so a personal or social brand could not sit beside a product brand
without overwriting it. brandwright 1.2.0 adds a roster and a selection step.

- `brand-definition.md` carries the **roster** — each brand'"'"'s slug, the surfaces it
  owns, its peers — and peers live in `brand-definition-<slug>.md` siblings that
  open only when selected, so the always-open cost stays one file.
- **Selection is a named workflow step**, resolved before any other work: named in
  the request, else scoped by the target, else **asked** in one line. Topic and tone
  never decide it — a personal-voice request aimed at a product surface is exactly
  the case to ask about rather than infer.
- **Cross-brand law**: never apply one definition to a surface another owns, never
  blend two in one output; they share a surface only where the owning definition
  declares an attribution mark for the peer.
- Build writes peers: a build for an unrostered brand creates its sibling and adds
  the roster row in one pass. Scope and coexistence are asked inside the existing
  firewall-map group — the count of 14 build groups is load-bearing.
- `tools/apply-install-swaps.py` takes `<primary-dir> [<peer-dir> ...]`, overlays
  peers as siblings, and warns when a peer is absent from the primary'"'"'s roster
  (overlaid but unreachable). Single-dir invocation is unchanged.
- brandwright'"'"'s body budget raised 3300 → 3450 with its reason recorded: the
  selection block is always-relevant routing and must be body-resident.

## [foundation-v2.1.0] - 2026-08-07

Additive doctrine release — no rename, no entry point moved, no description
changed on any member. Two members carry the pass; the other seven pick the
fresh manifests up on their own next release (`restamp: lazy`).

- **brandwright 1.0.2 → 1.1.0.** Palette doctrine, which until now was a
  role-token rule and a drift sweep note. `audit-doctrine.md` gains **Build —
  palette derivation** (D-1 to D-7): neutrals computed in OKLCH at the brand's
  own accent hue rather than hand-picked · a ~1.13:1 visibility floor per
  elevation step · the border token split quiet/lit with the lit one clearing
  3:1 on its own surface · lit and glow derived from the accent's own lightness
  with the contrast floor as a `max` second term, carrying the general rule that
  a rule tuned on one hue is re-tested on every hue before it becomes doctrine ·
  colour never carrying state alone (WCAG 1.4.1) · a shared accent set proved by
  a ΔE00 coverage matrix and optimised jointly rather than member-by-member,
  with semantic overrides recorded · CIEDE2000 as the separation metric with a
  regional floor where the wheel is crowded. The **palette drift** sweep note
  now puts the neutrals in scope and requires the ratios recomputed and
  reported. `application-doctrine.md` gains **Palette inheritance — structure,
  light, and marks**: structure may be shared system-wide, light belongs to one
  identity and one mode, a multi-mode brand needs a complete set per mode with a
  stated switch condition, and a parent accent may cross onto a child's surface
  as attribution but never as its light.
- **skillwright 1.0.6 → 1.1.0.** `rubrics.md` gains **Generator classes G-1 to
  G-3** — derive the source's section list or fail loudly rather than
  skip-and-continue, ship a `--check` parity mode as part of the generator, and
  detect stale output in the target directory — plus **Naming-class coverage**,
  the rule that a naming convention binds every class carrying a name, display
  names and artifact titles included, and that ids carry no cadence suffix.
  Wired from the body by two clauses at a cost of 33 tokens; the 7,800 budget row
  is unchanged and the member now sits 17 tokens under it.

Both passes are neutral by the brand-carriage law: the doctrine states
derivations, thresholds, and metrics, and adds no palette value, brand name, or
identity string anywhere.

## [foundation-v2.0.0] - 2026-08-07

The `revenant` → `revenantworks` migration (brand definition v2.1.0, History
rows dated 2026-08-06; owner-adjudicated 2026-08-07). Breaking rename — the
marketplace identity and every member name move; content is otherwise
unchanged, so no member version bumps and no eval re-anchors are owed.

- **Marketplace renamed `revenant` → `revenantworks`** (`marketplace.json`
  `name` + `owner.name` → `Revenantworks`). The platform has **no marketplace
  rename mechanism** (COLLISION.md C3/C4 — kept as record, supersession note
  appended): every `<plugin>@revenant` reference breaks by design. The owner
  adjudicated execute-anyway; the single-consumer estate migrates by local
  remove-and-re-add of the marketplace (`claude plugin marketplace add` under
  the new name, then `claude plugin update foundation@revenantworks`). The
  plugin keeps its name — `foundation` — so no `renames` map applies.
- **All nine members renamed** `revenant-foundation-<member>` →
  `revenantworks-foundation-<member>`: directory names, `name:` frontmatter,
  H1s, eval files, references, and every cross-reference, registry and
  manifests included. Each member CHANGELOG carries a dated rename note;
  version history is continuous across the rename.
- **Brand token** in the registry's Build defaults and each member's
  `metadata.brand` label → `revenantworks`.
- **Tooling follows**: `build.py` (registry path, `--parity` clone/cache
  surfaces now `marketplaces/revenantworks` and `foundation@revenantworks`),
  `test_build.py` fixture, `apply-install-swaps.py`, README/RUNBOOK commands.
- **promptwright budget row 8850 → 8860** — the member name grew 5 chars and
  appears in the body; bookkeeping, no content change.
- **LICENSE** (root + all nine member copies): copyright now carries both
  founding names, QuaziDed · DeD Pixel, per the definition's identity map.
- Frozen records keep the old strings by design: `audit/AUDIT.md`,
  `audit/COLLISION.md` (each with a dated supersession note),
  `AUDIT-2026-08-05.md`, `ledger.md` dated entries, predecessor-era eval
  ledgers, and this file's 1.0.0 entry.
- **Install-parity consequence, recorded not chased**: until the local
  remove-and-re-add lands, `build.py --parity` cannot see the old-name
  install (`marketplaces/revenant`, `foundation@revenant`) and reports
  nothing-installed/skip. The claude.ai copies still carry 1.0.0 bodies under
  the retired names — register ⑨ widened accordingly.

## [foundation-v1.2.0] - 2026-08-05

The AUDIT-2026-08-05 apply pass — every verdict from the adversarial
refinement audit (report at repo root), applied member by member on approval.

- **Registry**: new rigwright ↔ tokenwright seam row (motive-keyed, signal:
  one description) closing the undeclared "trim my CLAUDE.md" / "slim my
  CLAUDE.md" boundary opened by rigwright's 2026-07-30 addition; the stale
  naming note now counts three CLAUDE.md descriptions. Seam note records the
  close. 12 → 13 seams; all nine manifests regenerated.
- **promptwright 1.3.0**: Tier routing gains the user-named-target override
  (a model or effort the user names wins — built to, noted as user-directed,
  better fit offered in one line; Entry — Model bound identically). Four
  lossless trims offset it; body lands exactly at its 8,850 budget. Case 39.
- **tokenwright 1.1.0**: description gains the rigwright boundary clause
  (802 → 894 chars). Trigger evals extended (Y11/N11), 22 rows.
- **agentwright 1.1.0**: description slimmed 992 → 950 chars, every cue
  kept; the ceiling-riding fix `build.py`'s warn text had scheduled.
- **skillwright 1.0.6**: lossless trim at the two audit-named sites (Build
  step 6 registry guard; bare-invocation cap); Case 14/17 anchors intact.
- **rigwright 1.0.2**: description names hooks in the artifact list
  (952 → 959 chars).
- Cold re-judges of the four moved routing surfaces (tokenwright,
  agentwright, rigwright trigger suites; promptwright's did not move) are
  owed and recorded as owed in each suite's provenance line, not claimed.

## [foundation-v1.1.5] - 2026-08-02

lorewright brought current, promptwright gains two tier-routing rules.

- **lorewright 1.0.2 → 1.1.2.** The v1.1.0 doctrine (Selection/Decision class
  split, four-slot Selection recommendation, seeded must-have gate,
  independent-evidence-first, coverage disclosure, purchase link) had been
  authored in a separate session and never installed — repo, marketplace, and
  cache had all silently stayed on 1.0.2 with 23 cases. Installed as built.
  **1.1.1:** Finding G1 applied — §4a's Top overall slot now states the
  must-haves gate explicitly, matching the other three slots; Case 27
  re-confirmed. Cases 30, 32, 34, 36 cold-executed for real with live
  search/fetch (the four whose Asserts need real retrieval) — 4/4 PASS,
  logged in `evals/RESULTS.md`; the remaining 12 of Cases 24–39 are authored,
  not yet cold-run. **1.1.2:** tokenwright slim, no behavior change —
  `SKILL.md` body cut ≈3040 → ≈2717 tokens; registry row raised 2700 → 2750.
- **promptwright 1.1.1 → 1.2.0.** Tier routing (Phase 5) gains two
  role-based overrides, shared by the standalone Model entry and plan grain:
  a planning/orchestrator subtask defaults one effort notch lower (high
  effort over-thinks and scope-creeps a plan); a review subtask checking
  another model's output defaults to a different model family, stakes
  permitting. Closes the gap found by a skillwright niche-verdict + gap scan
  run against a candidate 10th foundation member (an orchestration skill,
  informed by real-world r/ClaudeCode prior art) — plan grain already covers
  the candidate's stated job end-to-end except these two rules, so a new
  pack member wasn't justified. Case 38 added. Registry row raised
  8800 → 8850.
- Roster and seams unchanged (9 members, 12 seams); seven members untouched.

## [foundation-v1.1.4] - 2026-08-01

Parity tells the truth now, and carries the two records files that had no
release to travel on.

- **`--parity` widened from `SKILL.md` frontmatter to every shipped file.**
  The narrow scope reported **clean** twice while the loaded copy was stale:
  the lagging files were `ledger.md` and `spec.md`, which are not frontmatter
  and so were never compared. It now lists each file as missing, differing or
  extra, normalises line endings (a CRLF working tree vs an LF clone is not
  drift), and skips runtime markers. Verified by running it against the real
  stale install, where it named exactly the two files and nothing else.
- **skillwright 1.0.5** — Install parity re-scoped to match, with the lesson
  stated once: a detector narrower than what it certifies produces false
  assurance, which is worse than no detector because it ends the
  investigation.
- **Delivers `ledger.md` and `spec.md`** as of `8fdeeb9`, the post-1.1.3
  docs commit that had no pack bump to ride. Records only — no skill loads
  either at runtime.
- Roster and seams unchanged (9 members, 12 seams); eight members untouched.

## [foundation-v1.1.3] - 2026-08-01

Pack-wide prose pass: every member's own files (SKILL.md, README, SOURCES,
reference docs) and the root/pack-level docs (README, this file, RUNBOOK,
NEXT, the always-on router, decisions.md) were rewritten for register —
connector cleanup (em dash and " - " used to join clauses that read better as
two sentences, matched-pair parenthetical asides left alone), cross-referenced
rule duplication (a rule stated in full in two places now has one home and one
pointer), and a few wording/consistency fixes. No rule, gate, count, or entry
point moved anywhere, so no eval re-anchor is owed pack-wide.

- **commwright → 1.0.2** — its own SKILL.md and README used em dashes in the
  sentences announcing its no-dash H1 rule; the framing prose now matches the
  policy it states. Rule bodies and `humanize.md` were already dash-free.
- **skillwright → 1.0.4** — the shared "foundation seam notes" history in
  `pack-registry.md` (the seam-table's canonical source, read by every
  member's generated `pack.md`) reformatted from one ~700-word paragraph into
  a dated list, same facts; plus SOURCES.md wording and reference-file
  connector fixes.
- **promptwright → 1.1.1** — `model-snapshot.md`'s footnote markers had a gap
  (¹, ³, ⁴ with no ²); renumbered sequentially. `hostile-interpreter.md`
  trimmed to stop re-stating SKILL.md's own failure-shape definitions.
- **tokenwright → 1.0.2** — SKILL.md's Preservation-contract list was missing
  an item (dependency declarations and absence behaviors) that
  `waste-taxonomy.md` and this file both already carried; added, closing a
  real 6-vs-7 gap, not a style choice.
- **agentwright, brandwright, lorewright → 1.0.2 each** — a duplicated
  quarantined-reader rule (agentwright), a triple-duplicated per-element
  exclusion example (brandwright), and one telegraphic line (lorewright) each
  now single-homed or reworded.
- **evalwright → 1.0.2, rigwright → 1.0.1** — SKILL.md rules that restated a
  reference file's rule in full (count-drift/provenance for evalwright,
  the secrets rule for rigwright) now cross-reference their one home.
- **`spec.md`** (the live baton, not itself a member): the Current-status
  block now reflects 1.1.2/1.1.3 instead of stopping at 1.1.1; the frozen
  1.3.2-pass history paragraph gained an inline tag marking it as the
  pre-rebaseline snapshot, since the live deferral register 100+ lines later
  states a different, current register count and the two were easy to
  mistake for a contradiction.
- **`ledger.md` and `IMPROVEMENTS.md`** headers now point at this file's own
  predecessor-era disclaimer instead of independently restating it — three
  copies of the same disclaimer collapsed to one canonical text plus two
  pointers. Neither file's dated historical entries were touched, per their
  own append-only doctrine.
- **`tools/build.py` fix, found by this pass:** the seam-note extractor
  assumed the registry's seam-notes annotation was always one physical line
  and silently returned nothing otherwise. Reformatting it into a dated list
  (above) tripped that assumption and would have shipped all nine `pack.md`
  copies with the section missing; the extractor now captures a multi-line
  block up to the next top-level pack annotation. Caught before commit, not
  after.
- Roster and seams unchanged (9 members, 12 seams); no member's rules,
  counts, or entry points changed except tokenwright's one named content fix
  above.

## [foundation-v1.1.2] - 2026-08-01

Frozen records marked, so no version number anywhere in the pack can be
mistaken for a current one. Delivery release for the 1.1.1 post-tag work.

- **13 `evals/` files across 7 members gained a frozen-record header** naming
  their version numbers as predecessor-era and pointing at the root note. The
  remaining eval files already carried the disclaimer. **Rows, verdicts,
  dates, counts and pass rates are untouched.** The ledgers stay evidence,
  which is why this is a marker and not a rewrite.
- **agentwright, brandwright, commwright, evalwright, lorewright, tokenwright
  → 1.0.1; skillwright → 1.0.3** (its 1.0.2 doc fix rides here too, having
  been undeliverable at member grain).
- Also carries **skillwright 1.0.2** and the `tools/build.py` date-anchoring
  from `3a3b084`, which had no pack bump to travel on.
- **`build.py` now prunes superseded `dist/` zips.** It wrote
  `<member>-<version>.zip` and never removed the old one, so every bump left
  its predecessor sitting beside the current build: 16 zips for 9 members at
  this release. Since release-doctrine treats `dist/` as the upload source of
  truth, a stale neighbour is a mis-upload waiting to happen. `dist/` now
  holds exactly one zip per member.
- Roster and seams unchanged (9 members, 12 seams); promptwright and
  rigwright untouched.

## [foundation-v1.1.1] - 2026-08-01

Install-parity release: the tooling fix from `4800918` reaching the copies
that actually load. Cut for delivery, not for new capability.

- **The pack version is the plugin cache key.** `claude plugin update`
  compares pack versions, so a member-only bump never reaches an installed
  user: the marketplace clone moves, the loaded cache does not, and the
  update reports "already at the latest version". skillwright 1.0.1 rode main
  and stayed unreachable until this bump, which is the whole reason it
  exists. Recorded in `release-doctrine.md` — Install parity and RUNBOOK
  step 5.
- **skillwright 1.0.1** — release-doctrine's Install parity described one
  installed copy where Claude Code has two (the clone an install reads from,
  the cache it loads); now states both surfaces, the two-step order, the
  cache-key rule, and that parity knows nothing about claude.ai.
- **`tools/build.py --parity`** diffs the clone **and** the loaded cache,
  names which surface drifted, and skips each cleanly when absent (CI-safe).
  Verified against a real stale cache, not trusted on a clean run.
- Roster and seams unchanged (9 members, 12 seams); no member behavior moved.

## [foundation-v1.1.0] - 2026-08-01

- **promptwright 1.1.0** — Entry — Model gains plan grain: a handed-in plan
  with a targets ask gets a per-subtask target table (tier + model,
  effort/depth, inline-or-subagent, one-line why) instead of a single
  recommendation. A living-table contract rows an emergent mid-session
  subtask through the same tier logic before it dispatches; a standing-rule
  line rides beneath every table, its layer placement left to rigwright.
  Trigger suite 30 → 34 rows (17/17), assertion suite 36 → 37 cases; see the
  member's own CHANGELOG and `evals/RESULTS.md` for the full account.
- Router `packs/foundation/CLAUDE.md` gains the plan-table route cue and the
  living-table compose bullet.
- Roster and seams unchanged (9 members, 12 seams); no other member touched.

## foundation 1.0.0 — 2026-07-31 — the wright baseline

Nine build-time wrights, one plugin (`foundation@revenant`), each routing on
its own description and standing alone on any Agent Skills surface. Every
member ships with its references, trigger evals, and an assertion suite;
the pack's cold trigger baseline is 97/97. Versions are 1.0.0 across the
pack, plugin manifest, marketplace entry, and all nine members.

The 1.0 feature set, member by member (each member's own CHANGELOG carries
the full list):

- **skillwright** — builds, audits, ports, and integrates install-ready
  Agent Skills and whole packs: research-backed niche verdicts, dual-scored
  audits carrying the S-1…S-4 security pass and a register-only prose pass,
  sanitizing port with PORT-REPORT, pack-wide integrate under count
  integrity, 60-day refresh plus the pack-wide upkeep sweep. Ships
  spec-clean neutral.
- **promptwright** — seven-phase prompt builds with five-dimension scoring,
  a named-origin framework menu, a gated fast path, hostile-read hardening,
  the knowledge-vacuum check, S/A/B/C model-tier routing with the standalone
  `promptwright model` pick, and an optional offline HTML prompt card.
- **commwright** — channel-profile drafting under the silent H1–H9 humanize
  rules, a humanize entry for handed-in text, report-only message audits,
  cadence sets, and a pre-publish redaction sweep; it never sends.
- **agentwright** — ten-area ops-spec design sized blast-radius-first, emit
  into seven profiled platforms with per-control enforcement-gap tables, the
  five-class runtime security-scan, trust-tier doctrine, and a restraint
  that refuses autonomy plus irreversibility without a human gate.
- **lorewright** — evidence-graded verdicts ending in one direct
  recommendation with a flip condition, versioned playbooks verified against
  primary sources, four-grade claim tagging, and source-is-data-never-
  instructions injection handling.
- **brandwright** — the single home of brand and voice: the 14-group
  definition (ships neutral), the apply cascade, a seven-category drift
  audit with the P0 score floor, and four export payloads including the
  offline HTML brand-guide card.
- **evalwright** — coverage-mapped trigger-eval tables and assertion suites
  under count integrity and the zero-runtime-dependency law; five-check
  suite audits and diff-scoped refresh.
- **tokenwright** — exact-or-disclosed-estimate measurement, the W1–W10
  waste taxonomy, the nine-rung lossless→lossy ladder behind a preservation
  contract, net-cost accounting with cache mechanics, the description-cap
  rule, and set-level budget plans.
- **rigwright** — standing Claude configuration (Project instructions,
  CLAUDE.md, `.claude` layout, `.mcp.json`) built and audited through the
  seven-layer placement stack, with secrets restraint and a hard boundary to
  agentwright for anything unattended.

Pack-level:

- The always-on router (`packs/foundation/CLAUDE.md`): the routing table,
  the composition seams, and the pack conventions — neutral by default, one
  catalog one gate, audits report rather than rewrite, declared
  dependencies, stamped volatile surfaces on a 60-day cadence.
- Registry-derived build and validation (`tools/build.py`): the pack
  registry is the single source of truth for rosters; the build syncs
  manifests, validates every member, and produces the `dist/` zips;
  `--check` is CI mode, `--parity` verifies the installed clone.
- Brand-carriage law: brandwright is the only brand carrier anywhere — repo
  or installs; `tools/apply-install-swaps.py` overlays a private definition
  onto the neutral repo copy to produce the branded install zip.
- The `foundation-upkeep` cloud routine carries the volatile-surface sweep
  and the brand-escrow reminder.
