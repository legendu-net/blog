---
title: Context Files for AI Agents
created: '2026-06-08T20:47:39.289506-07:00'
date: '2026-06-08T20:47:39.289516-07:00'
authors:
  - bendu
label: context-files-for-ai-agents
license: CC-BY-4.0
tags:
  - AI
  - agents
  - Antigravity
  - Claude
  - context
  - file
  - AGENTS.md
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

antigravity cli: GEMINI.md or AGENTS.md
claude cli: claude.md

Even though you can still configure the context file for antigravity cli using the key `context.fileName`,
e.g.,
```
"context": {
    "fileName": ["AGENTS.md"]
}
```
it is discouraged.
Antigravity CLI does not support the `/init` command (unlike the legacy Gemini CLI and Claude CLI).
This is because Antigravity CLI is designed to be completely zero-config and context-aware out of the box.
It automatically scans your workspace and setup files in real-time. 
You do not need to scaffold a configuration to get started.

It is suggested that you use AGENTS.md as the context file for AI agents.
Most AI agents already support it.
For AI agents which doesn't support AGENTS.md (e.g., Claude CLI),
a RELATIVE symbolic link works well.

## References

- [Provide context with GEMINI.md files](https://geminicli.com/docs/cli/gemini-md/)

- [[Docs] Documentation missing AGENTS.md as a default context filename](https://github.com/google-gemini/gemini-cli/issues/25205)

- [Managing conversations](https://antigravity.google/docs/cli-conversations)
