---
title: Visual Studio Code Server
created: '2019-10-24T11:28:44-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: visual-studio-code-server
license: CC-BY-4.0
tags:
  - software
  - Visual Studio Code
  - server
  - VS Code
  - IDE
  - web
  - VSCode
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Advanced Tips

1. The option `--link`\
   allows you to securely bind code-server via Coder Cloud with the passed name.
   You'll get a URL like https://myname.coder-cloud.com
   at which you can easily access your code-server instance.
   Authorization is done via GitHub.

1. [Hashed Password](https://github.com/cdr/code-server/blob/v3.8.0/doc/FAQ.md#can-i-store-my-password-hashed)

1. [dclong/docker-vscode-server](https://github.com/dclong/docker-vscode-server)

## Format Source Code

Format manually: Shift + Alt + F (Windows/Linux) or Shift + Option + F (macOS)
Please refer to
[Visual Studio Code - Formatting](https://code.visualstudio.com/docs/editor/codebasics#_formatting)
and
[How do you format code on save in VS Code](https://stackoverflow.com/questions/39494277/how-do-you-format-code-on-save-in-vs-code)
for more discussions.

## Auto Activate Python Virtual Environment

[Auto activate virtual environment in Visual Studio Code](https://stackoverflow.com/questions/58433333/auto-activate-virtual-environment-in-visual-studio-code)

## Setup Password

https://github.com/cdr/code-server/issues/940

## Settings

https://github.com/cdr/code-server/issues/965

https://github.com/cdr/code-server/issues/148

## Extensions

Please refer to
[Useful Visual Studio Code Extensions](useful-visual-studio-code-extensions)
.

[How `--user-data-dir` and `--extensions-dir` Work Together in code-server](https://instagit.com/coder/code-server/whats-the-relationship-between-user-data-dir-and-extensions-dir-configuration/?utm_source=chatgpt.com)

## [Debug Python Project](debug-python-project-in-visual-studio-code)

## Shortcuts

https://github.com/cdr/code-server/issues/112

https://github.com/cdr/code-server/issues/924

## Useful Tools

https://github.com/cdr/sshcode

## Snippets

[Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## References

- [How `--user-data-dir` and `--extensions-dir` Work Together in code-server](https://instagit.com/coder/code-server/whats-the-relationship-between-user-data-dir-and-extensions-dir-configuration/?utm_source=chatgpt.com)

- [Visual Studio Code Server Documentation](https://github.com/cdr/code-server/tree/master/doc)

- [Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

- [VSCode Shortcuts](tips-on-visual-studio-code-shortcuts)

- [VSCode Server Guidance](https://github.com/cdr/code-server/blob/master/doc/guide.md)

- [How to run VS Code on the server!](https://dev.to/babak/how-to-run-vs-code-on-the-server-3c7h)

- [Securing Visual Studio Code Server](https://www.pomerium.io/recipes/vs-code-server.html#background)
