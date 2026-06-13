---
title: Tips on Hyper
created: '2019-02-02T12:20:43-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-hyper
license: CC-BY-4.0
tags:
  - software
  - hyper
  - terminal
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Awesome Hyper](https://github.com/bnb/awesome-hyper)

## [Themes for Hyper](https://hyper.is/themes)

verminal is good one

## General Tips

1. Updating the environment variable `SHELL` (using the command `chsh`)
   to change the default shell doesn't work for Hyper.
   You have to set the default shell for Hyper in its configuration file directly.
   For more details,
   please refer to
   [Change Shell in Mac](change-shell-in-mac)
   .

1. If you install Hyper on Linux
   or install it using Homebrew on macOS,
   the `hyper` command is available.
   However,
   if you install Hyper on macOS using a DMG file,
   the `hyper` command is not exposed by default.
   You can follow instructions in the following screenshot
   to add the `hyper` command into the search path.

   ![hyper-cli-path](https://user-images.githubusercontent.com/824507/182229511-b5a6aeb4-903d-4ee6-a7fb-67685c61e3df.png)

## Shortcuts

- Cmd+left arrow, Cmd+right arrow navigates among tabs. So does Cmd-{ and Cmd-}.

- Cmd+number navigates directly to a tab.

- Cmd+Option+Number navigates directly to a window.

- **Cmd+Option+Arrow keys navigate among split panes.**

- **Cmd+\] and Cmd+\[ navigates among split panes in order of use.**

## References

https://github.com/zeit/hyper

https://github.com/zeit/hyper/issues/890

https://github.com/zeit/hyper/issues/828

https://github.com/bnb/awesome-hyper
