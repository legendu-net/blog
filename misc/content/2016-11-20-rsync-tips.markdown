UUID: 77915c23-f445-46cc-b630-4ffc7812020b
Status: published
Date: 2016-11-20 11:56:41
Author: Ben Chuanlong Du
Slug: rsync-tips
Title: rsync Tips
Category: Linux
Tags: Linux, copy, synchronization, file system, filesystem, rsync

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Tricks & Traps 

The command `rsync -avh src_dir des_dir` synchronizes the whole directory `src_dir` 
into the destination directory `des_dir`
while `rsync -avh src_dir/ des_dir` synchronizes the contents 
(sub-files and sub-directories) of `src_dir`
into the destination directory `des_dir`.
However, 
one thing tricky is that `rsync -avh . des_dir` synchronizes the content 
(sub-files and sub-directories) of the current directory 
into the destination directory `des_dir`.
This is especially tricky if you programmally get the source directory that you want to synchronize.
Here are a few good practices to follow.

1. Convert programmally generated path (for use in `rsync`) into its absolute form.

2. Always use the form `rsync -avh src_dir/ des_dir` instead of the form `rsync -avh src_dir des_dir`.

## Examples
```
rsync -e "ssh -o StrictHostKeyChecking=no" ...
```

```
rsync -e "ssh -p 323" ...
```

```
#!/usr/bin/env bash

dir=$(dirname $(dirname "$0"))

rsync -avh \
    --progress \
    --delete \
    --exclude=.git/ \
    --exclude=target/ \
    --exclude=build/ \
    --exclude=analysis/ \
    --exclude=classes/ \
    --exclude=maven-archiver/ \
    --exclude=surefire-reports/ \
    --exclude=test-classes/ \
    --exclude=generated-sources/ \
    --exclude=generated-test-sources/ \
    --exclude=java.io.tmpdir/ \
    --exclude=out \
    $dir/ \
    $tiger:/workdir/users/
```

## Errors & Solutions

### error in protocol data stream (code 12)
It is probably because the remote diretory does not exist.

### References

[14 Practical examples of the rsync command](http://www.librebyte.net/en/gnulinux/14-practical-examples-of-the-rsync-command/)

https://askubuntu.com/questions/625085/rsync-over-ssh-error-in-protocol-data-stream-code-12-ssh-works

