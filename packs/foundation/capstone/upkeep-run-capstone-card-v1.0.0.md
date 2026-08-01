UPKEEP RUN v1.0.0 — foundation capstone: sweep the pack, close the debt, ship

TRIGGER + INPUTS
Run this to bring an already-shipped pack from "released" to "clean" — the
maintenance counterpart to FORGE RUN, which ships one new skill. Use it at a
week/sprint close, before a release, after a ledgered eval re-run surfaces
findings, or whenever the honest answer to "what's still open?" is "I'd have to
go read every RESULTS.md to tell you."
Inputs: {{pack}} — pack + profile (default foundation / standalone) ·
{{scope}} — optional cap (a member list, or a class of finding) ·
{{budget}} — optional; state it up front so LEG 2 can scope to it.

Precondition: the pack is on `main`, working tree clean, and `build.py --check`
passes BEFORE anything is touched. If it does not, stop and report — an upkeep
run never opens on a dirty baseline, because it cannot then prove what it broke.

LEG 0 — ground the state in the repo, never in a transcript
Read the repo, not the last conversation. A prior session's summary of what is
open is a claim, not evidence; treat it as a lead to verify. Establish, by
command: HEAD vs origin · working tree state · each member's frontmatter
version · `spec.md`'s status line and deferral register · `decisions.md`'s
open decisions. Then grep every member's `evals/RESULTS.md` for the pack's own
open-item vocabulary — "remain open", "left open", "still owed", "untouched by
this pass", "authored, not executed", "NOT RUN", "FAIL". Read the hits; a
finding marked CLOSED in a later entry is closed even if the original text
above it still reads open, and a finding whose fix landed in a sibling session
may be closed already. Verify before you list it.
HANDOFF → <state>HEAD · per-member versions · every open item with its
member, its ledger location, and whether it is doctrine, suite, or owner-call
</state>.

LEG 1 — separate the four kinds of open
Not everything open is debt, and the pack's own conventions say so. Sort every
item from <state> into exactly one bucket, and say which:
· DOCTRINE GAP — a rule missing, contradictory, or stated twice differently.
  Real work. The fix lands in SKILL.md or a reference, never only in an assert.
· SUITE DEFECT — the behavior is correctly specified but the eval cannot see
  it, cannot fire, or passes on inference. Fix the case; do not patch the skill
  to satisfy a wrong assert.
· RECORDED-NOT-BUILT — an idea logged under the pack's own convention. It is
  at rest, not overdue. Moving it needs a gate, not a sweep.
· OWNER CALL — gated on a decision or a precondition outside the code (a second
  pack existing, a named target platform). Report it; never build it
  speculatively to look thorough.
HANDOFF → <catalog>every item, bucketed, with a one-line recommendation</catalog>.

LEG 2 — ONE GATE
Present <catalog> complete, once, with per-item recommendations and a rough
cost. This is the run's only approval round; per the pack's turn-shape law,
"apply all" / "just do it" anywhere in the request skips it. If the true item
count is materially larger than the requester's stated understanding — they
said "one each" and it is fifteen — say so plainly at this gate BEFORE any
work starts. A sweep that quietly triples its own scope is a worse failure than
one that stops to ask.
ON EMPTY: a pack with nothing open is a successful Upkeep Run. Say so and stop;
do not manufacture findings. (Same law as skillwright's already-strong audit and
tokenwright's already-lean restraint.)

LEG 3 — fix, one member per worker, no shared files
Approved DOCTRINE and SUITE items only. Parallelize by member — each worker
owns exactly one member's directory and touches nothing outside it. Every
worker carries these constraints verbatim:
· FIX AT THE DOCTRINE LEVEL. A finding closes when the rule is stated on a
  surface the run actually loads. Tightening the assert alone is how a finding
  reappears next quarter.
· SINGLE-HOME IT. State the rule once; reference it everywhere else. If it
  already exists somewhere, scan AGAINST it — do not write a second copy.
· REUSE THE EXISTING SCALE. Severity, score bands, and vocabulary already
  exist. A second scale is a new defect.
· THE STANDALONE LAW. No member may read, load, or depend on a file in another
  member's directory. Cross-member partition rides on a boundary sentence in
  the `description` — routing metadata, not a load-time dependency. This holds
  even when sharing would be tidier; a shared reference file breaks every
  install where the sibling is absent.
· LEDGER HONESTLY. New dated entry at the TOP of `evals/RESULTS.md`, in the
  file's own voice, with mechanical evidence — grep counts, line numbers,
  before/after states, re-derived arithmetic. Never claim a run you did not
  perform; "AUTHORED, NOT EXECUTED" is a valid and respected result.
· COUNT INTEGRITY. Declared counts must equal actual, verified by grep, in
  every file that states one.
· VERSION ARITHMETIC. Patch for a doctrine/suite correction against unchanged
  behavior; MINOR for a new capability or entry point. Bump `metadata.version`,
  add the dated CHANGELOG entry in the member's own style.
· DESCRIPTION BAND. If the `description` changes: hard cap 1024, house band
  600–800. Measure mechanically and report the count. Name every fragment
  traded away AND the eval row that rode on it — a silent trim is how a passing
  row starts failing for reasons nobody can trace.
HANDOFF → per member: files changed with line refs · version · description
char count · declared-vs-actual counts · `build.py --check` result.

LEG 4 — verify the constraints yourself, do not accept the report
A worker's summary is a claim. Re-run independently from the repo root:
· `build.py --check` — clean, whole pack, not per member.
· The standalone law — grep each touched member for a path into any sibling's
  directory. Zero hits, or the run is not done.
· Description lengths — measure all members, confirm the band.
· Count integrity — grep declared vs actual on every suite touched.
A worker that reports "clean" and a grep that disagrees means the grep wins.

LEG 5 — release, or say plainly why not
Member versions moved; the PACK version has not. Decide and act:
· If any member gained a capability → the pack takes a MINOR bump.
· Bump `.claude-plugin/plugin.json` AND the marketplace entry — both, they
  drift independently and an installed plugin compares the manifest string.
  A pack whose contents changed under an unchanged version string will be
  refused by `/plugin update` as already-current: the update is not broken,
  it is correctly declining to update something claiming not to have changed.
· Root CHANGELOG entry · `spec.md` status line and deferral register · tag
  `<pack>-vX.Y.Z` · push · then the install-side update commands for the human
  to run (an agent cannot run the interactive plugin flow).
ON NO RELEASE: state it — "in-place at current member versions, no tag" — and
say what that leaves stale for anyone running the installed plugin rather than
the repo.

OUTPUT CONTRACT
Close with four lines, in this order:
CLOSED — what actually landed, by member and version.
OPEN — what remains, bucketed as in LEG 1, each with why it stayed.
DEBT — every claim in this run that is text-level rather than executed, named
  as such. Owed eval re-runs go here, always, even when everything passed.
NEXT — the one thing to do first next session, and its precondition.

Anything the run declined to do is reported, never omitted. A finding recorded
and left open with its reason is a result; a finding quietly dropped is a
defect in the run itself.

RE-RUN CONDITION
Run at each release close, and after any ledgered eval execution that produces
findings. Not triggered by a member patch that closes nothing. If the previous
Upkeep Run's DEBT line still lists owed executions, discharge those first or
restate them — debt that survives two runs unmentioned has stopped being
disclosed and started being hidden.

Run log: v1.0.0 authored 2026-07-27, derived from the 2026-07-26/27 close-out
that closed fifteen recorded findings across four members, fixed the build
template's missing `volatile`/`body_budget` keys, and built the security-scan
split (agentwright Entry — Security-scan · skillwright Entry — Audit security
pass) — the run this card generalizes.
