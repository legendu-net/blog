Status: published
Date: 2015-05-02 21:55:44
Author: Ben Chuanlong Du
Slug: python-pandas-tips
Title: Python pandas Tips
Category: Computer Science
Tags: programming, Python, pandas, DataFrame, data frame, tips
Modified: 2023-07-18 17:55:52

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## `pandas` Settings

Please refer to
[Options for the pandas Package in Python](http://www.legendu.net/misc/blog/options-pandas-python/)
for discussions.

## Tips and Traps

1. Do NOT use `DataFrame.iterrows`. 
    Please refer to the 
    [issue](https://github.com/pandas-dev/pandas/issues/43874)
    for discussions on it shouldn't be used.
    There are lots of alternative
    `DataFrame.to_dict()`, `DataFrame.to_records()`, `DataFrame.itertuples()` and `DataFrame.to_numpy()` 
    are all much faster alternatives.
    For a detailed comparison of speed of different ways of iterating rows of a pandas DataFrame,
    please refer to
    [Here’s the most efficient way to iterate through your Pandas Dataframe](https://towardsdatascience.com/heres-the-most-efficient-way-to-iterate-through-your-pandas-dataframe-4dad88ac92ee)
    .
    According to the benchmark in the article,
    `DataFrame.to_dict("records")` is the most efficient way
    and is thus preferred.

2. Avoid using column/element names that conflict with pandas internal member names,
    otherwise you will not be able to access the column/element using the dot syntax.
    For example,
    if you name a column `size`
    you can to refer to the column as `df.size`
    because `df.size` is a method that returns the number of element in the DataFrame.
    The issue is that you won't be able to remember all members of the DataFrame/Series class. 
    One simple solution is to **always suffix column/element names in a DataFrame/Series with a underscore (`_`)**. 
    If you cannot follow (or don't like) this suggestion,
    then it is suggested that you always access columns of a DataFrame and element of a Series
    using the syntax `df["col_name"]` and `series["element_name"]` 
    (which is more verbose than the dot syntax of course).

2. Be careful when you use integers as column names or indexes
    as it might affect the way of slicing.
    It is suggested that you never use integers as column names or indexes.
    If you do not have a natural meaningful way for the index,
    it is recommended that you use "r1", "r2", ... as the index.

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

[Frequently Asked Questions (FAQ)](https://pandas.pydata.org/pandas-docs/stable/user_guide/gotchas.html)

https://www.youtube.com/watch?v=tcRGa2soc-c
