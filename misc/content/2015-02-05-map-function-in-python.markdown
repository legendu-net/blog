UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-02-05 22:58:56
Author: Ben Chuanlong Du
Slug: map-function-in-python
Title: Map Function in Python
Category: Programming
Tags: programming, Python, map, functional programming, reduce, apply

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**



the map ↔ *apply (R)
but it seems to me that map is not need as we have 

[f(e) for e in aList]   this is a much better approach
map(f, sequence1, sequence2)

is mostly equivalent to:

[f(x1, x2) for x1, x2 in zip(sequence1, sequence2)]


---------------------------------------------------
similar for filter

>>> def myreduce(fnc, seq):
	tally = seq[0]
	for next in seq[1:]:
		tally = fnc(tally, next)
	return tally

>>> myreduce( (lambda x, y: x * y), [1, 2, 3, 4])
24
>>> myreduce( (lambda x, y: x / y), [1, 2, 3, 4])
0.041666666666666664
>>> 

>>> import functools, operator
>>> functools.reduce(operator.add, L)
'Testing shows the presence, not the absence of bugs'
>>> 

>>> ''.join(L)
'Testing shows the presence, not the absence of bugs'

reduce sometimes might be helpful 

http://briansimulator.org/
https://pypi.python.org/pypi/brian/
