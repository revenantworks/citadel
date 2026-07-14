# Evaluation — Rubrics and Test Inputs

How to build the optional Phase 7 deliverable: a way to verify a prompt actually works. Reach for this on high-stakes, production, or reused-at-scale prompts. For a one-off, the score-and-self-check in the main workflow is usually enough.

---

## Contents

1. Start from success criteria
2. Objective vs. subjective grading
3. Designing test inputs
4. Writing good assertions
5. Rubric template
6. Iterate

---

## 1. Start from success criteria

Before checking anything, state concretely what good output looks like for this prompt: the required content, the format, the length or tone, and any hard rules (for example, "valid JSON, no PII present, sentiment is one of three values"). Vague criteria produce vague evals.

This pairs with Anthropic's advice to define success criteria and build evaluations *before* heavy prompt tuning.

---

## 2. Objective vs. subjective grading

Use the cheapest mode that captures the criterion.

**Objective (assertion-based):** exact, programmatic checks. Output contains X; output is valid JSON; output matches the schema; no email address appears; length under N words. Prefer these wherever possible — they are fast, repeatable, and unambiguous.

**Subjective (rubric-based):** quality judgments that need a human or a model grader, such as tone, helpfulness, or whether an explanation is clear. Use a named-criteria rubric and judge consistently; do not force a brittle assertion onto something that needs judgment.

---

## 3. Designing test inputs

A handful of diverse inputs beats many similar ones. Cover:

- **Happy path** — a typical, well-formed input.
- **Edge cases** — boundary values, unusual but valid formats, the largest or smallest input.
- **Empty / garbage** — blank input, malformed input, or input with nothing relevant.
- **Adversarial** — for prompts that face untrusted content, an injection attempt (see `prompt-hardening.md`) to confirm the prompt does not get hijacked.

---

## 4. Writing good assertions

- One check per assertion, objectively verifiable.
- Give each a descriptive name that reads clearly in a results view — `output_is_valid_json`, `no_pii_in_output` — not "test 1."
- Where a check can be scripted, script it rather than eyeballing it.

---

## 5. Rubric template

For subjective criteria, a small table keeps grading consistent:

| Criterion | How to check | Pass bar |
|---|---|---|
| Tone is confident, no jargon | Read output; flag jargon terms | No jargon; assertive phrasing |
| Covers all 3 required points | Check each point present | All present |
| Within length limit | Word count | ≤ limit |

---

## 6. Iterate

Run the prompt on the full test set, compare against a baseline (the prompt before your change, or no prompt), note which inputs fail, refine the prompt, and re-run. Stop when the set passes and the remaining failures are acceptable.

Keep the test set with the prompt so the next change can be checked the same way. Treat prompts like versioned code: save each iteration so a change that makes things worse can be rolled back.
