Status: published
Date: 2020-02-12 11:30:59
Author: Benjamin Du
Slug: tips-on-pex
Title: Tips on Pex
Category: Programming
Tags: programming, Python, pex, dependency, virtual environment

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


Python packages that have native code (C/C++, Fortran, etc.) dependencies work well in pex.
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
