UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-06-26 00:00:23
Slug: python-tips
Title: Some Fragmentary Tips About Python
Category: Programming
Tags: tips, Python, programming

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
<img src="http://dclong.github.io/media/python/python.png" height="200" width="240" align="right"/>

## Configuration

1. package site for user configurations,

PYTHONPATH

PYTHONHOME

3. PYTHonstartUP


## IDE

1. spyder
2. pycharm

## Programming Skills

1. Python varadic args can mimic function overloading

3. Python eval

4. `*args` and `**kwargs`

5. int str convert integer and string, constructors

6. sys.stdout.write sys.stdout.flush print('h', end='')

8. have to use import dateutil.parser, otherwise won't work

9. By default global variables in Python are already readable to methods 
defined in the same module.
However, if you want to write to a global variable in a method (in the same module),
you have to declare the global variable in the method using the keyword `global`.
For example, if `x` is a global variable 
and you want to write to it in a method,
you have to declare `global x` at the beginning of the method.

## Debugging

1. simply commenting out try catch or if else clause causes problems, 
becuase Python use idention to decide code structure!!!

2. "+=" on a non existing variable/object, causes funny mistake, 
sounds like exception happens

## tricks and traps

### Regular Expression

1. It seems that re.match deos not support some predefined regular expression classes very well.
For example,
`re.match` fails to match in the following example.

        re.match("\s", "a b\tc")

`re.search` is more robust and it is recommended that you use it instead `re.match` when possible.

### Others 

2. Mutator methods are ugly in the sense 
that they do not return a reference to the original file.
Mutator methods usually returns None, which makes coding a little inconvenient.
Do not use the following style of code in Python.
    `obj = obj.mutable_method()`

4. if, for no parentheses which is different from popular programming languages
such as C/C++, Java, R, etc., but similar to MATLAB.

6. Python does not automatically return value (unlike R). 
It is quite often that an R use forget to return a value
in a user-defined function and get a "NoneType" related error.

9. if collection is a list of string, double, integer, etc. not changed
check this to make sure ...

        for item in collection:
            item ...

In general practice, it's probably not that beneficial. In fact, most Python style guides encourage programmers to place all imports at the beginning of the module file.

## Design

12. There is no constant variables in Python. 
If you need a constant variable in Python,
just define one and never change it.
It is suggested that you use UPPER case to stand for const variables.

1. The bottom-most package in Java should be a file in Python

    Do not use inner classes. 
    Just put classes in the same module
    By convention, things that start with _ are "private".
    It is OK to have "public variables"

2. Python does not support method/function overloading.

## numerical

1. By default Python does integer division. 
If you want to do float division, 
you can either cast (explicit or implicitly) integers to float numbers before division
or you can import the `division` module.

15. % modulus

static variable inside a function in python is tricky, 
one possible way is to pass an extra variable and use it to as a role of static variable


## Misc

1. A list in Python is mutable and cannot be use as keys for set or dict objects.
An alternative way is to convert lists to tuples using `tuple(a_list)`.
Notice that not all tuples can used as keys for set and dict objects.
The fundamental requirement is that keys for set and dict objects must be immutable,
so a tuple must contain immutable object in order to be hashable.

## Numpy

1. numpy.unique

2. numpy.loadtxt

3. the array object in numpy has a `tolist` method.

## IO

write a list of tuple of numbers into a file

        open('rr.txt', "w").writelines(["%s %s\n" % e for e in rr])

## File System

1. You can get rid of file extension use the following code.

    os.path.splitext(filename)[0]

2. `os.mkdir` acts like `mkdir` in Linux and `os.makedirs` acts like `mkdir -p` in Linux.
Both of them throw an exception if the file already exists.

1. use execfile(open(filename).read()) to source a file,
variables defined in 'filename' are visible,
however, imported packages are invisible to the script running execfile

## Encoding
ord unichar
return ascii number of characters
chr return a string from a ascii number

## Data Structure

1. The list object in Python does not have a `find` method which is inconvenient.
To do a clean "find" in a list in Python,
you can use the following style of code.

    if x in alist:
        index = alist.index(x) 

3. You can use `set(alist)` to get unique values of a list. 
If you want to return a list (rather than a set) of unique values,
you can use `list(set(alist))`.
Another way is to use the method `numpy.unique`.

2. The difference between list and tuple in Python is that 
a list is mutable while a tuple is immutable.
So you can think of tuple as immutable version of list.
Tuples can be used in dictionarys in Python as keys 
while lists cannot.

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

## JSON
c=json.load(open('contractions.json'))
load -> from file
loads -> from str
c=json.loads(open('contractions.json').read())


1. use dir(module) to check methods in a module
help(method) to check help doc

## Environment Variable
os.getenv("HOME") only on Linux/Unix

the following works everywhere
from os.path import expanduser
home = expanduser("~")


use sys.exit(msg) to print error message and quit when error happens

```Python
type(obj).__name__
```

use `reload(module)` to reload a module.
In Python3, `imp.reload(module)`

## Containers
1. defaultdict
2. namedtuple
