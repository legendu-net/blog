UUID: 419c2341-e8fb-4233-b470-5a7443b5ec87
Status: published
Date: 2016-11-20 12:25:19
Author: Ben Chuanlong Du
Slug: git-performance
Title: Git Performance
Category: Software
Tags: programming, Git, version control

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

- [fatal: early EOF fatal: index-pack failed](http://stackoverflow.com/questions/21277806/fatal-early-eof-fatal-index-pack-failed)
- [Retrieve specific commit from a remote Git repository](http://stackoverflow.com/questions/14872486/retrieve-specific-commit-from-a-remote-git-repository/30701724#30701724)
- [Convert shallow clone to full clone](http://stackoverflow.com/questions/6802145/convert-shallow-clone-to-full-clone/6802238#6802238)
- [Git Fails On Large Files](http://blog.dinaburg.org/2013/07/git-fails-on-large-files.html)

fatal: early EOF fatal: index-pack failed

Git fails on repository containing large files. 
## Possible Reasons
1. Compression runs of memory
2. Poor network connection

## Possible Solutions
1. turn off compression
```bash
git config --global core.compression 0
```
3. try at a location with better network connection
4. Do a shallow clone.
```bash
git clone --depth 1 repos_url
```
This is equivalent to trieving the latest commit. 
2. repack remote 
6. use Git submodules

1. use 
```bash
git clone --depth 1 repos_url
```
You can get the full clone later by running either of the following two commands.
```bash
git fetch --unshallow
# or
git fetch --depth 1000000
```
This is perfectly safe with Git 2.5+. 
2. retrieve single commit
3. 
