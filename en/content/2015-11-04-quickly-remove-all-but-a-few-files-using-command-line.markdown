UUID: 88fb25ee-a2e6-4487-8ab9-76246309d1d4
Status: published
Date: 2016-07-09 22:42:56
Author: Ben Chuanlong Du
Slug: quickly-remove-all-but-a-few-files-using-command-line
Title: Quickly Remove All but a Few Files Using Command Line
Category: Linux
Tags: Linux, remove, cli, command-line, command line, file system, filesystem

You can use the following command to display `.txt` and `.csv` files and ignore other files.
```sh
ls (*.txt|*.csv)
```
And similarly, 
you can remove all files but `.txt` and `.csv` files using the following command. 
```sh
rm (*.txt|*.csv)
```
An alternative way is to move the files to the parent directory or a temp dir, 
remove all left files,
and then move thme back to the current directory.
