---
title: Tips on the Fish Shell
created: '2025-11-11T18:13:06-08:00'
date: '2026-07-03T17:11:55-07:00'
authors:
  - bendu
label: tips-on-the-fish-shell
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - shell
  - fish
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips & Traps

1. Configuration files of the fish shell are located at `~/.config/fish`.

## Installation & Configuration

[icon](https://github.com/legendu-net/icon)
makes it easy to install and configure the fish shell.

```
icon fish -ic
```

## Key Bindings

1. Use the built-in function `fish_key_reader` to tell you how to bind shortcuts.

1. If for whatever reason,
   `Alt`+`e` does edit the current command line in an external editor on macOS,
   `Alt`+`v` is the way to go (if you don't bother or don't have time to dig into configurations).

```{list-table}
---
header-rows: 1
---
- - Shortcuts
  - Description
- - Alt+.
  - Get parameter of previous commands.
- - Alt+e or Alt+v
  - Edit the current command line in an external editor.
```

Please refer to
[Interactive use](https://fishshell.com/docs/current/interactive.html)
for a more comprehensive list of key bindings.

## Globbing / Wildcard Matching

Fish only supports the `*` and `**` glob as syntax.
The `?` glob has been deprecated and is supported in newer version of fish.
For more details,
please refer to
[Fish Documentation - Wildcards (Globs)](https://fishshell.com/docs/current/fish_for_bash_users.html#wildcards-globs)
.

## Linting Tools for Fish Scripts

The fish shell provides built-in tools for lingting.

- `fish_ident`: format fish scripts.
- `fish -n`: check syntax of fish scripts.

## Completions

1. The built-in fish function
   [fish_update_completions](https://fishshell.com/docs/current/cmds/fish_update_completions.html)
   updates completions using manual pages.

1. Instead of writing completion scripts manually,
   lots of tools support exporting completion scripts for bash, zsh, fish, etc.

   - command-line applications developed using cobra (GoLang)
     - docker completion fish > ~/.config/fish/completions/docker.fish
     - icon completion fish > ~/.config/fish/completions/icon.fish

1. [crazy-complete](https://github.com/crazy-complete/crazy-complete)
   helps generate completion scripts based on YAML defined completion rules.
