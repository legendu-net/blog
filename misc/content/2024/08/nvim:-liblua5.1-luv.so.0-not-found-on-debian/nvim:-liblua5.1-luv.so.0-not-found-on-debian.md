Status: published
Date: 2024-08-26 17:49:56
Modified: 2024-08-26 17:55:56
Author: Benjamin Du
Slug: nvim:-liblua5.1-luv.so.0-not-found-on-debian
Title: NeoVim: liblua5.1-luv.so.0 Not Found on Debian
Category: Computer Science
Tags: Computer Science, programming

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

`liblua5.1-luv.so.0` is not present under `/lib/x86_64-linux-gnu/`.
Manually make a symbolic link from 
`liblua5.1-luv.so.1.0.0` resolved the problem.
