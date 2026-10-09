---
title: Committing Using Git Causes Orphan Commits in Jujutsu
created: '2026-10-08T22:56:10.150523-07:00'
date: '2026-10-08T22:56:10-07:00'
authors:
  - bendu
label: committing-using-git-causes-orphan-commits-in-jujutsu
license: CC-BY-4.0
tags:
  - VCS
  - Jujutsu
  - jj
  - Git
  - orphan
  - commit
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

In a colocated repo (created by `jj git init --colocate`),
Git and jj share the same commits
but each tracks its own position:
jj's `@` is the commit holding your current edits,
and jj keeps Git's `HEAD` pointing to the parent of `@`.
Unlike Git,
jj has no separate staging area or uncommitted state —
every jj command (`jj status`, `jj log`, etc.)
automatically snapshots your files into `@`.

Committing with Git (e.g., `git add a && git commit`)
while `@` holds jj-snapshotted edits
leaves the old `@` behind as an orphan commit.

1. Start: `@` (call it `W`) is on top of commit `P`, and Git's `HEAD` is `P`.

1. You edit files `a` and `b` and run any jj command.
   jj snapshots both edits into `W`.

1. You run `git add a && git commit`.
   Git knows nothing about `W`,
   so it creates a new commit `X` (containing `a`) on top of `P`
   and moves `HEAD` to `X`.

1. On the next jj command,
   jj sees that `HEAD` moved to `X`
   and creates a new `@` on top of `X` (holding `b`, which is still on disk).

1. The old `W` (containing `a` and `b`) is neither `@` nor `HEAD`.
   jj never automatically discards a non-empty commit,
   so `W` stays around as an orphan,
   duplicating changes that now also live in `X` and the new `@`.

In the diagram below,
arrows point from a commit to its parent.

```text
P ← W (a + b)          ← orphan
 ↖
  X (a) ← @ (b)        Git HEAD = X
```

In this exact scenario,
`W` holds nothing beyond what `X` and the new `@` already have,
so you can simply run `jj abandon W`.

To spot such leftovers,
list the mutable heads (tips of branches not yet merged into main)
other than the working copy.
Not every result is an orphan —
feature branches you are still working on show up too.

```sh
jj log -r 'heads(mutable()) ~ @'
```

To check whether an orphan's changes have already been merged into main (`trunk()`),
test-rebase it onto main and inspect the result:
empty means fully merged,
conflicted means main changed the same lines differently (needs review),
and neither means it has changes (at least partially) not yet in main.
Then undo the rebase.
`--ignore-working-copy` keeps `jj log` from snapshotting the working copy,
so that `jj undo` undoes the rebase rather than a new snapshot.

```sh
jj rebase -r <commit> -o 'trunk()'
jj log --ignore-working-copy -r <commit>
jj undo
```

The fish function
[jj_orphans](https://github.com/legendu-net/fish/blob/main/functions/jj_orphans.fish)
automates this check for all orphan heads
without modifying them.
If the test rebase makes an orphan empty
(or `jj_orphans` labels it `empty`),
it can be safely removed with `jj abandon <commit>`.

To avoid orphan commits in the first place,
use the jj way of staging changes
(see [Jujutsu Equivalent of Git Stage](#jujutsu-equivalent-of-git-stage))
instead of committing with Git.
