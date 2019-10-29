Status: published
Date: 2019-10-29 10:16:41
Author: Benjamin Du
Slug: vscode-tips
Title: Tips for Visual Studio Code
Category: Software
Tags: software, vscode, Visual Studio Code, tips, IDE

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Useful Extensions

[Terminal](https://marketplace.visualstudio.com/items?itemName=formulahendry.terminal)

[Python (by Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

[Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)

[Visual Stuido IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

[Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

## Fix the Caps Lock Mapping to Escape Issue

https://github.com/Microsoft/vscode/wiki/Keybinding-Issues

A simple fix is to add the following configuration into the user's setting.json file.

```
{
    "keyboard.dispatch": "keyCode"
}
```

## Install Extensions from Command-line

https://stackoverflow.com/questions/34286515/how-to-install-visual-studio-code-extensions-from-command-line/34339780#34339780

## Change Indention/Shift Width

https://stackoverflow.com/questions/34174207/how-to-change-indentation-in-visual-studio-code/45671704

## Launching VS Code from Command Line on Mac

https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line

## Tricks & Traps

1. It seems that Visual Studio Code installed using snap in Kubuntu 18.10 has issues.
    It is suggested that you install Visual Studio Code using the `.deb` package instead of snap.


## References

- [Visual Studio Code Blog](https://code.visualstudio.com/blogs/2019/05/02/remote-development)

- [Visual Studio Code Updates](https://code.visualstudio.com/updates/)

- [Download Visual Studio Code Insiders](https://code.visualstudio.com/insiders/)
