---
title: Use Flake8 to Lint Python Scripts
created: '2020-08-25T14:52:31-07:00'
date: '2026-11-15T09:24:58-08:00'
authors:
  - bendu
label: use-flake8-to-lint-python-scripts
license: CC-BY-4.0
tags:
  - computer science
  - Python
  - flake8
  - linter
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Configuration

It is suggested that you put the configuration into a file named `.flake8`
in the root directory of your project.
When flake8 supports `pyproject.toml` later,
it is best to configure flake8 in `pyproject.toml`.
Below is an example of configuration.

```text
[flake8]
ignore = C901,E501,E251,E124,E125,E722,E261,E265,W291,W292,W293
exclude = __init__.py,docs/source/conf.py,old,build,dist,.git,__pycache__
max-complexity = 10
```

Please refer to the following link for an example of configuration.

https://github.com/dclong/xinstall/blob/dev/xinstall/data/flake8/flake8

## References

https://flake8.pycqa.org/en/latest/index.html

https://flake8.pycqa.org/en/latest/user/violations.html
