Status: published
Author: Ben Chuanlong Du
Date: 2019-08-12 20:15:00
Slug: python-tips
Title: Some Fragmentary Tips About Python
Category: Programming
Tags: tips, Python, programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

<img src="http://dclong.github.io/media/python/python.png" height="200" width="240" align="right"/>

## Python Doc

[Comprehensive Python Cheatsheet](https://gto76.github.io/python-cheatsheet/)

- [The Python Wiki](https://wiki.python.org/moin/)
- [Useful Modules](https://wiki.python.org/moin/UsefulModules)
- [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/)
- [PyVideo](http://pyvideo.org/)

## Python Distirbutions

1. When people talks about Python,
  it usually means the CPython implementation
  which you can download from <www.python.org>.
  There are other interesting Python implementations
  such as [PyPy](https://pypy.org/) (Python implementation in Python),
  [Jython](http://www.jython.org/) (Python implementation in Java), etc. exists,
  however,
  they have relatively very small use groups.
  Generally speaking,
  you want to stay with CPython,
  i.e., the Python people are taling about unless you have very strong reasons to go with another choice.
  There are also different distributions among CPython implementations.
  Anaconda Python is a good one if you do not have sudo permissions in the system.

2. For the CPython implementation,
  there are different distributions as well.
  Besides the official Python distribution
  (which comes by default in many operating systems),
  Anaconda Python rules the unofficial distributions.
  It is a great choice which provies an all-in-one installer
  to use on machines that you don't have sudo permissions
  as it installs to your home directory by default.
  Anaconda Python supports 2 different flavors:
  Anaconda (binded with many popular Python packages) and miniconda (with minimum Python packages).
  It also invented another package management tool named `conda` to replace `pip`.
  `conda` is a general purpose package management tool instead of for Python only.
  It eases the pain of figuring out the right dependencies of Python packages
  but it is a little bit bloated (with larger installation sizes) compared to `pip`.

## Environment Variable

1. `os.getenv` gets the value of an environment variable
  while `os.setenv` creates a new environment variable or
  sets the value of an environment variable.

2. You should use `os.pathexpanduser("~")` instead of `os.getenv('HOME')`
  to get the home directory of the current user in Python.
  `os.getenv('HOME')` only works on Linux/Unix.

## Programming Skills

1. Python varadic args can mimic function overloading

3. Python eval

4. `*args` and `**kwargs`

6. `sys.stdout.write`, `sys.stdout.flush`, `print`

9. Global variables in a Python module are readable but not writable to functions in the same module by default.
  If you want to write to a global variable in a function (in the same module),
  you have to declare the global variable in the method using the keyword `global`.
  For example, if `x` is a global variable
  and you want to write to it in a method,
  you have to declare `global x` at the beginning of the method.

## Tricks and Traps

https://docs.python-guide.org/writing/gotchas/

https://stackoverflow.com/questions/101268/hidden-features-of-python


1. Use type annotation to make your code more readable and easier to understand.

2. Restrict the types of objects that your function/method can be applied to 
  and throw a (ValueError) exception when a wrong type is provided.
  This helps minimize surprisings.

3. AVOID returning objects of different types from a Python function/method.

4. Be CAREFULL about Python scripts in the current directory. 
  They might mess up Python import as they are search for when Python looking for modules.
  For example, 
  if you have a Python script named `datetime.py` in the current working directory,
  it will likely mess up your import if you use the official `datetime` module.
  This is true even if the official `datetime` module is indirectly used,
  e.g.,
  if you have imported the `numpy` module which imports the `datetime` module,
  which makes things tricky.
  It is even more tricky if you invoke a Python script in shell 
  and there are other Python scripts in the current working directory of shell 
  (not the directory which the invoked Python script is located in)
  whose names conflict with official Python modules.
  If unfortunately, 
  the invoked Python script depends on (even if indirectly) an official module which is hidden by Python scripts in the current working directory,
  it will likely make your Python script mal-function.
  It is suggested that you follow the practices below to avoid such tricky issues.
  - If you use Python shell interactively, avoid placing your scripts into the current working directory of the Python shell.
    Instead, place them into subdirectories (of the current working directly) and import them as submodules.
  - If you plan to invoke a Python script via shell, disable Python from search scripts in the current working directory as modules. 
    This can be done this by removing `''` from `sys.path`.
  
2. Almost all modern programming languages follow the convention
  of not returnting anything (or in another words, retun void, None, etc.)
  from a mutator method so that you cannot chain on a mutator method.
  Functional programming languages enough chaining on methods
  as they often have immutable objects and the methods return new objects
  rather than changing the original objects.

2. Python functions (except lambda functions) do not automatically return value
  unlike functional programming languages.
  Forgotting a `return` statement is a common mistake in Python.

3. Do NOT use the ternary expression in complicated expressions!!!
```
update = {
    'status': 'succeed', 
    'partitions': 52,
    'size': 28836,
    'end_time': 1563259850.937318
}
[key + ' = ' + f'{val}' if isinstance(val, (int, float)) else f"'{val}'" for key, val in update.items()]
```
returns
```
["'succeed'", 'partitions = 52', 'size = 28836', 'end_time = 1563259850.937318']
```
The issue can be fixed by putting the ternary expression into parentheses or define a (lambda) function for the ternary expression.
```
[key + ' = ' + (f'{update[key]}' if isinstance(update[key], (int, float)) else f"'{update[key]}'") for key in update]
```

4. Backslash (`\`) cannot be used in a f-string (introduced in Python 3.6).
  There are multiple ways to resolve this issue.
  First, you can precompute things needed to avoid using `\` in a f-string.
  Second, you can use `chr(10)` (which returns the backslash) instead.

5. If you need trackback information when throwing an exception use `raise ExceptionClass(msg)`,
  otherwise, use `sys.exit(msg)` instead.



## Design

1. There is no constant variables in Python.
    If you need a constant variable in Python,
    just define one and never change it.
    It is suggested that you use UPPER_WITH_UNDERSCORE naming style for const variables in Python.
    There is no private variables/method in Python either.
    You can change/call any variable/method in a module/class.
    However,
    members that start with a single underscore (`_`) are considered as private by convention
    and you should avoid using them directly.

2. The bottom-most package in Java should be a file in Python.
    Do not use inner classes in Python.
    Just put classes in the same module.

3. Python is a dynamic language and thus does not support function/method overloading.

## Numerical

1. Division is float division in Python 3 which is different from Python 2.
    If you want integer division,
    use the `//` operator.

## Misc

1. Keys for set and dict objects must be immutable in Python
    (and the same concept holds in other programming languages too).
    Since a list in Python is mutable,
    it cannot be used as a key in set and dict objects.
    You have to convert it to an immutable equivalence (e.g., tuple).

2. Use sys.exit(msg) to print error message and quit when error happens

3. Get the class name of an object.

		type(obj).__name__

## File System

1. You can get rid of file extension use the following code.

        os.path.splitext(file_name)[0]

2. `os.mkdir` acts like `mkdir` in Linux and `os.makedirs` acts like `mkdir -p` in Linux.
    Both of them throw an exception if the file already exists.

3. Use `execfile(open(filename).read())` to source a file,
    variables defined in 'filename' are visible,
    however, imported packages are invisible to the script running execfile

## Encoding

`ord` `unichar`
return `ascii` number of characters
`chr` return a string from a ascii number

## Syntax

1. Python expression is calculated from left to right.

7. You can use a `dict` structure to mimic switch in other programming languages.
    However, it is kind of evil and has very limited usage.,
    You should avoid use this.
    Just use multiple `if ... else ...` branches instead.

5. `:` has higher priority than arithmetic operators in Python,
    which is opposite to that in R.

3.  `return v1, v2` returns a tuple `(v1, v2)`.
    And if a function `f` returns a tuple `(v1, v2, v3)`,
    you can use
    `v1, v2, v3 = f()`

11. Stay away from functions/methods/members starting with `_`.
    For example,
    you should use the built-in function `len` to get the length of a list
    instead of using its method `__len__`.

7. Python does not support `++`, `--` but support `+=`, `-+`, etc.


- [Python日报](http://py.memect.com/)
- [Python Homepage](http://www.python.org/)
- [Python Documentation](http://docs.python.org/py3k/)
- [Useful Modules](https://wiki.python.org/moin/UsefulModules)
- [LearningJython](http://wiki.python.org/jython/LearningJython)
- [Jython Tutorial](http://www.jython.org/currentdocs.html)
- [PEP 8 -- Style Guide for Python](http://legacy.python.org/dev/peps/pep-0008/)


### Programming Tips and Traps

- [Common Mistakes](http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)


http://builtoncement.org/

https://pythonhosted.org/pyCLI/

### Encryption

- [pycrypto](https://pypi.python.org/pypi/pycrypto)

https://github.com/dlitz/pycrypto

http://stackoverflow.com/questions/3504955/using-rsa-in-python


## Data Structure

1. The list object in Python does not have a `find` method which is inconvenient.
    To do a clean "find" in a list in Python,
    you can use the following style of code.

        if x in alist:
            index = alist.index(x)

2. You can use `set(alist)` to get unique values of a list.
    If you want to return a list (rather than a set) of unique values,
    you can use `list(set(alist))`.
    Another way is to use the method `numpy.unique`.

3. The difference between list and tuple in Python is that
    a list is mutable while a tuple is immutable.
    So you can think of tuple as immutable version of list.
    Tuples can be used in dictionarys in Python as keys
    while lists cannot.

## Collections

1. defaultdict

2. namedtuple


