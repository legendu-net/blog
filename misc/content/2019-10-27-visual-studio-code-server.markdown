Status: published
Date: 2019-10-27 23:18:28
Author: Benjamin Du
Slug: visual-studio-code-server
Title: Visual Studio Code Server
Category: Software
Tags: Software, Visual Studio Code, server, VS Code, IDE, web, vscode

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


docker run --user root -it -p 8080:8080 -v $HOME:/home/coder/project codercom/code-server:v2  --allow-https --auth password


## Docker Images

https://github.com/jefferyb/code-server-openshift/blob/master/Dockerfile

https://github.com/monostream/code-server/blob/develop/Dockerfile

https://github.com/linuxserver/docker-code-server/blob/master/Dockerfile


https://github.com/keatontaylor/code-server-python-go

## References

https://dev.to/babak/how-to-run-vs-code-on-the-server-3c7h

[Securing Visual Studio Code Server](https://www.pomerium.io/recipes/vs-code-server.html#background)
