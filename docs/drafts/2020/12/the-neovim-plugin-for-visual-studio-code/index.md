---
title: The Neovim Plugin for Visual Studio Code
created: '2020-12-10T23:23:59-08:00'
date: '2026-08-11T22:19:25-07:00'
authors:
  - bendu
label: the-neovim-plugin-for-visual-studio-code
license: CC-BY-4.0
tags:
  - computer science
  - software
  - Neovim
  - IDE
  - Visual Studio Code
  - VSCode
  - plugin
  - extension
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://github.com/asvetliakov/vscode-neovim

## Installation

1. Install NeoVim 0.5+ using [icon](https://github.com/legendu-net/icon).

   ```bash
   icon nvim -ic --ppa
   ```

1. Install the NeoVim plugin from the extension market in VSCode or Code Server.

1. Set the path of NeoVim via the extension settings.
   You can also do this by editing the settings file directly.

   ```json
    {
        "terminal.integrated.commandsToSkipShell": [
            "-workbench.action.quickOpen"
        ],
        "editor.fontSize": 12,
        "editor.detectIndentation": false,
        "editor.suggestSelection": "first",
        "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
        "autoDocstring.docstringFormat": "sphinx",
        "keyboard.dispatch": "keyCode",
        "workbench.startupEditor": "newUntitledFile",
        "python.linting.mypyEnabled": false,
        "python.linting.pylintArgs": [
            "--extension-pkg-whitelist=numpy,cv2,pyspark",
            "--generated-members=cv2.*,pyspark.*",
            "--ignored-modules=pyspark.sql.functions"
        ],
        "extensions.autoUpdate": false,
        "workbench.colorTheme": "Default Dark+",
        "python.formatting.provider": "yapf",
        "vscode-neovim.neovimPath": "/usr/bin/nvim"
    }
   ```

## Tips

1. There are various issues with the plugin current.
   It is suggested that you avoid using this plugin but use the Vim plugin instead.

1. SpaceVim configuration works with this plugin.
   Once you have the VSCode NeoVim plugin installed,
   you can install SpaceVim and you are ready to go.
