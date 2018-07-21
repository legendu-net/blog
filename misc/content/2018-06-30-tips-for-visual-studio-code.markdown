UUID: 10a28b01-2201-4964-9fbb-a7798c7db52a
Status: published
Date: 2018-06-30 16:03:46
Author: Ben Chuanlong Du
Slug: tips-for-visual-studio-code
Title: Tips for Visual Studio Code
Category: Software
Tags: software, Visual Studio Code, vscode, IDE

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Fix the Caps Lock Mapping to Escape Issue

https://github.com/Microsoft/vscode/wiki/Keybinding-Issues

A simple fix is to add the following configuration into the user's setting.json file.

```
{
    "keyboard.dispatch": "keyCode"
}
```


## Launching VS Code from Command Line on Mac 

https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line