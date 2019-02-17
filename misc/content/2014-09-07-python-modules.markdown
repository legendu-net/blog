Status: published
Date: 2019-02-17 19:48:08
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

1. pandas: data frame.

2. scipy: scientific computing.

3. numpy: multi-dimensional array.

4. re: regular expression
    - re.sub
    - re.search
        + return none if match is not found
        + use the `group` method to extract found match

5. inspect: check class, function definition and so on

## File System

9. shutil: Copy, move and remove files.
    - shutil.copy
    - shutil.copy2
    - shutil.copyfile
    - shutil.copytree
    - shutil.rmtree

5. tempfile
    - tempfile.mkdtemp
    - tempfile.mkstemp

7. os.path file path related utilities.
    - os.path.join
    - os.path.basename file name without parent directory

6. os: Operating system related utilities.

## Logging

1. logging

2. warnings: Warning message.

## [Visualization](http://www.legendu.net/misc/blog/python-modules-for-visualization/)

## Multimedia

1. ReportLab 

seems interesting

2. Pweave 

R knitr equivalence in Python.

2. PDFMiner
2. pyPDF
3. slate (based on PDFMiner and make it much easier to use)
4. pdftables 
doc – antiword
docx – python-docx
odt – odt2txt 

## Database

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

2. pyodbc, pypyodbc, SQLAlchemy

3. teradata, sqlalchemy-teradata

4. JayDeBeApi

5. PyMongo

6. PyMySQL, MySQLdb

7. sqlite3

## Date/Time

11. dateutil: Parses time in all kinds of format.
```bash
pip install python-dateutil
```

2. monthdelta

## High Performance Computing

13. PyCUDA

14. PyGPU

## Command-line 

1. argparse 
    This is the recommended package to use for argument parsing in Python.

2. curses 

3. getopt
    Not as convenient as argparse.


## Text Mining

1. NLTK

2. scrapy: Web cr

3. textmining package 

https://pypi.python.org/pypi/textmining/1.0
http://www.christianpeccei.com/textmining/

4. email.parser

## Machine Learning

1. mlpy

2. shogun

3. [scikit-learn](http://scikit-learn.org/stable/)

4. orange

5. theano (deep learning)

## GUI application

1. PyQt

2. PySide

3. Tkinter 
```bash
wajig install python-tk
```

## command-line application

0. subprocess 

Call bash commands and return results to Python.

write down the bash commands and split it by space into a list, this is how you can construct list command for subprocess

1. clint 

2. pycurse

3. Clint

clint is a Python module which is filled with very useful tools for developing command-line applications. 
It supports features such as; CLI colors and indents, 
simple and powerful column printer, iterator based progress bars and implicit argument handling.

4. Click

click is an upcoming Python package for creating command-line interfaces in a composable way with as little code as possible. 
This "Command-line Interface Creation Kit" is highly configurable but comes with good defaults out of the box.

5. docopt

docopt is a lightweight, 
highly Pythonic package that allows creating command-line interfaces easily and intuitively, 
by parsing POSIX-style usage instructions.

6. Plac

Plac is a simple wrapper over the Python standard library argparse, 
which hides most of its complexity by using a declarative interface: the argument parser is inferred rather than written down by imperatively. 
This module targets especially unsophisticated users, programmers, sys-admins, scientists and in general people writing throw-away scripts for themselves, 
who choose to create a command-line interface because it is quick and simple.

7. Cliff

Cliff is a framework for building command-line programs. It uses setuptools entry points to provide subcommands, 
output formatters, and other extensions. 
The framework is meant to be used to create multi-level commands such as subversion and git, 
where the main program handles some basic argument parsing and then invokes a sub-command to do the work.

## encryption

4. gnupg 

5. pycrypto

You can use incremental encryption. 
For this reason, you cannot use the same object to encrypt and decrypt texts.
You must create a new object ...
can I use an object to decrypt repeated? for different texts?
probably not ...

## Internet

1. email.parser

## Unit Testing

1. unittest

It is previous referred to as PyUnit.
PyUnit is the standard unit testing framework module for Python.
It is a Python implementation of JUnit.

2. nose


## Others

1. fuzzywuzzy

2. weechat

3. python-virtualenv virtual environment is good, 

