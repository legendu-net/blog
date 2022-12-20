Status: published
Date: 2015-09-12 01:39:06
Author: Ben Chuanlong Du
Slug: undelete-files-in-linux
Title: Undelete Files in Linux
Category: OS
Tags: Linux, undelete, recover, files, filesystem, restore, trash
Modified: 2022-12-20 12:05:13

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The best way to "recover deleted files"
is really to avoid permanently delete files.
It is suggested that you avoid using the `rm` command
(unless you are 100% sure what you are doing)
.
Insted,
you can use a file manager provided by a Linux desktop to delete files.
This way, 
deleted files are moved to the Trash directory,
which can be recovered easily.
If you must use a command-line tool,
it is suggested that you use one of the following safer alternatives to `rm`.

- [rip](https://github.com/nivekuil/rip)
- [trash-cli](https://github.com/andreafrancia/trash-cli)
- [%trash magic for IPython](https://github.com/legendu-net/icon/blob/dev/utils/data/ipython/startup.ipy#L111)

## Recover Files Using `extundelete`

```bash
sudo mount -o remount,ro /dev/sdb1
sudo extundelete --restore-all /dev/sdb1 
```

## References

- [How to recover a removed file under Linux?](https://superuser.com/questions/150027/how-to-recover-a-removed-file-under-linux)

- [3 Ways to Recover Deleted Files by RM Command on Ubuntu](https://recoverit.wondershare.com/file-recovery/recover-deleted-files-by-rm-command-on-ubuntu.html)
