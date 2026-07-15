# Pack audit fixes — 2026-07-14 (post-launch skillsmith audit, apply-all)

Verdict: 8/8 ship-ready · Rubric A 9.6–9.8 · profile + C-1 + C-2 pass ×8 ·
niche DEFENSIBLE ×8 · installed == canonical at foundation-v1.0.0 HEAD.

## Applied here (P2-1, P2-2) — unzip this bundle over the repo root

| File | Change |
|---|---|
| skillsmith `references/brand-config.md` | Identity-map row → org live; canonical-repo row → "Relocated … 2026-07-14; prior copy is a private archive" (both completed-relocation notes retired) |
| skillsmith `SKILL.md` | evals/ load-budget line → "(maintenance archive — never loaded at runtime)"; version → **1.0.1** |
| promptsmith `SKILL.md` | same evals-line rewording; version → **1.0.1** |
| both `CHANGELOG.md` | dated 1.0.1 entries |
| `packs/foundation/spec.md` | footnote ¹ on the two rows (snapshot column preserved) |

Validation: `build.py` clean — count integrity 8 = 8 = 8, 0 manifests synced
(registry-derived pack.md unchanged; no roster/URL change → no ×8 restamp).
Lazy restamp blast radius: 2 packages.

Commit line:

    audit: post-launch pack audit — retire relocation notes, fix evals-line wording (skillsmith 1.0.1, promptsmith 1.0.1)

No tag — member patches ride until the next pack release.

## Your side (P1-1, P1-2) — install-state swaps

Run `py apply-install-swaps.py <citadel-clone> <private brand-definition.md> <private voices.md>`
→ emits brandsmith + commsmith 1.0.0 zips with your active v1.2.2 definition
and saved voices overlaid. Sources live in the OLD local folder (definition:
your full v1.2.2, not the repo's house-only edition; voices: the pre-cleanup
copy with the saved voice block). The script hard-fails if pointed at the
neutral repo copies.

## Upload checklist — due now (claude.ai › Skills, replace existing)

1. revenant-foundation-skillsmith-1.0.1.zip   (this delivery)
2. revenant-foundation-promptsmith-1.0.1.zip  (this delivery)
3. revenant-foundation-brandsmith-1.0.0.zip   (from your swap-script run)
4. revenant-foundation-commsmith-1.0.0.zip    (from your swap-script run)

Other 4 members: unchanged — no upload (lazy policy).
