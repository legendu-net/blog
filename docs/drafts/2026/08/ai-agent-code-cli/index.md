---
title: AI Agent Code CLI
created: '2026-08-04T23:01:21.516455-07:00'
date: '2026-08-08T22:12:49-07:00'
authors:
  - bendu
label: ai-agent-code-cli
license: CC-BY-4.0
tags:
  - AI
  - agent
  - code
  - programming
  - CLI
  - Claude Code
  - Codex
  - OpenCode
  - Goose
  - Pi
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## AI Agent Code CLI

Most opensource AI agent code cli tools

- are LLM agnostic
- support multi-model mode (different models for planning, execution, etc)

```{list-table} AI Agent Code CLIs Comparison
---
header-rows: 1
name: ai-agent-code-clis-table
widths: 15 10 12 15 10 20 10 10 10
---
* - Agent CLI / Repository
  - LLM Agnostic?
  - Multi-Model Mode?
  - Remote API / Headless?
  - Dedicated Mobile App?
  - Primary Focus
  - Language
  - License
  - Popularity (Stars)
* - [OpenCode](https://github.com/anomalyco/opencode)
  - Yes
  - **Yes**
  - Yes (JS/TS SDK)
  - **Yes** (OpenCode Mobile)
  - Full ecosystem (CLI, Desktop, Mobile, SDK)
  - TypeScript
  - MIT
  - ~192.7k ★
* - [Pi](https://github.com/earendil-works/pi)
  - Yes
  - **Yes** (`toolModel`: separate reasoning vs. tool-calling model)
  - Yes (RPC / SDK)
  - **No**
  - Minimalist, extensible harness
  - TypeScript
  - MIT
  - ~82.8k ★
* - [Goose](https://github.com/aaif-goose/goose)
  - Yes
  - **Yes**
  - Yes (API)
  - **No** (Desktop & CLI only)
  - General OS execution / testing
  - Rust / TS
  - Apache 2.0
  - ~52.2k ★
* - [Aider](https://github.com/aider-ai/aider)
  - Yes (100+ via LiteLLM)
  - **Yes** (`--model`/`--editor-model`)
  - Yes (`--message` headless)
  - **No**
  - Git-integrated pair programming
  - Python
  - Apache 2.0
  - ~47.3k ★
* - [Reasonix](https://github.com/esengine/deepseek-reasonix)
  - No (DeepSeek only)
  - **Yes** (executor + planner via `planner_model`)
  - Yes (JSON-RPC)
  - **No** (Desktop / VS Code only)
  - DeepSeek prefix-cache optimization
  - Go / TS
  - MIT
  - ~31k ★
* - [Crush](https://github.com/charmbracelet/crush)
  - Yes (Multi-model)
  - **Yes** (large model for Coder agent, small model for Task agent)
  - No (Focuses on TUI)
  - **No**
  - Elegant TUI with LSP integration
  - Go
  - MIT
  - ~27k ★
* - [Plandex](https://github.com/plandex-ai/plandex)
  - Yes
  - **Yes** (per-role model packs: planner/architect/coder/builder/summarizer)
  - Yes (Client/Server)
  - **No**
  - Multi-step planning for large tasks
  - Go
  - MIT
  - ~15.6k ★
* - [Oh-My-Pi](https://github.com/can1357/oh-my-pi)
  - Yes
  - **Yes** (role-based routing, e.g. dedicated `plan` role)
  - Unknown
  - **No**
  - Hash-anchored edits, subagents
  - Python / TS
  - Open Source
  - ~11.6k ★
* - [ForgeCode](https://github.com/tailcallhq/forgecode)
  - Yes (300+ models)
  - **Yes** (Forge/Muse/Sage agents each configurable with their own model)
  - Unknown
  - **No**
  - Multi-model MCP-driven coding
  - Rust
  - Apache 2.0
  - ~7.5k ★
* - [Pi Agent Rust](https://github.com/Dicklesworthstone/pi_agent_rust)
  - Yes
  - **Yes** (ports Pi's `toolModel` dual-model design)
  - Yes (HTTP Server)
  - **No**
  - High-perf, zero-unsafe isolation
  - Rust
  - Open Source
  - ~1.5k ★
* - [Codex CLI](https://github.com/openai/codex) *(OpenAI Official)*
  - No* (Forks yes)
  - No (Plan mode inherits the global model; manual switch only)
  - Yes (Python SDK)
  - **No**
  - Enterprise proxy/sandbox workflows
  - Rust
  - Apache 2.0
  - N/A
* - [Claude Code](https://github.com/anthropics/claude-code)
  - No (Anthropic)
  - **Yes** (per-subagent model config)
  - Yes (via MCP/Hooks)
  - **Yes** (Handoff via QR)
  - Native terminal integration w/ MCP
  - TypeScript
  - Closed
  - N/A
```

## References

- [AIDER VS OPENCODE VS CLAUDE CODE: WHICH WINS IN JUNE 2026?](https://sanj.dev/post/comparing-ai-cli-coding-assistants/)

- [OpenCode vs Codex 2026: Which CLI Tool Wins?](https://composio.dev/content/codex-vs-opencode)

- [Claude Code vs Codex vs OpenCode: Which AI Coding Agent Is Actually The Best in 2026?](https://medium.com/@unicodeveloper/claude-code-vs-codex-vs-opencode-which-ai-coding-agent-is-actually-the-best-in-2026-baa9f6fd5374)
