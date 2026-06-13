---
title: Use wget with Proxy
created: '2014-07-06T14:31:55-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: use-wget-with-proxy
license: CC-BY-4.0
tags:
  - software
  - download
  - wget
  - proxy
---

1. If you don't already know the proxy in use (in your company),
   read the post [Find out Proxy in Use](find-out-proxy-in-use)
   to figure it out.

1. Put the following lines into your wget configuration file,
   which is usually `~/.wget`.

   ```
    use_proxy = on
    http_proxy = http://username:password@proxy_ip:port
    https_proxy = http://username:password@proxy_ip:port
    ftp_proxy = http://username:password@proxy_ip:port
   ```

1. Use wget to download files.
   A illustration is given below.

   ```
    wget --no-check-certificate --load-cookies=/home/mobaxterm/ff_cookies.txt -p https://bitbucket.org/dclong/config/get/master.zip
   ```

   You have to use the `--no-check-certificate` option
   if you encounter "certificate verification" errors.
   Another way to do this is to set environment variables `http_proxy`, `https_proxy` and `ftp_proxy` etc.
