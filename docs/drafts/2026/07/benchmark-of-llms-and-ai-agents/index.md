---
title: Benchmark of LLMs and AI Agents
created: '2026-07-21T23:01:21.529121-07:00'
date: '2026-11-24T02:16:30-08:00'
authors:
  - bendu
label: benchmark-of-llms-and-ai-agents
license: CC-BY-4.0
tags:
  - AI
  - LLM
  - agents
  - benchmark
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

- [Models.dev - An open-source database of AI models](https://models.dev/)

- [Artificial Analysis Coding Agent Benchmarks](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=benchmark-score-by-eval)

- [Benchmarking Coding Agents on Databricks’ Multi-Million Line Codebase](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase)

- [LLM Rankings](https://openrouter.ai/rankings)

## LLM Subscriptions

### Free

- [Gemini Free Tier](https://aistudio.google.com/)

- [OpenCode Free Tier](https://opencode.ai/)

  - automatically included in OmniRoute and no signup is required

- Felo Free Tier

  - automatically included in OmniRoute and no signup is required

#### Coding Agent CLI Free Quotas (as of 2026-11)

Among major coding agent CLIs, **Antigravity CLI (`agy`)** offers the most usable free tier for personal development, **Codex CLI** provides only a limited ChatGPT Free allowance, and **Claude Code** has no free tier at all.

```{list-table} Coding Agent CLI Free Quota Comparison (as of 2026-11)
---
header-rows: 1
name: coding-agent-cli-free-quotas-table
widths: 20 10 30 40
---
* - Agent CLI
  - Free Tier?
  - Quota / Reset Window
  - Models & Notes
* - [Antigravity CLI (`agy`)](https://antigravity.google/)
  - Y[^ft-agy]
  - Weekly dynamic work-based quota + burst limits
  - Lighter/standard Gemini models (unpublished exact caps); check with `/usage` or `/quota`
* - [Codex CLI](https://github.com/openai/codex)
  - Y[^ft-codex]
  - Unpublished small daily/rolling allowance
  - Lighter/older models (unpublished exact list) via ChatGPT Free account
* - [Claude Code](https://github.com/anthropics/claude-code)
  - N[^ft-claude]
  - None
  - Requires Pro/Max plan or pay-per-token API
```

#### Practical Use Cases for Free Older-Model Quotas

- **Avoid on critical-path workflows**: Do not replace reliable paid/primary models in interactive or blocking tools (such as `ccm` for git/jj commit messages) with free older-model quotas—hitting an unexpected rate limit or weekly cap mid-workflow creates more hassle than the cost savings are worth.
- **Fallback routing**: Place free older models in a fallback tier behind a primary model in [OmniRoute](#ai-routing-services) or `ccm`.
- **Non-blocking batch jobs**: Offline classification, blog-post tagging/triage, or summarizing commit logs where hitting a rate limit simply pauses the batch.
- **Mechanical transformations**: Boilerplate generation, regex writing, docstrings, or HTML-to-MyST `list-table` conversions.
- **Pre-filtering / first-pass summarization**: Summarizing long logs or emails before escalating complex items to a frontier model.

### Cheap

- [DeepSeek](https://platform.deepseek.com/)

- [Qwen AI](https://qwen.ai/apiplatform)

- [OpenCode Go](https://opencode.ai/go)

## References

- [Opencode Go plan is really worth it, or just like Google's AGY (antigravity).](https://www.reddit.com/r/opencode/comments/1v1ii2p/opencode_go_plan_is_really_worth_it_or_just_like/)

[^ft-agy]: Individual (Free) tier at $0/mo with no paid credit overflow; all concurrent `agy` sessions share the same account pool.
[^ft-codex]: Limited access via a ChatGPT Free account (no standalone permanent free API tier); paid Plus ($20/mo) and Pro plans use rolling 5-hour and weekly windows.
[^ft-claude]: Requires a Claude Pro ($20/mo) or Max ($100–$200/mo) subscription (sharing the 5-hour/weekly pool with Claude.ai) or an `ANTHROPIC_API_KEY` (with Haiku as the lowest-cost option).
