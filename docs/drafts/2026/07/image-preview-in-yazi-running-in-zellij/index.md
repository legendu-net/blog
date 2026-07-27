---
title: Image Preview in Yazi Running in Zellij
created: '2026-07-26T22:47:43.213715-07:00'
date: '2026-07-26T22:47:43.213725-07:00'
authors:
  - bendu
label: image-preview-in-yazi-running-in-zellij
license: CC-BY-4.0
tags:
  - yazi
  - file manager
  - terminal
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Image Preview

### How Yazi Picks an Image Protocol

Yazi decides which image protocol to use based on the environment variables
`$TERM`, `$TERM_PROGRAM` and `$XDG_SESSION_TYPE` first.
If none of them identifies a known terminal,
Yazi falls back to querying the terminal at runtime,
writing a kitty graphics query (`ESC _G i=31,s=1,v=1,a=q,t=d,f=24`)
followed by a primary device attributes request (`ESC [ 0c`),
and picks a protocol from the reply.
When nothing supports images, it falls back to `chafa`,
which draws the image with Unicode block characters and truecolor.

`yazi --debug` prints the outcome of this whole process,
which is the fastest way to debug a broken preview.
The interesting lines are `Brand.from_env`, `Emulator.detect` and `Adapter.matches`.

### Blank Image Preview in a Zellij Web Session

Image preview renders as a blank rectangle
when a Zellij session is viewed through the Zellij web client (`zellij web`),
even though the very same session previews images correctly
when attached from a native terminal.

The web client is [xterm.js](https://xtermjs.org/) built **without** the image addon.
Inspecting the JavaScript bundle embedded in the `zellij` binary (version 0.44.1)
shows no sixel decoder and no kitty graphics handler,
and the only OSC handlers registered are
`0, 1, 2, 4, 8, 10, 11, 12, 104, 110, 111` and `112`,
which notably excludes OSC 1337 (the iTerm2 inline image protocol).
In other words, the web client cannot display an image by *any* protocol.

The Zellij server, on the other hand, does support sixel
and advertises it in its device attributes reply.
So Yazi asks, is told sixel is available, emits a sixel sequence,
and xterm.js silently discards it.
Hence the blank rectangle rather than an error.

The workaround is to make Yazi believe it is running in a terminal without graphics support,
so that it short-circuits the query and falls back to `chafa`.
`Apple_Terminal` works because Apple Terminal is a brand Yazi knows has no image protocol.

```
TERM_PROGRAM=Apple_Terminal yazi
```

As a Fish abbreviation:

```
abbr --add yazi.web TERM_PROGRAM=Apple_Terminal yazi
```

A few caveats.

1. This cannot be automated.
   Nothing in the pane environment tells you whether the client rendering it is a browser or a terminal,
   `zellij action list-clients` does not distinguish them,
   and a single session can have a native client and a web client attached at the same time.
   It has to be opt-in.

1. `TERM_PROGRAM` is inherited by every child process of Yazi,
   including `$EDITOR`.
   Tools that gate truecolor or undercurl on this variable
   (Neovim among them) may render worse in those children.

1. Prefer overriding `TERM_PROGRAM` rather than `TERM`.
   Setting `TERM` to something like `rxvt-unicode-256color` also works
   but risks breaking keys and colors if that terminfo entry is missing.

1. `chafa` must be installed, otherwise the preview degrades further instead of erroring out.

1. If `ueberzugpp` is installed and `$XDG_SESSION_TYPE` is set,
   Yazi prefers Ueberzug over `chafa`.
   That draws an overlay window on the local desktop rather than in the browser,
   which is not what you want here.

## References

- [Image Preview - Yazi](https://yazi-rs.github.io/docs/image-preview/)
- [Previews in Zellij](https://github.com/sxyazi/yazi/issues/334)
- [Support for yazi's image preview](https://github.com/zellij-org/zellij/issues/4336)
