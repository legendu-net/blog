UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2017-04-03 17:37:33
Author: Ben Chuanlong Du
Slug: configure-debian-sources
Title: Configure Debian Sources
Category: Linux
Tags: operating system, OS, Linux, Debian, sources, apt-get

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

[Debian Sources List Generator](http://debgen.simplylinux.ch/)

Personally, I prefer stable with backports.
Testing is also good but still update might introduce critial bugs sometimes.
It is not easy to maitainly a stable and update to date balance.
You can certainly use multi-sources,
i.e., use stable, testing, sid and experimental at the same time.
multi-source is much harder to maintain especially when you want to support multi-archi
It is not recommended.



```bash
deb http://ftp.us.debian.org/debian stable main contrib non-free
deb-src http://ftp.us.debian.org/debian stable main contrib non-free

deb http://ftp.debian.org/debian/ wheezy-updates main contrib non-free
deb-src http://ftp.debian.org/debian/ wheezy-updates main contrib non-free

deb http://security.debian.org/ wheezy/updates main contrib non-free
deb-src http://security.debian.org/ wheezy/updates main contrib non-free
```


```bash
# stable
deb http://ftp.us.debian.org/debian/ stable main contrib non-free
deb-src http://ftp.us.debian.org/debian/ stable main contrib non-free

# stable Security
deb http://security.debian.org/ stable/updates main contrib non-free
deb-src http://security.debian.org/ stable/updates main contrib non-free

# stable-updates, previously known as 'volatile'
deb http://ftp.us.debian.org/debian/ stable-updates main contrib non-free
deb-src http://ftp.us.debian.org/debian/ stable-updates main contrib non-free

# stable-backports
deb http://ftp.us.debian.org/debian/ stable-backports main contrib non-free
deb-src http://ftp.us.debian.org/debian/ stable-backports main contrib non-free

# testing
deb http://ftp.us.debian.org/debian/ testing main contrib non-free
deb-src http://ftp.us.debian.org/debian/ testing main contrib non-free

# testing Security
deb http://security.debian.org/ testing/updates main contrib non-free
deb-src http://security.debian.org/ testing/updates main contrib non-free

# sid
deb http://ftp.us.debian.org/debian/ sid main contrib non-free
deb-src http://ftp.us.debian.org/debian/ sid main contrib non-free

# experimental
deb http://ftp.us.debian.org/debian/ experimental main contrib non-free
deb-src http://ftp.us.debian.org/debian/ experimental main contrib non-free
```
