UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-07-13 00:11:34
Author: Ben Chuanlong Du
Slug: install-python-on-windows-behind-proxy
Title: Install Python Packages Behind Proxy on Windows 
Category: Programming
Tags: Python, programming, Windows, proxy, install package


It is recommended that you use `pip` to install Python packages.
You can follow the following steps to install `pip` on Windows.

1. Download [distribute](http://python-distribute.org/distribute_setup.py) 
and save it as `distribute_setup.py`.

2. Install distribute.

        python distribute_setup.py

If you don't have permission to change environment variables on your office laptop,
you cannot run the `python` command directly.
You have to either use the full path to the python executable 
or run it in the directory containing it.

3. Download [pip](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) 
and save it as `get-pip.py`.

4. Install `pip`.

        python get-pip.py

After `pip` is installed, 
you can then follow the steps below to install Python packages.

0. If you don't already know the proxy in use (in your company),
read the post [Find out Proxy in Use](http://www.legendu.net/en/blog/find-out-proxy-in-use/)
to figure it out.

1. Open the Windows command prompt.

2. Set proxy environment variables. 

        set http_proxy=http://user:password@proxy_ip:port
        set https_proxy=https://user:password@proxy_ip:port

3. Install Python packages using proxy in the same Windows command prompt.

        pip install --proxy="user:password@proxy_ip:port" package_name

Note that working in a Linux virtual machine on your office laptop with Windows OS
can possibly help you circumvent the proxy issue.
