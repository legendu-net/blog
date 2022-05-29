Status: published
Date: 2022-05-28 11:18:47
Modified: 2022-05-28 22:36:56
Author: Benjamin Du
Slug: reduce-grub-timeout
Title: Reduce GRUB Timeout
Category: OS
Tags: OS, Linux, GRUB, timeout, GRUB_TIMEOUT, GRUB_RECORDFAIL_TIMEOUT

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Open the file `/etc/default/grub` 
    with sudo permission.

        sudo vim /etc/default/grub

2. Update the value assigned to `GRUB_TIMEOUT`
    to a smaller one (e.g., 3).
    Notice that the time unit is second.

        :::text
        GRUB_TIMEOUT=3

4. Update the value assigned to `GRUB_RECORDFAIL_TIMEOUT`
    to `$GRUB_TIMEOUT`.

        :::bash
        GRUB_RECORDFAIL_TIMEOUT=$GRUB_TIMEOUT

4. Update the GRUB.

        :::bash
        sudo update-grub

## References

- [‘GRUB_TIMEOUT’ Change – Not Working [SOLVED]](https://www.shellhacks.com/grub_timeout-change-not-working/)
