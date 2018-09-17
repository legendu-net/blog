UUID: bac41a69-cf6d-43d2-b4a4-f1c97784b37d
Status: published
Date: 2018-09-18 00:13:28
Author: Ben Chuanlong Du
Slug: socks-proxy-to-http-proxy
Title: Socks Proxy to HTTP Proxy
Category: Network
Tags: network, socks proxy, http proxy, polipo

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Convert Socks Proxy to HTTP Proxy

```
# install polipo
wajig search polipo

# create a http proxy at 8123 using the socks proxy
polipo socksParentProxy=localhost:1080
```

## HTTP Proxy to Socks Proxy

https://www.npmjs.com/package/http-proxy-to-socks


## References

https://www.codevoila.com/post/16/convert-socks-proxy-to-http-proxy-using-polipo
