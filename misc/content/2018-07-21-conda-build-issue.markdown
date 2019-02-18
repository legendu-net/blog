Status: published
Date: 2018-07-21 12:19:14
Author: Ben Chuanlong Du
Slug: conda-build-issue
Title: Conda Build Issue
Category: Programming
Tags: programming, Anaconda, Python, conda build, sqlalchemy-teradata

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

I encountered an issue building the package
[sqlalchemy-teradata](https://pypi.org/project/sqlalchemy-teradata/).
There are a few related issues:
[issues/2790](https://github.com/conda/conda-build/issues/2790),
[issues/2826](https://github.com/conda/conda-build/issues/2826).
It seems that the recipe uses an outdated URL.
Change the URL to the following updated one resolves the issue.

https://files.pythonhosted.org/packages/13/ba/bd5ebedd251630a822cfa2ad819caa99f6b494726aa05c8ef69bbb39330e/sqlalchemy_teradata-0.1.0.dev0.tar.gz