---
title: Install sbt on CentOS
created: '2017-06-25T10:37:51-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: install-sbt-on-centos
license: CC-BY-4.0
tags:
  - Linux
  - CentOS
  - RedHat
  - sbt
  - install
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```sh
wget http://dl.bintray.com/sbt/rpm/sbt-0.13.5.rpm
sudo yum install sbt-0.13.5.rpm
```

```sh
curl https://bintray.com/sbt/rpm/rpm | sudo tee /etc/yum.repos.d/bintray-sbt-rpm.repo
sudo yum install sbt
```
