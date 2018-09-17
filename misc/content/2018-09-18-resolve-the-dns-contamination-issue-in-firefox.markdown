UUID: 038d74d6-ae3a-4d15-a718-b72275cb56d0
Status: published
Date: 2018-09-18 00:05:42
Author: Ben Chuanlong Du
Slug: resolve-the-dns-contamination-issue-in-firefox
Title: Resolve the Dns Contamination Issue in Firefox
Category: Software
Tags: software, Firefox, proxy, DNS contamination, socks

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

The local DNS you use in China is probably contaminated
and popular sites like Google, Facebook, etc. are not interpreted correctly.
So if you are in China and use Firefox with Proxy,
make sure to set `network.proxy.socks_remote_dns` to be true (follow the steps below).

1. Open an empty tab in Firefox.

2. Go to about:config in the URL bar.

3. Search for `network.proxy.socks_remote_dns`.

4. Change the value to be `true`.
