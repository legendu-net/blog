---
title: Tips on Yazi
created: '2026-07-26T23:03:52.607491-07:00'
date: '2026-07-28T20:20:00-07:00'
authors:
  - bendu
label: tips-on-yazi
license: CC-BY-4.0
tags:
  - yazi
  - file manager
  - terminal
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. Yazi accepts a working dir as parameter.
   That is,
   `yazi /dest/working/dir` runs `yazi` under the directory `/dest/working/dir`.
   This is useful in large and deep directory (e.g., when working in a monorepo)
   .

1. The `--cwd-file <CWD_FILE>` flag tells Yazi to write its Current Working Directory to a specific text file on exit.
   Because Yazi runs as a child process, it cannot directly change the parent shell's working directory. The `--cwd-file` flag acts as a communication bridge.
   By combining this flag with a shell wrapper function, you can configure your shell to read the written path and automatically `cd` into Yazi's last working directory when it closes.

1. The `--chooser-file <FILE>` flag transforms yazi into a visual file picker
   for other applications or scripts.
   Instead of just browsing and opening files normally,
   running Yazi with this flag tells it to write the absolute paths of the files you select
   to the specified text file when it exits.

## Image Preview in Yazi Running in Zellij

See discussion in i
[Image Preview in Yazi Running in Zellij](image-preview-in-yazi-running-in-zellij)
.

## References

- [Image Preview in Yazi Running in Zellij](image-preview-in-yazi-running-in-zellij)

- [Yazi @ GitHub](https://github.com/sxyazi/yazi)

- [Yazi Official Doc](https://yazi-rs.github.io/)

- [Yazi is the Terminal-based File Manager I Didn't Know I Needed](https://itsfoss.com/yazi/)
