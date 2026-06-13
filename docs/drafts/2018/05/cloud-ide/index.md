---
title: Cloud IDE
created: '2018-05-20T09:49:30-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: cloud-ide
license: CC-BY-4.0
tags:
  - software
  - cloud
  - IDE
  - cloud9
  - Codenvy
  - Eclipse Che
  - Koding
  - Codeanywhere
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [GitHub Codespaces](https://github.com/features/codespaces)

## Google Firebase Studio (Will Sunset in 2027)

See
[Tips on Google Firebase Studio](tips-on-google-firebase-studio)
.

## [Code Server](https://github.com/cdr/code-server)

## [Makepad](https://github.com/makepad/makepad)

## [GitPod](https://gitpod.io/)

GitPod (based on [theia](http://www.theia-ide.org/))
is a web IDE for repositories on GitHub.

## [CodeSandbox](https://codesandbox.io/)

CodeSandbox is a web IDE specifically for web application development.

## [StackBlitz](https://stackblitz.com/)

StackBlitz provides web IDE for web application development.
It is more than a cloud IDE
but allows users to deploy web apps as well.

## [theia](http://www.theia-ide.org/)

https://github.com/theia-ide/theia

1. Syntax highlighting and checking works well.

1. Debugging is not supported currently but under active development.

1. best to mount a directory that has mode 777

1. support installling VS Code extensions (\*.vsix) by drag and drop.
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

1. vi keybindings is stupid

1. Scala support is not ready

Conclusion: basically unusable, not recommended

## [Cloud9](tips-on-cloud9)

1. Looks much better Codenvy/Eclipse Che.

1. Python autocompletion works in the official online version.
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
