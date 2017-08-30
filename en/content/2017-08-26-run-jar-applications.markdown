UUID: cb0a319b-e363-4905-867b-bc04df8a303b
Status: published
Date: 2017-08-26 09:34:53
Author: Ben Chuanlong Du
Slug: run-jar-applications
Title: Run Jar Applications
Category: Programming
Tags: programming, Java, JAR, main

If there is only 1 class with a main method
or if there is a Main-Class defined for the JAR,
you can use the following command to run the application.

    java -jar app.jar

If you there are multiple classes with main methods in the JAR, 
you can execute any of them using the commands below. 

    java -cp app.jar com.mycomp.myproj.AnotherClassWithMainMethod
