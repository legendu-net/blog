Status: published
Date: 2019-04-26 22:58:57
Author: Ben Chuanlong Du
Slug: install-python-packages
Title: Install Python Packages
Category: Programming
Tags: programming, Python, package, module, install, pip, conda

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


`pip` is preferred over OS tools
(e.g., `apt-get`, `yum`, `wajig`, `aptitude`, etc.) for managing Python packages.
If you are using Anaconda Python,
use `conda` to manage python packages.

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


## Install Python packages Locally

You can install Python packages to your local directory 
by specifying the `--user` option to `pip`.
This is extremely useful if you do not have permission 
to install packages to system-wide locations.

    pip3 install --user mercurial

The same option `--user` can be used to install a package to local directory
if you install using the `setup.py` file.

    python setup.py install --user

Notice that if your Python is installed by Homebrew or you are using Anaconda Python,
the whole Python is installed to your local directory,
so that you do not need to use the `--user` option when installing Python packages.

## Install a Specific Version of a Python Package

1. List all available versions of a Python package. 

        pip3 install pylibmc==

2. Install a specific version of a Python package.

        pip3 install MySQL_python==1.2.2

3. You can install the pre-release version of a package using the `--pre` option.
    For example, 
    the current version of pybuilder (0.11.7) is not compatible with Python 3.7.
    If you are using Python 3.7 and still want to use the pybuilder package, 
    you can install the pre-release version (0.12) which is compatible with Python 3.7.

        pip3 install --pre pybuilder

## Difference between --ignore-installed and --force-reinstall

https://stackoverflow.com/questions/51913361/difference-between-pip-install-options-ignore-installed-and-force-reinstall

https://github.com/blockstack/blockstack-core/issues/504

Sometimes a package is installed by distutils
which cannot be reinstalled using `pip`, 
not even with the `--force-reinstall` option.
In that case, 
you have to use the `--ignore-installed` option.

## Install Python Packages Without Installing Dependencies

```
pip3 install --no-deps some_package
```

## Upgrade Python Packages

```sh
pip3 install --upgrade wheel
```

## List All Installed Python Packages

1. List all installed modules.

        pip3 list --outdated

2. List outdated modules only.

        pip3 list --outdated

3. You can also use `help('modules')` to show all installed modules in Python.

## Use pip with Proxy

```
pip3 --proxy http://proxy__server_ip:port install some_pkg
```

## Misc

1. `pip` supports downloading without installation!

2. Install from the current directory

        pip3 install .

4. `export LC_ALL=C` resolved an issues of pip3

## References

http://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting

http://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do

https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available

https://stackoverflow.com/questions/5226311/installing-specific-package-versions-with-pip
