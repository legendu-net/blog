Status: published
Date: 2019-02-10 13:30:54
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

## Change Indention/Shift Width

https://stackoverflow.com/questions/34174207/how-to-change-indentation-in-visual-studio-code/45671704

## Launching VS Code from Command Line on Mac

https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line

## Tricks & Traps

1. It seems that Visual Studio Code installed using snap in Kubuntu 18.10 has issues.
    It is suggested that you install Visual Studio Code using the `.deb` package instead of snap.