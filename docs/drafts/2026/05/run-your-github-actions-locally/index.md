---
title: Run Your GitHub Actions Locally
created: '2026-05-28T00:05:08.917806-07:00'
date: '2026-10-22T20:10:04-07:00'
authors:
  - bendu
label: run-your-github-actions-locally
license: CC-BY-4.0
tags:
  - programming
  - code
  - GitHub
  - Actions
  - local
  - wrkflw
  - act
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [act](https://github.com/nektos/act)

### Installation (Linux / macOS)

```sh
brew install act
```

### Trigger Workflows Listening on Pull Request

```sh
act pull_request
```

## [wrkflw](https://github.com/bahdotsh/wrkflw)

Wrkflw has a great TUI
which makes it easy to selectively run workflow and insepct results.
However,
wrkflw currently maps the ubuntu-latest VM to the ubuntu:latest Docker image
which are not compatible
(see [issues 113](https://github.com/bahdotsh/wrkflw/issues/113))
.
This causes many GitHub Actions workflow fail to run with wrkflw.

## References

- [Why I built wrkflw](https://blog.gokuls.in/posts/why-i-built-wrkflw.html)

- [act - User Guide | Manual | Docs | Documentation](https://nektosact.com/)
