Status: published
Date: 2021-09-05 13:00:45
Modified: 2021-09-06 14:08:09
Author: Benjamin Du
Slug: tips-on-winget
Title: Tips on winget
Category: Computer Science
Tags: Computer Science, OS, Windows, winget

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You can search for packages on https://winget.run/.

    :::bash
    winget search grep
    winget install grep

Notice that winget does not handle the PATH environment 
if you install a command-line tool.
You have to do it yourself.