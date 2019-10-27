Status: published
Date: 2019-10-27 22:54:36
Author: Benjamin Du
Slug: visual-studio-code-server
Title: Visual Studio Code Server
Category: Software
Tags: Software, Visual Studio Code server, VS Code server, IDE, web IDE, vscode server

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


docker run --user root -it -p 8080:8080 -v $HOME:/home/coder/project codercom/code-server:v2  --allow-https --auth password

## References

https://dev.to/babak/how-to-run-vs-code-on-the-server-3c7h

[Securing Visual Studio Code Server](https://www.pomerium.io/recipes/vs-code-server.html#background)
