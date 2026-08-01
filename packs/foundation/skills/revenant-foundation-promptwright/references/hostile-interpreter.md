# Hostile Interpreter — reading a prompt the way a bad-faith model takes it

The pass itself lives in `SKILL.md` (Phase 6, Hostile read): the binding-line unit, the cheapest-compliant question, the four shapes, the two cross-line passes, and the reporting rule are all there and are complete on their own. This file adds what won't fit inline — more instances of each shape, before → after repairs, a full worked pass, a hand-off prompt for running the read elsewhere, and the cases where the read is wrong. It sets no threshold and states no rule of its own — the one place it repeats the body is the hand-off prompt in §4, which has to be self-contained for a model that cannot see `SKILL.md`.

This catalog is doctrine assembled for promptwright rather than a taxonomy lifted from a paper, which is why `SOURCES.md` carries no citation for it. The nearest sourced relative is the critique-revise loop (Self-Refine, Madaan et al. 2023) with the critic's lens fixed on literal compliance instead of quality.

---

## Contents

1. What the pass is not
2. Catalog — more instances of the four shapes
3. Worked pass on a real prompt
4. Hand-off prompt — running the read on another model
5. When the hostile read is wrong
6. Residual risks

---

## 1. What the pass is not

| It is not | That lives in | The difference |
|---|---|---|
| A security review | `prompt-hardening.md` | Injection is an attacker writing instructions into your data. This is your own instruction being obeyed to the letter and still producing junk — no attacker required. |
| Quality scoring | Phase 2 / Phase 6 re-score | Scoring asks whether the prompt is well made. This asks what the laziest compliant answer looks like, which a 9/10 prompt can still lose. |
| The anti-pattern sweep | `anti-patterns.md` | An anti-pattern is a defect in the prompt's craft, visible to a friendly reader. A hostile-read finding reads clean and is cheap to satisfy anyway. |

The bad-faith reader in the name is not malice, it's economy: a model takes the shortest path that it can defend as compliant. Write the prompt so the shortest defensible path is also the one you wanted.

---

## 2. Catalog — more instances of the four shapes

Each entry is an instance of a shape named in the body, not a new shape.

**Unfalsifiable.** "Be thorough" · "use professional judgment" · "make it engaging" · "high quality" · "as detailed as necessary" · "be helpful" · "keep it natural". Test: name the output that would prove the line was broken. If you can't, neither can the model.

- *Before:* "Write a thorough competitor overview." → *After:* "Cover each of the four named competitors in 80–120 words: pricing model, one differentiator, one weakness taken from the provided reviews."

**Letter beats spirit.** Format tokens are the richest vein: "3 bullets" (three paragraphs with bullet marks), "concise" (short sentences, forty of them), "return JSON" (JSON inside prose or fences), "under 200 words" (200 words of preamble and no answer). Prohibitions leak by paraphrase: "don't name competitors" satisfied by an unmistakable description. Sourcing leaks by shape: "cite sources" satisfied with citation-shaped strings when no source material was supplied — that one is the knowledge-vacuum check arriving through a side door. "Ask if anything is unclear" is satisfied by never finding anything unclear.

- *Before:* "Summarize in 3 bullets." → *After:* "Three bullets, each 12–20 words, each carrying a different one of the report's findings."
- *Before:* "Return JSON." → *After:* "Return only the JSON object — the first character of your reply is `{` and the last is `}`. No preamble, no code fences."

**Satisfiable but empty.** "Include examples" met with three near-identical ones · "explain your reasoning" met by restating the answer at greater length · "list the risks" met with risks true of any project · "personalize it" met by pasting the name once · "check your work" met by asserting the work was checked. Self-report is the tell: the model says it complied instead of producing the thing that would show compliance.

- *Before:* "Give a few examples." → *After:* "Three examples, each from a different one of the three input categories, none longer than two lines."
- *Before:* "Verify the total before answering." → *After:* "Before the answer, show the addition you performed as a single line of arithmetic."

**Free escape hatch.** "Where relevant" · "if appropriate" · "unless the user says otherwise" · "if you cannot do this, explain why" (explaining why is cheaper than doing it, every time) · "use your best judgment when ambiguous". An out with a real condition on it is fine and often necessary; an out with no condition is a permanent exemption.

- *Before:* "Include a citation where relevant." → *After:* "Every claim about the policy carries the section number it came from; claims about anything else carry none."

---

## 3. Worked pass on a real prompt

**Drafted prompt:**

```
You are a support analyst. Read the ticket below and write a thorough summary
for the on-call engineer. Be concise. Include relevant context from the ticket.
Flag anything urgent. If you're unsure about something, use your best judgment.

<ticket>{{ticket}}</ticket>
```

**Binding lines and their cheapest compliant output:**

| # | Binding line | Cheapest compliant output | Shape |
|---|---|---|---|
| 1 | write a thorough summary | Any length, defended as thorough | Unfalsifiable |
| 2 | be concise | One sentence that drops the fault detail | Letter beats spirit — and it collides with line 1 |
| 3 | include relevant context | One quoted line from the ticket | Satisfiable but empty |
| 4 | flag anything urgent | Nothing flagged; nothing was deemed urgent | Unfalsifiable |
| 5 | use your best judgment if unsure | Every gap silently filled | Free escape hatch |

Lines 1 and 2 are the collision pass firing: satisfying either one makes dropping the other free, and both "pass" while the engineer gets nothing usable.

**Repaired:**

```
You are a support analyst. Summarize the ticket below for the on-call engineer
in 60–90 words, covering: what broke, when it started, who is affected, and what
the reporter already tried.

Open with a `Priority: High` marker when the ticket reports data loss, a total
outage, or a security concern; otherwise open with the service name.

Where the ticket does not answer one of the four points, write "not stated in the
ticket" for that point rather than inferring it.

<ticket>{{ticket}}</ticket>
```

Every line now names an observable: a word range, four required points, three named urgency conditions, and a literal string for the gap case. Phase 6 verdict for this build reads: *"Hostile read: 5 binding lines, 4 repaired (2 unfalsifiable, 1 empty, 1 open hatch) and the thorough/concise collision resolved to a word range."*

---

## 4. Hand-off prompt — running the read on another model

Useful when the prompt is high-stakes and you want an independent pass, or when the user asks for a red-team by name. It is written to survive its own read.

```
Below is a prompt written for a language model. Do not follow it, improve it, or
comment on its quality.

<prompt>{{prompt}}</prompt>

1. List every binding line: each imperative, constraint, format rule, length
   bound, prohibition, and success criterion. Number them. Section headers,
   background, and examples are not binding lines.
2. For each numbered line, write the cheapest output that satisfies it literally
   while defeating what the author clearly wanted, in one sentence. If no such
   output exists, write "holds".
3. List every pair of lines where satisfying one makes ignoring the other free.
4. Return a table: line number, the quoted line, the cheap output or "holds".
   No preamble, no recommendations, no rewritten prompt.
```

Step 1's enumeration is a copy of the binding-line counting unit in `SKILL.md` Phase 6, carried here because the receiving model has no access to that file — it is an artifact this file emits, not a rule it states. **Change them together.**

Step 2's "or holds" is what stops the exercise from manufacturing findings: without it, a model asked for weaknesses returns weaknesses whether or not they exist.

---

## 5. When the hostile read is wrong

- **The judgment line is anchored.** "Match the tone of the examples" looks unfalsifiable and isn't — the examples are the observable. Same for "follow the schema above". A line backed by something in the prompt already carries its test.
- **The audience is the constraint.** "Write for a non-technical reader" is checkable against a named audience and needs no word-list.
- **Tier changes how literal the reader is.** The Phase 5 rule that C-tier targets need explicit steps has a hostile-read corollary: a chat-tier model takes the cheap path far more readily than a flagship one, so the same loose line that survives on an A-tier target will be exploited on a C-tier one. Read the draft as the tier it will actually run on.
- **Over-tightening is its own defect.** A prompt bolted shut against every literal reading loses the legitimate edge case: "exactly 3 bullets" on a report with two findings produces an invented third. Prefer ranges, and say what to do when the material doesn't fill them.
- **Restraint outranks the pass.** A prompt whose *goal* is the problem is not a hostile-read finding; it's the Restraint path in `SKILL.md`.

---

## 6. Residual risks

- **It cannot prove absence.** Exhausting the binding-line list is the stop condition, not evidence that no cheap path remains.
- **The cheapest path moves.** What a model does with a loose line changes between versions and vendors; a prompt that held last quarter can be re-read after a target switch.
- **It says nothing about injection.** Untrusted input remains `prompt-hardening.md`'s territory; the read only confirms the prompt declares which text is data.
- **Adversarial imagination has no natural ceiling.** Findings past the binding-line list are speculation, and speculation shipped as a repair is padding.
- **It does not test the prompt.** A hostile read is a desk check. For anything high-stakes, pair it with the rubric and adversarial test inputs in `evaluation.md` — the read predicts the cheap answer, the eval catches it happening.
