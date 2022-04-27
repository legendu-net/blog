Status: published
Date: 2021-05-02 12:31:26
Author: Benjamin Du
Slug: git-implementations-and-bindings-in-python
Title: Git Implementations and Bindings in Python
Category: Computer Science
Tags: Computer Science, programming, Git, Python, Dulwich, pygit2, GitPython 
Modified: 2022-04-27 09:49:43

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are multiple Git implementations/bindings in Python:
[pygit2](https://github.com/libgit2/pygit2),
[Dulwich](https://github.com/dulwich/dulwich)
and
[GitPython](https://github.com/gitpython-developers/GitPython)
.

Below is a simple comparison of the 3 packages.

|                | pygit2              | dulwich       | GitPython                   |
|----------------|---------------------|---------------|-----------------------------|
| Implementation | bindings to libgit2 | pure Python   | bindings to the git command |
| License        | GPLv2               | Apache, GPLv2 | BSD 3                       |
| Feature        | complete            | incomplete    | complete                    |

pygit2 is preferred if the GPLv2 license is not an issue,
otherwise GitPython is preferred.

## References 

- [Hands on Dulwich](http://www.legendu.net/misc/blog/hands-on-Dulwich)
- [Hands on GitPython](http://www.legendu.net/misc/blog/hands-on-GitPython)

