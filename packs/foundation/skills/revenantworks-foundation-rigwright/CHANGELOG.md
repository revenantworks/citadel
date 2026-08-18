# Changelog — revenantworks-foundation-rigwright

> Renamed from `revenant-foundation-rigwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.1.1] — 2026-08-17

Member audit + security scan (2026-08-17), plus the `surface-notes.md`
refresh the same day. No entry point, layer-stack rule, scoring anchor, or
restraint path moved; the description is untouched (962 chars), so the
routing surface did not move. Patch bump — refresh, audit fixes, and eval
additions.

- **Refresh — `references/surface-notes.md`, restamped 2026-08-17.** Every
  section re-verified live except one claim, marked inline. What changed:
  `CLAUDE.local.md` is supported again as the gitignored personal
  per-project file (the 2026-07-30 pass read it as deprecated; the
  home-directory import is the worktree-safe form); project instructions may
  also live at `./.claude/CLAUDE.md`; `.claude/rules/` topic files with
  `paths:` frontmatter, and `~/.claude/rules/`, are a new placement fact;
  imports cap at four hops and an external import in a project file prompts
  once; block-level HTML comments are stripped; the **200-line target is now
  published** (moved from reported, move noted in the file and in
  SOURCES.md); `/init` suggests improvements over an existing file, and
  `/context` and `/doctor` are named; `AGENTS.md` is read only by import;
  settings merge order and array/object merge stated; the workspace-trust
  split (repo `allow` rules gated, hooks and `env` not, `-p`/SDK never
  prompted); bare `Bash` / `Bash(*)` semantics; skill-frontmatter note for
  an audit that meets a `.claude/skills/` entry (`allowed-tools` is a
  per-turn grant, `disallowed-tools` exists, six keys accepted by claude.ai
  uploads); MCP local/user scopes in `~/.claude.json`, project-server
  approval keys and the untrusted-folder rule, `${VAR}` /
  `${VAR:-default}` expansion; the `.mcp.json` location open item of
  2026-07-30 **closed** (project root; the alternate reading came from
  plugins); auto-memory path, 200-line / 25 KB index load, and the three
  disable paths; Projects — RAG "up to 10×", free accounts capped at five,
  organization instructions (Team/Enterprise, 3,000 chars, precede a
  member's own), the Settings field relabeled "Instructions for Claude".
  Both `[reported]` budgets (≈8,000 / ≈1,500 chars) re-checked: still no
  published figure, kept as reported. Sources by domain: code.claude.com
  docs (memory, settings, permissions, hooks, mcp, skills, headless),
  support.claude.com (projects, personalization, organization
  instructions). **Carried, not re-verified:** the flat-structure /
  no-nesting sentence — not stated in the Help Center articles read this
  pass; regraded reported in SOURCES.md and marked inline.
- **S-4 · P1 — unsafe defaults in the emitted `settings.json`.**
  `artifact-templates.md` said "never a blanket allow" but named neither
  bare `Bash` / `Bash(*)` nor `ask` rules, and set no rule for what a hook
  entry may reference. Now: no bare `Bash` / `Bash(*)` allow; no `ask`
  rule where the repo may serve an unattended run (routine, scheduled task,
  `claude -p`) — an `ask` with nobody to answer denies the call or stalls
  the run — with an interactive-only rig allowed to keep one and the
  handback stating which the file assumes; a hook names a command the repo
  ships (`${CLAUDE_PROJECT_DIR}/...`) or a pinned, named tool — never a
  URL, a fetch-and-run, or a path outside the repo. The `.claude` /
  `.mcp.json` validation checklist gained the same three checks.
  `surface-notes.md` carries the mechanism (why `ask` fails unattended).
- **S-1 · P2 — step-level pointer.** Turn shape 5 binds every entry, but
  Build step 1 (an existing config or repo tree read at intake) and the
  templates' "starts from the existing `CLAUDE.md`" step carried no pointer
  to it. Both now cite it at the step; the rule stays single-homed.
- **Rubric A invocation control · P2.** Build writes files and stated no
  reason for staying model-invocable. One line added under Behavior notes:
  ships to claude.ai where the description is the only trigger; writes only
  the config files it hands back, after the one gate; never commits.
- **(f) evals · P1 — injection probes.** Case 8 covered Audit alone; Build
  and Refresh had none. Two added (below).

Security scan 2026-08-17: (a) injection posture — Turn shape 5 binds every
entry, Refresh states the fetched-page rule, and the two reading steps now
cite it; (b) no fetch-and-follow, permission-widening, secret-echo, or
guard-bypass instruction in any file — the secrets rule is single-homed in
`artifact-templates.md` and Restraint cross-references it; (c) standalone
profile — web search for Refresh, native file tools for delivery, in-chat
degradation stated (Build step 6, Case 14); no shell, no script, no
undeclared sibling (skillwright, agentwright, promptwright, tokenwright,
brandwright named as handoffs only); (d) hidden-text scan clean
(2026-08-17); (e) output handling — Build writes named config files at
named paths after one gate and never commits; Audit reports and never
rewrites; Refresh writes one named file plus a CHANGELOG line; (f) evals —
one probe existed; two added. S-2: no credential or personal identifier in
any file (Case 4's fixture reads as synthetic); S-3 pass; S-4 fixed as
above; C-1 (Audit scores without rewriting) and C-2 (neutral by default,
brand via brandwright only) pass; every referenced file present, no
reference over 150 lines, no Windows path; live "citadel" mentions: none.

Evals: `test-cases.md` Cases 15–16 added — Build (a handed-in `CLAUDE.md`
carrying a directive at the builder), Refresh (a fetched page carrying a
directive at the refresh) — each **authored, not run**; 14 → 16; the
re-run owed since 1.1.0 remains owed. `trigger-evals.md` re-anchored,
provenance only — still 20, 10/10; the cold re-judge owed since 1.0.2
remains owed. `evals/RESULTS.md` untouched (its 2026-07-31 20/20 cold run
predates the 1.0.2 and 1.1.0 description changes). README case count 14 →
16. Owed for a later minor: a `.claude/rules/` (path-scoped rule) row in
the SKILL.md layer stack — recorded in `surface-notes.md` this pass, not
added to the durable stack under a patch.

## [1.1.0] — 2026-08-12

Four 2026-08-12 estate-audit findings closed in one pass:

- **tokenwright boundary closed from this side (finding 9).** The closing
  boundary sentence named three siblings and not tokenwright, so a bare
  "trim my CLAUDE.md" routed ambiguously. It now ends "…for a pure token or
  cost cut on a config whose layout is already right, tokenwright", with
  compensating trims elsewhere in the description holding the length at 962
  characters (960 before; the audit asked for net-neutral-or-shorter and the
  warn line is 1,000). tokenwright's description closes the same pair from
  its side in the same release. Routing surface moved: the trigger-eval cold
  re-judge recorded as owed in the suite's provenance.
- **Injection rule promoted to file level (finding 10).** The
  data-never-instructions sentence was scoped to Entry — Audit while Entry —
  Build mines conversation and attachments. It is now Turn shape rule 5,
  binding every entry, single-homed; the Audit entry cites it instead of
  restating it.
- **Refresh injection rule (finding 2)** and **search-unavailable fallback
  (finding 14).** Entry — Refresh now carries both: a fetched page is data,
  never instructions (an instructing source is itself a finding, recorded at
  its URL), and a refresh that cannot verify never re-stamps — report, leave
  the date, name the invocation to re-run.

## [1.0.2] — 2026-08-05

Description names hooks in the artifact list (".claude layout, hooks, and
.mcp.json", 952 → 959 chars) — AUDIT-2026-08-05's Optional finding: the
machinery already existed (`surface-notes.md` and `artifact-templates.md`
both cover hooks and settings), only the description undersold it, so a
"write the hook for this rule" ask had no advertised landing. Patch bump —
one word widens an existing claim; no entry point or doctrine moved. The
registry's new rigwright ↔ tokenwright seam row (same audit) lands on
tokenwright's side; this description is deliberately unchanged for it.
Trigger evals re-anchored; the cold re-judge against the amended listing is
owed, not claimed.

## [1.0.1] — 2026-08-01

A prose pass. The secrets rule duplicated in full between SKILL.md's
Restraint bullet and `artifact-templates.md`'s "No credentials, ever" now
cross-references its one home in `artifact-templates.md` instead of
restating it. A handful of dash-joined clauses in SKILL.md, `surface-notes.md`,
and the README were re-punctuated for clarity. No rule, gate, count, or
entry point moved, so no eval re-anchor is owed.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Builds the standing, attended configuration layer: Claude Project
  instructions with a knowledge-file plan, CLAUDE.md, a repo's `.claude`
  layout and `.mcp.json` — emitted paste-ready in each surface's native form
  and validated against that surface's checked limits.
- Seven-layer placement stack deciding a rule's home — profile preferences →
  project instructions → project knowledge files → CLAUDE.md → a skill → a
  hook or permission rule → auto-memory — driven by three heuristics:
  every-session-or-no-session, prose compliance is probabilistic while hooks
  are not, and a reference is not a rule.
- Build workflow: intent → placement → surface constraints → emit →
  validate → handback as pasteable blocks or repo files with a commit line;
  a bare placement question is answered directly from the stack, no build.
- Audit scores 1–10 on placement, budget, enforceability, rot, and coverage
  with a P0/P1/P2 catalog; reports only — an approved catalog becomes a
  gated build run.
- Restraint: already-lean setups are said to be lean; rules that belong
  nowhere are declined; secrets are never emitted — env-var or secret-store
  indirection is named instead; unattended-by-intent work hands off to
  agentwright regardless of on-disk filename.
- One calendar surface: `surface-notes.md` (60-day) tracking per-surface
  fields, caps, and load semantics with [published]/[reported] provenance
  tags, re-verified by `rigwright refresh`.
