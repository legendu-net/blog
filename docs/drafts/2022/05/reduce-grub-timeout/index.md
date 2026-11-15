---
title: Reduce GRUB Timeout
created: '2022-05-28T11:18:47-07:00'
date: '2026-11-15T12:20:38-08:00'
authors:
  - bendu
label: reduce-grub-timeout
license: CC-BY-4.0
tags:
  - OS
  - Linux
  - GRUB
  - timeout
  - GRUB_TIMEOUT
  - GRUB_RECORDFAIL_TIMEOUT
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Open the file `/etc/default/grub`
   with sudo permission.

   ```
    sudo vim /etc/default/grub
   ```

1. Update the value assigned to `GRUB_TIMEOUT`
   to a smaller one (e.g., 3).
   Notice that the time unit is second.

   ```
    :::text
    GRUB_TIMEOUT=3
   ```

1. Update the value assigned to `GRUB_RECORDFAIL_TIMEOUT`
   to `$GRUB_TIMEOUT`.

   ```
    :::bash
    GRUB_RECORDFAIL_TIMEOUT=$GRUB_TIMEOUT
   ```

1. Update the GRUB.

   ```
    :::bash
    sudo update-grub
   ```

## References

- [‘GRUB_TIMEOUT’ Change – Not Working [SOLVED]](https://www.shellhacks.com/grub_timeout-change-not-working/)
