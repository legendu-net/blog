Status: published
Date: 2019-03-06 03:43:42
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
The `venv` module provides several parameters to control the behavior of the virtual environment to be created.
```
$ python3 -m venv -h
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT]
            ENV_DIR [ENV_DIR ...]

Creates virtual Python environments in one or more target directories.

positional arguments:
  ENV_DIR               A directory to create the environment in.

optional arguments:
  -h, --help            show this help message and exit
  --system-site-packages
                        Give the virtual environment access to the system
                        site-packages dir.
  --symlinks            Try to use symlinks rather than copies, when symlinks
                        are not the default for the platform.
  --copies              Try to use copies rather than symlinks, even when
                        symlinks are the default for the platform.
  --clear               Delete the contents of the environment directory if it
                        already exists, before environment creation.
  --upgrade             Upgrade the environment directory to use this version
                        of Python, assuming Python has been upgraded in-place.
  --without-pip         Skips installing or upgrading pip in the virtual
                        environment (pip is bootstrapped by default)
  --prompt PROMPT       Provides an alternative prompt prefix for this
                        environment.
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
