Status: published
Date: 2018-05-20 09:49:30
Author: Ben Chuanlong Du
Slug: cloud-ide
Title: Cloud IDE
Category: Software
Tags: software, cloud IDE, Cloud9, Codenvy, Eclipse Che, Koding, Codeanywhere
Modified: 2020-05-20 09:49:30

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## [VS Code Server](https://github.com/cdr/code-server)

## [GitPod](https://gitpod.io/)

GitPod (based on [theia](http://www.theia-ide.org/))
is a web IDE for repositories on GitHub.

## [CodeSandbox](https://codesandbox.io/)

CodeSandbox is a web IDE specifically for web application development.

## [StackBlitz](https://stackblitz.com/)

StackBlitz provides web IDE for web application development.
It is more than a cloud IDE
but allows users to deploy web apps as well.

## [Visual Studio Code](https://code.visualstudio.com/) with the Plugin [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

## [theia](http://www.theia-ide.org/)

https://github.com/theia-ide/theia

1. Syntax highlighting and checking works well.

2. Debugging is not supported currently but under active development.

3. best to mount a directory that has mode 777

4. support installling VS Code extensions (*.vsix) by drag and drop.
    Installing from VS Code Marketplace is not supported at this time.

[Enable username/password for Theia](https://github.com/theia-ide/theia-apps/issues/167)

### Docker for theia
```
docker pull theiaide/theia-full
```

```
docker run -d -p 3000:3000 -v /workdir:/home/project:cached theiaide/theia-full
```

## [ShareLatex ](https://www.sharelatex.com/)


## [Codenvy](https://codenvy.io/) / [Eclipse Che](https://www.eclipse.org/che/)

1. very slow

2. vi keybindings is stupid

3. Scala support is not ready

Conclusion: basically unusable, not recommended

## [Cloud9](http://www.legendu.net/misc/blog/cloud9-tips/)

1. Looks much better Codenvy/Eclipse Che.

2. Python autocompletion works in the official online version. 
    However, debugging is supported only for Python2 currently.


## [Koding](https://www.koding.com/)

## [Codeanywhere](https://www.codeanywhere.com/)

## [Codiad](http://codiad.com/)

https://github.com/Codiad/Codiad

http://market.codiad.com/

https://hub.docker.com/r/bitnami/codiad/

https://github.com/linuxserver/docker-codiad

https://hub.docker.com/r/wernight/codiad/

https://github.com/QuantumObject/docker-codiad

## [wdb](https://github.com/Kozea/wdb)

An improbable web debugger through WebSockets for Python.

## [CodiMD](https://hackmd-ce.herokuapp.com/)

## References

https://matttrent.com/remote-development/
