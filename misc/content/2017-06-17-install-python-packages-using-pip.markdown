Status: published
Date: 2019-11-02 10:20:52
Author: Ben Chuanlong Du
Slug: install-python-packages
Title: Install Python Packages Using pip
Category: Programming
Tags: programming, Python, package, module, install, pip, conda

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## PyPi Statistics

You can check download statistics of Python Packages on PYPI at https://pypistats.org/.
This is especially helpful if you want to choose from multiple packages.

## Prefer [pip](https://pip.pypa.io/en/stable/reference/)

[pip](https://pip.pypa.io/en/stable/reference/)
is preferred over OS tools
(e.g., `apt-get`, `yum`, `wajig`, `aptitude`, etc.) for managing Python packages.
If you are using Anaconda Python,
use `conda` (instead of `pip`) to manage Python packages
especially when you encounter dependency issues.

## Install [pip](https://pip.pypa.io/en/stable/reference/)

### On Ubuntu

```Bash
apt-get install python3-pip
```

### On Mac

`pip` should have already been installed when you instal Python using Homebrew or Anaconda.

## Bootstrapping the pip Installer

The package [ensurepip](https://docs.python.org/3.8/library/ensurepip.html)
provides support for bootstrapping the pip installer into an existing Python installation or virtual environment.

```Bash
sudo python3 -m ensurepip
```

## Proper Way of Using pip

1. Upgrading pip via the system package management tools only.

2. Do NOT use `sudo pip install pkg1 pkg2` install packages to system-wide locations. 
    Instead, use `pip install --user pkg1 pkg2` to install packages to your local directory.

https://github.com/pypa/pip/issues/5599

https://stackoverflow.com/questions/49940813/pip-no-module-named-internal


## Install Python packages Locally

You can install Python packages to your local directory 
by specifying the `--user` option to `pip`.
This is extremely useful if you do not have permission 
to install packages to system-wide locations.
```Bash
pip3 install --user mercurial
```
The same option `--user` can be used to install a package to local directory
if you install using the `setup.py` file.
```Bash
python setup.py install --user
```
Notice that if your Python is installed by Homebrew or you are using Anaconda Python,
the whole Python is installed to your local directory,
so that you do not need to use the `--user` option when installing Python packages.

## Install a Specific Version of a Python Package

1. List all available versions of a Python package. 
    ```
    pip3 install pylibmc==
    ```
2. Install a specific version of a Python package.
    ```
    pip3 install MySQL_python==1.2.2
    ```
3. Install pyarrow with a verison of at least 0.14.0.
    ```
    pip3 install pyarrow>=0.14.0
    ```
4. You can install the pre-release version of a package using the `--pre` option.
    For example, 
    the current version of pybuilder (0.11.7) is not compatible with Python 3.7.
    If you are using Python 3.7 and still want to use the pybuilder package, 
    you can install the pre-release version (0.12) which is compatible with Python 3.7.
    ```
    pip3 install --pre pybuilder
    ```

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
    ```
    pip3 list --outdated
    ```

2. List outdated modules only.
    ```
    pip3 list --outdated
    ```

3. You can also use `help('modules')` to show all installed modules in Python.

## Use pip with Proxy

You can export environment variables `http_proxy` and `https_proxy`
or you can use `pip` with the `--proxy` option directly.
```Bash
pip3 --proxy http://proxy__server_ip:port install some_pkg
```
When using the `--proxy` with `pip`/`pip3`, 
you can omit `http://` and the port if the port is 80.
```Bash
pip3 --proxy 10.135.227.47 search notifiers
```

Notice that sometimes `pip` does not respect the environment variables.
In that case, 
you have to use the option `--proxy` to pass proxy to `pip`.
And even with the option `--proxy`,
pip might not work well if you install from a version control system. 
Just be ware of that.
[ProxyChains](http://www.legendu.net/misc/blog/proxychains-tips/)
is likely a solution when that issue happens.

## Caching

1. You can disable pip caching using the option `--no-cache-dir`.

https://pip.pypa.io/en/latest/reference/pip_install/#caching


https://github.com/pypa/pip/issues/4685

https://github.com/pypa/pip/pull/6391

## Misc

1. `pip` supports downloading without installation!

2. Install from the current directory
    ```
    pip3 install .
    ```

4. `export LC_ALL=C` resolved an issues of pip3

## References

https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/

http://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting

http://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do

https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available

https://stackoverflow.com/questions/5226311/installing-specific-package-versions-with-pip

https://stackoverflow.com/questions/14149422/using-pip-behind-a-proxy

https://stackoverflow.com/questions/9510474/removing-pips-cache
