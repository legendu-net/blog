Status: published
Date: 2020-02-17 16:11:27
Author: Ben Chuanlong Du
Slug: conda-build-issue
Title: Conda Build Issue
Category: Programming
Tags: programming, Anaconda, Python, conda build, sqlalchemy-teradata, conda

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


## Example

https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/building-conda-packages.html#building-a-sep-package-with-conda-and-python-2-or-3

https://github.com/conda/conda-recipes

## References

https://docs.conda.io/projects/conda-build/en/latest/concepts/recipe.html

https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/index.html

https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/building-conda-packages.html
