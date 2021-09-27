Status: published
Date: 2018-09-08 18:57:48
Author: Ben Chuanlong Du
Slug: socks-proxy-to-http-proxy
Title: Convert a Socks Proxy to a HTTP Proxy
Category: Internet
Tags: network, socks proxy, http proxy, polipo
Modified: 2021-09-26 21:54:00

There are multiple tools available 
to convert a Socks proxy to a HTTP/HTTPS proxy. 
The work by convertting HTTP requests into socks requests 
and send them to the socks proxy. 
Be aware that this might not be necessary 
as many tools accepting HTTP/HTTPS proxies 
also accept socks proxies. 
In that case,
you can direct your socks proxy
(e.g., `socks5://localhost:1080`)
to those tools.
If you do need to convert a socks proxy to a HTTP/HTTPS proxy
for tools that accept HTTP/HTTPS proxies only,
read the below.

## Polipo

1. Install Polipo.

        :::bash
        wajig search polipo

2. Create a HTTP proxy listening on 8123
    (assuming you have a Socks proxy `localhost:1080`). 

        :::bash
        polipo socksParentProxy=localhost:1080

## [http-proxy-to-socks](https://www.npmjs.com/package/http-proxy-to-socks)

1. Install http-proxy-to-socks.

        :::bash
        npm install -g http-proxy-to-socks

2.  Create a HTTP proxy listening on 8080
    (assuming you have a Socks proxy `localhost:1080`).
    Please make sure your socks service is available at the corresponding port.

        :::bash
        hpts -s 127.0.0.1:1080 -p 8080

## References

https://www.codevoila.com/post/16/convert-socks-proxy-to-http-proxy-using-polipo
