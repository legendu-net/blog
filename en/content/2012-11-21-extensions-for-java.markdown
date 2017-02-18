UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-02-20 10:37:03
Slug: extensions-for-java
Author: Ben Chuanlong Du
Category: Programming
Title: Extensions for Java
Tags: JNI, JNA, extension, Java, programming


[Here](https://bitbucket.org/dclong/java_learn/src/1d6428249cae93dc7ad6ca61fa93479dcc7390fc/src/study/access?at=master) are some code examples for the following topics.
## Java Native Interface

1. You can call native code (typically C, C++ or Fortran) in Java using the Java Native Interface (JNI). 
For the code implemented in native code, 
you must use keyword "native" to tell the compiler that it is implemented outside Java. 
Also, 
you should surround the Java code which load the compile native code in `static{}` 
(i.e. static initialized). 
This will get executed when Java load the class. 
For more information, please refer to Calling C library Routines from Java.

## Java Native Access

1. Java Native Access is a more convenient way to call native code than the Java Native Interface.
It is based on Java Native Interface.


