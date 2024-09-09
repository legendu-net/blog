Status: published
Date: 2022-11-10 20:31:49
Modified: 2024-06-17 11:28:39
Author: Benjamin Du
Slug: mercurial-for-git-users
Title: Mercurial for Git Users
Category: Computer Science
Tags: Computer Science, programming, mercurial, git, hg

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Mercurial and Git Equivalent Commands](https://hyperpolyglot.org/version-control)

[Mercurial source code management system](https://www.mercurial-scm.org/doc/hg.1.html)

The codes used to show the status of files are:

    M = modified
    A = added
    R = removed
    C = clean
    ! = missing (deleted by non-hg command, but still tracked)
    ? = not tracked
    I = ignored
      = origin of the previous file (with --copies)

Remove a missing file from tracking.

    :::bash
    hg remove -A

## Some Useful Command

List changed files with their status.
    
    :::bash
    hg pstatus

List changed files without status.

    :::bash
    hg pstatus --no-status
    
## .hgignore

https://wiki.mercurial-scm.org/.hgignore

## References

- [Mercurial for Git Users (and vice versa)](https://www.rath.org/mercurial-for-git-users-and-vice-versa.html)


- [Mercurial source code management system](https://www.mercurial-scm.org/doc/hg.1.html)
