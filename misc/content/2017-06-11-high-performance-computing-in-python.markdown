Status: published
Date: 2019-02-18 19:57:43
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

## [mars](https://github.com/mars-project/mars)

## [Apache Ray](https://github.com/ray-project/ray)

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

