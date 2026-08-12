---
title: mdformat Is an Extensible Markdown Formatter
created: '2026-04-08T20:49:46.627882-07:00'
date: '2026-08-11T22:19:16-07:00'
authors:
  - bendu
label: mdformat-is-an-extensible-markdown-formatter
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - markdown
  - formatter
  - MyST
  - extensible
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```
mdformat path/to/file.md
```

## Tips and Traps

1. When mdformat is used via the command-line interface,
   it automatically enables installed code formatter plugins and parser plugins
   so that you don't have to manually specify `--extensions e1 --extensions e2 ...`.
   However,
   when mdformat is used via the Python API,
   you have to manually enable plugins.

## Some Useful Plugins

- mdformat-myst
- mdformat-ruff
- mdformat-beautysh
- mdformat-config
- mdformat-rustfmt
- mdformat-web

## References

- [mdformat @ GitHub](https://github.com/hukkin/mdformat)
