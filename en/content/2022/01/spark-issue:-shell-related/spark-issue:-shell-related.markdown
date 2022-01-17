Status: published
Date: 2022-01-15 14:23:15
Modified: 2022-01-17 12:33:30
Author: Benjamin Du
Slug: spark-issue:-shell-related
Title: Spark Issue: Shell Related
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, shell, command, big data 



## Symptom 1

> /bin/sh: hdfs: command not found

## Possible Causes of Symptom 1

The command `hdfs` is not on the search path. 

## Possible Solutions to Symptom 1

1. Use the full path to the command.
2. Configure the environment variable `PATH` before you use the command.
3. Find other alternatives to the command.


## Sympton 2 

> ... died with &lt;Signals.SIGILL: 4&gt;.

## Possible Causes of Symptom 2

1. The binary executable is compiled for a specific CPU type
    and cannot be run on the Spark cluster 
    since its nodes have a different CPU type.
    For example,
    if Rust application is compiled with `RUSTFLAGS="-C target-cpu=native"`
    then running it on machine with a different CPU type (even if the OS is the same) will cause this issue.  

## Possible Solutions to Symptom 1

1. Do NOT compile your binary executable for a specific CPU type
    so that it can run on different CPUs (with the same OS).
