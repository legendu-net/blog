Status: published
Date: 2025-05-06 14:27:02
Modified: 2025-05-11 16:48:14
Author: Benjamin Du
Slug: tips-on-bash-completion
Title: Tips on Bash Completion
Category: Computer Science
Tags: Computer Science, programming, shell, bash, completion, complete

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

### Ubuntu / Debian

    wajig install bash-completion

### macOS

    brew install bash-completion

If you don't like or cannot install bash-completion,
bash-it provies completion scripts for many popular tools.

## Develop Bash Completion

- [Completion files](https://devmanual.gentoo.org/tasks-reference/completion/index.html)

- [A Programmable Completion Example](https://www.gnu.org/software/bash/manual/html_node/A-Programmable-Completion-Example.html)

## Auto Generate Bash Completion Scripts

1. The cobra library in GoLang supports auto genrating shell (bash, fish, zsh and PowerShell) completion scripts.

2. The Python library
  [argcomplete](https://github.com/kislyuk/argcomplete)
  provides easy, extensible command line tab completion of arguments for your Python application.
  It makes two assumptions:
    - You're using bash or zsh as your shell.
    - You're using argparse to manage your command line arguments/options.

3. The Ruby library (and also command-line tool)
  [completely](https://github.com/DannyBen/completely)
  lets you generate bash completion scripts from simple YAML configuration.

