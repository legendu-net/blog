---
title: Tips on Google Gemini CLI
created: '2025-07-06T08:55:45-07:00'
date: '2026-11-15T09:28:43-08:00'
authors:
  - bendu
label: tips-on-google-gemini-cli
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Google
  - Gemini
  - CLI
  - AI
  - LLM
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Use
[Antigravity CLI](develop-with-google-antigravity)
instead.

## Tips & Traps

1. Gemini CLI is extremely useful as it doesn't requires your favorite IDE to have integration with LLM tools.
   You can use whichever IDE you like.
   What you need is just a terminal.
   Even if you do prefer IDE,
   Gemini CLI might work better than the VSCode extension "Gemini Code Assist".

1. You can do concurrent tasks by opening multiple Gemini CLI (in a multiplexing tool, say Zellij).

1. The YOLO mode (`gemini --yolo`) is strongly discouraged.
   It is suggested that you leverage
   [Policy Engine](https://geminicli.com/docs/reference/policy-engine/)
   to grant permissions for each specific tool.

1. You can pipe output of another command into Gemini.
   Below is such an example.

   ```
   git diff --cached | gemini -p "Generate a conventional commits message based on this diff. Output only the message."
   ```

1. Gemini CLI allows you run shell commands directly by prefixing it with an exclamation mark (!)
   similar to IPython.

1. Use `/help` for more information on Gemini CLI.

1. Use the command `/vim` to toggle on Vim mode.
   This sets `vimMode: true` in the file `~/.gemini/settings.json`.

## Manage Prompts

1. Use the command `/init` to generate `GEMINI.md` in the root directory of your project.
   This generated file `GEMINI.md` contains high-level summary about your project,
   which serves as the context for Geminii CLI.
   You can polish `GEMINI.md` as needed.

1. You can write prompts (even each one-time) in text file and then use `@/path/to/prompt/file` to load it to Gemini CLI.
   This can make writing prompts easier as you can write prompts in your favorite IDE and can easily polish it as needed.

1. Define custom command for reusable prompts.

## Memory Management

Saves your effort about historical conversations.

https://geminicli.com/docs/cli/tutorials/memory-management/

https://geminicli.com/docs/cli/tutorials/memory-management/#scenario-saving-a-memory

```
/memory show
/memory reload
```

## Gemini Custom Commands vs Skills

Skills are preferred to custom commands for a few reasons.

1. Skill is open standard and is portable to other agents (Claude, Codex, etc).

1. A custom command can be implemented as a skill.

1. It's easier and more flexible to trigger a skill (though mismatch might happen).

## Gemini Extensions

Gemini supports extensions
(similar concepts to [Claude Plugins](https://claude.com/plugins))
.

- [Official Gemini Extension Market](https://geminicli.com/extensions/)

- [More Gemini Extensions](https://github.com/gemini-cli-extensions)

## Automation Workflows Based on Gemini CLI

[Automate tasks with headless mode](https://geminicli.com/docs/cli/tutorials/automation/)

## References

- [The Gemini CLI turns me into an unstoppable coding beast](https://www.youtube.com/watch?v=YAy7kd5Nqm0)

- [Google Gemini CLI: AI in Your Terminal (Windows • Linux • macOS)](https://www.youtube.com/watch?v=xqvprnPocHs)
