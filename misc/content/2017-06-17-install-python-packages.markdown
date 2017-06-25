UUID: 4a8d5a5a-e2c3-423e-88fa-600e220896de
Status: published
Date: 2017-06-18 12:11:32
Author: Ben Chuanlong Du
Slug: install-python-packages
Title: Install Python Packages
Category: Programming
Tags: programming, Python, package, module, install, pip

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. You should use `pip` instead of OS tools (e.g., `apt-get`, `yum`, `wajig`, `aptitude`, etc.) to manage Python packages.
If you are using Anaconda Python, 
use `conda` to manage python packages.

## Install Location

1. If you do not have root access, 
then pip installs to your local directory (`$HOM/.local`) by default.
You can of course explicitly specify the option `--user` to `pip` 
to install packages to your local directory.
```bash
pip install --user mercurial
```
The same option can be used to install a package to local directory 
if you install using the `setup.py` file.
```bash
python setup.py install --user
```

## Upgrade Packages

```sh
pip install --upgrade wheel
```

## List Modules

1. List outdated modules.
```sh
pip list --outdated
```

2. You can use `help('modules')` to display all locally installed modules.



Questions
pip install, is it possible to choose repository?



pip download
cool!!!



install from the current directory
pip install .

Upgrade spyder from the Python package index.
pip install --upgrade spyder
pip install package 

--pre --sys --user, etc. ... 
Pre-release 
pip3 install --pre toree 

## Error Messages

Could not find a version that satisfies the requirement toree:
network issue, no candidate, pre release


http://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting
☐ python: http://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do
☐ python, pip3 export LC_ALL=C

 
