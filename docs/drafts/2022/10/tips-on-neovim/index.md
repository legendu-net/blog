---
title: Tips on Neovim
created: '2022-10-16T19:54:05-07:00'
date: '2026-08-03T01:20:50-07:00'
authors:
  - bendu
label: tips-on-neovim
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Vim
  - Neovim
  - AstroNvim
  - IDE
  - PPA
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

### Using Homebrew on Linux/macOS (Recommended)

```
brew install neovim
```

This is the recommended way to install Neovim.

### Ubuntu / Debian

```
sudo apt update
sudo apt install neovim
```

Note that the Neovim installed might be an old version.
Use Homebrew of AppImage instead if you want a newer version of Neovim.

## Tips and Traps

1. [AstroNvim](tips-on-astronvim) is the BEST configuration framework for NeoVim.

1. NeoVim with a complicated configuration (e.g., AstroNvim, SpaceVim, etc)
   might be too slow when editing a large (>50M) text file.
   One trick helps is to disable plugins when editing large files.
   For example,
   you can use the following command to edit a large file without loading plugins.

   ```bash
   nvim --noplugin /path/to/large/text/file
   ```

1. You can open a terminal tab within Neovim using `:term`.
   Or use `:vsplit | term` to open a terminal in vertical split mode.
   The default CWD of the terminal is the user's home directory.
   You can change it using something like `:vsplit | term cs % && fish`.

1. `NVIM_APPNAME` is an environment variable that allows you to
   manage and switch between multiple, completely isolated Neovim configurations.
   By changing this variable,
   you change the subfolder name where Neovim looks for your configurations, plugins, caches, and state files.
   Instead of defaulting to `~/.config/nvim`, it will target `~/.config/$NVIM_APPNAME`.
   This can be extremly useful if you have to keep multiple Neovim configurations.
   For example,
   if you use Firenvim with Neovim and want to use a different configuration for it.

## Manage Language Servers

### Python

```
:LspInstall ruff pyright
```

## Repeat

- [Tips on AstroNvim](tips-on-astronvim)

- [Adding dot-repeat to your Neovim plugin](https://gist.github.com/kylechui/a5c1258cd2d86755f97b10fc921315c3)

- [Better repeat #1025](https://github.com/neovim/neovim/issues/1025)
