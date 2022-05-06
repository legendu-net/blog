Status: published
Date: 2022-05-03 22:58:37
Modified: 2022-05-03 23:14:54
Author: Benjamin Du
Slug: absolute-or-relative-path-for-executables
Title: Absolute or Relative Path for Executables
Category: Computer Science
Tags: Computer Science, programming, executable, path, absolute, relative

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

When you call shell commands in your code,
a nature question to ask is whether you should the absolute or a relative path (command).
Both ways have their advantages and disadvantages.


## Path of Executables

1. Use the absolute path if the executable has a standard location.
2. If an executable does not have a standard location,
    use command instead.
    If the executable is not always on the search path,
    provide an option for user to specify the path of the command.

## Paths in Shell Commands

If you call a shell command from another language (e.g., Python)
and the shell command takes a path as parameter,
in most situations you want to use an absolute path to avoid potential issues.

