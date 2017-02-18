UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Containers in Popular Programming Languages
Date: 2012-05-22 00:00:00
Tags: Mathematica, generic, C++, list, programming, Julia, Python, hash, D, array, Java, Ruby, R, vector, VB/VB.net, MATLAB
Category: Programming
Slug: containers-summary-in-popular-languages
Author: Ben Chuanlong Du

Here is a brief summary about containers in programming languages such as 
C/C++, D, Java, VB/VB.net, MATLAB, Mathmatica, R, Julia, Python and Ruby. 
All of these programming languages defined support containers. 
Some of the languages distinguish different types of containers 
and have many different kind of containers while some of them 
have more general definition thus have fewer types of containers. 
For example, 
R distinguishs array and list while in some other programming
languages (e.g., Mathematica, Python and Ruby), 
array and list are the same thing. 
In C/C++, D and Java, 
array is one of the basic data structure, 
and a list can be based on either arrays or linked-list. 
This is a trade-off. 
If a language distingusish different types of containers, 
it is usually faster but at the cost of inconvenience, verse versa.
All of these programming I list here lanuages support different types of containers. 
Elements in a container must be of the same type, 
however, 
using a top level type can make containers support differnt runtime/actual types of elements. 
Some lanaguges (e.g., Mathmatica, Python and Ruby)
make this default with all their containers while some languages 
(e.g., R and Mathematica) distinguish between different types of containers. 
The most popular way for accessing elements in a container (mostly array) is to use "[]", 
e.g., 
C/C++, D, Java, R, Julia and Python all support this operator for accessing elements of containers; 
a less popular way for accessing elements in a container 
(array, list, dictionary and so on) 
is to use "{}", 
e.g., Mathematica, Python and ? (other languages ...?); 
another way for slicing containers is to use "()" 
e.g., MATLAB, VB/VB.net and C++ via `operator()`. 

The concept of arrays is sort of similar in C/C++, D, Java, VB/VB.net, MATLAB,
Julia and R. The type of elements of array in these languages must be of the same
type unless you declare an array with super type of types you want to use in
it. All of these languages support dynamic array except C in which you must
maintain one by yourself. Among them, R and MATLAB use 1-based arrays while
others use 0-based arrays. An exception is that VB allows `k`-based arrays
where `k` is an arbitray integer. I am not sure whether VB.net allows this or
not.

The concept of arrays is sort of similar in Mathematica, Python and Ruby.
Arrays in these languages are all dynamic, and elements do not have to be of
the same type (or more actually arrays in these languages have the super type
of all types). An element in an array can be an array. This concept of 2-d
array is similar to the concept of 2-d array in Java. 
Lists in R and cells and struct arrays in MATLAB are sort of similar to arrays
in these languages. 

Notice that some languages support hash tables. In D it is called
association arrays; in python it is called dictionaries; in Ruby it is either
called hashes or arrays whose subscript is not necessarily ordered or numeric.
Noticed that a hash table cannot be sorted. If you do want to sort a hash
table, you have to use a differnt data structure (e.g., the sort method of a
hash table in Ruby changes the data structure to a 2-d array). 

The following is a brief summary about codes on containers in these languages. 

## C/C++
//create array 
