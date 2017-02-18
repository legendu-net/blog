UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-04-07 20:35:33
Author: Ben Chuanlong Du
Slug: matlab-tips
Title: MATLAB Tips
Category: Programming
Tags: programming, tips, MATLAB 

Things on this page are 
fragmentary and immature notes/thoughts of the author.
It is not meant to readers 
but rather for convenient reference of the author and future improvement.



5. MATLAB uses float computing by default. 
`3/5` return 0.6 in MATLAB instead of 0 
as will be returned in some other programming languages (e.g., Python).

7. to get size of an object, md = whos(obj); md.bytes

6. do we have `x *= 2` in matlab, if not, use ultisnips to do it!!! and python, R, Mathematica, bash, etc.


1. nohup matlab -nodesktop -nosplash -r "run('./RunSimulation10.m');quit;"

2. num2str, numbers cannot be used as string directly

3. Subscript indices must either be real positive integers or logicals. you confused matlab with your variable and the built-in function size!!!

4. dlmwrite 'precision', edit the corresponding post

1. You can use `warning('off','all')` to supress warnings in MATLAB.

1. fitlm support the table data structure in R2015a and after but it only support matrix and dataset in R2013b and before.

2. matlab's strength is for engineering uses, it is a piece of shit for statistical purposes ... stay away from matlab and live longer!

3. matlab about array of string is too stupid, you need to use cell array of string ...

## Statistics

4. Use categorical to create a categorical array from data with values from a finite set of discrete categories. 
To group numeric data into categories, use discretize.

## Data Structure

1. Table in matlab is the equivalent data structure of data frame in R.

2. table(c1, c2) to join tables/cells/varaibles horizontally 

3. You can use the function `readtable` to read the content of a file into a table.
