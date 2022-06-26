Status: published
Date: 2022-06-04 12:09:03
Modified: 2022-06-04 12:13:59
Author: Benjamin Du
Slug: extended-globbing-in-bash
Title: Extended Globbing in Bash
Category: Computer Science
Tags: Computer Science, programming, bash, shell, glob, globbing, extended

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Enable Extended Globbing

    :::bash
    shopt -s extglob

Or you can run bash with the option `-O extglob`.

    :::bash
    /bin/bash -O extglob -c "your command to run"

## Set Shell to be Bash with Extended Globbing in Docker

    :::bash
    SHELL ["/bin/bash", "-O", "extglob", "-c"]

## References

[Bash Extended Globbing](https://www.linuxjournal.com/content/bash-extended-globbing)

