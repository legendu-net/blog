---
title: Tips on yapf
created: '2019-07-08T19:37:50-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: tips-on-yapf
license: CC-BY-4.0
tags:
  - programming
  - Python
  - yapf
  - code formatting
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Black is preferred to yapf!

[yapf Online Demo](https://yapf.now.sh/)

1. There are 4 predefined styles: google, facebook, chromium, and pep8.
   You can specify a style to use using the `--style` option
   or you can specify the style to use in the file `.style.yapf` under the root directory of your project.

   ```
    [style]
    based_on_style = facebook
    column_limit = 88
   ```

   YAPF searches for the formatting style in the following manner:

   1. Specified on the command line
   1. In the [style] section of a .style.yapf file in either the current directory or one of its parent directories.
   1. In the [yapf] section of a setup.cfg file in either the current directory or one of its parent directories.
   1. In the [style] section of a ~/.config/yapf/style file in your home directory.
      If none of those files are found, the default style is used (PEP8).

1. You can control the behavior of yapf via settings in the file `.style.yapf` under the root directory of your project.

```
[style]
EACH_DICT_ENTRY_ON_SEPARATE_LINE = True
ALLOW_SPLIT_BEFORE_DICT_VALUE = False
```

## Tricks and Traps

1. When `--diff/-d` is supplied, YAPF returns zero when no changes were necessary,
   non-zero otherwise (including program error).
   You can use this in a CI workflow to test that code has been YAPF-formatted.

## Ignore Files

Put patterns of files to ignore into the file `.yapfignore`.

```
*/.ipynb_checkpoints/
```

## References

https://github.com/google/styleguide

https://github.com/google/yapf

https://github.com/life4/awesome-python-code-formatters
