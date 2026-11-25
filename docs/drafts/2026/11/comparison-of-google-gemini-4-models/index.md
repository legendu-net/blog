---
title: Comparison of Google Gemini 4 Models
created: '2026-11-25T10:28:23.671571-08:00'
date: '2026-11-25T10:28:23.671580-08:00'
authors:
  - bendu
label: comparison-of-google-gemini-4-models
license: CC-BY-4.0
tags:
  - AI
  - LLM
  - Gemini
  - Google
  - OpenAI
  - Anthropic
  - Claude
  - GPT
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Summary

- **Gemini 4 Hydrogen** (`gemini-4-hydrogen`) is the fast, cost-efficient default
  for everyday coding, high-volume tasks, multimodal document pipelines,
  and parallel worker subagents.
- **Gemini 4 Neon** (`gemini-4-neon`) is the balanced workhorse
  for multi-file refactoring, repository-wide debugging, and dense knowledge work.
  It directly replaced Argon in the Gemini app model picker and Google Antigravity.
- **Gemini 4 Carbon** is Google's highest-capability frontier reasoning model,
  built for the most demanding multi-step workflows, deep research,
  advanced mathematics, and scientific analysis (Google AI Ultra).
- **Gemini 4 Argon** was the original Gemini 4 frontier model (October 2026).
  Carbon succeeded it at the top end, while Neon replaced it in the app picker;
  Argon remains temporarily accessible via API for existing workloads.
- **Agentic workflow pattern:** Because Hydrogen and Neon share the same request schema,
  context window, and tool support, a common pattern is using Neon (or Carbon)
  to plan architecture or isolate a complex bug on the first turn,
  then delegating code edits and parallel test loops to Hydrogen.

## Gemini 4 Lineup Overview

Google rolled out the Gemini 4 lineup within six weeks in late 2026:

1. **2026-10-13 — Gemini 4 Argon:** Released first as the original Gemini 4 frontier model.
2. **2026-11-10 — Gemini 4 Carbon:** Released next as a heavier, higher-ceiling flagship model above Argon.
3. **2026-11-12 — Gemini 4 Hydrogen:** Released as the fast, lightweight Flash-tier model.
4. **2026-11-18 — Gemini 4 Neon:** Released as a newer, faster mid-tier workhorse adapted from Carbon.

```{list-table} Google Gemini 4 Model Tiers
---
header-rows: 1
name: gemini-4-lineup-table
widths: 18 20 18 44
---
* - Model
  - Picker Label / Role
  - Access Tier
  - Primary Focus & Strengths
* - Gemini 4 Hydrogen
  - Fast / Everyday coding
  - Free & paid API (free in AI Studio)
  - Low latency, high throughput, and low cost. Best for quick chat, interactive web apps, routine code edits, document pipelines, and parallel worker subagents.
* - Gemini 4 Neon
  - Deeper analysis / Balanced workhorse
  - Gemini App (Pro & Ultra); paid API tier
  - Strong reasoning and coding accuracy with fast turnaround. Ideal for everyday deep analysis, multi-file refactoring, debugging, and dense knowledge work.
* - Gemini 4 Carbon
  - Most complex work
  - Google AI Ultra
  - Highest-capability frontier reasoning model with adjustable thinking levels (Chat & Task modes). Built for deep research, advanced math, science, and ambiguous multi-step problems.
* - Gemini 4 Argon (legacy)
  - Complex tasks (replaced in app picker)
  - Temporarily available via API
  - Original Gemini 4 frontier model supporting up to a 1M output token limit for massive single-trajectory generation, large-scale refactoring, enterprise work, and cybersecurity.
```

## Gemini 4 Hydrogen vs. Gemini 4 Neon

Hydrogen is Google's fast, cost-efficient default for everyday coding and agentic workloads,
while Neon sits one tier higher with stronger reasoning and accuracy at double the API token price.

```{list-table} Gemini 4 Hydrogen vs. Gemini 4 Neon
---
header-rows: 1
name: gemini-4-hydrogen-vs-neon-table
widths: 24 38 38
---
* - Feature
  - Gemini 4 Hydrogen (`gemini-4-hydrogen`)
  - Gemini 4 Neon (`gemini-4-neon`)
* - Positioning
  - Everyday coding, high-volume tasks, low-latency interactions
  - Complex, interactive software engineering, dense knowledge work, science
* - API Pricing (per 1M tokens)
  - $1.50 input / $7.50 output
  - $3.00 input / $15.00 output
* - Access Tier
  - Free and paid API tiers (and free in Google AI Studio)
  - Paid API tier only
* - Speed / Throughput
  - Fast (~164 tokens/sec at `xhigh` effort)
  - Moderate (~110 tokens/sec at `xhigh` effort)
* - Reasoning (`thinking_level`)
  - `low`, `medium`, `high` (default), `xhigh`
  - `low`, `medium`, `high` (default), `xhigh`
* - Context & Output Limits
  - 1M unified context window
  - 1M unified context window (65K synchronous output; up to 1M via long decode)
* - Intelligence Index (v5.0.1)
  - 54 at `xhigh` (drops more sharply at `low` effort)
  - 61 at `xhigh` (leads Hydrogen by 7–17 points across every effort level)
```

### Key Takeaways

- **Default to Hydrogen** for interactive web apps, routine code edits, multimodal document pipelines,
  and parallel worker subagents. It generates tokens roughly 1.5x faster than Neon and costs half as much per token.
- **Step up to Neon** for multi-file refactoring, repository-wide debugging, and harder analytical tasks.
  Running Neon at `medium` effort slightly outscores Hydrogen at `xhigh` effort (55 vs. 54 on the Intelligence Index)
  while finishing faster and often costing less overall because it uses fewer thinking tokens.
- **Pair them in agentic workflows:** Both share the exact same request schema, context window, and tool support,
  making it straightforward to plan with Neon (or Carbon) and execute edits/tests with Hydrogen.

## How Neon and Carbon Relate to Argon

Because the four Gemini 4 models launched within six weeks, Neon and Carbon each "replaced" Argon in a different sense:

- **Product-slot & workflow replacement (Neon):**
  When Google launched Gemini 4 Neon on 2026-11-18, it removed Argon from the Gemini app model picker
  (specifically the "Deeper analysis" slot for Google AI Pro and Ultra subscribers) and from Google Antigravity,
  putting Neon in its place.
  Even though Neon is priced as a mid-tier workhorse ($3 input / $15 output per 1M tokens
  vs. Argon's post-November standard rate of $4 / $20),
  its newer distillation/adaptation from Carbon lets it outscore Argon on coding and general intelligence benchmarks
  while running faster (~110 tokens/sec).
- **Flagship capability successor (Carbon):**
  In terms of architectural role and raw reasoning ceiling, Argon was originally built to compete
  in the heavyweight flagship tier alongside Claude Opus 5.5 and GPT-6.2 Astra.
  Gemini 4 Carbon took over that top-of-the-line reasoning mantle for massive, long-horizon sessions,
  while Neon occupies the balanced workhorse tier alongside Claude Sonnet 5.5 and GPT-6.2 Sol.

In short: **Carbon** succeeded Argon as Google's heaviest flagship model,
while **Neon** replaced Argon in day-to-day workflows and app pickers.

## Competitor Equivalents (OpenAI & Anthropic)

Google, OpenAI, and Anthropic have converged on a similar four-tier lineup spanning ultra-fast workers
up to heavy frontier reasoning models.

```{list-table} Cross-Vendor Model Mapping (Late 2026)
---
header-rows: 1
name: cross-vendor-model-mapping-table
widths: 28 24 24 24
---
* - Tier / Role
  - Google (Gemini 4)
  - OpenAI (GPT-6 / 6.2)
  - Anthropic (Claude 5.2 / 5.5)
* - Ultra-Fast / High-Volume (routing, extraction, simple chat, subagents)
  - Gemini 4 Hydrogen (or Flash-Lite)
  - GPT-6 Luna / GPT-6 Instant
  - Claude Haiku 5.5
* - Balanced Workhorse (everyday coding, general reasoning, iterative builds)
  - Gemini 4 Neon
  - GPT-6.2 Sol
  - Claude Sonnet 5.5
* - Flagship Reasoning (complex engineering, multi-step agents, deep analysis)
  - Gemini 4 Carbon (and former Argon)
  - GPT-6.2 Astra
  - Claude Opus 5.5
* - Ultra-Frontier / Specialized (maximum depth, edge-case science/coding)
  - Gemini 4 Carbon (at `xhigh` effort)
  - GPT-6.2 Astra (high reasoning) / GPT-6 Cyber
  - Claude Fable 5.2 (and Mythos 5.2 for vetted bio/cyber)
```

### Tier Breakdown

- **Ultra-Fast / High-Volume (Hydrogen ↔ GPT-6 Luna / Instant ↔ Haiku 5.5):**
  Focused on low latency, high token throughput, and low API cost ($0.10–$1.50 per 1M input tokens).
  Best for quick interactive chat, classification, summarization, and parallel subagent execution
  where turnaround speed matters more than deep multi-step planning.
- **Balanced Workhorse (Neon ↔ GPT-6.2 Sol ↔ Sonnet 5.5):**
  The sweet spot of speed, cost ($2–$3 per 1M input tokens), and strong agentic coding performance.
  Best for day-to-day software engineering, multi-file edits, tool-use loops, and general knowledge work;
  both Neon and Sonnet 5.5 handle 80–90% of flagship tasks at a fraction of the cost and latency.
- **Flagship Frontier Reasoning (Carbon / Argon ↔ GPT-6.2 Astra ↔ Opus 5.5):**
  Built for deep, sustained reasoning across complex, long-horizon workflows, large-scale migrations,
  and rigorous math/science or financial/legal analysis.
  OpenAI's GPT-6.2 Astra leans heavily into native OS/browser computer-use workflows,
  while Anthropic splits its top end between Opus 5.5 as the standard flagship
  and Fable 5.2 for tasks that exceed Opus's ceiling.

## References

- [](#comparison-of-google-gemini-products)

- [](#tips-on-gemini)

- [](#develop-with-google-antigravity)

- [](#benchmark-of-llms-and-ai-agents)

- [](#tips-on-claude)

- [](#tips-on-openai-codex)
