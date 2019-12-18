Status: published
Date: 2019-12-18 15:57:03
Author: Ben Chuanlong Du
Slug: high-performance-computing-in-python
Title: High Performance Computing in Python
Category: Programming
Tags: programming, Python, HPC, high performance computing, pybind11, numba, Cython, mars, Apache Ray

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

First of all,
make sure that you have read 
[Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips).
However,
keep in mind that some of the tips might be outdated.

## [Python Profilers](https://docs.python.org/3/library/profile.html)

1. [cprofile](https://docs.python.org/3/library/profile.html#module-cProfile)

## [mars](https://github.com/mars-project/mars)

## [Apache Ray](https://github.com/ray-project/ray)

Ray does not handle large data well (as of 2018/05/28).

## [modin-project/modin](https://github.com/modin-project/modin)

Notice that modin leverages the Apache Ray project.

## Celery

## RQ

## Dask

## Numba

1. numba should be the first thing to try, minimum effort, can probably increase the performance to what you need

2. need to install llvm

## Cython

1. cython, close to python implementation but close to C speed

cython3 ma.pyx
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python3.5 -o ma.so ma.c


## pybind11

```C++
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
```
`#include <pybind11/stl.sh>` is for auto type conversion of STL.

```bash
g++ -O2 -shared -std=c++11 -I/usr/local/include/python3.5 -I/usr/include/python3.5m -fPIC ma_cpp.cpp -o macpp.so
```



```C++
PYBIND11_PLUGIN(ma_cpp) {
```
`PYBIND11_PLUGIN` defines the module name and the compiled shared object must use this name.


The cppimport package makes things easy.
Don't forget to use the following setup
when using cppimport.

```C++
<%
setup_pybind11(cfg)
%>
```

## PyCUDA & PyGPU

## References

https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script

http://zhuoqiang.me/bring-cpp-class-to-python-through-cython.html

https://stackoverflow.com/questions/145270/calling-c-c-from-python

http://matthewrocklin.com/blog/work/2016/09/13/dask-and-celery

https://stackoverflow.com/questions/13440875/pros-and-cons-to-use-celery-vs-rq/13441828

https://groups.google.com/forum/#!topic/ray-dev/8E03APnG_zg

http://www.algorithm.co.il/blogs/computer-science/10-python-optimization-tips-and-issues/
