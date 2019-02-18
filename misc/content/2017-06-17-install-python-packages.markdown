Status: published
Date: 2017-06-18 12:11:32
Author: Ben Chuanlong Du
Slug: install-python-packages
Title: Install Python Packages
Category: Programming
Tags: programming, Python, package, module, install, pip, conda

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. `pip` is preferred over OS tools
    (e.g., `apt-get`, `yum`, `wajig`, `aptitude`, etc.) to manage Python packages.
    If you are using Anaconda Python,
    use `conda` to manage python packages.

## Install Location

1. If you do not have root access,
    then `pip` installs to your local directory (`$HOM/.local`) by default.
    You can of course explicitly specify the option `--user` to `pip`
    to install packages to your local directory.

        pip install --user mercurial

    The same option can be used to install a package to local directory
    if you install using the `setup.py` file.

        python setup.py install --user

## Upgrade Packages

```sh
pip install --upgrade wheel
```

1. List all available versions of a Python package. 

	pip install pylibmc==

2. Install a specific version of a Python package.

	pip install MySQL_python==1.2.2

## List Modules

1. List outdated modules.

        pip list --outdated

2. You can use `help('modules')` to display all locally installed modules.

## Misc

1. `pip` supports downloading without installation!

2. install from the current directory

        pip install .

3. Install pre-release of `toree`.

        pip3 install --pre toree

4. `export LC_ALL=C` resolved an issues of pip3

## Error Messages

Could not find a version that satisfies the requirement toree:
network issue, no candidate, pre release


http://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting

http://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do

https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available

https://stackoverflow.com/questions/5226311/installing-specific-package-versions-with-pip
