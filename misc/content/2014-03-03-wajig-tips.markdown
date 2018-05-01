UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2017-04-17 09:25:41
Slug: wajig-tips
Title: Wajig Tips
Category: Software
Tags: software, wajig, Linux, package management, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

[Wajig on Debian Wiki](https://wiki.debian.org/Wajig)


1. You can type enter the CLI of `wajig` by typing `wajig` in terminal,
so that you can use commands of `wajig` directly
instead of typing `wajig` every time.

        $ wajig
        wajig>

2. Let wajig also search description

        wajig search -v youtube

3. Download a package for install later.
    This is very helpful if the package is big.

        wajig download pkg_name

1. Remove all GNOME desktop related packages

        wajig list | awk '{print $2}' | grep -i ^gnome | xargs wajig purge

2. install a package of specific version using wajig

        wajig search libssl/testing

3. check which repository a package comes from

        wajig policy geary

6. To install backport packages, use

        wajig install libreoffice/wheezy-backports
        wajig -t install/wheezy-backports libreoffice
        apt-get -t wheezy-backports libreoffice

    It does not work if you use

        wajig install libreoffice/stable-backports

## Download Packages (for Installation Later)
If your network speed is a concern,
you can download a package for installation later using the command below. 
```
wajig download pkg_name  
```

## Issues

1. it seems to me that `wajig purge package_name` fails to remove packages sometimes
even though it seems to succeed.
