UUID: e23473cf-f47a-4ffc-af77-c1caf7f2fcad
Status: published
Date: 2017-08-26 21:45:58
Author: Ben Chuanlong Du
Slug: rjava-failed-to-load-rjava.so
Title: Rjava Failed to Load Rjava.So
Category: Programming
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

rJava failed to load rJava.so and libjvm.so

Reconfigure Java for R using the command below resolves the issue.

    sudo R CMD javareconf
