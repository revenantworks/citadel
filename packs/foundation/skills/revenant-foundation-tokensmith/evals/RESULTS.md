# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.1 — runner: claude (listing-based routing simulation, single pass)

Judged cold against the current frontmatter descriptions of all eight foundation members (name + description only); verdict formed per row before comparing to the expected column.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| Y1 | Fire — "slim" + explicit token budget on a system prompt; promptsmith's own boundary hands token trims here | Fire | PASS |
| Y2 | Fire — "why … costs so many tokens" on CLAUDE.md, a verbatim trigger clause | Fire | PASS |
| Y3 | Fire — "tokensmith audit" keyword | Fire | PASS |
| Y4 | Fire — agent spec must "fit a token or context budget"; agentsmith owns the system around an agent, not its footprint | Fire | PASS |
| Y5 | Fire — "token budgets" for an artifact set, the Budget entry verbatim | Fire | PASS |
| Y6 | Fire — JUDGE: "always-on surface … eating context" must be read as an artifact (skill's session-start load), not a live session; the context-cost + "trim" vocabulary carries it | Fire | PASS |
| Y7 | Fire — "compress" a reference doc under a preservation contract; loresmith verifies docs, never shrinks them | Fire | PASS |
| Y8 | Fire — "tokensmith refresh" keyword | Fire | PASS |
| Y9 | Fire — measure-first cost estimate + cache payoff = stated measurement methods and net-cost accounting | Fire | PASS |
| Y10 | Fire — JUDGE: SKILL.md pulls toward skillsmith, but "under 300 lines without changing what it does" is shrink-behavior-preserving, tokensmith's charter; the budget being lines rather than tokens is the only wrinkle | Fire | PASS |
| N1 | No fire → promptsmith — prompt quality/wording, named in tokensmith's boundary sentence | No fire | PASS |
| N2 | No fire → skillsmith — best-practice conformance, named boundary; no token/footprint vocabulary in the ask | No fire | PASS |
| N3 | No fire → commsmith — human-facing message length, named boundary | No fire | PASS |
| N4 | No fire — JUDGE → runtime/platform tools: "context" lures, but "session … mid-task … live" is runtime and tokensmith declares itself build-time on artifacts | No fire | PASS |
| N5 | No fire → evalsmith — "assertion suite" is its verbatim trigger; "slimmed" is decoration | No fire | PASS |
| N6 | No fire → promptsmith — model-tier question is its verbatim trigger | No fire | PASS |
| N7 | No fire → skillsmith — a build ask; terse responses are a runtime output style, not an artifact footprint | No fire | PASS |
| N8 | No fire — definitional question; no artifact to measure or shrink | No fire | PASS |
| N9 | No fire — summarization for a human reader, not an LLM-facing artifact slim | No fire | PASS |
| N10 | No fire — an AWS bill is not an LLM text artifact | No fire | PASS |

**Pass rate: 20/20.** No failure pattern; the three JUDGE rows (Y6, Y10, N4) all resolve on the description's build-time-artifact framing plus its explicit boundary sentences — the closest call is Y6, whose "always-on surface" phrasing appears nowhere in the description and routes correctly only via the context-cost vocabulary.
