---
title: Static Type Checking of Python Scripts Using pytype
created: '2020-08-30T09:16:10-07:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: static-type-checking-of-python-scripts-using-pytype
license: CC-BY-4.0
tags:
  - computer science
  - Python
  - type annotation
  - static
  - type checking
  - pytype
---

## Configuration

There are 3 ways to control the behavior of \`pytype.

1. Pass command-line options to `pytype`.

1. Specify a configuration file using `pytype --config /path/to/config/file ...`.
   You can generate an example configuration file
   using the command `pytype --generate-config pytype.cfg`.

1. If no configuration file is found,
   pytype uses the first `setup.cfg` it founds
   and use the `[pytype]` section.

Please refer to
[xinstalll::pytype/setup.cfg](https://github.com/dclong/xinstall/blob/dev/xinstall/data/pytype/setup.cfg)
for an example of configuration file of `pytype`.

## Exclude Files and/or Directories

1. Use the `--exclude` option.

   ```bash
   PATH=.venv/bin:$PATH pytype xinstall --exclude xinstall/data
   ```

1. Specify files and/or directories to exclude in the configuration file `setup.cfg`.

   ```
    [pytype]
    exclude = 
        **/*_test.py 
        **/test_*.py 
   ```

## Silent Errors

Please refer to
[Silencing errors](https://google.github.io/pytype/user_guide.html#silencing-errors)
for detailed explanations.

## References

https://google.github.io/pytype/faq.html

https://google.github.io/pytype/user_guide.html

https://google.github.io/pytype/
