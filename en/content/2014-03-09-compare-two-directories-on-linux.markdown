UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Author: Ben Chuanlong Du
Date: 2016-06-20 22:17:05
Slug: compare-two-directories-on-linux
Title: Compare Two Directories on Linux
Category: Linux
Tags: difference, directory, folder, Linux, md5sum, md5deep, diff, ssh

If the two directories are on the same machine, 
you can use the following command to find the difference between them. 
```sh
diff -qr d1 d2
```
It is a little bit tricky when the two directories are on different machines. 
You have to first calculate md5sums of files in the two directories recursively,
and then compare the md5sums.
To calculate the md5sums of files in a directory recursively 
and output the results into a file "j.txt", 
you can use the following command.
```sh
md5deep -r path_to_directory > j.txt
```
Once you have the md5sums for the 2 directories calculated 
and outputed into files (e.g., "j.txt") on the 2 machines,
you can then compare the contents of the 2 files on the 2 machines.
One way to achieve this is to run the following command on one of the machines.
```sh
ssh -p port user_name@the_other_server cat j.txt | diff j.txt -
```
You can also copy (using `rsync` or `scp`) the output file on one machine to the other machine 
and then compare locally using `diff`.
