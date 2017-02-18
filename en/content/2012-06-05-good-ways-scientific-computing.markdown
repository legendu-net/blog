UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Good Ways to Do Scientific Computing
Date: 2012-06-05 00:00:00
Tags: Research
Category: Research
Slug: good-ways-scientific-computing
Author: Ben Chuanlong Du

1. Save important intermediate results. It can happen that you did right from
step A to B, but messed up from step B to C. If you save the intermediate
results that step B to C needs, you can resume the work faster. 

2. Use good and consistent way to name objects if you use scripting language
(e.g., R). If your proeject is a big one and takes a long time to do, you had
better plan a continuable way for your work. You do not want to come back to
your project several days later and get confused about work you have done
before. When you name files storing results, a clear name is prefer though it is
long. Or at least you should organize in hierarchical directories. 
Another way to keep your work clear, is to organize object belong a a similar
work together. For example, if you have to do work A and B, both of which are
related to many datasets and objects. You can create two lists (or similar data
structure) and put all datasets and objects related to A into one list and datasets
and objects related to B into the other one. In this way, you keep the workspace
clean, which makes you productive. 

3. Writing help documents for functions you wrote and keep a "readme" file for you project. 
You can put work you did, 
work you have to do and ideas related to the project into the "readme" document.

4. Use seeds when you generating random numbers. This helps reproducing work you
did before. 

5. Test your simulation using a faily small dataset or complexity degree to estimate 
the time needed to run bigger simulations. 
If a simulation takes a very long time to run, it is a good idea to  
continuingly update the progress of the simulation after, say, a fixed number of iterations. 
Printing time and summary of results based on currently progress is alwasy benefitial. 


