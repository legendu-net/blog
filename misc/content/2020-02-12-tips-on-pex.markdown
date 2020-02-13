Status: published
Date: 2020-02-13 08:57:05
Author: Benjamin Du
Slug: tips-on-pex
Title: Tips on pex
Category: Programming
Tags: programming, Python, pex, dependency, virtual environment

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


1. Python with the same version as the one that generated the pex file
    need to be installed in on the machine to run the pex file.
    And the Python executable must be searchable by `/usr/bin/env`.
    It is kind of like that Java need to be installed on the machine to run a JAR application.

2. Python packages that have native code (C/C++, Fortran, etc.) dependencies work well in pex.
    However,
    you have to make sure that pex runs on the same type of OS. 
    For example, 
    if you build a pex environment containing numpy on macOS,
    it won't run on a Linux OS.
    You will get the following error message 
    if you try to run the pex environment (generated on macOS) in a Linux OS.

> root@013f556f0076:/workdir# ./my_virtualenv.pex 
> Failed to execute PEX file. Needed manylinux2014_x86_64-cp-37-cp37m compatible dependencies for:
> 1: numpy==1.18.1
>    But this pex only contains:
>      numpy-1.18.1-cp37-cp37m-macosx_10_9_x86_64.whl

## References

https://github.com/pantsbuild/pex

https://punchplatform.com/2019/10/08/packaging-python/
