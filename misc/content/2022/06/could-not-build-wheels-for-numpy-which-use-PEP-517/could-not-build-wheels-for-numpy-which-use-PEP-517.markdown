Status: published
Date: 2022-06-06 13:26:43
Modified: 2022-06-06 13:26:43
Author: Benjamin Du
Slug: could-not-build-wheels-for-numpy-which-use-PEP-517
Title: Could Not Build Wheels for Numpy Which Use Pep 517
Category: Computer Science
Tags: Computer Science, programming, Python, numpy, scipy, pip, pip3, PEP 517

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

This is due to outdated version of pip.
Update your pip to the latest version should fix the issue.

    :::bash
    pip3 install -U pip

## References

- [ERROR: Could not build wheels for scipy which use PEP 517 and cannot be installed directly](https://stackoverflow.com/questions/61365790/error-could-not-build-wheels-for-scipy-which-use-pep-517-and-cannot-be-installe)

- [ERROR: Could not build wheels for numpy which use PEP 517 and cannot be installed directly](https://github.com/numpy/numpy/issues/18901)
