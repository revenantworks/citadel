# Prompt Anti-Patterns and Fixes

Common ways prompts fail, each with the fix that replaces it. Consult this during Phase 2 (to spot issues in the input) and Phase 6 (to confirm the draft did not introduce one).

---

## Contents

1. Vague or undefined task
2. Kitchen-sink over-stuffing
3. Over-constraining (always/never pile-ups)
4. Negative framing
5. Example contamination
6. Reliance on deprecated prefill
7. MUST / CRITICAL shouting
8. Asking when the answer was inferable
9. Critical instructions buried in the middle
10. Unparseable structured output
11. Contradictory requirements

---

## 1. Vague or undefined task

**Pattern:** "Summarize this" / "make it better" with no object, audience, or bar. The model guesses, and the guess varies run to run.

**Why it hurts:** every downstream choice — length, tone, format — is unanchored, so output is inconsistent and usually wrong for the real need.

**Fix:** state the task, the audience, and what "good" looks like. If the task is genuinely unclear and not inferable, ask one targeted question rather than guessing.

---

## 2. Kitchen-sink over-stuffing

**Pattern:** piling in every instruction, caveat, and example "just in case," producing a sprawling prompt where the core ask is buried.

**Why it hurts:** competes for attention, dilutes the important rules, and costs tokens. The model may latch onto a minor instruction over the main one.

**Fix:** include only the sections the task needs. A one-line classifier needs no persona and three examples. Curate a few diverse, canonical examples instead of an exhaustive edge-case list.

---

## 3. Over-constraining (always/never pile-ups)

**Pattern:** stacking many absolute rules — "always do X, never do Y, you must always Z."

**Why it hurts:** absolutes collide with each other and with edge cases. A literal reader hits a contradiction and stalls or picks one arbitrarily.

**Fix:** keep constraints to the few that matter, phrase them positively, and explain why each exists so the model can generalize at the edges instead of obeying blindly.

---

## 4. Negative framing

**Pattern:** describing the output only by what to avoid — "don't use markdown," "no bullet points," "don't be verbose."

**Why it hurts:** the model has to invert every prohibition into an action, and often doesn't.

**Fix:** say what to do. "Respond in flowing prose paragraphs" beats "don't use bullets." Use a positive format instruction, optionally with an XML tag naming the desired shape.

---

## 5. Example contamination

**Pattern:** few-shot examples that carry incidental patterns — all the same length, all end with a question, all about one topic — that you didn't intend to teach.

**Why it hurts:** modern models imitate examples precisely, including the accidental pattern, so the output inherits a quirk you never asked for.

**Fix:** make examples relevant and diverse; vary surface features deliberately; cover an edge case. Every example should model exactly the behavior you want and nothing else. Flag generated examples for a sanity check.

---

## 6. Reliance on deprecated prefill

**Pattern:** seeding the assistant's reply with a prefilled opening to force a format.

**Why it hurts:** current Claude models no longer support prefilled final assistant turns. The call errors or the technique silently does nothing.

**Fix:** steer format with an explicit output-format instruction in the prompt body, structured outputs, or strict tool use.

---

## 7. MUST / CRITICAL shouting

**Pattern:** ALL-CAPS imperatives and "CRITICAL: YOU MUST…" sprinkled throughout.

**Why it hurts:** latest models over-trigger on this. It raises false urgency, can distort behavior, and reads as noise that crowds out the substantive instruction.

**Fix:** reserve emphasis for genuinely critical rules, and prefer explaining the reason. A clearly stated, motivated rule outperforms a shouted one.

---

## 8. Asking when the answer was inferable

**Pattern:** opening with a wall of clarifying questions the context already answered, or that have one obvious sensible default.

**Why it hurts:** wastes the user's time and signals the prompt-builder didn't read the room.

**Fix:** infer everything reasonable, state the assumption, and ask only when two or more readings genuinely diverge. Always offer the fast path: "just make smart assumptions."

---

## 9. Critical instructions buried in the middle

**Pattern:** placing the key rule or question in the middle of a long context, between large blocks of data or examples.

**Why it hurts:** models attend least to the middle of a long context, so a buried instruction gets under-weighted or missed.

**Fix:** put the most important instructions at the start or the end. Put long data near the top and the actual question after it.

---

## 10. Unparseable structured output

**Pattern:** asking for JSON (or any machine-read format) without forbidding preamble, so the model wraps it in prose or code fences.

**Why it hurts:** the consuming code can't parse it. "Here is the JSON: \`\`\`json …\`\`\`" breaks a naive parser.

**Fix:** specify the exact schema, require the model to return only that structure with no preamble and no code fences, and parse defensively on the consuming side (strip fences, handle failure). Prefer a platform's native structured-output feature when one exists.

---

## 11. Contradictory requirements

**Pattern:** the prompt stacks requirements that can't all hold in one output — "a single tweet under 280 characters" that must also contain "a full citation list with URLs" and "a step-by-step reasoning trace."

**Why it hurts:** there's no output that satisfies all of them, so the model silently sacrifices whichever rule it weights least — and which one it drops varies run to run, making the failure invisible.

**Fix:** catch it in Phase 2. Name the conflict rather than building over it. Then either reconcile it into a coherent design and state the assumption, or ask one targeted question to learn which requirement wins. Don't ship a prompt whose rules fight each other.
