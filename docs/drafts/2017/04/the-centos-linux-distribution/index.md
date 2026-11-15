---
title: The CentOS Linux Distribution
created: '2017-04-22T14:59:57-07:00'
date: '2026-11-15T09:23:43-08:00'
authors:
  - bendu
label: the-centos-linux-distribution
license: CC-BY-4.0
tags:
  - Linux
  - CentOS
  - tips
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. The `wheel` group is the `sudo` group.
   So to grant a user the sudo privilege,
   just add it to the `wheel` group.

   ```
    :::bash
    gpasswd -a user_name wheel
   ```

## EPEL

```
:::bash
sudo yum -y install epel
```

## IUS Release

```
:::bash
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
```
