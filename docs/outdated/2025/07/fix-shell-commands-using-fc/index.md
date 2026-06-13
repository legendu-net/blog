---
title: Fix Shell Commands Using fc
created: '2025-07-06T11:08:48-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: fix-shell-commands-using-fc
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - shell
  - command
  - Bash
  - zsh
  - fc
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Fish Shell](tips-on-the-fish-shell)
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

[fzf.history](https://github.com/legendu-net/icon/blob/dev/utils/data/bash-it/plugins/custom.plugins.bash#L149)
is a better alternative to `fc`'s core functionality (edit and re-execute command).

## Tips & Traps

1. In Linux shells like Bash and Zsh,
   `fc` is a built-in command that stands for "Fix Command".
   Its primary purpose is to let you edit and re-execute commands
   from your history using `$EDITOR`.

1. `fc -l 1` might throw the error `-bash: fc: history specification out of range` in bash
   (some people say that this won't be an issue in zsh as zsh is smart enough to handle specification out of range but I haven't verified it yet)
   if the (absolute) first bash history command has been pruned (due to large number of history commands).
   `HISTTIMEFORMAT="" history | sed -E 's/^[ ]*[0-9]+[ ]*//'` is a more robust command for the same purpose.

```{list-table}
---
header-rows: 1
---
- - Command
  - Action
- - `fc`
  - Edit the last shell command using `$EDITOR` and send it for execution.
- - `fc 123`
  - Edit and execute command number 123 from history.
- - `fc git`
  - Edit and execute the last command starting with "git".
- - `fc -l`
  - List all history commands.
- - `fc -ln`
  - List all history commands without numbers.
- - `fc -ln 100 110`
  - List commands from 100 to 110 without numbers.
- - `fc -ln -5`
  - List the last 5 historical commands without numbers.
- - `fc -s`
  - Re-execute the last command without editing.
- - `fc -s old=new`
  - Re-execute the last command, replacing `old` with `new`.
- - `fc -s old=new git`
  - Re-execute the last `git` command, replacing `old` with `new`.
```
