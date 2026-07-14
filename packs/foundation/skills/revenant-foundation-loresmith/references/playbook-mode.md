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
<primary sources with check dates · tag legend>
## Changelog
v1.0 — <date> — initial, verified
```

## 2. Fill rules

Answer before explanation in every section. Tags inline per the verdict-mode legend. Steps are numbered and testable; opinions are marked as such; version-sensitive facts carry their checked version ("as of vX.Y").

## 3. Verification pass

After drafting: every [documented] claim re-checked against its primary source this run; failures downgrade the tag rather than soften the wording. The pass is a step, not a virtue statement — its date goes in the header.

## 4. Versioning & consolidation

Updates re-verify only touched sections; version bumps per SemVer feel (content-correcting = minor, restructure = major). Before creating any new playbook, check the docs the user names or supplies for overlap — extend the canonical doc instead of rivaling it; propose merges when handed duplicates. One canonical doc per question.
