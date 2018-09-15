UUID: 88529d1e-95dc-4534-bf5a-eefb10845b2a
Status: published
Date: 2018-07-21 12:23:31
Author: Ben Chuanlong Du
Slug: command-line-tools-for-python-developing
Title: Command-Line Tools for Python Developing
Category: Programming
Tags: programming, Python development, command-line, pylint, yapf, pdb, linter, formatting, debugging

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Check Python Script

### [pylint](https://github.com/PyCQA/pylint)

pylint your_script.py

### mypy

mypy your_script.py

mypy --ignore-missing-imports roas.py

## Type Annotation

### [MonkeyType](https://github.com/Instagram/MonkeyType)

1. Run the following command to annotate your Python script.

        monkeytype run yourscript.py


2. MonkeyType supports pytest.

        monkeytype run `which pytest` 

## Formatting 

1. [yapf](https://github.com/google/yapf)

        yapf -d yourscript.py

## Debugging

1. [pdb](https://docs.python.org/3/library/pdb.html)


## Installation

```
pip3 install yapf, pylint, monkeytype, mypy
```
```
conda install -c conda-forge MonkeyType
conda install mypy
```
