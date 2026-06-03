---
title: Tips on gh
created: '2022-05-02T00:03:11-07:00'
date: '2026-06-02T23:50:57-07:00'
authors:
  - bendu
label: tips-on-gh
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - gh
  - GitHub
  - CLI
  - command
  - terminal
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation via Homebrew (Linux / macOS)

```
brew install gh
```

## Installation on Fedora

```sh
sudo dnf config-manager addrepo --from-repofile=https://cli.github.com/packages/rpm/gh-cli.repo
sudo dnf install -y gh
```

## Create a Release

```
gh release create --title v0.0.1 --rep o dclong/test10 --notes "" v0.0.1
```

https://cli.github.com/

https://github.com/cli/cli

https://cli.github.com/manual/gh_secret

https://cli.github.com/manual/gh

https://github.com/topics/gh-extension
