---
title: Jujutsu Rebase
created: '2026-07-28T20:06:12.515508-07:00'
date: '2026-07-28T20:06:52-07:00'
authors:
  - bendu
label: jujutsu-rebase
license: CC-BY-4.0
tags:
  - programming
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## `jj rebase --onto main` vs `jj rebase -r @ --onto main`

Both commands rebase onto `main` (via `--onto/-o`),
but they differ in **which** revisions are selected to be rebased.

`jj rebase` has to be told which revisions to move.
When no selector (`-b`/`-s`/`-r`) is given, it defaults to `-b @`,
i.e. it operates on the *whole branch* containing the working copy `@`.

1. `jj rebase --onto main`

   ```sh
   jj rebase --onto main
   ```

   With no revision selector, this defaults to `-b @`,
   so it rebases the **entire branch** containing `@` onto `main`.
   The "branch" is the set of revisions reachable from `@`
   that are not already ancestors of `main`, plus all their descendants
   (the revset `(main..@)::`).
   Use this when you want to move your current line of work,
   as a whole, on top of the latest `main`.

1. `jj rebase -r @ --onto main`

   ```sh
   jj rebase -r @ --onto main
   ```

   With `-r @`, this rebases **only the single revision `@`** onto `main`,
   *without* its descendants.
   Any "hole" left behind is filled automatically:
   `@`'s original descendants are rebased onto `@`'s former parent(s),
   so they stay where they were rather than following `@`.
   Use this when you want to lift just one commit out of its current place
   and replant it on `main`.

**Summary**

| Command                      | Revisions rebased                                | Descendants                                      |
| ---------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| `jj rebase --onto main`      | whole branch containing `@` (defaults to `-b @`) | move together with the branch                    |
| `jj rebase -r @ --onto main` | only `@`                                         | stay behind, reparented onto `@`'s old parent(s) |

In short: without a selector, `jj rebase` moves the whole branch (`-b @`),
whereas `-r @` surgically moves just the working-copy revision and leaves its descendants in place.
