UUID: 74511706-899d-4324-92fd-3ffbca0e4d2f
Status: published
Date: 2018-07-21 12:31:03
Author: Ben Chuanlong Du
Slug: fix-package-installation-issue-in-linux
Title: Fix Package Installation Issue in Linux
Category: OS
Tags: Linux, package management, issue, apt, dpkg
Modified: 2018-07-21 12:31:03

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Error message: The package hl1440lpr needs to be reinstalled, but I can't find an archive for it.


Steps to fix the issue:

Start with

```
sudo dpkg --remove --force-all hl1440lpr
```

If that fails ...

```
sudo -i
cd /var/lib/dpkg/info
rm -rf hl1440lpr*
dpkg --remove --force-remove-reinstreq hl1440lpr
exit
```

Confirm apt-get is fixed
```
sudo apt-get update
```

## Reference

https://askubuntu.com/questions/88371/apt-synaptic-needs-to-reinstall-package-but-cant-find-the-archive-for-it