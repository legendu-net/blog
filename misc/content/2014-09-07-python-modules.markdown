UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2017-04-03 18:12:05
Author: Ben Chuanlong Du
Slug: python-modules
Title: Python Modules
Category: Programming
Tags: programming, Python, module, package

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

- [https://wiki.python.org/moin/UsefulModules](https://wiki.python.org/moin/UsefulModules)

- [20 Python libraries you can’t live without](https://freepythontips.wordpress.com/2013/07/30/20-python-libraries-you-cant-live-without/)

1. Accroding to PEP, 
you should import packages at the beginning of your module.

### Install Modules

1. Do not use OS tools (e.g., `apt-get`, `yum`, `wajig`, `aptitude`, etc.) 
to manage Python packages.
Use Python's own package managing tools instead.
`pip` is recommended (over `easy_install`, etc.).
If you are using Anaconda Python, 
then use `conda` to install python packages.

2. The following are ways to install a python module 
to a local directory.

```bash
python setup.py install --user
```
or
```bash
pip install --user mercurial
```

pip list --outdated

pip install --upgrade wheel

2. You can use `help('modules')` to display all locally installed modules.

1. sys.path.append

```bash
import module_name  
import module_name as alias 
from module import pkg_mod_or_fun
```

10. Python built-in functions are acutally in the `__builtins__` module.

1. `__file__` path of a module 
[Retrieving python module path](http://stackoverflow.com/questions/247770/retrieving-python-module-path)

### Numerical Computing

1. numpy: numerical computing

2. scipy (a super set of numpy)

2. pandas: data frame

3. re: regular expression
    - re.sub
    - re.search
        + return none if match is not found
        + use the `group` method to extract found match

4. inspect: check class, function definition and so on

5. tempfile
    - tempfile.mkdtemp
    - tempfile.mkstemp

6. os: Operating system related utilities.

7. os.path file path related utilities.
    - os.path.join
    - os.path.basename file name without parent directory

8. warnings: Warning message.

9. shutil: Copy, move and remove files.
    - shutil.copy
    - shutil.copy2
    - shutil.copyfile
    - shutil.copytree
    - shutil.rmtree

### Visualization/Graph

1. ggplot
2. matplotlib
1. [plotly](https://plot.ly/python/user-guide/)

### Multimedia

1. PDFMiner
2. pyPDF
3. slate (based on PDFMiner and make it much easier to use)
4. pdftables 
doc – antiword
docx – python-docx
odt – odt2txt 

### Database

1. json/simplejson 

json is simplejson, added to Python standard library.
But since json was added in 2.6, 
simplejson has the advantage of working on more Python versions (2.4+).

simplejson is also updated more frequently than Python, 
so if you need (or want) the latest version, it's best to use simplejson itself, if possible.

A good practice, in my opinion, is to use one or the other as a fallback.

try: import simplejson as json
except ImportError: import json

Methods of json ending with `s` takes string arguments 
and others take file stream arguments.


10. PyMongo

11. MySQLdb

11. sqlite3

### Date/Time

11. dateutil: Parses time in all kinds of format.
```bash
pip install python-dateutil
```

2. monthdelta

## High Performance Computing

13. PyCUDA

14. PyGPU

### Command-line 

3. curses 

1. argparse

2. getopt: great for paring arguments in a list! very cool, sounds like more general than argparse



### Text Mining

2. NLTK

1. scrapy: Web cr

3. textmining package 

https://pypi.python.org/pypi/textmining/1.0
http://www.christianpeccei.com/textmining/

4. email.parser

### Machine Learning

1. mlpy

2. shogun

3. [scikit-learn](http://scikit-learn.org/stable/)

4. orange

5. theano (deep learning)

### GUI application

1. PySide

2. PyQt

3. Tkinter 
```bash
wajig install python-tk
```

### command-line application

0. subprocess 

Call bash commands and return results to Python.

write down the bash commands and split it by space into a list, this is how you can construct list command for subprocess

1. clint 

2. pycurse

3. Clint

clint is a Python module which is filled with very useful tools for developing command-line applications. It supports features such as; CLI colors and indents, simple and powerful column printer, iterator based progress bars and implicit argument handling.

4. Click

click is an upcoming Python package for creating command-line interfaces in a composable way with as little code as possible. This “Command-line Interface Creation Kit” is highly configurable but comes with good defaults out of the box.

5. docopt

docopt is a lightweight, highly Pythonic package that allows creating command-line interfaces easily and intuitively, by parsing POSIX-style usage instructions.

6. Plac

Plac is a simple wrapper over the Python standard library argparse, which hides most of its complexity by using a declarative interface: the argument parser is inferred rather than written down by imperatively. This module targets especially unsophisticated users, programmers, sys-admins, scientists and in general people writing throw-away scripts for themselves, who choose to create a command-line interface because it is quick and simple.

7. Cliff

Cliff is a framework for building command-line programs. It uses setuptools entry points to provide subcommands, output formatters, and other extensions. The framework is meant to be used to create multi-level commands such as subversion and git, where the main program handles some basic argument parsing and then invokes a sub-command to do the work.

### encryption

4. gnupg 

5. pycrypto

You can use incremental encryption. 
For this reason, you cannot use the same object to encrypt and decrypt texts.
You must create a new object ...
can I use an object to decrypt repeated? for different texts?
probably not ...

### Others

1. fuzzywuzzy

2. weechat

3. python-virtualenv virtual environment is good, 

1. ipython-notebook is great,
and you can restrict ip ...

10. module vs class:
you can use module to simulate a class,
however, class still has advantages.
class is smaller unit, and can encapsulate state variables.
Global variables are comparable to state variables of a class,
the things is that they are exposed to all modules, class ...

11. Python module import does not have the transitivity property (unlike C++ include).
That is if you import module a in module and then import module b in module c,
you cannot access members of module a in module c.
Module kind of encapsulates its members.
so it is similar to a class.
The differene is that class is smaller unit.

When you import module a in module b, things defined in module b cannot be used in module a either

2. the conflict of function and module names seems tricky!!!

### Internet

1. email.parser

### IO

1. csv (reading and writing CSV files)

2. numpy (use methods loadtxt, etc.)

## Unit Testing

1. unittest

It is previous referred to as PyUnit.
PyUnit is the standard unit testing framework module for Python.
It is a Python implementation of JUnit.

2. nose

