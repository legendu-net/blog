UUID: 143f0a38-db55-4d60-9025-825983fefcfe
Status: published
Date: 2018-05-06 10:36:05
Author: Ben Chuanlong Du
Slug: httpd-tips
Title: Httpd Tips
Category: Software
Tags: software, httpd, HTTP, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. A directory must be executable by others in order to show up.
    Even if a directory show up,
    it does NOT mean that you can access it.
    It must be readable by others (at the same)
    so that it can be accessed using HTTP.

2. A directory/file must be readable by others on the host
    so that it can be accessed using HTTP,
    otherwise you will encounter error messages like the one below.

    > You don't have permission to access /wwwroot/somedir/ on this server.
