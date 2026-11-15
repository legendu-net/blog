---
title: Tips on Kerberos
created: '2019-06-05T13:11:06-07:00'
date: '2026-11-15T12:20:35-08:00'
authors:
  - bendu
label: tips-on-kerberos
license: CC-BY-4.0
tags:
  - OS
  - Linux
  - CentOS
  - Ubuntu
  - kerberos
  - authentication
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

### Ubuntu

apt-get install krb5-user

### CentOS

yum install -y ntp
yum install krb5-workstation krb5-libs krb5-auth-dialog

## Issues

### kinit: Permission denied while initializing Kerberos 5 library

It is likely due to the fact that /etc/krb5.conf is not readable.
Run the following command can help fix the issue.

```
:::bash
sudo chmod +r /etc/krb5.conf
```

## References

https://gist.github.com/ashrithr/4767927948eca70845db
