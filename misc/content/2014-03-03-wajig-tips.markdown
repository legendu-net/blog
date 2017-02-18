UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-07-05 20:27:39
Slug: wajig-tips
Title: Wajig Tips
Category: Software
Tags: software, wajig, Linux, package management, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
<http://www.togaware.com/linux/survivor/Wajig_Overview.html>


20. Let wajig also search description 
```bash
wajig search -v youtube
```
19. Remove all GNOME desktop related packages
```bash
wajig list | awk '{print $2}' | grep -i ^gnome | xargs wajig purge
```
7. install a package of specific version using wajig 
```bash
wajig search libssl/testing
```
13. check which repository a package comes from
```bash
wajig policy geary
```
6. To install backport packages, use 
```bash
wajig install libreoffice/wheezy-backports 
wajig -t install/wheezy-backports libreoffice
apt-get -t wheezy-backports libreoffice
```
It doesn't work if you use 
```bash
wajig install libreoffice/stable-backports 
```

## Issues
1. it seems to me that `wajig purge package_name` fails to remove packages sometimes
even though it seems to succeed. 
