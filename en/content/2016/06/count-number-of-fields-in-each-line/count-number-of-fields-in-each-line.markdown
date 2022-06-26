Status: published
Date: 2016-06-13 23:08:03
Modified: 2021-09-26 21:56:40
Author: Ben Chuanlong Du
Slug: count-number-of-fields-in-each-line
Title: Count Number of Fields in Each Line
Category: Computer Science
Tags: programming, data manipulation, R, awk, number, field, text file

Sometimes,
a structured text file might be malformatted.
A simple way to verify it is to count the number of fields in each line.

## Using awk

You can count the number of fields in each line 
using the following awk command.
Unfortunately, 
awk does not take escaped characters into consideration.
So this only works for simple formatted (without escaped characters) text files.

    :::bash
    awk '{print NF}' filename

## Using R

There is a function named `count.field` in R.

