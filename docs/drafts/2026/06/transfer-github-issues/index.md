---
title: Transfer GitHub Issues
created: '2026-06-03T08:07:33.866252-07:00'
date: '2026-06-03T08:07:33.866261-07:00'
authors:
  - bendu
label: transfer-github-issues
license: CC-BY-4.0
tags:
  - GitHub
  - transfer
  - issue
  - public
  - private
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Transferring an issue to another repository
https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository?tool=cli

You can only transfer issues between repositories owned by the same user or organization account. A private repository issue cannot be transferred to a public repository.

There are a few ways to circumstance the limitation.

1. You write you own command-line application to read an issue and open a new one in another repository.

2. You can create intermediate GitHub repository.
  Let's says that you want transfer issues from a private repository `entity1/repo1`
  to a public repository `entity2/repo2`.
  - Create a private repository `entity1/repo3`.
  - Transfer issues from `entity1/repo1` to `entity1/repo3`.
  - Transfer ownership of `entity1/repo3` to `entity2`, that it transfer it to `entity2/repo3`.
  - Make `entity2/repo3` public.
  - Transfer issues from the public repository `entity2/repo3` to the public repository `entity2/repo2`.

