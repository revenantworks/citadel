# Playbook Mode — Template-First Reference Docs

Loaded on every playbook run. Mutually exclusive with verdict-mode.md.

## 1. Template first

Before content: the doc's skeleton — title, the questions it answers (as headers), and the answer-up-front block at the top. One gate on the template; "just write it" skips.

## Standard skeleton

```
# <Playbook name> — v1.0 · verified <date>
**The answer:** <the thing the reader came for, ≤5 lines>
## <Question the reader asks, in their words>
<answer first · then method · then caveats, tags inline>
## Sources & verification
<primary sources with check dates · tag legend — the body's four glosses, verbatim>
## Changelog
v1.0 — <date> — initial, verified
```

## 2. Fill rules

Answer before explanation in every section. Tags inline on every claim, the four grades the SKILL body defines — they ride the body, which is loaded whenever this file is. The doc itself carries a legend for its reader, in the Sources & verification section: the body's four glosses copied verbatim, never re-worded or shortened — that reader never sees this skill, so a paraphrased legend would describe tagging rules the doc's own cells did not follow. Steps are numbered and testable; opinions are marked as such; version-sensitive facts carry their checked version ("as of vX.Y").

## 3. Verification pass

After drafting: every [documented] claim re-checked against its primary source this run; failures downgrade the tag rather than soften the wording. The pass is a step, not a virtue statement — its date goes in the header.

## 4. Versioning & consolidation

Updates re-verify only touched sections; version bumps per SemVer feel (content-correcting = minor, restructure = major). Where the body's consolidation doctrine sends an overlapping request into an existing doc, the extension is a section-level edit and a version bump on that doc, never a second file.
