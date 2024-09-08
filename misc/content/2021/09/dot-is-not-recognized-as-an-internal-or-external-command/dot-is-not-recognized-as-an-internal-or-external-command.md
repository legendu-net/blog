Status: published
Date: 2021-09-05 12:51:24
Modified: 2021-09-05 12:51:24
Author: Benjamin Du
Slug: .-is-not-recognized-as-an-internal-or-external-command
Title: "." Is Not Recognized as An Internal or External Command
Category: Computer Science
Tags: Computer Science, programming, IPython, shell, Windows

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

I encountered the following error message 
when running a Windows command `!./osqueryi.exe .tables` in the IPython shell.

> In[15] >>> !./osqueryi.exe .tables  
> '.' is not recognized as an internal or external command,  
> operable program or batch file.

It turns out to be that the issue is caused by using `/` (instead of `\`) in a Windows shell.
As is known to all,
a Windows path uses `\` (instead of `/`) to delimit directories.
So the fix is very simple,
which is to replace `/` to `\`.

> In[16] >>> !.\osqueryi.exe .tables  