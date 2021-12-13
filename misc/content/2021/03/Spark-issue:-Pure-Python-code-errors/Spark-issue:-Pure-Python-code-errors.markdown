Status: published
Date: 2021-03-22 10:18:22
Author: Benjamin Du
Slug: Spark-issue:-Pure-Python-code-errors
Title: Spark Issue: Pure Python Code Errors
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, big data, Spark issue, Python, error, exception
Modified: 2021-12-12 21:31:54

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

This post collects some typical pure Python errors in PySpark applications.

## Symptom 1
> object has no attribute

## Solution 1
Fix the attribute name.


## Symptom 2
> No such file or directory

## Solution 2
Correct the path to the file/directory or upload the file using `--file` of the spark-submit command.


## Symptom 3
> error: the following arguments are required

## Solution 3
Add the required arguments to the command invoking your Python script. 


## Symptom 4
> error: unrecognized arguments

## Solution 4
Correct tthe argument name or remove non-exist arguments from the command invoking your Python script.


## Symptom 5
> error: argument
## Solution 5


## Symptom 6
> ModuleNotFoundError: No module named

## Solution 6
Fix typo in the module name or install missing modules.

## Symptom 7
> SyntaxError: invalid syntax

## Solution 7
Fix syntax error in your Python script.

## Symptom 8
> NameError: name .* is not defined

## Solution 8
Fix typo in variable/function name or import/define it.

## Symptom 9

> Runtimeerror: Result vector of pandas_udf was not the required length: expected 1, got 101456

## Cause 9
The length of the result returned by the pandas UDF does not match the length of its input series. 
Notice that if your pandas UDF parses the stdout of a command,
it is possible that extra prints to the stdout was introduced which breaks the parsing. 

## Solution 9
Fix issue in the pandas UDF. 

## Symptom 10

> Error: b"error: Found argument '--id1-path' which wasn't expected, or isn't valid in this context ...

## Cause 10

The argument `--id1-path` is not a valid argument to the command called by Python.

## Solution 10 

Fix the non-valide argument of the command called by Python. 

## Symptom 11

> subprocess.CalledProcessError: Command './pineapple test --id1-path id1.txt' returned non-zero exit status 1. 

## Cause 11

The command invoked by Python failed. 

## Solution 11

Figure out why the command invoked by Python failed and fix the issue. 
 
## Symptom 12 

> TypeError: object of type 'generator' has no len()

## Cause 12

Calling the function `len` on a generator.

## Solution 12

Assume `it` is an iterator 
(a generator is a special case of iterator)
,
use `sum(1 for _ in it)`
instead of `len(it)`.
.
Of course,
you have to make sure that the iterator is finite.

## Symptom 13
> pyarrow.lib.ArrowInvalid: Could not convert ... with type function: tried to convert to int

## Cause 13

The Python object (e.g., a function object) cannot be converted to int in PyArrow.

## Solution 13

Fix the issue in the Python code.
For example,
did you use a function without passing parameters to it?

## Symptom 14 
> pyarrow.lib.ArrowInvalid: Value 2147483651 too large to fit in C integer type

## Cause 14
Cast a long integer (64 bits) in Python to int (32 bits) in PyArrow.

## Solution 14
Use long integer instead for the return type in pandas UDF.

