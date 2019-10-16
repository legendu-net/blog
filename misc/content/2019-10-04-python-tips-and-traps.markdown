Status: published
Date: 2019-10-16 22:07:28
Author: Benjamin Du
Slug: python-tips-and-traps 
Title: Python Tips and Traps
Category: Programming
Tags: programming, Python, tricks, traps, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## Tricks and Traps

https://docs.python-guide.org/writing/gotchas/

https://stackoverflow.com/questions/101268/hidden-features-of-python


1. Use type annotation to make your code more readable and easier to understand.

2. Restrict the types of objects that your function/method can be applied to 
  and throw a (ValueError) exception when a wrong type is provided.
  This helps minimize surprisings.

3. AVOID returning objects of different types from a Python function/method.

4. Be CAREFULL about module name conflictions!
  It happens when there are more than one Python scripts with the same name on Python module search paths.
  This is often not a problem when developing Python packages due to absolute and relative import.
  However, 
  this issue can come up in a few situations and can be quite tricky for uers to figure out.
    a. If an user run a Python script whose parent directory contains a Python script with a name conflicting with other (official) Python modules,
      this issue will come up.
    b. An even trickier situation is when a Python script is piped to a Python interpreter directly. 
      According to [docs about sys.path](https://docs.python.org/3/library/sys.html#sys.path),
      `sys.path[0]` is initailized to be the empty string on the startup of Python in this situation 
      which directs Python to search modules in the current directly first.
      Since an user can run the command in any directory, 
      it is more likely for him/her to encounter the issue of conflicting module names. 
  If a Python script is never intended to be imported as a module, 
  one way to resolove the issue is to simply remove the first element from `sys.path`.
  ```
  import sys
  sys.path.pop(0)
  ```

2. Almost all modern programming languages follow the convention
  of not returnting anything (or in another words, retun void, None, etc.)
  from a mutator method so that you cannot chain on a mutator method.
  Functional programming languages enough chaining on methods
  as they often have immutable objects and the methods return new objects
  rather than changing the original objects.

2. Python functions (except lambda functions) do not automatically return value
  unlike functional programming languages.
  Forgotting a `return` statement is a common mistake in Python.

3. According to [Python Operator Precedence](https://docs.python.org/2/reference/expressions.html#operator-precedence),
  the ternary expression `if - else` has a very low precedence. 
  However, it has higher precedence than the tuple operator `,`.
  It is suggested that you always use parentheses to make the precedence clear 
  when you use the ternary expression in a complicated expression.
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


6. You cannot use `return` to return result from a generator function.
  Instead a `return` behaves like raising a StopIteration.
  Please see this [issue](https://stackoverflow.com/questions/26595895/return-and-yield-in-the-same-function)
  for more discussions.

7. `max(some_iterable, default=0)`

8. `itertools.chain(iter1, iter2, ...)`


## Referneces

- [Common Mistakes](http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)

- [Least Astonishment and The Mutble Default Argument](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)
