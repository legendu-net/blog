UUID: 238e6a1a-0b18-457c-98ad-1a7fbdc0c6d5
Status: published
Date: 2017-03-05 21:30:21
Author: Ben Chuanlong Du
Slug: eclipse-che-tips
Title: Eclipse Che Tips
Category: Software
Tags: software, cloud IDE, Eclipse Che, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

You can launch an Eclipse Che server using the command below.
```
docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v /wwwroot/che:/data eclipse/che start
```
The launched Eclipse Che server can be visited at `server:8080`,
where `server` is the ip/address of your server.
Please refer to the [Quick Start](https://www.eclipse.org/che/docs/quick-start.html#docker) for more details.

## Git/GitHub & SSH Keys

I encountered issues import a project from enterprise version of GitHub.
An alternative way was to manually clone the project in terminal.
Of course,
the SSH public key has to be configured in GitHub.
Here is a [related ticket](https://github.com/eclipse/che/issues/1938) on GitHub.

## [Language Servers](https://microsoft.github.io/language-server-protocol/implementors/servers/)

## Shortcuts

Ctrl + Insert: Copy

Shift + Insert: Paste
