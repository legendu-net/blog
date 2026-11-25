---
title: Skills for AI Agents
created: '2026-04-28T22:28:33.673249-07:00'
date: '2026-11-15T09:29:59-08:00'
authors:
  - bendu
label: skills-for-ai-agents
license: CC-BY-4.0
tags:
  - programming
  - AI
  - agent
  - skill
  - market
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Sources of Skills

1. Use `/plugins` to manage marketplaces/plugins/skills for Claude CLI.

### Official

- [Claude Plugins](https://claude.com/plugins)

https://github.com/anthropics/claude-plugins-official

### Third-part MCP / Skill Platforms

- [skills.sh](https://skills.sh/)

- [Claude Marketplaces](https://claudemarketplaces.com/)

- [MCP Market - Find the best MCP Servers, Agents and Skills](https://mcpmarket.com/)

https://agentskills.io/home

https://skills-registry-web.vercel.app/

https://www.skillsdirectory.com/

https://clawhub.ai/

### Misc

https://github.com/anthropics/skills

https://github.com/google/skills

https://github.com/addyosmani/agent-skills

https://github.com/softaworks/agent-toolkit

https://gitlab.com/lx-industries/setup-devcontainer-skill
Agent skill that generates hardened .devcontainer/ setups for Claude Code autonomous mode and IDE use.

https://github.com/masoncl/review-prompts
AI-assisted code review prompts for Linux kernel, systemd, and iproute development. Works with Claude Code and other AI tools.

## Create Skills

Gemini CLI has a built-in meta skill named `skill-creator`
which can help create new skills quickly.
For more details,
please refer to
[Gemini CLI Docs - Creating Agent Skills](https://geminicli.com/docs/cli/creating-skills/)
.

## When to Use vs. Not Use Sub-Skills

A skill without scripts or external resources is essentially a reusable chunk of prompts.
Splitting a complex skill into smaller pieces is often good practice,
but whether a piece should become a **standalone sub-skill** or stay an **internal sub-prompt** (for example, under `references/*.md` inside the parent skill) depends on visibility and reuse.

In most agent tools, every top-level skill's `name` and `description` is injected into the system prompt on *every* turn across *every* conversation.
Exposing internal helper steps as standalone skills wastes context tokens and risks trigger pollution—misfiring when the user never intended to invoke them directly.

1. **Use `references/<sub-prompt>.md` (internal sub-prompt) when**:
   - Only one parent skill uses it.
   - Users should never invoke it standalone.
   - You want progressive disclosure—loaded on demand only when the parent skill enters that branch—with zero global catalog overhead (e.g., `deep-design/references/adversarial_design_critic.md` and `simplicity_auditor.md` in a personal skill setup).
2. **Use a standalone sub-skill when**:
   - Multiple parent skills or human users invoke it independently (e.g., `plan-exec-review` or `compare-tools`).
   - It has its own clear user-facing trigger boundary, independent lifecycle, or bundled scripts/tooling.
3. **Use a shared script or module when**:
   - Multiple skills only share deterministic logic (not prompt instructions)—extract a Python/shell module instead of duplicating prompts or creating a thin wrapper skill.

```{list-table} Sub-Skill vs. Reference Sub-Prompt vs. Shared Script
:header-rows: 1

* - Pattern
  - When to Use
  - Global Catalog Cost
  - Example
* - `references/*.md` (internal sub-prompt)
  - Used by one parent skill; not meant for direct user invocation
  - None (loaded on demand)
  - `deep-design/references/`
* - Standalone sub-skill
  - Reused across multiple skills or invoked directly by users; owns its own trigger/scripts
  - Always in system prompt (`name` + `description`)
  - `plan-exec-review`, `compare-tools`
* - Shared script / module
  - Deterministic logic shared across skills without prompt instructions
  - None
  - —
```

## Some Useful Skills

### General

- [vercel-labs/skills/find-skills](https://www.skills.sh/vercel-labs/skills/find-skills)

- [useful-ai-prompts/semantic-versioning](https://www.skills.sh/aj-geddes/useful-ai-prompts/semantic-versioning)

### Rust

- [rust-skills](https://github.com/actionbook/rust-skills)

### Investment

https://claude.com/plugins/equity-research

## References

- [MCP Market - Find the best MCP Servers, Agents and Skills](https://mcpmarket.com/)
