Status: published
Date: 2019-08-18 00:46:22
Author: Ben Chuanlong Du
Slug: python-pandas-tips
Title: Python pandas Tips
Category: Programming
Tags: programming, Python, pandas, DataFrame, data frame, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## `pandas` Settings
```Python
import pandas as pd
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_colwidth', 100)
```

## Tips

1. Avoid column names that conflict with pandas internal member names,
    otherwise you will not be able to access the column using the dot syntax.
    For example,
    if you name a column `size`
    you can to refer to the column as `df.size`
    because `df.size` is a method that returns the number of element in the DataFrame.

2. Be careful when you use integers as column names or indexes
    as it might affect the way of slicing.
    It is suggested that you never use integers as column names or indexes.
    If you do not have a natural meaningful way for the index,
    it is recommended that you use "r1", "r2", ... as the index.

3. `pandas.series.str.replace` supports regular expression.

4. `pandas` also support time delta, you should compare with the MonthDelta module

5. `pandas` keeps the underlying precision (instead of the display precision)
    while reading Excels files.
    However,
    be aware that pandas displays 7 significant digits by default.

6. Label-based slicing is inclusive
    as it is not clear what "pass by 1" means for label-based slicing.

7. You can apply a function on a row/column using the method `DataFrame.apply`.
    However, 
    it is suggested that you use list compression as much as possible for the following reasons.
    - A list comprehension is more flexible as lambda is limited (1-line without comma) in Python.
    - A list comprehension is faster than `DataFrame.apply`, generally speaking.

## Questions

1. get the row where index is NaN?

4. it is strange that sometimes series of booleans cannot be used for slicing?

5. what operations cause a data frame to sort its columns and/or rows?

6. difference between merge and join?

7. it seems that DataFrame.str.replace and Series.str.replace
    use regular expression by default.
    Is there any way to perform literal string substitution
    like what the `fixed=True` options does for regular expression related functions in R?

## References 

https://www.youtube.com/watch?v=tcRGa2soc-c