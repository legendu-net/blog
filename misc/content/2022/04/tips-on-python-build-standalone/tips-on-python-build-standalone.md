Status: published
Date: 2022-04-12 08:52:10
Modified: 2022-04-12 08:52:10
Author: Benjamin Du
Slug: tips-on-python-build-standalone
Title: Tips on Python Build Standalone
Category: Computer Science
Tags: Computer Science, programming, Python, portable, python-build-standalone 

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The GitHub repository
[python-portable](https://github.com/dclong/python-portable)
has some example scripts for bundling standalone Python environments.
It also releases standalone Python environemnts regularly.

## Tips on Using `env_python.tar.gz`

This section is specifically on using the `env_python.tar.gz` environemnt
released in the GitHub repository
[python-portable](https://github.com/dclong/python-portable)
.

### Update Shebang

1. Start an IPython shell using the following code.

        :::bash
        ~/env_python/bin/python3 -m IPython

2. Run the following code in the IPython shell to update Shebangs of Python scripts. 

        :::python
        dsutil.shebang.update_shebang("env_python/bin/", "/home/your_user_name/env_python/bin/python3")
