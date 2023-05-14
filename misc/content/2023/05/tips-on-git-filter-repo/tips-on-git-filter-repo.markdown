Status: published
Date: 2023-05-13 17:19:37
Modified: 2023-05-13 17:32:32
Author: Benjamin Du
Slug: tips-on-git-filter-repo
Title: Tips on Git-Filter-Repo
Category: Computer Science
Tags: Computer Science, programming, Git, filter-repo, git-filter-repo, strip, blobs

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu / Debian

wajig install git-filter-repo

## Example Usages

Note: git-filter-repo changes the history commits of a Git repository 
which is a dangerous operation.
Make sure you know what you are doing!

git filter-repo --strip-blobs-bigger-than 30M --force

## References

https://github.com/newren/git-filter-repo
