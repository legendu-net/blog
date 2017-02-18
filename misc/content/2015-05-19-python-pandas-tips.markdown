UUID: f3694b1d-6b99-49bf-98de-7a54b99f88c9
Status: published
Date: 2015-06-20 21:07:30
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

Python pandas settings
```Python
import pandas as pd
pd.set_option('display.height', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 100)
```

1. avoid naming a column "size" 
as you will not be able to access the column using dot.
`df.size` show the number of element in the DataFrame.

2. be careful when you use integers as column names or indexes
this might affect the way of slicing
It is suggested that you never use integer as column names or indexes.
If you do not have a natural meaningful way for the index,
it is recommended that you use "r1", "r2", ... as the index.

3. pandas.series.str.replace: regular expression manipulation supported!

4. pandas also support time delta, you should compare with the MonthDelta module

5. pandas keeps the precision while reading excels files but just be careful 
that pandas display 7 significant digits by default ...

6. label-based slicing is inclusive as it is not clear what "pass by 1" means for label-based slicing
Integer index based slicing is passing by 1 as usual
Notice that `.ix` is mixed slicing, 
so its slicing can be both inclusive and exclusive 
depending on whether you are using integer-based slicing or label-based scling.

7. some operations on data frame will sort the index and column names.
It is better to use acending indexes to avoid surprise.
