Status: published
Date: 2023-02-02 13:58:33
Modified: 2023-03-05 22:18:43
Author: Benjamin Du
Slug: tips-on-tar
Title: Tips on the tar Command in Linux
Category: Computer Science
Tags: Computer Science, programming, tar, compress, decompress

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

--strip-components


--exclude

tar --strip-components=1 -C /usr/local/bin/ -zxvf sccache-v0.4.0-pre.8-x86_64-unknown-linux-musl.tar.gz */sccache
