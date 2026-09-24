---
title: Develop with Google Antigravity
created: '2026-05-24T23:28:22.137138-07:00'
date: '2026-09-24T08:17:43-07:00'
authors:
  - bendu
label: develop-with-google-antigravity
license: CC-BY-4.0
tags:
  - programming
  - code
  - AI
  - agent
  - Antigravity
  - CLI
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## General Tips

1. Antigravity CLI intends to replace Gemini CLI.

1. Antigravity CLI doesn't support the `/init` command.
   It manages context automatically.

## Install Antigravity CLI

```sh
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

## Permissions

ctrl + k to approve

```sh
agy --dangerously-skip-permissions
```

Avoid passing flags like `--dangerously-skip-permissions`
if you need the agent to stop at /plan review checkpoints.

- [CLI Bug: --dangerously-skip-permissions bypasses /plan mode stop hooks · Issue #1074](https://github.com/google-antigravity/antigravity-cli/issues/1074?utm_source=gemini)

- [Understanding Antigravity CLI Stop Hook](https://share.gemini.google/sEyxQJnWCWMV)

## References

- [Antigravity Documentation](https://antigravity.google/docs/home)

- [Migrating from Gemini CLI](https://antigravity.google/docs/gcli-migration)

- [Tips on Google Gemini CLI](tips-on-google-gemini-cli)

- [Tips on Gemini](tips-on-gemini)
