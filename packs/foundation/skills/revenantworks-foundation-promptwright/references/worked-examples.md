# Worked Examples

Three full worked examples in the current output contract, one per entry-point. Read the matching one in Phase 2 or Phase 5 when you're unsure what good output looks like. Each shows the finished footer order: **TL;DR → Model → Score → Structure → Changed/Variables/Assumed → test → Keep going selection**. The Model line is mandatory on every prompt-delivering output. On full builds these footers appear under the `── Phase 7 / 7 — Output ──` header. The examples show the Keep going selection in its **plain-text fallback form**; on a surface with native tappable selection those same four options render as a tappable single-select instead. Model names in these examples are illustrative snapshots from when they were written — a live build sources current names from `model-snapshot.md`, never from here.

## Contents

- Example 1 — CO-STAR: audience-and-tone explainer (build from scratch)
- Example 2 — TIDD-EC: structured extraction with a hard constraint (improve existing)
- Example 3 — Agent/System: code-review agent with tools and an escalation rule

---

## Example 1 — CO-STAR: audience-and-tone explainer (build from scratch)

**Request:** *"Write a prompt that explains quantum entanglement to a bright 12-year-old. Warm, curious tone. No equations."*

---

**Prompt**
```
You are a science communicator who loves making hard ideas click for curious kids.

Your task: explain quantum entanglement to a bright 12-year-old who has never seen
physics beyond school science, so they come away genuinely understanding the core idea.

Tone: warm and curious — spark wonder, treat the reader as clever, never talk down.

Guidelines:
- Build the idea with one vivid everyday analogy, not equations or jargon
- Keep it under 220 words
- End with one surprising, true "isn't that wild?" fact to leave them thinking

Return only the explanation — no heading, no preamble.
```

**TL;DR**  Ask it to explain quantum entanglement and it returns a warm, equation-free explanation under 220 words aimed at a curious 12-year-old — built on one everyday analogy and capped with a surprising true fact.

**Model**  Tier B — Claude Sonnet 5 · effort low — plain-language explanatory writing is squarely in the balanced tier's wheelhouse; no need to pay for a flagship

**Score**  4.0 → 8.8  (+4.8)
Clarity 9 · Specificity 9 · Context 8 · Completeness 9 · Structure 9

**Structure**  CO-STAR — audience and tone drive the whole task; the physics is simple to state but the voice has to land for a young reader

**Assumed**
- "No equations" also rules out numeric examples; a single analogy is the substitute
- 220-word cap keeps it engaging for a young reader who'll drift if it runs long

Test it without the analogy instruction, to confirm the model doesn't fall back on a textbook definition.

Keep going: harden + examples · switch model · generate savable prompt card · run it now

---

## Example 2 — TIDD-EC: structured extraction with a hard constraint (improve existing)

**Request:** *"Improve this prompt — it's supposed to classify support tickets into a JSON object with urgency and category, but it keeps softening 'critical' tickets."*

Existing prompt: *"Read the support ticket and classify it by urgency (low, medium, high, critical) and category (billing, technical, account, other). Return JSON."*

---

**Prompt**
```
You are a support triage system. Classify the ticket in <ticket> into a JSON object.

<ticket>
{{support_ticket}}
</ticket>

Return exactly this schema — no other keys, no preamble, no code fences:
{
  "urgency": "<low | medium | high | critical>",
  "category": "<billing | technical | account | other>"
}

Urgency rules:
- critical: data loss, security breach, complete service outage, or user explicitly states business is stopped
- high: significant feature broken, workaround exists but painful
- medium: partial degradation, workaround available
- low: question, cosmetic issue, or future request

Do not downgrade urgency based on polite tone. A user who says "sorry to bother you,
our entire system is down" is critical — not low.
```

**TL;DR**  Paste a raw support ticket in and it returns a two-field JSON object rating the ticket's urgency and category — with an explicit rule that stops polite wording from downgrading a genuine critical outage.

**Model**  Tier C — Claude Haiku 4.5 · effort low — single-label ticket classification is exactly the fast tier's job; the explicit rule table does the heavy lifting, so paying for a bigger model buys nothing

**Score**  3.1 → 9.2  (+6.1)
Clarity 9 · Specificity 9 · Context 9 · Completeness 10 · Structure 9

**Structure**  TIDD-EC — the bug is a missing explicit rule; TIDD-EC's Do/Don't pairing is exactly the right fix for a binary correctness constraint the model was softening

**Changed**
- Vague "classify by urgency" → explicit four-level rule table with concrete examples per band
- No schema spec → exact JSON schema with forbidden extras (no preamble, no code fences)
- Silent on tone bias → explicit rule: "do not downgrade urgency based on polite tone"

**Variables**
- `{{support_ticket}}` — the raw support ticket text, as submitted

Test it on a ticket from a user who opens with an apology and then describes a full outage, to confirm `"urgency": "critical"` fires correctly.

Keep going: harden + examples · switch model · generate savable prompt card · run it now

---

## Example 3 — Agent/System: code-review agent with tools and an escalation rule

**Request:** *"Build a system prompt for a code-review agent. It has two tools: read_file and post_comment. It should flag issues, post inline comments, and escalate critical security findings without approving."*

---

**Prompt**
```
You are a code-review agent. Your job is to review the diff provided, identify issues,
and post inline comments. You have two tools:

- read_file(path): reads the full contents of a file from the repository
- post_comment(file, line, body): posts an inline comment on the pull request

Review process:
1. Read any files referenced in the diff that you need full context for (use read_file)
2. Identify issues across three categories: correctness, security, and style
3. For each issue, post one comment using post_comment — be specific: name the exact
   problem, explain why it matters, and suggest a fix in code or plain terms
4. After posting all comments, output a brief summary: total issues by category

Hard rules:
- Security findings rated critical (SQL injection, hardcoded secrets, unsafe deserialization,
  authentication bypass) must be flagged and must NOT result in approval — output
  "ESCALATE: security finding requires human review" after the summary and stop
- Do not post duplicate comments on the same line
- Do not approve the PR if any critical security finding was posted
- If a file is unreadable, note it in the summary and continue — do not halt the review

Act on what you can read. Ask only if a file is essential and cannot be inferred.
```

**TL;DR**  This system prompt turns Claude into a code-review agent: it reads the files it needs, posts specific inline comments on correctness, security, and style, summarizes what it found, and hard-stops with an escalation flag rather than approving whenever it hits a critical security issue.

**Model**  Tier A — Claude Opus 4.8 · effort medium — a tool-driven agent making security judgments on real code is exactly where flagship reliability earns its cost; adaptive thinking handles the reasoning, so no CoT scaffolding in the prompt

**Score**  3.4 → 9.0  (+5.6)
Clarity 9 · Specificity 9 · Context 8 · Completeness 9 · Structure 9

**Structure**  Agent/System — tool-using agent with act-vs-ask logic, a hard stop condition, and an explicit output contract

**Assumed**
- Agent has access to the PR diff in context; read_file is for full file content only
- "Inline comment" means per-file, per-line; post_comment handles placement
- Style issues are posted but do not block or escalate

Test it with a diff containing a hardcoded API key, to confirm the ESCALATE output fires and no approval is issued.

Keep going: harden + examples · switch model · generate savable prompt card · run it now
