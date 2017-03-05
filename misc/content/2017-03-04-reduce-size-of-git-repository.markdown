UUID: 8ce9e86f-a210-4196-a0a9-7b10343d50f5
Status: published
Date: 2017-03-04 12:17:54
Author: Ben Chuanlong Du
Slug: reduce-size-of-git-repository
Title: Reduce Size of Git Repository
Category: Software
Tags: software, Git, repository, size

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


git push --force


$ git gc --prune=now --aggressive

git filter-branch --prune-empty -d /dev/shm/scratch \
  --index-filter "git rm --cached -f --ignore-unmatch oops.iso" \
  --tag-name-filter cat -- --all
$ git reflog expire --expire=now --all
git filter-branch --tree-filter 'rm -f DVD-rip' HEAD

git filter-branch --force --index-filter 'git rm --cached -r --ignore-unmatch oops.iso' --prune-empty --tag-name-filter cat -- --all
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
git gc --aggressive --prune=now

#!/bin/bash
git checkout --orphan temp $1 # create a new branch without parent history
git commit -m "Truncated history" # create a first commit on this branch
git rebase --onto temp $1 master # now rebase the part of master branch that we want to keep onto this branch
git branch -D temp # delete the temp branch

The following 2 commands are optional - they keep your git repo in good shape.

git prune --progress # delete all the objects w/o references
git gc --aggressive # aggressively collect garbage; may take a lot of time on large repos

Or another way is just to remove the .git directory, 
reinitial a git repository and push to remote with the `--force` option.

http://stackoverflow.com/questions/2100907/how-to-remove-delete-a-large-file-from-commit-history-in-git-repository

http://blog.gbacon.com/2009/08/git-shrinking-subversion-import.html

http://stackoverflow.com/questions/2116778/reduce-git-repository-size

shadow clone using the depth option
git clone git://source.winehq.org/git/wine.git ~/wine-git --depth 1
