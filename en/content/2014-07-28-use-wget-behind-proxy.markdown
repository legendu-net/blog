Status: published
Title: Use wget with Proxy
Author: Chuanlong (Ben) Du
Date: 2019-03-07 23:42:48
Slug: use-wget-behind-proxy
Category: Software
Tags: software, download, wget, proxy


1. If you don't already know the proxy in use (in your company),
    read the post [Find out Proxy in Use](http://www.legendu.net/en/blog/find-out-proxy-in-use/)
    to figure it out.

2. Put the following lines into your wget configuration file,
    which is usually `~/.wget`.

        use_proxy = on
        http_proxy = http://username:password@proxy_ip:port
        https_proxy = http://username:password@proxy_ip:port
        ftp_proxy = http://username:password@proxy_ip:port

3. Use wget to download files.
    A illustration is given below.

        wget --no-check-certificate --load-cookies=/home/mobaxterm/ff_cookies.txt -p https://bitbucket.org/dclong/config/get/master.zip

    You have to use the `--no-check-certificate` option
    if you encounter "certificate verification" errors.
    Another way to do this is to set environment variables `http_proxy`, `https_proxy` and `ftp_proxy` etc.

## Question

A HTTP proxy can be used as HTTPS/FTP proxy for wget,
but can a socks proxy be used as HTTP/HTTPS/FTP proxy for wget?