---
title: AI Agent Code CLI
created: '2026-08-04T23:01:21.516455-07:00'
date: '2026-08-09T10:40:14-07:00'
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
- support [multi-model mode](https://share.gemini.google/2Im7RTv2OcbI)

```{list-table} AI Agent Code CLIs Comparison
---
header-rows: 1
name: ai-agent-code-clis-table
widths: 15 6 6 8 6 20 10 10 10
---
* - Agent CLI
  - LLM Agnostic?
  - Multi-Model?
  - Remote API?
  - Mobile App?
  - Primary Focus
  - Language
  - License
  - Popularity (Stars)
* - [OpenCode](https://github.com/anomalyco/opencode)
  - Y
  - Y
  - Y[^ra-opencode]
  - Y[^ma-opencode]
  - Full ecosystem (CLI, Desktop, Mobile, SDK)
  - TypeScript
  - MIT
  - ~192.7k ★
* - [Pi](https://github.com/earendil-works/pi)
  - Y
  - Y[^mm-pi]
  - Y[^ra-pi]
  - N
  - Minimalist, extensible harness
  - TypeScript
  - MIT
  - ~82.8k ★
* - [Goose](https://github.com/aaif-goose/goose)
  - Y
  - Y
  - Y[^ra-goose]
  - N[^ma-goose]
  - General OS execution / testing
  - Rust / TS
  - Apache 2.0
  - ~52.2k ★
* - [Aider](https://github.com/aider-ai/aider)
  - Y[^la-aider]
  - Y[^mm-aider]
  - Y[^ra-aider]
  - N
  - Git-integrated pair programming
  - Python
  - Apache 2.0
  - ~47.3k ★
* - [Reasonix](https://github.com/esengine/deepseek-reasonix)
  - N[^la-reasonix]
  - Y[^mm-reasonix]
  - Y[^ra-reasonix]
  - N[^ma-reasonix]
  - DeepSeek prefix-cache optimization
  - Go / TS
  - MIT
  - ~31k ★
* - [Crush](https://github.com/charmbracelet/crush)
  - Y[^la-crush]
  - Y[^mm-crush]
  - N[^ra-crush]
  - N
  - Elegant TUI with LSP integration
  - Go
  - MIT
  - ~27k ★
* - [Plandex](https://github.com/plandex-ai/plandex)
  - Y
  - Y[^mm-plandex]
  - Y[^ra-plandex]
  - N
  - Multi-step planning for large tasks
  - Go
  - MIT
  - ~15.6k ★
* - [Oh-My-Pi](https://github.com/can1357/oh-my-pi)
  - Y
  - Y[^mm-ohmypi]
  - Unknown
  - N
  - Hash-anchored edits, subagents
  - Python / TS
  - Open Source
  - ~11.6k ★
* - [ForgeCode](https://github.com/tailcallhq/forgecode)
  - Y[^la-forgecode]
  - Y[^mm-forgecode]
  - Unknown
  - N
  - Multi-model MCP-driven coding
  - Rust
  - Apache 2.0
  - ~7.5k ★
* - [Pi Agent Rust](https://github.com/Dicklesworthstone/pi_agent_rust)
  - Y
  - Y[^mm-pirust]
  - Y[^ra-pirust]
  - N
  - High-perf, zero-unsafe isolation
  - Rust
  - Open Source
  - ~1.5k ★
* - [Codex CLI](https://github.com/openai/codex) *(OpenAI Official)*
  - N[^la-codex]
  - N[^mm-codex]
  - Y[^ra-codex]
  - N
  - Enterprise proxy/sandbox workflows
  - Rust
  - Apache 2.0
  - N/A
* - [Claude Code](https://github.com/anthropics/claude-code)
  - N[^la-claude]
  - Y[^mm-claude]
  - Y[^ra-claude]
  - Y[^ma-claude]
  - Native terminal integration w/ MCP
  - TypeScript
  - Closed
  - N/A
```

## References

- [AIDER VS OPENCODE VS CLAUDE CODE: WHICH WINS IN JUNE 2026?](https://sanj.dev/post/comparing-ai-cli-coding-assistants/)

- [OpenCode vs Codex 2026: Which CLI Tool Wins?](https://composio.dev/content/codex-vs-opencode)

- [Claude Code vs Codex vs OpenCode: Which AI Coding Agent Is Actually The Best in 2026?](https://medium.com/@unicodeveloper/claude-code-vs-codex-vs-opencode-which-ai-coding-agent-is-actually-the-best-in-2026-baa9f6fd5374)

[^ra-opencode]: JS/TS SDK.

[^ma-opencode]: Dedicated OpenCode Mobile app.

[^mm-pi]: `toolModel`: separate reasoning vs. tool-calling model.

[^ra-pi]: RPC / SDK.

[^ra-goose]: REST API.

[^ma-goose]: Desktop & CLI only, no mobile app.

[^la-aider]: 100+ providers via LiteLLM.

[^mm-aider]: `--model`/`--editor-model` flags.

[^ra-aider]: `--message` flag for headless/one-shot runs.

[^la-reasonix]: DeepSeek models only.

[^mm-reasonix]: Executor + planner via `planner_model`.

[^ra-reasonix]: JSON-RPC interface.

[^ma-reasonix]: Desktop / VS Code integration only, no mobile app.

[^la-crush]: Multi-model support across providers.

[^mm-crush]: Large model for the Coder agent, small model for the Task agent.

[^ra-crush]: Focuses on the TUI; no dedicated remote API.

[^mm-plandex]: Per-role model packs: planner/architect/coder/builder/summarizer.

[^ra-plandex]: Client/server architecture.

[^mm-ohmypi]: Role-based routing, e.g. a dedicated `plan` role.

[^la-forgecode]: 300+ models via OpenRouter and direct providers.

[^mm-forgecode]: Forge/Muse/Sage agents, each configurable with its own model.

[^mm-pirust]: Ports Pi's `toolModel` dual-model design.

[^ra-pirust]: Built-in HTTP server.

[^la-codex]: Locked to OpenAI models officially; community forks add other providers.

[^mm-codex]: Plan mode inherits the global model; manual switching only, no built-in per-role split.

[^ra-codex]: Python SDK.

[^la-claude]: Anthropic models only (official).

[^mm-claude]: Per-subagent model configuration.

[^ra-claude]: Via MCP servers and hooks.

[^ma-claude]: Session handoff to mobile via QR code.
