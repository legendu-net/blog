Status: published
Date: 2019-05-23 18:30:04
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

[Homebrew Documentation](https://docs.brew.sh/Homebrew-on-Linux)

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

Follow the instructions below if you have to install Linuxbrew using a proxy.

1. Configure the environment variables `http_proxy` and `https_proxy`.
    ```Bash
    export http_proxy=http://your.proxy.server:port
    export https_proxy=http://your.proxy.server:port
    ```
2. Configure proxy for Git (as Linuxbrew rely on Git to work) following instructions in
  [Use Git Behind a Proxy](http://www.legendu.net/en/blog/use-git-behind-a-proxy/).

