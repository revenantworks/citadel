# foundation — decisions & roster boundaries

> Durable decisions, the adopt register (jobs owned by strong incumbents), and the
> recorded-not-built candidates. Split out of `spec.md` 2026-07-25 (deferral-register
> item ⑥). The live baton is `spec.md`; build/execution history is in `ledger.md`.


---

## Decisions log

- 2026-07-13 — Pack born at uniform 1.0.0 baseline (seven members); tokenwright
  added same day (roster of eight); conformance C-1/C-2 adopted pack-wide;
  restamp policy lazy (per-release flip allowed).
- 2026-07-14 — Pack self-audit (Phase 1.8 step 1), gated and approved:
  verdict **KEEP 8 / COMBINE 0 / BUILD 0**; partition test 12/12; findings
  P2-1 (promptwright↔tokenwright boundary — applied, promptwright 1.0.1) and
  P2-2 (this baton — applied). Combine analysis rejected all four candidate
  merges (evalwright⇄skillwright, tokenwright⇄promptwright,
  brandwright⇄skillwright-configure, commwright⇄lorewright).
- 2026-07-14 — Release bar adopted (closes OD12): release-solid = set
  discoverability pass with no open P0/P1 + repo/release/account parity +
  a current capstone card with one live run.
- 2026-07-23 — **CORRECTION (D-3):** earlier 2026-07-14 lines here declared
  "Foundation 1.0 as pack release 1.2.0, tag v1.2.0" and a capstone "v1.2.1".
  The shipped artifacts — the live Release, `.claude-plugin` manifests, and
  every member's frontmatter — are **1.0.0 / tag `foundation-v1.0.0`**. Those
  1.2.x lines were predecessor-era numbering that never shipped and are
  superseded; the shipped state is authoritative. Semver tags going forward
  (date tags kept as history); member versions independent per pack norm.
- 2026-07-23 — **Forge Run 3 approved in full** ("approve all"): 1.1.0
  uniformity + brand-decoupling build. Brand decoupled into brandwright as the
  single brand home; skillwright `upkeep` + promptwright `model` entries added;
  native-first packaging; uniform volatility/anti-patterns/README structure;
  build.py extended to validate volatility metadata. Plan + status tracked in
  the Forge Run 3 section of `ledger.md`. Cowork 61-day upkeep cadence to follow.
- 2026-07-27 — **Deferral item ⑧ split and half of it dropped.** The
  security-scan half was approved and built: agentwright gains `Entry —
  Security-scan` with its own doctrine reference (the agent at runtime — tool-grant
  scope, guardrails, kill switches, credential handling, untrusted-content flow),
  skillwright's `Entry — Audit` gains its own security pass (the skill artifact as
  built — injection surface in instructions, secrets in the package, undeclared
  tool assumptions, unsafe generated defaults). **Each ships self-contained**:
  neither loads the other's files, per the standalone profile; the split is carried
  by reciprocal boundary sentences in the two descriptions, which is routing
  metadata and not a load-time dependency. **The multi-host export half is
  dropped, not deferred.** No cross-vendor Agent Skill standard exists to export
  *to*, so the work would mean inventing a translation format speculatively for an
  unnamed host: the exact build this pack's "recorded, not built" convention
  declines ("earns a build only if asked for by name"). Revisit only if a named
  target platform is on the table, at which point it is a fresh gate, not a
  resumed item.

---

## Adopt register

Strong incumbents own these jobs — recorded, linked, left out of the roster.

| Job | Incumbent | Recorded (as of 2026-08-01) |
|---|---|---|
| MCP server generation | `mcp-builder` — anthropics/skills, first-party | 2026-07-14 |
| Baseline skill drafting/review | `skill-creator` — built into claude.ai and Claude Code | 2026-07-14 |
| Code-level engineering (review, tests, debug, incidents) | Anthropic's open-sourced engineering plugins | 2026-07-14 |
| Document production (docx/pdf/pptx/xlsx) | first-party document skills | 2026-07-14 |
| Broad multi-source research reports | Claude Research feature (lorewright partitions this away) | 2026-07-14 |
| Code-level threat coverage | security harness / STRIDE-class skills (agentwright partitions this away) | 2026-07-14 |
| Model selection (standalone) | multiple community skills (Claude Model Selector, model-selection ×N) — 5B folds the need into promptwright instead | 2026-07-23 |

---

## Recorded, not built (nice-to-have)

- **contextwright** — CLAUDE.md / project-instructions / memory-file
  architecture. Mostly decomposes into tokenwright (footprint) + promptwright
  (instruction quality); a ninth member would blur two seams to cover one
  sliver. Earns a build only if asked for by name at a future gate.
  (2026-07-23: the foundation `CLAUDE.md` in Phase 3 covers the always-on
  routing sliver without a skill.)
- **runwright** — runtime review of scheduled-agent runs (logs, behavior
  drift). No incumbent found 2026-07-14; partially covered by agentwright
  audit; platform-bound (needs run logs → breaks standalone profile). Natural
  home is the future trading-pack quarterly audits. Record.
- **session-helper / model-picker (standalone)** — rejected 2026-07-23 as
  members: model-picking is CROWDED standalone and folds into promptwright (5B);
  always-on session help is CLAUDE.md territory, not a skill (5C).
