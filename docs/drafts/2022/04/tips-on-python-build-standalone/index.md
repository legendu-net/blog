---
title: Tips on Python Build Standalone
created: '2022-04-12T08:52:10-07:00'
date: '2026-11-15T09:24:06-08:00'
authors:
  - bendu
label: tips-on-python-build-standalone
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Python
  - portable
  - python-build-standalone
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The GitHub repository
[python-portable](https://github.com/dclong/python-portable)
has some example scripts for bundling standalone Python environments.
It also releases standalone Python environments regularly.

## Tips on Using `env_python.tar.gz`

This section is specifically on using the `env_python.tar.gz` environment
released in the GitHub repository
[python-portable](https://github.com/dclong/python-portable)
.

### Update Shebang

1. Start an IPython shell using the following code.

   ```bash
   ~/env_python/bin/python3 -m IPython
   ```

1. Run the following code in the IPython shell to update Shebangs of Python scripts.

   ```python
    dsutil.shebang.update_shebang("env_python/bin/", "/home/your_user_name/env_python/bin/python3")
   ```
