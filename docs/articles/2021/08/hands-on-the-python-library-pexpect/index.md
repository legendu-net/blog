---
title: Hands on the Python Library pexpect
created: '2021-08-03T18:14:35-07:00'
date: '2026-11-15T09:17:02-08:00'
authors:
  - bendu
label: hands-on-the-python-library-pexpect
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Python
  - pexpect
  - shell
  - command
  - terminal
---

## Tips and Traps

1. [pexpect.spawn.expect](https://pexpect.readthedocs.io/en/stable/api/pexpect.html#pexpect.spawn.expect)
   takes a pattern parameter.
   The pattern can be a StringType, EOF, a compiled re, or a list of any of those types.
   Notice that strings will be compiled to `re` types,
   so make sure to **use valid regular expression patterns** if you provide strings.
   For example,
   if password is asked after the prompt "password for user (not stored): ",
   passing the literal string `"password for user (not stored): "` won't work.
   You have to use something like `"password for user \(not stored\): "`
   or a simpler one `"password for user"` (if no ambiguity).

1. The command-line tool of some (e.g., network) applications might be slow to authenticate.
   If you use pexect to automate such a command-line tool,
   it is best to wait for sometime after sending password using `child.sendline(passwd)`.
   If the authentication has output on both success and failure,
   a smart way is to wait for the success or failure message to come out.

   ```
    child.expect(".*success_pattern.*|.*failure_pattern.*")
   ```

   If the the output of authentication contains the same keyword (e.g., dclong) on both success and failure,
   the pattern can be further simplified.

   ```
    child.expect(".*dclong.*")
   ```

1. The method `spawn.interact` gives control of the child process back to the interactive user
   (the human at the keyboard).
   Keystrokes are sent to the child process, and the stdout and stderr output of the child process is printed.
   This is extremely useful
   if you only want `pexpect` to hijack the child process for certain interactions.
   For example,
   if a command-line tool requires both a password and a hardware token for authentication,
   you can use `pexpect` to hijack the child process to enter password automatically
   and then give control of the child process back to the user to authenticate using hard token.

   ## References

- [pexpect @ GitHub](https://github.com/pexpect/pexpect)
- [使用popen和专用TTY Python运行交互式Bash](https://www.cnpython.com/qa/81808)
