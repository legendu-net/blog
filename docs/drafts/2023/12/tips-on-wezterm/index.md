---
title: Tips on WezTerm
created: '2023-12-13T20:53:16-08:00'
date: '2026-11-15T12:20:40-08:00'
authors:
  - bendu
label: tips-on-wezterm
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - terminal
  - wezterm
  - app
  - application
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The development of WezTerm is not very active right now.
[Ghostyy](https://github.com/ghostty-org/ghostty)
might be a better alternative.

## Installation

Follow
https://wezfurlong.org/wezterm/install/linux.html#__tabbed_1_3
to install Wezterm on Debian/Ubuntu series of Linux distributions.

## Wezterm CLI

https://wezterm.org/cli/general.html

### Split Panels

https://wezterm.org/cli/cli/split-pane.html

```bash
wezterm cli split-pane
```

### Connect to Wezterm Multiplexer

```bash
wezterm connect
```

## Show Image

```bash
wezterm imgcat /path/to/image
```

## Shortcuts

```{list-table}
---
header-rows: 1
---
- - Shortcut
  - Description
- - Fn + F
  - Enter/exit full screen
- - Shift + Ctrl + C
  - Copy
- - Shift + Ctrl + V
  - Paste
```

## Configuration

- [Change WezTerm blurred Window Background & Opacity on Focus](https://romanzipp.com/blog/how-to-toggle-wezterm-blurred-window-background-on-focus)

  -- Pull in the wezterm API
  local wezterm = require("wezterm")

  local config = wezterm.config_builder()
  config.initial_cols = 120
  config.initial_rows = 28
  config.font_size = 11
  config.color_scheme = "Tokyo Night"

  local dimmer = { brightness = 0.1 }
  config.background = {
  -- This is the deepest/back-most layer. It will be rendered first
  {
  source = {
  --File = "/home/USERNAME/Downloads/wallpaper/outer_space.jpg",
  File = "/home/USERNAME/Downloads/wallpaper/robot_castle.jpg",
  },
  -- The texture tiles vertically but not horizontally.
  -- When we repeat it, mirror it so that it appears "more seamless".
  -- An alternative to this is to set `width = "100%"` and have
  -- it stretch across the display
  repeat_x = "Mirror",
  hsb = dimmer,
  -- When the viewport scrolls, move this layer 10% of the number of
  -- pixels moved by the main viewport. This makes it appear to be
  -- further behind the text.
  attachment = { Parallax = 0.1 },
  },
  }
  --config.window_background_opacity = 0.3

  return config

## References

- [wezterm imgcat](https://wezfurlong.org/wezterm/cli/imgcat.html)
