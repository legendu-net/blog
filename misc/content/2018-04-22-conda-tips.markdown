Status: published
Date: 2018-04-22 09:09:46
Author: Ben Chuanlong Du
Slug: conda-tips
Title: Conda Tips
Category: Programming
Tags: programming, Python, conda, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. conda and executables installed by conda might not be able to run by sudo directly. 
    If this happends, 
    use the full path of the executable
    or add the option `-E "PATH=$PATH"` to sudo.
    
        sudo -E env "PATH=$PATH" <command> [arguments]

2. By defaut, conda installs things into /opt/conda.

## Administering a multi-user conda installation

https://conda.io/docs/user-guide/configuration/admin-multi-user-install.html

## References

https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html
