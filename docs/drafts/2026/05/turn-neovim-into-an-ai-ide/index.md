---
title: Turn Neovim into An AI IDE
created: '2026-05-01T21:18:26.870750-07:00'
date: '2026-06-11T19:59:13-07:00'
authors:
  - bendu
label: turn-neovim-into-an-ai-ide
license: CC-BY-4.0
tags:
  - editor
  - IDE
  - Neovim
  - avante
  - AI
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[avante.nvim](https://github.com/yetone/avante.nvim)
is a Neovim plugin designed to emulate the behaviour of the Cursor AI IDE.
It provides users with AI-driven code suggestions
and the ability to apply these recommendations directly to their source files with minimal effort.

## Installation and Configuration via AstroNvim

1. Enable avante.nvim in
   [lua/community.lua](https://github.com/legendu-net/AstroNvim_template/blob/main/lua/community.lua#L10)
   .

## Configure

1. Customize configuration (e.g., LLM provider) in
   [lua/plugins/avante.lua](https://github.com/legendu-net/AstroNvim_template/blob/main/lua/plugins/avante.lua)
   if needed.

### Configure API Keys

There are multiple ways to provide LLM API keys to Avante.
We will take Gemini as examples in discussions below.

1. Do not configure any API key and let Avante ask for it when first used.

1. Exporting environment variables.
   Taking Gemini as an example,
   exporting `AVANTE_GEMINI_API_KEY` works.
   To achieve in the fish shell, use the following command

```fish
set -Ux AVANTE_GEMINI_API_KEY "your_api_key_here"
```

3. Configure `api_key_name` for each provide.
   `api_key_name` takes flexible values.
   It can one of the following.

- An (customized) environment variable containing an API key.
- A string specifying a shell command to run to extract the API key.

```
gemini = {
    api_key_name = "cmd:gopass show -o google/gemini-api",
}
```

- A table of string specifying a shell command to run to extract the API key.

```
gemini = {
    api_key_name = {"gopass", "show", "-o", "google/gemini-api"},
}
```

I personally suggest taking approach 2 (exporting environment variables).

- Approach 1 makes it inconvenient to use Avante.
- Approach 3 might encounter various issues.
  - Command-line password managers might ask for password. And depending on your terminal environment, this might fail to work with Avante.
  - Depnding on your terminal environment, the encryption (GPT or age) agent might fail to work making your password manager ask you for password every time.
  - You might work across multiple machines with the same AstroNvim configuration but some environment doesn't have the password manager installed.
- Approach 2 itself (exporting environment variables) isn't secure due to increase attach through AI agents/skills.
  However, this can be mitigated by using a command-line password mananger and setting environment variables for Neovim only.
  That is,
  you can run `AVANTE_GEMINI_API_KEY=(gopass show -o gemini/token) nvim` to start Neovim with Gemini API key exported to Neovim only.

## Usage

1. If you run into errors saying "cannot make changes. modifiable is off" when using the sidebar,
   run `:set modifiable` to toggle on modifiable.

```{list-table}
---
header-rows: 1
---
* - Mode
  - Key bindings
  - Description
* - Visual
  - <leader>Ae
  - Edit the selected block
* - Normal
  - <leader>+A+enter
  - Chat with Avante
* - Normal
  - <leader>+A+n
  - New chat
```

## Thoughts on Avante

1. early stage and there are still lots of issues
1. slow response
1. Neovim (without Avante) + Claude/Antigravity CLI is an alternative way

## References

- [Avante.nvim Leader Key Configuration](https://gemini.google.com/share/75f7c0526efc)

- [Fix avante.nvim Build Error](https://gemini.google.com/share/7016ae809f58)
