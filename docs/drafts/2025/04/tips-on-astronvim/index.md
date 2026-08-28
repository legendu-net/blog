---
title: Tips on AstroNvim
created: '2025-04-28T10:55:17-07:00'
date: '2026-08-27T19:07:27-07:00'
authors:
  - bendu
label: tips-on-astronvim
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - IDE
  - Vim
  - AstroNvim
  - Neovim
  - LSP
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## LSP

Use the command `:LspInstall` to open the prompt
to select a LSP to install for the current file type.

## Snippets

https://github.com/L3MON4D3/LuaSnip

https://github.com/rafamadriz/friendly-snippets

```{tip}
Use AI tools to quickly generate code snippets.
```

You can show all available snippets for the current document type using the command `:LuaSnipListAvailable`
.
However,
the most popular and "Astro-like" way to search snippets is via Telescope (telescope-luasnip.nvim).
Please refer to
[telescope-luasnip.lua](https://github.com/legendu-net/AstroNvim_template/blob/main/lua/plugins/telescope-luasnip.lua)
on enable and configure telescope-luasnip.
The configuration set the keybinding `<leader>fS` for finding snippets.

- [Global](https://github.com/rafamadriz/friendly-snippets/blob/main/snippets/global.json)

- [Markdown](https://github.com/rafamadriz/friendly-snippets/blob/main/snippets/markdown.json)

- [Python](https://github.com/rafamadriz/friendly-snippets/tree/main/snippets/python)

- [Rust](https://github.com/rafamadriz/friendly-snippets/tree/main/snippets/rust)

- [Go](https://github.com/rafamadriz/friendly-snippets/blob/main/snippets/go.json)

- [Docker](https://github.com/rafamadriz/friendly-snippets/tree/main/snippets/docker)

- [SQL](https://github.com/rafamadriz/friendly-snippets/blob/main/snippets/sql.json)

- [Java](https://github.com/rafamadriz/friendly-snippets/tree/main/snippets/java)

- [JavaScript](https://github.com/rafamadriz/friendly-snippets/tree/main/snippets/javascript)

- [Git Commit](https://github.com/rafamadriz/friendly-snippets/blob/main/snippets/gitcommit.json)

## Changing Keyword Cases

[gregorias/coerce.nvim](https://github.com/gregorias/coerce.nvim)
is the best Neovim plugin for changing keyword cases.
See
[lua/plugins/coerce.lua] (https://github.com/legendu-net/AstroNvim_template/blob/main/lua/plugins/coerce.lua)
for an example of enabling and configuring coere.nvim.
By default,
coerce.nvim uses keybindings `cr` and `gcr` (visual mode) to toggle on options for changing cases.

## Custom Lua Script

- markdown_link_title.lua: trigger by `,at`.
- commit_msg.lua: trigger by Git/JJ.

## References

- [🚀 Getting Started](https://docs.astronvim.com/)

- [VS Code Integration](https://docs.astronvim.com/recipes/vscode/)

- [lazy.nvim - 🚀 Getting Started](https://lazy.folke.io/)
