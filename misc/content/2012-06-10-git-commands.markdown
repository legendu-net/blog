UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-10-22 18:47:03
Author: Ben Chuanlong Du
Slug: git-commands
Title: Useful Git Commands
Category: Software
Tags: Git, repository, software, remote, version control, branching

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## General Git Tips

0. Do not work on the master branch directly. 
Use it purely as the production branch and merge mature features from other branches. 
You can apply one or more commits in a branch into other branches.
@TODO: give an example


1. Keep a production repository for using the your product and dev repository for developing.

1. Do not use symbolic links (to files outside the repository) in a Git repository.

2. Keep each commit small and specific. 
Do not mix different work together in a single commit. 
This make it convenient to apply part of your work to other branches. 

4. Git support several protocols: Git, SSH and HTTP. 
The Git protocol is preferred.
If you are behind a firewall and/or proxy server and cannot use the Git protocol,
you can try the HTTP protocol.
The HTTP protocol requires a password every time you access a private repository 
or you push to a repository (not matter private or not).

1. Do not amend public commits.

3. it seems to me that you should use many smaller files
rather than a single big file to avoid conflicts while working collaboratively.

## Git Syntax

### Repository

1. Add a Remote repository `origin` 
```Bash
git remote add origin git@github.com:dclong/jmail.git
```
`origin` is a popular default name for remote repositories,
however, you can use any valid name you like.

If you want to add a local bare repository, 
```Bash
git remote add origin path_to_repository_dir
```
7. Overwrite the remote repository `origin` using the master branch.
Notice that no patching is going on. 
The entire remote repository is overwritten by the master branch.
```Bash
git push origin master --force
```
10. Tells git default branches to use when pushing
```Bash
git push -u origin master
```
### Misc

2. Track all Files
```Bash
git add *
```
or 
```Bash
git add .
```
3. Add all modifed tracked files for commit
```Bash
git add *
```
or
```Bash
git add .
```
4. Remove a file but keep it in the local repository
```Bash
git rm --cached file_name
```
6. Init current directory as a bare repository (for local sharing purpose).
```Bash
git init --bare
```
Note that the directory must end with `.git` 
in order to be a sharing repository.

5. Other commands
```Bash
git cherry-pick
git push
```

### Branching

1. Show all branches.
```Bash
git branch -v
```
2. Checkout the branch "dev".
```Bash
git checkout dev
```
2. Checkout the last branch that you were on.
```Bash
git checkout -
```
3. Check out the remote branch named "dev".
```Bash
git fetch
git checkout dev
```
4. Create a branch named "dev" and switch to it.
```Bash
git checkout -b dev
```
5. Merge the branch named "hotfix" to the current branch
```Bash
git merge hotfix
```
6. Rename "old_branch" to "new_branch".
```Bash
git branch -m old_branch new_branch
```
7. Delete a fully merged branch.
```Bash
git branch -d branch_name
```
8. Force to delete a branch no matter it has been merged or not.
```Bash
git branch -D branch_name
```

### Patch

1. Show patches of a file
```Bash
git log -p file_name
```
6. Show diff of a staged file
```Bash
git diff -cache file_name
```
1. to find commits not on remote

```Bash
git log origin/master..
```
or 
```Bash
git cherry -v origin/master
```

2. `git log origin/master..HEAD` lists unpushed commits.
Uncommitted changes are not listed.
Notice the syntax `git log <since>..<until>` is similar to Bash `..` in list.

4. Switching branches carries uncommitted changes with you. 
Either commit first, run git checkout . to undo them, 
or run git stash before switching. 
(You can get your changes back with git stash apply)

### Tags

1. List your tags
```Bash
git tag
```
2. Create a tag
```Bash
git tag -a v0.1 -m "description about the tag"
```
3. Show a tag
```Bash
git show v0.1
```
4. Push tags to remote repository
```Bash
git push origin v0.1
```
5. Create a branch at a specific tag
```Bash
git checkout -b branch_name v0.1
```

### Configuration

16. Git in Windows automatically convert Linux/OSX line termiantors to Windows line terminators. 
To turn off auto line terminator conversion globally, use the following command.
```Bash
git config core.autocrlf false
```
You can also use the `dos2unix` command 
to change a Windows text file (with Windows line terminators) 
to a Unix/Linux file (with Unix/Linux line terminators).
The `unix2dos` does the opposite conversion.

17. Git track permissions of files by default. 
This can be an issue if you work on multiple operating systems.
You can use the following command to ask Git 
to ignore executable differences between the index and the working copy.

```Bash
git config --global core.fileMode false
```
For one-off ignoring, you use
```Bash
git -c core.fileMode false
```

20. Git does not colorize output automatically on some (old) Linux servers. 
You can use `git config --global color.ui auto` to force Git to colorize output. 

11. List all tracked files in a git repository
```Bash
git ls-tree --full-tree -r HEAD
```
1. Stash your work
```Bash
git stash
```

