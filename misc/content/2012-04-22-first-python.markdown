UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2014-09-27 23:30:23
Slug: first-python
Author: Ben Chuanlong Du
Title: Easier Blogging Using Python Program
Category: Programming
Tags: programming, blog, Jekyll, Python, Ruby

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

**
As the program has been modified a lot, 
this post need to be updated.
**

I switched my blog from Wordpress to Github a few months ago. 
Github is a general purpose repository. 
The biggest advantage to reposit your blog on Github is that 
it allows you to work offline without the hassle to login to your online account. 

Jekyll Bootstrap use Ruby rake to help make posts and pages. 
For some reason I cannot use it on my laptop. 
I am a newbie to Linux. 
I have spent much time figuring out things in Linux, 
and I hessitate to dig into every problem I come accross. 
To automatically generate a post/page template sounds like a very simple job. 
A person with very basic programming skill can do this. 
Most programming languges (C/C++, Java, MATLAB, Mathmatica, R) 
I know well focus on scientific computing, and among them R seems to be the one suitable for this job. 
However, I found that Python is extremely popular among Linux users. 
Many script in Linux are written by python. 
Plus the fact that I want to use Jython as a dynamic interpreter for Java, 
I decide to force myself to write code in Python, 
because this is best way that one can master a programming language. 
I wrote a Python modules ["epost.py"]({{ site.url }}/epost.py). 
This module allows you to manipulate a post easily. 
If no post with the specified pattern exists, 
it prompt for creating a new post.
If a post with the specifed pattern exists, 
it ask for a bash command that operate the file.
You can use `%` to stand for the path of the post 
and `#` to denote the prefix (.../yyyy-mm-dd-) of the path of the post, 
which makes things convenient.
The module "epost.py" is directly runnable. 
For example to edit, rename, or create a post with paritial name "abcd",
you can type in the following in terminal.

    ./epost abcd

If no post with name containing "abcd" exists, it asks you whether to create a
new post with name "yyyy-mm-dd-abcd", where "yyyy-mm-dd" is the current date.
If a post with name containing "abcd" exists, it asks you for a bash command
operating the post. You can use `%` to stand for the path of the post. For
example, if you want to edit the post using vim, you can type in `vim %`.
You can also rename the post easily with "#" denoting the prefix of the path 
of the post. For example, to rename the post to "yyyy-mm-dd-ABCD.md", 
you can type in command `mv % #ABCD` or `mv % #ABCD.md`. 
The program takes care of the file extension, so you need not to worry about whether to include it or not.

