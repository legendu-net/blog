UUID: a474d8dc-ad7c-49fd-a89a-0d5b22360e14
Status: published
Date: 2017-04-03 17:50:27
Author: Ben Chuanlong Du
Slug: sudo-proxy
Title: Proxy for `sudo`
Category: Network
Tags: Network, proxy, Linux, sudo

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

You can setup proxy in a terminal by export environment variables `http_proxy` and `https_proxy'. 
```bash
export http_proxy='proxy_server:port'
export https_proxy='proxy_server:port'
```
However, you might find the exported environment variables are not visible to `sudo`. 
This can be resovled by simplying adding the `-E` (preserve environment) option to `sudo`.
```bash
sudo -E command_to_run
```
