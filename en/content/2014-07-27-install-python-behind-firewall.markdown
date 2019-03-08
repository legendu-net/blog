Status: published
Date: 2019-03-08 00:20:54
Author: Ben Chuanlong Du
Slug: install-python-behind-firewall
Title: Install Python Packages Behind Firewall
Category: Programming
Tags: Python, programming, Windows, proxy, install package


It is recommended that you use `pip` to install Python packages.

## Install pip

### Ubuntu

```Bash
wajig install python3-pip
```

### Mac

`pip` should have already been installed when you instal Python using Homebrew or Anaconda.

### Universal Way

`pip` can be installed directly from Python.

```Bash
python3 -m ensurepip
```

This is a universal and convenient way of installing `pip` for Python.
For example,
it can be used to install `pip` for Python in Cygwin.

## Install Packages Using pip with Proxy

1. If you don't already know the proxy in use (in your company),
    read the post [Find out Proxy in Use](http://www.legendu.net/en/blog/find-out-proxy-in-use/)
    to figure it out.

2. Open the Windows command prompt.

3. Set proxy environment variables. 

        set http_proxy=http://user:password@proxy_ip:port
        set https_proxy=https://user:password@proxy_ip:port

4. Install Python packages using proxy in the same Windows command prompt.

        pip install --proxy="user:password@proxy_ip:port" package_name

    Note that working in a Linux virtual machine on your office laptop with Windows OS
    can possibly help you circumvent the proxy issue.
