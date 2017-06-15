UUID: c86f6efc-25f7-41da-87ab-7392b6dbb9f1
Status: published
Date: 2017-06-11 11:58:35
Author: Ben Chuanlong Du
Slug: use-environment-variable-in-docker-entrypoint
Title: Use Environment Variable in Docker Entrypoint
Category: Software
Tags: software, docker, shell form, exec form, environment variable

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


The exec form of ENTRYPOINT does not invoke a command shell, 
unlike the shell form. 
This means that normal shell processing does not happen for exec form. 
For example, 
`ENTRYPOINT [ "echo", "$HOME" ]` will not do variable substitution on `$HOME`.
If you want shell processing then either use the shell form 
or execute a shell directly,
e.g.,
`ENTRYPOINT [ "sh", "-c", "echo", "$HOME" ]`.
When using the exec form and executing a shell directly,
as in the case for the shell form,
it is the shell that is doing the environment variable expansion, not docker.
