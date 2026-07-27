---
title: Zellij Is the Best Terminal Multiplexer
created: '2021-11-09T10:19:10-08:00'
date: '2026-07-26T22:41:47-07:00'
authors:
  - bendu
label: zellij-is-the-best-terminal-multiplexer
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - Zellij
  - multiplexer
  - terminal
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Mouse Mode

By default Zellij captures mouse events
(click to switch panes/tabs, drag borders to resize, wheel to scroll scrollback).
The command

```
zellij options --disable-mouse-mode
```

turns mouse handling off for the session,
handing the mouse back to your terminal emulator and the program running inside the pane.
The main reason to do this is **text selection / copy-paste**:
with mouse mode on you usually have to hold `Shift` to select text,
while disabling it restores native terminal selection.
The tradeoff is you lose click-to-focus panes, drag-resize, and wheel scrolling of Zellij's scrollback.

To make it permanent, set it in `~/.config/zellij/config.kdl` instead:

```kdl
mouse_mode false
```

## Session Management

```
zellij -l welcome
```

## Zellij Web

1. You can create a token using `zellij web --create-token`
   and then start a web server for zellij using `zellij web`
   .

1. By default,
   `zellij web` uses the IPv4 address `127.0.0.1`.
   Modern browsers (Chrome, Edge, ect) might resolves `localhost` as the IPv6 address `::1`.
   If that's the case,
   visiting `localhost:8082` will results in the error code `ERR_EMPTY_RESPONSE`
   .
   It is suggested that you use `127.0.0.1` instead of `localhost`
   when visiting the web page or doing local port fowarding via SSH tunneling.

1. Use `mkcert` to create certificate for hosting HTTPS
   if you need to share sessions beyong the local network.

For more discussions,
please refer to
[The Zellij Web Client - Share Sessions in the Browser](https://zellij.dev/tutorials/web-client/)
.

## Resize Panes

```{list-table}
---
header-rows: 1
---
* - Shortcut
  - Description
* - `Alt` + `+`
  - Increase the size of the focused pane.
* - `Alt` + `-`
  - Decrease the size of the focused pane.
* - `Alt` + `f`
  - Toggle floating panes on and off.
```

For more discussions,
please refer to
[Stacked Resize and Pinned Floating Panes](https://zellij.dev/tutorials/stacked-resize/)
.

## Filepicker

filepick is cool but doesn't seem to be as useful as your `ffd` & `fcd`, etc

zellij run -f -- plugin filepicker

zellij run -- plugin filepicker

zpipe filepicker | xargs -I {} cp {} ./destination-folder/

zpipe filepicker | xargs -I {} \$EDITOR {}

In **Zellij**, the filepicker is an alias for the built-in filesystem navigator plugin, **Strider**. Reworked significantly starting with version 0.40.0, it allows you to quickly browse files, fuzzy-find, and jump right into editing.

Depending on how you want to use it, here is how to launch and pipe data through it:

### 1. Launching the Filepicker Directly

You can open the filepicker inside a new floating or tiled pane directly from your terminal:

- **As a floating pane:**

```bash
zellij run -f -- plugin filepicker

```

- **As a tiled pane:**

```bash
zellij run -- plugin filepicker

```

### 2. Using the Filepicker with CLI Pipes (`zpipe`)

Zellij supports terminal pipes, which means you can pass the path chosen in the filepicker directly to another CLI utility or text editor.

For example, to pick a file and immediately copy it:

```bash
zpipe filepicker | xargs -I {} cp {} ./destination-folder/

```

Or to open the selected file in your default `$EDITOR`:

```bash
zpipe filepicker | xargs -I {} $EDITOR {}

```

### 3. Custom Keybindings

If you want to pull up the filepicker with a quick keyboard shortcut, you can add a binding to your Zellij configuration file (`config.kdl`).

Add this under the `shared_except "locked"` block to launch it in a floating pane with `Alt` + `f`:

```kdl
keybinds {
    shared_except "locked" {
        bind "Alt f" {
            LaunchOrFocusPlugin "filepicker" {
                floating true
                move_to_focused_pane true
            }
        }
    }
}

```

### 4. Overriding the Default Filepicker

Because `filepicker` is an **alias** in Zellij,
you aren't locked into using Strider.
If you prefer a full-featured terminal file manager like `yazi` or `ranger`,
you can redefine the alias in your `config.kdl`:

```kdl
plugins {
    filepicker url="file:/path/to/your/custom/picker_plugin.wasm"
}

```

## References

- [Zellij @ GitHub](https://github.com/zellij-org/zellij)

- [Zellij Tutorials - screencasts](https://zellij.dev/screencasts/)
