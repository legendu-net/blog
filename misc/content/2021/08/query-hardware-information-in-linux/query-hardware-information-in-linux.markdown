Status: published
Date: 2021-08-21 23:05:47
Modified: 2021-09-06 13:01:45
Author: Benjamin Du
Slug: query-hardware-information-in-linux
Title: Query Hardware Information in Linux
Category: Computer Science
Tags: Computer Science, OS, Linux, hardware, information, query, list, check, osquery, hw-probe
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```
sudo lshw -html > hardware.html
```

osquery


[hw-probe](https://github.com/linuxhw/hw-probe)
is a hardware probe tool
which probes for hardware, 
check operability and find drivers with the help of 
[Linux hardware database](https://linux-hardware.org)
.

