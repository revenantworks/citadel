# Prompt Card — self-contained HTML output (opt-in)

A presentation layer for a finished prompt: one self-contained HTML file showing a plain-language TL;DR, the prompt in a copy box, the before → after score as a gauge, the structure, the model to run it on, variables, and assumptions. A pure offline artifact — no API calls, no network dependency — saveable and shareable independent of the conversation that produced it. (Live execution belongs to the chat "run it now" path, not the card.)

Emit it as a claude.ai artifact on surfaces that render HTML, or as a single self-contained `.html` code block the user can save where they don't. On Chat/Cowork surfaces, never deliver the card as a Markdown file; if a surface can render neither HTML form, omit the card.

> Model names anywhere in this file — fill-rule examples and the template alike — are illustrative. Fill a real card's Run on section from `model-snapshot.md`, never from here; copied-through example names go stale.

## Contents

- Fill rules — header & branding · structure chip · TL;DR · prompt block · score gauge · Run on · Variables / Assumed / Test · additional rules
- Template — the full self-contained HTML

---

## Fill rules

### Header and branding

The header is a `revenant-foundation-promptsmith` brand lockup — an accent mark plus the highlighted `revenant-foundation-promptsmith` wordmark — with a dynamic title beneath it: a concise 3–6 word name for what the prompt does (e.g. "Security Audit → CISO Summary," "Cold Email Rewriter"). The footer echoes the `revenant-foundation-promptsmith` mark. Keep the wordmark constant on every card; only the title changes. Set the page `<title>` to `revenant-foundation-promptsmith — <name>` so saved files and browser tabs are identifiable.

### Structure chip and footer recap

Set the header chip to the chosen structure name and the footer recap to `structure · before → after · model` (e.g. `CO-STAR · 6.4 → 8.8 · Sonnet 5`).

### TL;DR section *(always include, at the top)*

Directly under the header, before the prompt block, add a TL;DR section: `<div class="label">TL;DR</div>` plus one plain-language paragraph, ≤2 sentences / ~40–50 words. Say what the prompt does, what input it needs, and what it returns — no jargon, no framework names, no scores. This is the one section written for the end user who didn't build the prompt, so name variables in plain terms ("paste a raw support ticket"), not `{{tokens}}`. It carries the same text as the chat TL;DR footer line.

### Prompt block

Paste the delivered prompt into `#prompt`, HTML-escaped for display (`&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`). The copy button reads `textContent`, so the user still copies the real, un-escaped prompt.

### Score gauge

Set the `6.4 → 8.8` numbers and the `+2.4` delta. The gauge is stacked — a base segment at `before × 10%` and a teal gain segment at `(after − before) × 10%` (6.4 → 8.8 = `64%` base + `24%` gain).

**Per-dimension bars:** one row per scored dimension. Each bar stacks a base segment (`before × 10%`) and a teal gain segment (`(after − before) × 10%`), so the gain shows where the prompt improved. Show the value as `before → after` (e.g. `6 → 9`). Use all five dimensions — this needs the per-dimension *before* scores from Phase 2, not just the after scores.

### Run on section *(always include)*

Mirror the chat footer's **Model** line so the card carries its own run target: tier + vendor + model, the effort/thinking level, and the one-line rationale (e.g. `Tier B — Claude Sonnet 5 · effort low — search-and-synthesize; the balanced tier clears it`). It sits between Structure and Variables. A card without a model recommendation strands whoever opens it later — this section is not optional.

### Sections — Variables / Assumed / Test

Keep a section only if it has content — delete the whole `<div class="section">…</div>` block if the prompt has no variables, no inferences to surface, or no test note. Order: Variables before Assumed.

**Variable hints:** each Variables row reads `{{name}}` — what it expects. Fold a format or type hint into the line when it helps (an ISO-8601 date, a positive integer, plain text). Skip the hint when the expected input is self-evident. Don't add a rigid Type / Default column.

### Additional rules

- **Improvement runs:** you may add a `Changed` section before Score, summarizing what was removed / added and why.
- **No Keep going options on the card:** they belong in chat, not on a saved card — a recipient can't act on them.
- **Stay single-file and fully offline:** no external scripts, fonts, CDNs, network calls, or `localStorage` / `sessionStorage`, so the saved `.html` works anywhere with no dependencies.
- **Brand-neutral by default:** the template ships a neutral dark theme. You may re-skin the wordmark, title, and colors — just keep any exported card honest about what it is.

---

## Template

> The TL;DR section belongs at the top (under the header, before the prompt) per the fill rules above; the template shows its placement.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>revenant-foundation-promptsmith — Security Audit → CISO Summary</title>
<style>
  :root {
    --bg: #0d0f14; --surface: #151821; --surface2: #1b1f2a;
    --text: #e7ebf3; --muted: #9aa3b2; --border: #262b38;
    --accent: #5eead4; --accent-dim: #234e49; --good: #4ade80; --base: #6b7891;
    --radius: 14px;
    --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  * { box-sizing: border-box }
  body {
    margin: 0; background: var(--bg); color: var(--text);
    font-family: var(--sans); line-height: 1.5;
    padding: 32px 16px; display: flex; justify-content: center;
  }
  .card {
    width: 100%; max-width: 720px; background: var(--surface);
    border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden;
  }
  .card-h {
    display: flex; align-items: center; justify-content: space-between;
    gap: 12px; padding: 18px 22px; border-bottom: 1px solid var(--border);
  }
  .brandlock { display: flex; align-items: center; gap: 10px; min-width: 0 }
  .dot {
    width: 9px; height: 9px; border-radius: 2px; background: var(--accent);
    box-shadow: 0 0 10px var(--accent); flex: none;
  }
  .brandtext { display: flex; flex-direction: column; gap: 1px; min-width: 0 }
  .brand { font-family: var(--mono); font-size: 15px; font-weight: 600; color: var(--accent); line-height: 1.15 }
  .cardtitle { font-size: 13px; font-weight: 500; color: var(--text); line-height: 1.2 }
  .chip {
    font-family: var(--mono); font-size: 12px; color: var(--accent);
    background: var(--accent-dim); border: 1px solid var(--accent-dim);
    padding: 3px 10px; border-radius: 999px;
  }
  .section { padding: 20px 22px; border-bottom: 1px solid var(--border) }
  .section:last-child { border-bottom: 0 }
  .label {
    font-size: 11px; letter-spacing: .16em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 10px;
  }
  .promptwrap { position: relative }
  pre {
    margin: 0; background: var(--surface2); border: 1px solid var(--border);
    border-radius: 10px; padding: 16px; overflow: auto; max-height: 420px;
  }
  code {
    font-family: var(--mono); font-size: 13px; color: var(--text);
    white-space: pre-wrap; word-break: break-word;
  }
  .copy {
    position: absolute; top: 10px; right: 10px; font-family: var(--sans);
    font-size: 12px; color: var(--text); background: var(--surface);
    border: 1px solid var(--border); border-radius: 8px;
    padding: 6px 12px; cursor: pointer; transition: .15s;
  }
  .copy:hover { border-color: var(--accent); color: var(--accent) }
  .scorerow { display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 14px }
  .score-nums { font-size: 26px; font-weight: 600; font-family: var(--mono) }
  .delta {
    font-family: var(--mono); font-size: 13px; color: var(--good);
    border: 1px solid var(--accent-dim); border-radius: 999px; padding: 2px 10px;
  }
  .gauge {
    height: 8px; background: var(--surface2); border-radius: 999px;
    overflow: hidden; border: 1px solid var(--border); display: flex;
  }
  .base { display: block; height: 100%; background: var(--base); flex: none }
  .gain { display: block; height: 100%; background: var(--accent); flex: none }
  .gauge > span + span, .dim .bar > span + span { border-left: 2px solid var(--surface) }
  .legend { display: flex; gap: 16px; font-size: 11px; color: var(--muted); margin: 14px 0 8px }
  .legend i { display: inline-block; width: 9px; height: 9px; border-radius: 2px; margin-right: 6px; vertical-align: middle }
  .sw-base { background: var(--base) }
  .sw-gain { background: var(--accent) }
  .dims { display: grid; gap: 8px }
  .dim { display: grid; grid-template-columns: 120px 1fr 46px; align-items: center; gap: 10px; font-size: 13px }
  .dim .bar {
    height: 6px; background: var(--surface2); border-radius: 999px;
    overflow: hidden; border: 1px solid var(--border); display: flex;
  }
  .dim .v { font-family: var(--mono); color: var(--muted); text-align: right; font-size: 12px }
  .muted { color: var(--muted) }
  .var { font-family: var(--mono); color: var(--accent) }
  ul { margin: 0; padding-left: 18px }
  li { margin: 4px 0; font-size: 13px }
  .foot {
    padding: 14px 22px; font-size: 11px; color: var(--muted);
    display: flex; align-items: center; justify-content: space-between;
  }
  .footbrand { display: flex; align-items: center; gap: 6px; font-family: var(--mono) }
  .dot-sm { width: 6px; height: 6px; border-radius: 2px; background: var(--accent); flex: none }
  .mono { font-family: var(--mono) }
</style>
</head>
<body>
  <div class="card">

    <div class="card-h">
      <div class="brandlock">
        <span class="dot"></span>
        <div class="brandtext">
          <span class="brand">revenant-foundation-promptsmith</span>
          <span class="cardtitle">Security Audit &rarr; CISO Summary</span>
        </div>
      </div>
      <span class="chip">CO-STAR</span>
    </div>

    <div class="section">
      <div class="label">TL;DR</div>
      <div class="muted">Paste a full security audit report in and it returns exactly three plain-language bullets a non-technical CISO can act on — each leading with the risk and its business impact, no CVE numbers or tool names.</div>
    </div>

    <div class="section">
      <div class="label">Prompt</div>
      <div class="promptwrap">
        <button class="copy" onclick="copyPrompt(this)">Copy</button>
        <pre><code id="prompt">You are a CISO's chief of staff. Summarize the security audit in &lt;report&gt; into
exactly three bullets for a non-technical CISO.

&lt;report&gt;
{{audit_report}}
&lt;/report&gt;

Write each bullet to:
- lead with the decision or risk, not the methodology
- state the business impact in plain language (no CVE numbers, no tool names)
- stay under 25 words

Return only the three bullets — no preamble, no heading.</code></pre>
      </div>
    </div>

    <div class="section">
      <div class="label">Score</div>
      <div class="scorerow">
        <span class="score-nums">6.4 &rarr; 8.8</span>
        <span class="delta">+2.4</span>
      </div>
      <div class="gauge">
        <span class="base" style="width:64%"></span>
        <span class="gain" style="width:24%"></span>
      </div>
      <div class="legend">
        <span><i class="sw-base"></i>before</span>
        <span><i class="sw-gain"></i>gain</span>
      </div>
      <div class="dims">
        <div class="dim"><span>Clarity</span><span class="bar"><span class="base" style="width:70%"></span><span class="gain" style="width:20%"></span></span><span class="v">7 &rarr; 9</span></div>
        <div class="dim"><span>Specificity</span><span class="bar"><span class="base" style="width:60%"></span><span class="gain" style="width:30%"></span></span><span class="v">6 &rarr; 9</span></div>
        <div class="dim"><span>Context</span><span class="bar"><span class="base" style="width:60%"></span><span class="gain" style="width:20%"></span></span><span class="v">6 &rarr; 8</span></div>
        <div class="dim"><span>Completeness</span><span class="bar"><span class="base" style="width:60%"></span><span class="gain" style="width:30%"></span></span><span class="v">6 &rarr; 9</span></div>
        <div class="dim"><span>Structure</span><span class="bar"><span class="base" style="width:70%"></span><span class="gain" style="width:20%"></span></span><span class="v">7 &rarr; 9</span></div>
      </div>
    </div>

    <div class="section">
      <div class="label">Structure</div>
      <div>CO-STAR &mdash; <span class="muted">audience and tone are what drive an executive summary.</span></div>
    </div>

    <div class="section">
      <div class="label">Run on</div>
      <div>Tier B &mdash; Claude Sonnet 5 <span class="muted">&middot; effort low &mdash; executive summarization sits squarely in the balanced tier; no flagship needed.</span></div>
    </div>

    <div class="section">
      <div class="label">Variables</div>
      <ul>
        <li><span class="var">{{audit_report}}</span> &mdash; the full security audit report, as plain text.</li>
      </ul>
    </div>

    <div class="section">
      <div class="label">Assumed</div>
      <ul>
        <li>Audience reads for decisions, not method &mdash; bullets lead with risk and impact.</li>
        <li>"No jargon" includes CVE IDs and tool names; both excluded explicitly.</li>
      </ul>
    </div>

    <div class="section">
      <div class="label">Test</div>
      <div class="muted">Test it on an audit with no critical findings, to confirm the bullets stay confident without inventing severity.</div>
    </div>

    <div class="foot">
      <span class="footbrand"><span class="dot-sm"></span>revenant-foundation-promptsmith</span>
      <span>CO-STAR &middot; 6.4 &rarr; 8.8 &middot; Sonnet 5</span>
    </div>

  </div>

<script>
  function copyPrompt(btn) {
    var t = document.getElementById('prompt').textContent;
    navigator.clipboard.writeText(t).then(function() {
      var o = btn.textContent;
      btn.textContent = 'Copied';
      btn.style.color = 'var(--good)';
      setTimeout(function() { btn.textContent = o; btn.style.color = ''; }, 1400);
    }).catch(function() {
      var r = document.createRange();
      r.selectNode(document.getElementById('prompt'));
      window.getSelection().removeAllRanges();
      window.getSelection().addRange(r);
      try { document.execCommand('copy'); } catch(e) {}
      window.getSelection().removeAllRanges();
      btn.textContent = 'Copied';
    });
  }
</script>
</body>
</html>
```
