UUID: 3df72304-6f5c-44b8-aebd-db65163d617e
Status: published
Date: 2017-08-26 21:23:56
Author: Ben Chuanlong Du
Slug: macports-tips
Title: Macports Tips
Category: Mac OSX
Tags: Mac OSX, MacPorts, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

sudo port selfupdate

port search pkg

sudo port install pkg

MacPorts behind Firewall

1. use http instead of rsync 

Open the file `/opt/local/etc/macports/sources.conf`
and replace the line 

        rsync://rsync.macports.org/release/tarballs/ports.tar [default]

with

        http://www.macports.org/files/ports.tar.gz [default]

2. use a proxy

## Proxy for MacPorts

https://destefano.wordpress.com/2011/03/18/macports-behind-a-proxy/

https://samkhan13.wordpress.com/2012/06/15/make-macports-work-behind-proxy/

export http_proxy=http://username:password@proxyURL:portNumber
export HTTP_PROXY=http://username:password@proxyURL:portNumberexport 
export ftp_proxy=ftp://username:password@proxyURL:portNumber
export FTP_PROXY=ftp://username:password@proxyURL:portNumber
export rsync_proxy=username:password@proxyURL:portNumber
export RSYNC_PROXY=username:password@proxyURL:portNumber

Use `sudo port -d sync` instead of `sudo port selfupdate` to print debugging information while updating.
