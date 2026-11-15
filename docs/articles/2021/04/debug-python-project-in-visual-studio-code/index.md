---
title: Debug Python Project in Visual Studio Code
created: '2021-04-23T10:26:29-07:00'
date: '2026-11-15T12:16:23-08:00'
authors:
  - bendu
label: debug-python-project-in-visual-studio-code
license: CC-BY-4.0
tags:
  - computer science
---

## Ways to Open a Command Palette

1. Use Menu `Menu -> View -> Command Palette...`.
1. Use the shortcut `Shift + Command + P` (on macOS).

![Command Palette](https://user-images.githubusercontent.com/824507/108890375-5b40a300-75c2-11eb-801e-481063921e17.png)

You can search for commands in the Command Palette,
which makes things very convenient.

## Run Tests or a Python File

1. Open the Command Palette.
1. Search for `Python: Run` in the Command Palette.
1. Select the right command to run for your case.

![Python: Run](https://user-images.githubusercontent.com/824507/108890540-917e2280-75c2-11eb-99a6-b0294ee29056.png)

## Debug Tests or a Python File

1. Open the Command Palette.
1. Search for `Python: Debug` in the Command Palette.
1. Select the right command to run for your case.

![Python: Debug](https://user-images.githubusercontent.com/824507/108890085-fb49fc80-75c1-11eb-8121-a52743e07960.png)

## Example of Debugging Configuration

`launch.json` for debugging Python code.

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```
