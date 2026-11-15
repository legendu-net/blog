---
title: Auto Completion Using YouCompleteMe in Vim
created: '2015-09-22T14:00:13-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: auto-completion-using-youcompleteme-in-vim
license: CC-BY-4.0
tags:
  - software
  - YouCompleteMe
  - YCM
  - Vim
  - plugin
  - addon
  - editor
  - tips
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. You might need the package `python-dev` (in Debian Series)
   or `python-devel` (in Arch Linux) in order to compile the Vim addon YouCompleteMe.

1. you should use install.py instead of install.sh.
   The later one is deprecated.

1. Run the following command to compile YouCompleteMe with clang support.

   ```bash
   ./install.py --clang-completer
   ```

   This has been integrated into the script `linfig.vim`

1. YouCompeleteMe configuration file, this is done via the command linfig.vim currently

1. YCM can be installed on Cygwin as well
   if you do not have clang installed on cygwin then compile with the following command

   ```language
   ./install.py 
   ```

1. functions opened in all buffers are accessible by YCM,
   so they can be autocompleted

1. requires cmake to compile, added to linstall.vim
