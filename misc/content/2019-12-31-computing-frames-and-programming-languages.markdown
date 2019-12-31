Status: published
Date: 2019-12-31 12:14:55
Author: Benjamin Du
Slug: computing-frames-and-programming-languages
Title: Computing Frames and Programming Languages
Category: Programming
Tags: programming, computing frameworks, programming languages, GPU, Python, Rust

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Multi-threading & Multi-Processing are not discussed here 
since they are relatively simple for scientific computing.

## Computing Frameworks
GPU
Python Distributed Computing Frameworks (Ray, Celery, Dask, Modin, etc.)
Spark
TPU

## Programming Languages
Python
Rust
JVM (Java, Scala, Kotlin)
C/C++

1. GPU is more accisible for average individual people.
    GPU still dominates deep learning right now.


2. Python Distributed Computing Frameworks (Ray, Modin, etc.)
    servers as a mid solution between GPU and Spark. 
    It can handle more data than GPU but less then Spark.
    Ray, Modin, etc is easier to use and maintain than Spark.

3. Even though there are many libraries making it possible to run deep learning on Spark,
    I still don't it is the right choice unless you have really large data that cannot be handle by other frameworks.
    There are rarely such situations.
    Real big data mostly occur in the ETL and preprocessing stage 
    rather than in the model training stage.

4. Python and Rust are good choices. 
    C is not productive. 
    C++ is too complicated.
    JVM-based languages are OK.
    Rust seems to have a bright future. 

5. As the development of Kubernetes, 
    there will be distributed computing frameworks that does not limit you into a specific languages. 
    Once that is a common situation,
    people will start shifting away from JVM languages and seek for better performance and easier to use solutions.
    Rust is a good language choice for performance 
    while Python is a good choice for glue-language that is easy to use.
