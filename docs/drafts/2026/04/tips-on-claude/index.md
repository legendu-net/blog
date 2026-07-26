---
title: Tips on Claude
created: '2026-04-18T18:53:35.655987-07:00'
date: '2026-07-26T09:05:03-07:00'
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

## General Tips

1. Use `/review` and `/ultra-review` to review code changes.

1. Enable voice mode using the command `/voice`.
   See discussions in
   [claude cli voice input](https://share.gemini.google/j9U9cXKTfWRn)
   .

## Permissions

1. If you are already inside an active Claude Code CLI session,
   you can cycle through available permission modes by pressing `shift+tab`.

   - `default`: Ask for most actions
   - `acceptEdits`: Auto-approve file edits and common filesystem operations
   - `plan`: Read-only planning, no changes
   - `auto`: Auto-approve actions with safety checks

   There are actually 2 another permission modes `dontAsk` and `bypassPermissions`.

   - `dontAsk` automatically denies every tool call that would otherwise prompt.
     The only things that run are:

     - Actions matching your `permissions.allow` rules
     - Read-only Bash commands

     Even explicit ask rules get denied (rather than pausing for you),
     and writes to protected paths (.git, .claude, etc.) are denied.
     The result is a fully non-interactive session where Claude can only do what you've pre-approved in advance.
     The user case for `dontAsk` is locked-down CI pipelines or restricted environments where you whitelist exactly what's allowed.
     The `dontAsk` permission mode never appears in the `shift+tab` cycle,
     instead,
     it can only be turned on by starting Claude CLI with `claude --permission-mode dontAsk`.

   - `bypassPermissions` allows everything.
     It is sometimes called the YOLO (you only look once) permission mode in other agentic tools (e.g., Antigravity CLI).
     By default,
     you don't see `bypassPermissions` when pressing `shift+tab` to cycle through permission modes.
     You have to start Claude CLI with `claude --allow-dangerously-skip-permissions`
     to make it show up when cycling through permission modes.
     You can also directly directly get into the `bypassPermissions` mode
     by starting Claude with `claude --dangerously-skip-permissions`.

     You can start Claude with a specific permission mode toggled on
     using the option `--permission-mode`.

1. The "auto"permission mode is generally the recommended setting for non-security-critical tasks.
   It strikes a good balance between productivity and safety.
   The "auto" permission mode is a good fit for

   - Refactoring code
   - Writing tests
   - Updating documentation
   - Creating scripts
   - Data analysis on non-sensitive data
   - Local development in personal projects
   - Prototyping and experimentation

   You might prefer a more restrictive mode when:

   - Working with production infrastructure
   - Managing secrets, credentials, or sensitive customer data
   - Running destructive operations (database migrations, large file deletions, etc.)
   - Operating in regulated environments

   And you might use bypassPermissions only when:

   - You're in a disposable environment (Docker container, VM, sandbox)
   - You fully trust the workflow
   - You want maximum automation and accept the risks

1. The command `/fewer-permission-prompts` scans your transcripts for common read-only Bash and MCP tool calls,
   then add a prioritized allowlist to **project** (not global) `.claude/settings.json` to reduce permission prompts.

1. You can set the default permission mode in
   `~/.claude/settings.json`
   .
   For example,

   ```json
   "permissions": {
       "defaultMode": "auto"
   }
   ```

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

Notice that there are issues in the generated workflow `claude-code-review.yml`.
Please see discussions in
[Claude doesn't generate any output from PR review](https://github.com/anthropics/claude-code-action/issues/944)
for root causes and solutions.

- [claude-code-action/examples](https://github.com/anthropics/claude-code-action/tree/main/examples)

## Anthropic / Claude APIs

See [Claude API Docs](https://platform.claude.com/docs/en/home)
.

## References

- [Claude Code Docs](https://code.claude.com/docs/en/quickstart)

- [Claude Code Docs - Permission Modes](https://code.claude.com/docs/en/permission-modes)

- [Stop Fighting Claude Code’s Permission Prompts — Here’s How the System Actually Works](https://blog.stackademic.com/stop-fighting-claude-codes-permission-prompts-here-s-how-the-system-actually-works-ae594e59fb13)

- [Claude API Docs](https://platform.claude.com/docs/en/home)
