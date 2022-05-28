Status: published
Date: 2022-05-28 11:18:47
Modified: 2022-05-28 11:18:47
Author: Benjamin Du
Slug: reduce-grub-timeout
Title: Reduce GRUB Timeout
Category: OS
Tags: OS, Linux, GRUB, timeout

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Open the file `/etc/default/grub` 
    with sudo permission.

        sudo vim /etc/default/grub

2. Locate the line start with `GRUB_TIMEOUT`.

3. Update the value assigned to `GRUB_TIMEOUT`
    to a smaller one (e.g., 3).
    Notice that the time unit is second.

4. Update the GRUB.

        :::bash
        sudo update-grub
