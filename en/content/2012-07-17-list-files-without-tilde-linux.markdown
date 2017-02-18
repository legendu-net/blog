UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-04-12 00:19:00
Slug: list-files-without-tilde-linux
Author: Ben Chuanlong Du
Title: Advanced Use of "ls" in Linux
Category: Linux
Tags: Linux, ls, shell

## Ignore Backup Files

When you use the `ls` command to list files in a directory 
the backup files (whose names end with `~`) also show up, 
which is often annoying. 
You can use the following command to ignore backup files when listing contents of a directory.
```bash
ls -B
```
Or you can use 
```bash
ls --ignore=*~
```

## List Contents of a Directory with the Directory Name Prefixed

When you list the contents of a directory (e.g., `raw`) using the following command.
```bash
ls raw
```
the directory name `raw` is not prefixed to the returned/printed contents.
You can of course concatenate the directory name `raw` to each of its subdirectory/subfile manually,
however, 
a more convenient way is to use the the following command.
```bash
ls raw/* 
```

## List Only Subdirectories
You can use the following command to list directories only in the current directory.
```bash
ls -d ./* 
```

## List Hidden Files and Directories
```language
ls -d .*
```
