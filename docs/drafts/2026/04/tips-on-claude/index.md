---
title: Tips on Claude
created: '2026-04-18T18:53:35.655987-07:00'
date: '2026-06-02T23:52:42-07:00'
authors:
  - bendu
label: tips-on-claude
license: CC-BY-4.0
tags:
  - programming
  - AI
  - tool
  - terminal
  - CLI
  - Claude
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Claude CLI Installation

```
curl -fsSL https://claude.ai/install.sh | bash
```

Works simiarly to [Gemini CLI](tips-on-google-gemini-cli).

## Claude Desktop

1. Runs in a sandboxed VM and cannot access local files (which limits its power).

## [Claude Plugins](https://claude.com/plugins)

1. [Claude Plugins](https://claude.com/plugins) (similar concept to Gemini extensions)
   .

## GitHub Integrations

```{list-table}
---
column-width: auto
---
- - Name
  - Description
- - github.com/anthropics/claude-code 
  - Claude CLI source code
- - github.com/anthropics/claude-code-action 
  - the GitHub Action for tagging @claude in PRs and issues
- - github.com/apps/claude 
  - the Claude GitHub App for repository integrations
```

The simplest way to setup GitHub integration is to run the following command.

```sh
claude /install-github-app
```

- [claude-code-action/examples](https://github.com/anthropics/claude-code-action/tree/main/examples)

## Anthropic / Claude APIs

See [Claude API Docs](https://platform.claude.com/docs/en/home)
.

## References

https://code.claude.com/docs/en/quickstart

- [Claude API Docs](https://platform.claude.com/docs/en/home)
