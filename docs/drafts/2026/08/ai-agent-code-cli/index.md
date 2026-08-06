---
title: AI Agent Code CLI
created: '2026-08-04T23:01:21.516455-07:00'
date: '2026-08-04T23:01:21.516463-07:00'
authors:
  - bendu
label: ai-agent-code-cli
license: CC-BY-4.0
tags:
  - programming
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## AI Agent Code CLI

- [AIDER VS OPENCODE VS CLAUDE CODE: WHICH WINS IN JUNE 2026?](https://sanj.dev/post/comparing-ai-cli-coding-assistants/)

- [OpenCode vs Codex 2026: Which CLI Tool Wins?](https://composio.dev/content/codex-vs-opencode)

- [Claude Code vs Codex vs OpenCode: Which AI Coding Agent Is Actually The Best in 2026?](https://medium.com/@unicodeveloper/claude-code-vs-codex-vs-opencode-which-ai-coding-agent-is-actually-the-best-in-2026-baa9f6fd5374)

OpenAI Codex CLI

https://github.com/anthropics/claude-code

https://github.com/anomalyco/opencode

https://github.com/earendil-works/pi

https://github.com/aaif-goose/goose

https://github.com/charmbracelet/crush

https://github.com/can1357/oh-my-pi

https://github.com/aider-ai/aider

https://github.com/plandex-ai/plandex

https://github.com/tailcallhq/forgecode

https://github.com/esengine/deepseek-reasonix

https://github.com/Dicklesworthstone/pi_agent_rust

```{list-table} AI Agent Code CLIs Comparison
:header-rows: 1
:name: ai-agent-code-clis-table
:widths: 15 10 10 10 10 15 10 20

* - Agent CLI / Repository
  - Popularity (Stars)
  - LLM Agnostic?
  - Language
  - License
  - Remote API / Headless?
  - Dedicated Mobile App?
  - Primary Focus
* - **OpenCode** `anomalyco/opencode`
  - ~192.7k ★
  - Yes
  - TypeScript
  - MIT
  - Yes (JS/TS SDK)
  - **Yes** (OpenCode Mobile)
  - Full ecosystem (CLI, Desktop, Mobile, SDK)
* - **Pi** `earendil-works/pi`
  - ~82.8k ★
  - Yes
  - TypeScript
  - MIT
  - Yes (RPC / SDK)
  - **No**
  - Minimalist, extensible harness
* - **Goose** `aaif-goose/goose`
  - ~52.2k ★
  - Yes
  - Rust / TS
  - Apache 2.0
  - Yes (API)
  - **No** (Desktop & CLI only)
  - General OS execution / testing
* - **Aider** `aider-ai/aider`
  - ~47.3k ★
  - Yes (100+ via LiteLLM)
  - Python
  - Apache 2.0
  - Yes (`--message` headless)
  - **No**
  - Git-integrated pair programming
* - **Reasonix** `esengine/deepseek-reasonix`
  - ~31k ★
  - No (DeepSeek only)
  - Go / TS
  - MIT
  - Yes (JSON-RPC)
  - **No** (Desktop / VS Code only)
  - DeepSeek prefix-cache optimization
* - **Crush** `charmbracelet/crush`
  - ~27k ★
  - Yes (Multi-model)
  - Go
  - MIT
  - No (Focuses on TUI)
  - **No**
  - Elegant TUI with LSP integration
* - **Plandex** `plandex-ai/plandex`
  - ~15.6k ★
  - Yes
  - Go
  - MIT
  - Yes (Client/Server)
  - **No**
  - Multi-step planning for large tasks
* - **Oh-My-Pi** `can1357/oh-my-pi`
  - ~11.6k ★
  - Yes
  - Python / TS
  - Open Source
  - Unknown
  - **No**
  - Hash-anchored edits, subagents
* - **ForgeCode** `tailcallhq/forgecode`
  - ~7.5k ★
  - Yes (300+ models)
  - Rust
  - Apache 2.0
  - Unknown
  - **No**
  - Multi-model MCP-driven coding
* - **Pi Agent Rust** `Dicklesworthstone/...`
  - ~1.5k ★
  - Yes
  - Rust
  - Open Source
  - Yes (HTTP Server)
  - **No**
  - High-perf, zero-unsafe isolation
* - **Codex CLI** *(OpenAI Official)*
  - N/A
  - No* (Forks yes)
  - Rust
  - Apache 2.0
  - Yes (Python SDK)
  - **No**
  - Enterprise proxy/sandbox workflows
* - **Claude Code** *(Anthropic)*
  - N/A
  - No (Anthropic)
  - TypeScript
  - Closed
  - Yes (via MCP/Hooks)
  - **Yes** (Handoff via QR)
  - Native terminal integration w/ MCP
```

## AI Subscriptions

https://opencode.ai/go

## References

Opencode Go plan is really worth it, or just like Google's AGY (antigravity).
https://www.reddit.com/r/opencode/comments/1v1ii2p/opencode_go_plan_is_really_worth_it_or_just_like/
