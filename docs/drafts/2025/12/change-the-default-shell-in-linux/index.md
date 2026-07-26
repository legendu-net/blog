---
title: Change the Default Shell in Linux
created: '2025-12-07T17:48:30-08:00'
date: '2026-07-25T22:47:16-07:00'
authors:
  - bendu
label: change-the-default-shell-in-linux
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Linux
  - shell
  - chsh
  - atomic
  - change
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```{note}
Changing the default shell might not work with certain desktop login manangers (e.g, SDDM).
A safer alternative is to change the default shell for terminal applications.
```

## Atomic Linux Distributions

[How to change the default shell in fedora silverblue?](https://discussion.fedoraproject.org/t/how-to-change-the-default-shell-in-fedora-silverblue/21203/10)

```
sudo usermod --shell $(which fish) $(id -un)
```

The above command updates the configuration file `/etc/passwd`.

## Mutable Linux Distributions

```
sudo chsh -s $(which fish) $(id -un)
```

You have to add the path of `fish` into `/etc/shells`,
if you get the error message
"chsh: /usr/bin/fish is an invalid shell".

Log out and then log in (or simplify reboot) for the change to take effect.

## References

- [Universal Blue Black Screen Fix](https://share.gemini.google/rubzGtHG18OM)
