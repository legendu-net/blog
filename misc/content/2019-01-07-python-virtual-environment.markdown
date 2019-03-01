Status: published
Date: 2019-01-07 09:49:27
Author: Ben Chuanlong Du
Slug: python-virtual-environment
Title: Python Virtual Environment
Category: Programming
Tags: programming, Python, virtual environment, venv

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

It is suggested that you use `venv` for managing virtual environments in Python3. 

## Installation on Ubuntu

```bash
wajig install python3-venv
```

## Create a Virtual Environment

```bash
python3 -m venv /path/to/your/environment
```

## Activate the Virtual Environment

```bash
source <DIR>/bin/activate
# or 
. <DIR>/bin/activate
```

## Use the Virtual Environment in PyCharm

1. Click on the `PyCharm` menu.

2. Click on `Preferences...`.

3. Select `Project Interpreter` in the left panel under `Project`.

4. If no virtual environment is configured for PyCharm, 
    you can select `Using Existing Virtual Environment` and then choose the virtual environment directory.

## References

https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments


[Best Practice for Virtual Environment and Git Repository](http://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html)
