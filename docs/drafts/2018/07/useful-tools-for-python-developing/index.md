---
title: Useful Tools for Python Developing
created: '2018-07-08T10:46:18-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: useful-tools-for-python-developing
license: CC-BY-4.0
tags:
  - programming
  - Python
  - development
  - command line
  - pylint
  - yapf
  - pdb
  - linter
  - formatting
  - debugging
  - dev
  - lint
  - format
  - dead code
  - type
  - annotation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

- [vulture](https://github.com/jendrikseipp/vulture)

  [vulture](https://github.com/jendrikseipp/vulture)
  finds unused code in Python programs.
  It is useful for cleaning up and finding errors in large code bases.

- [pandas-stubs](https://pypi.org/project/pandas-stubs/)

## Testing

- [pytest](https://github.com/pytest-dev/pytest)

## Typing Checker

- [ty](ty-is-a-new-modern-static-type-checking-and-language-server-for-python)

- [pyrefly](tips-on-pyrefly)

- [pytype](https://github.com/google/pytype)

- pyright

- [mypy](static-type-checking-of-python-scripts-using-mypy)

## Lint Python Scripts

### [ruff](https://github.com/charliermarsh/ruff/)

[ruff](https://github.com/charliermarsh/ruff/)
is an extremely fast Python linter, written in Rust.
It is preferred to other Python linters such as pylint and flake8.

## Formatting

`ruff` is prerred for formating Python script (and notebooks).
Just run `ruff format` to format code.

## [Debugging, Unit Testing and CICD](debugging-unit-testing-and-cicd-in-python)

## Reference

- [Type Annotation in Python](type-annotation-in-python)

- [Type Annotation](type-annotation-in-python)

- [Hypermodern Python Chapter 1: Setup](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

- [Hypermodern Python Chapter 2: Testing](https://cjolowicz.github.io/posts/hypermodern-python-02-testing/)

- [Hypermodern Python Chapter 2: Linting](https://cjolowicz.github.io/posts/hypermodern-python-03-linting/#managing-dependencies-in-nox-sessions-with-poetry)
