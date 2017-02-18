UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Use "wget" Behind Proxy
Author: Chuanlong (Ben) Du
Date: 2016-07-13 00:09:56
Slug: use-wget-behind-proxy
Category: Software
Tags: software, download, wget, proxy


0. If you don't already know the proxy in use (in your company),
read the post [Find out Proxy in Use](http://www.legendu.net/en/blog/find-out-proxy-in-use/)
to figure it out.

1. Put the following lines into your wget configuration file,
which is usually `~/.wget`.

        use_proxy = on
        http_proxy = http://username:password@proxy_ip:port
        https_proxy = http://username:password@proxy_ip:port
        ftp_proxy = http://username:password@proxy_ip:port

2. Use wget to download files.
A illustration is given below.
        wget --no-check-certificate --load-cookies=/home/mobaxterm/ff_cookies.txt -p https://bitbucket.org/dclong/config/get/master.zip
You have to use the `--no-check-certificate` option 
when you encounter "certificate verification" errors.

Another way to do this is to set environment variables `http_proxy`, `https_proxy` and `ftp_proxy` etc.


Note that working in a Linux virtual machine on your office laptop with Windows OS
can possibly help you circumvent the proxy issue.
