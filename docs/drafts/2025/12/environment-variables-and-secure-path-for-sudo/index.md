---
title: Environment Variables and Secure Path for sudo
created: '2025-12-22T15:29:11-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: environment-variables-and-secure-path-for-sudo
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - sudo
  - environment
  - variable
  - path
  - secure path
  - ENV
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```
sudo -E command_to_run

sudo $(which command_to_run)

sudo env "PATH=$PATH" nvim
```

The "correct" way is to update the secure path using the commanding `sudo visudo`.

For more discussions,
please refer to
[Chat with Gemini - sudo nvim Not Found, Fixes](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221eecorE7tx_iICYiZGqR4veuaXD_AmzHL%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## References

- [Proxy for sudo](proxy-for-sudo)
