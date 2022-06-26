Status: published
Date: 2019-04-28 11:53:55
Author: Benjamin Du
Slug: regular-expression-in-bash
Title: Regular Expression in Bash
Category: Computer Science
Tags: programming, Bash, regular expression, regex
Modified: 2021-10-27 20:23:31


It is suggested that you **use Python script instead of Shell script** as much as possible.
If you do have to stick with Shell script,
you can use `=~` for regular expression matching in Bash.
This make Bash syntax extremely flexible and powerful.
For example, 
you can match multiple strings using regular expression.
```
if [[ value =~ ^(v1|v2|v3)$ ]]; then
    ...
fi
```
