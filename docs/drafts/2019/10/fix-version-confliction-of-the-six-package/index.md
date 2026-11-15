---
title: Fix Version Confliction of the Six Package
created: '2019-10-15T08:31:38-07:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: fix-version-confliction-of-the-six-package
license: CC-BY-4.0
tags:
  - programming
  - Python
  - six
  - version confliction
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

ERROR: jsonschema 3.1.1 has requirement six>=1.11.0, but you'll have six 1.10.0 which is incompatible.

```
:::Python
sudo pip3 install six -U
```
