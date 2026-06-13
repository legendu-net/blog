---
title: Tips on Bash Completion
created: '2025-05-06T14:27:02-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-bash-completion
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - shell
  - Bash
  - completion
  - complete
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Fish Shell](tips-on-the-fish-shell)
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

It is suggested that you use the fish shell
instead of the bash shell
(for iteractive use cases)
.

## Installation

### Ubuntu / Debian

```
sudo apt install bash-completion
```

### macOS

```
brew install bash-completion
```

If you don't like or cannot install bash-completion,
[bash-it](https://github.com/Bash-it/bash-it)
provies completion scripts for many popular tools.

## Develop Bash Completion

- [Completion files](https://devmanual.gentoo.org/tasks-reference/completion/index.html)

- [A Programmable Completion Example](https://www.gnu.org/software/bash/manual/html_node/A-Programmable-Completion-Example.html)

## Auto Generate Bash Completion Scripts

1. The cobra library in GoLang supports auto genrating shell (bash, fish, zsh and PowerShell) completion scripts.

1. The Python library
   [argcomplete](https://github.com/kislyuk/argcomplete)
   provides easy, extensible command line tab completion of arguments for your Python application.
   It makes two assumptions:

   - You're using bash or zsh as your shell.
   - You're using argparse to manage your command line arguments/options.

1. The Ruby library (and also command-line tool)
   [completely](https://github.com/DannyBen/completely)
   lets you generate bash completion scripts from simple YAML configuration.
