# Release Doctrine — cutting a pack version

> What a pack release requires beyond the member work. Loaded only when the deliverable **is** a release or the close of a versioned pass — no build, audit, port, or integrate run reads it. The worked example throughout is this pack's own shipped history — the 2026-07-24 hygiene release, the 2026-07-23 run before it, and the pass that opened after. Those releases are cited **by date, not by tag**: they predate the 2026-07-31 re-baseline, so their tags and commits no longer exist and two of their names have since been reused by unrelated releases. The lessons hold; the version numbers do not resolve.

Nothing here is a rule this file invents. Each section below names the mechanism that owns its step — the pack build script, the CI job, the RUNBOOK loop, or the pack-spec baton — what it looks like when it fires, and what the release still has to decide by hand. Where a step has no mechanism behind it, it says so and stands as adopted practice the pack has kept release to release, owed by hand. **The eval ledger is the mixed section:** two of its checks are gated and the rest is owed by hand, so read that one step by step rather than as a whole.

## Contents

- Two clocks — member versions and the pack version
- The eval ledger — before, after, and what may not be written *(partly gated)*
- Count integrity at release scale
- Install parity — the live drift mechanism
- Release assets — the tag is not the release
- The deferral register — findings recorded as evidence
- Release order

---

## Two clocks

A pack carries two independent version series, moving on different triggers.

**A member bumps when its own contract changes** — a new entry point or a new capability, in the baton's own wording — and the bump rides a dated entry in that member's own CHANGELOG. Editing existing text is not a contract change: the 1.2.0 pass rewrote all eight member descriptions and bumped nothing, while the same pass's commwright work added an entry point and a default register and moved that one member alone. Post-release audit fixes take a patch bump on the members actually touched; the 2026-07-24 hygiene release patch-bumped all eight because the audit had found something in each — and they landed on different numbers, because two of them had already taken a patch at the previous release's post-audit. The pack version cannot be read off any member, and members mid-pass sitting at several different versions is the healthy state, not drift.

**The pack bumps once, at the close of the pass**, and the tag `<pack>-vX.Y.Z` is cut from that state; everything the pass touched rides that one tag. An open pass therefore has a known-but-unwritten tag — the baton names it, the files do not carry it yet.

The pack version lives in **two** files — the marketplace catalog entry and the pack's own plugin manifest — and they must agree. Write both in one stroke (`build.py --bump-pack <pack> <X.Y.Z>`, which also scaffolds the root CHANGELOG heading). Hand-editing one of the two is exactly how this pack shipped a 1.0.0-vs-1.1.0 split-brain for a month with CI green: nothing compared them until the 1.1.1 release added the check.

Two gates hold the arithmetic, both in the build script, both hard failures: a member's CHANGELOG head must equal its frontmatter version, and the plugin manifest must equal the marketplace entry.

## The eval ledger

**Mostly convention, partly enforced — know which is which.** `build.py`'s `validate_evals()` globs `evals/*.md`, so `RESULTS.md` *is* read, and two things in it are mechanized: the FIRST `vX.Y.Z` token following the first `Provenance`/`derived`/`target` keyword in a file's first six lines warns when it does not equal the member's version and no dated re-anchor line sits in those same six lines (so a head opening on its derivation history trips it even when a later line names the current version), and a numbered row that follows prose instead of sitting in a table warns as orphaned from the count checks. Both are warns today and flip to failures at the next tag. Nothing else here is enforced: no exit code checks that a before/after pair exists, that a pass rate is honest, or that a row marked NOT RUN was ever run. What follows is what this pack's releases have actually done, kept by hand where no exit code keeps it.

The recording format itself is not this file's either — it is evalwright's, `eval-doctrine.md` § Provenance discipline: a dated `evals/RESULTS.md` section, date · target version · runner · per-row verdicts · pass rate. The release-specific delta is the **pair**: a release that touched a routing surface leaves both the before and the after in that file, so the earlier run stands as the baseline the next one is read against.

- **The after-run is judged cold** against the changed surface, then compared to the baseline. "No flips" is not the whole result: a row that now passes on a thinner margin is recorded as **watched**, naming the single clause it survives on. Skillwright's own post-slim run is the pattern — 34/34 both ways, five watched rows, and the after-run *corrected the baseline's own note* (the baseline claimed brand application had left the description; the slimmed port clause still carried "rebranding", so the row passes on the deferral sentence, not on the word's absence).
- **The pack-level number is quoted both ways.** The description pass reports 187/187 against a 185/187 baseline — one number without the other is not a ledger.
- **What may not be written: a row that was not run.** A suite that was authored but not executed is recorded as authored-not-executed, never scored. A bump that changed no routing surface owes no run at all — say that in the changelog rather than manufacture a pass rate.
- **Provenance re-anchors in the same commit as the bump** — one of the two gated parts of this section; the orphan-row scan is the other. Provenance discipline is evalwright's rule, stated in `eval-doctrine.md` § Provenance discipline and already deferred to by Build step 7; the release-specific delta is only *the same commit*, so no tag ever carries a suite pointing at a version the tag itself replaced. The build script's check is narrower than the rule: it reads only the first six lines and only the first version token after the first provenance keyword, so the discipline is owed by hand and the check merely catches the common miss. Its docstring records the warn as a failure at the next tagged release.

## Count integrity at release scale

The three-number contract — registry **roster** rows = `pack.md` **roster** rows = manifests written — is Entry — Integrate step 5's, and the SKILL body states it. The build script closes every full run and every `--check` with its own `count integrity:` line, and the two are not the same three numbers: the script prints `registry N = folders N = manifests N`, where *folders* is registry rows confirmed to have a directory on disk — not a scan of the skills folder. The whole run is registry-derived, so it catches a registry row with no folder behind it and nothing at all about a folder no row names: an unregistered member is never counted, never drift-compared, never validated. The roster-row count stays Integrate's own check, and no script prints it. In this pack all three land on 8 today, so the difference is invisible — until someone chases a real mismatch and hunts for a count the script never emitted.

Read the line before tagging anyway: a release cut over a mismatch ships a roster that disagrees with itself in N members at once, and the manifests are byte-identical by design, so the disagreement is uniform and silent. CI runs `--check` on every push to main and every pull request — never on the tag, where the full build runs instead — so a mismatch on main is a red build long before tag time, which means an integrity failure discovered *at* the tag usually means the check never ran, not that it passed.

The build also prints a non-fatal warning count. Warnings are instrumentation, not gates: the release's job is to read them, decide, and record the decision (fix now, or register it) — never to leave them unread because the exit code was zero.

## Install parity — the live drift mechanism

**The installed copy does not follow the repo.** A Claude Code marketplace install is a git clone under `~/.claude/plugins/marketplaces/<marketplace>` that moves only when the user updates it; on claude.ai a custom skill is an uploaded zip that, **on personal accounts**, changes only on delete-and-re-upload (Team/Enterprise has org-wide provisioning — one central upload instead of the per-user set; RUNBOOK, *Install / update on claude.ai*). This is where a pack actually drifts, and it is not theoretical — this pack's clone served pre-1.1.0 descriptions for a month after the repo had moved on, which is why the parity detector exists.

**On Claude Code there are two installed copies, not one, and they drift independently.** The clone above is what an install reads *from*; `~/.claude/plugins/cache/<marketplace>/<pack>/<version>/` is what Claude Code actually *loads*, and it is rewritten only by `claude plugin update <pack>@<marketplace>`. Refreshing the clone does not move the cache — so clone-current and loaded-stale is a real, silent state. It is not theoretical either: at foundation 1.1.0 a session kept loading promptwright 1.0.0 while parity reported clean, because parity only knew about the clone. Two steps, in order: refresh the clone, then update the plugin.

**The pack version is the cache key — which is what makes a member-only bump undeliverable.** `claude plugin update` compares *pack* versions, not member versions, so a patch that bumps only a member leaves the loaded cache untouched and reports "already at the latest version" while serving the old body; the clone, which does track the branch, moves — so the two installed surfaces disagree and only the cache-side check sees it. This is the practical edge of Two clocks above: the member clock decides what changed, the pack clock decides what *ships*. A member fix reaches an installed user only when a pack version carries it, so a post-tag member patch is undelivered work until the next pack bump — recorded at 1.1.1, which existed for exactly that reason.

`build.py --parity` diffs **every shipped file** in both copies against the repo and exits non-zero on drift, naming which surface drifted and listing each file as missing, differing, or extra. Scope was the lesson: it compared `SKILL.md` frontmatter only until 2026-08-01, and twice reported **clean** while the loaded copy was stale — the files that lagged were `ledger.md` and `spec.md`, which are not frontmatter and so were never looked at. A detector whose scope is narrower than the thing it certifies produces false assurance, which is worse than no detector, because it ends the investigation. Line endings are normalised, so a CRLF working tree against an LF clone is not reported as drift; runtime markers (`.in_use`) and VCS internals are skipped. Two honest limits remain: it skips each surface cleanly when absent, which makes it CI-safe and therefore *not* a CI gate, and it knows nothing about claude.ai, where upload is manual and parity stays owner-observed. Parity is an owner-machine step: refresh the clone, update the plugin, run parity to clean, then re-upload changed members on the surfaces where upload is manual.

## Release assets — the tag is not the release

CI builds the member zips on a version tag and attaches them to the release; installers are pointed at Releases, so a tag whose assets lag main hands out stale skills. Confirm the attach after pushing — "CI is configured to attach" and "the assets are on the release" are two different facts, and only the second one installs.

When a tag predates fixes that landed after it — as on 2026-07-24, when a hygiene release's audit fixes rode main after the tag was cut — the locally built `dist/` zips are the upload source of truth (they are build artifacts, gitignored, never committed), and a re-tag for asset parity is the documented option. Either way, state which build the upload set came from.

## The deferral register — findings recorded as evidence

The habit that makes the rest survivable: **a finding that is not fixed in this release is recorded as evidence, not carried in someone's head, and never patched silently.** The register is the pack-spec baton's seventh section, defined with the other six in `pack-design.md` — The pack-spec baton. Three shapes recur:

- **Structural work parked out of a hygiene release.** The 1.1.1 release fixed every finding its audit raised and pushed the structural work into a numbered register, which then opened the next pass. A hygiene release that had also restructured would have shipped two unrelated risk profiles under one tag.
- **A finding recorded against a later patch.** The commwright item shipped, then wrote down that one of its boundaries holds only because a sibling owns a single literal token — and named the eval row to re-check on the next edit there.
- **A cost accepted on purpose.** The same item recorded that its body crossed the pack's token gloss deliberately, and why, so the next reader does not "fix" it back.

What the evidence requirement buys a release is specifically this: a deferred finding stays actionable a month later, for someone who was not in the room, without re-deriving why it was raised.

## Release order

The RUNBOOK of the repo being released is the authority; this is the shape it enforces here.

1. **Member work lands** — each touched member with its own dated CHANGELOG entry, eval provenance re-anchored in the same commit.
2. **Pack version written in one stroke**, never field by field.
3. **Full build run** — roster manifests regenerated from the registry, every member validated, `dist/` written. Read the count line and the warning count before going further.
4. **Commit, tag `<pack>-vX.Y.Z`, push.**
5. **Confirm the release assets attached.**
6. **Owner surfaces** — update the marketplace clone, parity to clean, re-upload the changed members where upload is manual.
7. **Close the baton** — status line, register updated with what closed and what carried, so the next pass opens on a resume point rather than a memory.

Steps 1–5 are repo work and mostly mechanized. Step 6 cannot be mechanized and is the one that decides whether anyone is running the release, and step 7 is the one that decides whether the next release starts from evidence.
