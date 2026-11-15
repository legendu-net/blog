---
title: Java PPA for Ubuntu
created: '2017-04-22T15:00:33-07:00'
date: '2026-11-15T09:23:29-08:00'
authors:
  - bendu
label: java-ppa-for-ubuntu
license: CC-BY-4.0
tags:
  - programming
  - Java
  - Ubuntu
  - PPA
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```bash
sudo add-apt-repository ppa:webupd8team/java
```

If you are behind a firewall and has to communicate to the internal via a proxy,
you can first export the environment variables `http_proxy` and `https_proxy`.

```bash
export http_proxy='proxy_server:port'
export https_proxy='proxy_server:port'
```

If a user name and password is needed,
export them using the following command.

```bash
export http_proxy=http://username:password@proxy_server:port
export https_proxy=https://username:password@proxy_server:port
```

However, make sure to run `sudo` with the `-E` (preserve environment) option.

```bash
sudo -E add-apt-repository ppa:webupd8team/java
```
