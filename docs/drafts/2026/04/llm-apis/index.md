---
title: LLM APIs
created: '2026-04-16T20:55:36.570950-07:00'
date: '2026-11-23T19:42:00-08:00'
authors:
  - bendu
label: llm-apis
license: CC-BY-4.0
tags:
  - programming
  - code
  - AI
  - LLM
  - tool
  - API
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

- [Talk to Google Gemini Using Python API](talk-to-google-gemini-using-python-api)

## [LiteLLM](https://github.com/BerriAI/litellm)

[LiteLLM](https://github.com/BerriAI/litellm)
is an open source AI Gateway that gives you a single,
unified interface to call 100+ LLM providers — OpenAI, Anthropic, Gemini, Bedrock, Azure, and more — using the OpenAI format.

## [TextGrad](https://github.com/zou-group/textgrad)

[TextGrad](https://github.com/zou-group/textgrad)
is a powerful framework building automatic \`\`differentiation'' via text.
TextGrad implements backpropagation through text feedback provided by LLMs,
strongly building on the gradient metaphor.

## Free Quotas Across Coding Agent CLIs (as of 2026-11)

Major coding agent CLIs handle free-tier access and older-model quotas very differently.
Neither OpenAI nor Google publishes fixed token counts for free CLI quotas—both use dynamic,
compute- or task-based limits that can change without notice.

```{list-table} Free Quota Comparison Across Coding Agent CLIs
---
header-rows: 1
name: coding-cli-free-quotas
---
* - CLI Tool
  - Free Tier Availability
  - Quota & Reset Window
  - Models & Notes
* - **Codex CLI** ([OpenAI](https://developers.openai.com/codex/pricing))
  - Limited via ChatGPT Free account (no standalone permanent free API tier).
  - Small, unpublished daily/rolling allowance; API keys use pay-as-you-go RPM/TPM tiers.
  - Routes free/lower-tier usage through lighter or older models. Paid Plus/Pro plans use rolling 5-hour and weekly windows.
* - **Antigravity CLI (`agy`)** ([Google](https://antigravity.google/docs/cli/reference))
  - Yes, Individual (Free) tier at $0/month.
  - Dynamic work-based quota (no published fixed token counts), refreshing weekly with short-term burst limits; no paid credit overflow.
  - Accesses lighter/standard Gemini models (e.g., Flash variants). Check remaining quota via `/usage` or `/quota` in the TUI. All concurrent `agy` sessions share the same account pool.
* - **Claude Code** ([Anthropic](https://www.anthropic.com/pricing))
  - **No free tier.**
  - Requires a paid Claude subscription (Pro $20/mo, Max 5x $100/mo, Max 20x $200/mo, sharing the 5-hour/weekly pool with Claude.ai) or an `ANTHROPIC_API_KEY` (pay-per-token).
  - Haiku is the lowest-cost Claude API model, with prompt caching support.
```

### Practical Use Cases for Free Older-Model Quotas

Because free-tier quotas on older or lighter models are tightly capped and lack credit-pool overflow,
they are **not** ideal for critical-path interactive workflows where a rate-limit error interrupts your flow
(for example, replacing a reliable primary model like `gemini-4-hydrogen-low` in a commit-message generator such as `ccm` when you never hit its quota).
Instead, free older-model quotas work best for:

- **Fallback routing**: Placing a free model behind your primary model in a gateway like [OmniRoute](#ai-routing-services) or `ccm` so it only absorbs overflow.
- **Non-blocking batch jobs**: Offline classification, blog-post tagging/triage, or summarizing git/jj logs where hitting a rate limit simply pauses the batch.
- **Mechanical transformations**: Generating boilerplate, regexes, docstrings, or format conversions (e.g., HTML tables to MyST `list-table`).
- **Pre-filtering / first-pass summarization**: Summarizing long logs or emails before escalating complex items to a frontier model.
