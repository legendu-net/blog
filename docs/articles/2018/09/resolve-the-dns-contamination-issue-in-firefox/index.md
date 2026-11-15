---
title: Resolve the DNS Contamination Issue in Firefox
created: '2018-09-11T01:11:28-07:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: resolve-the-dns-contamination-issue-in-firefox
license: CC-BY-4.0
tags:
  - software
  - Firefox
  - proxy
  - DNS contamination
  - socks
---

The local DNS you use in China is probably contaminated
and popular sites like Google, Facebook, etc. are not interpreted correctly.
So if you are in China and use Firefox with Proxy,
make sure to set `network.proxy.socks_remote_dns` to be true (follow steps below).

1. Open an empty tab in Firefox.

1. Go to about:config in the URL bar.

1. Search for `network.proxy.socks_remote_dns`.

1. Change the value to be `true`.
