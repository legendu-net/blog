Status: published
Date: 2019-05-20 22:21:39
Author: Ben Chuanlong Du
Slug: linuxbrew-tips
Title: Tips on Homebrew for Linux (Linuxbrew)
Category: Linux
Tags: Linux, Homebrew, Linuxbrew, package management

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

https://blog.eduardovalle.com/2015/10/15/installing-software-without-root/

https://github.com/Linuxbrew/brew

https://github.com/Linuxbrew/install

https://docs.brew.sh/Homebrew-on-Linux

1. Linuxbrew/brew has been merged into Homebrew/brew.
  For more please refer to [this issue](https://github.com/Linuxbrew/brew/issues/1).

```Bash
sh -c "$(curl --proxy http://your.proxy.servder:port -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
```
The installation script installs Homebrew to /home/linuxbrew/.linuxbrew using sudo if possible 
and in your home directory at ~/.linuxbrew otherwise. 
Homebrew does not use sudo after installation. 
Using /home/linuxbrew/.linuxbrew allows the use of more binary packages (bottles) 
than installing in your personal home directory.
