# NEXT — remaining follow-ups

Updated 2026-08-17.

## Standing decisions (2026-08-17)

- **Frozen members: tokenwright, commwright, evalwright** — "frozen — no
  bumps unless broken". They stay installed (rig junctions). No eval
  re-anchoring, no refresh restamps, unless a change lands for a real defect
  — a security finding is a real defect. Consequence recorded here rather
  than hidden: tokenwright's `measurement.md` stamp (2026-07-27) reaches 60
  days on 2026-09-25 and is left for the upkeep routine to flag; refreshing
  it is an owner call under the freeze.
- **Ossuary marketplace release train frozen.** The pack stays canonical in
  this repo and ships to its only consumer by the longshot mirror
  (`tools/release.py` re-syncs it) plus the rig junctions (linecaller → the
  mirror, bonecaller → this repo). `ossuary-v2.4.0` (this session) is the
  closing release; a later ossuary change is mirrored and junction-live
  without a marketplace tag unless the owner asks for one. The public
  marketplace entry stays registered.
- **Rig install is by junction** — see RUNBOOK. `claude plugin update` is out
  of the loop; `--parity` is CI/public-only.

## Owed by hand

- **Cold re-judges and re-runs owed** after the 2026-08-17 audit: every
  member's `evals/` head lists them (authored-not-run injection probes on
  every ingesting entry point; linecaller R5/R6/R12, bonecaller B1/B6, and
  the trigger re-judges older bumps already owed). None is claimed.
- **claude.ai re-uploads** — see the `README.txt` in the estate's
  `artifacts/exports/skills-2026-08-17/` folder (bonecaller and the branded
  brandwright install zip are required; the rest optional).
- **longshot:** a `python -m longshot` subcommand for the first-Monday
  ledger block arithmetic (linecaller 1.7.0 computes it with `PY` from the
  two files for now); the routine prompt's fixed-artifact publish step now
  duplicates linecaller step 8 — drop it from the prompt at the next prompt
  edit and re-capture `docs/routine.md`.
- The rig's local marketplace registration still names the source
  `revenantworks/citadel` (GitHub redirects); harmless, cosmetic.

## From the 2026-07-31 audit

Older list, still open where marked. Discharged: the wright 1.0.0 baseline release
(`foundation-v1.0.0`), the cold trigger re-run (97/97,
`packs/foundation/ledger.md`), registry-parser unit tests in CI, Claude Code
plugin install + parity, and the nine claude.ai re-uploads (owner,
2026-08-01).

1. **Re-verify `audit/COLLISION.md` when its 60-day stamp ages out**
   (~2026-09-29). The naming verdict rests on July-2026 collision data; a
   claimant going commercial (skillwright.app especially) triggers a revisit.
2. **Confirm the branded brandwright reached claude.ai.** A branded
   `+install` zip was built 2026-08-07 (`dist/install/`), which supersedes
   this item's old "the copy uploaded today is the neutral one" state — but
   whether that zip was actually uploaded cannot be verified from this
   machine. If it was not: delete-and-re-upload the `+install` zip per the
   RUNBOOK.
3. **Discharged 2026-08-18 — orchestration-skill candidate scan (opened 2026-08-01,
   blocked 2026-08-12).** The candidate shipped as `revenantworks-foundation-
   dispatchwright` 1.0.0: a session-fan-out skill that decomposes a request into
   units, tiers each one through promptwright's target table, dispatches with a
   durability contract, and reconciles against origin. The prior-art block (a
   private Telegram thread never pasted into a session) was not resolved before
   the build — this entry records that gap rather than hiding it. Two things this
   item still owes: the routing-seam row for dispatchwright's three boundary pairs
   (promptwright, rigwright, agentwright) was not added to the pack registry, and
   no assertion suite exists yet, both named in the member's own README.
