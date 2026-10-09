---
title: Jujutsu Equivalent of Git Stage
created: '2026-10-08T22:47:04.861637-07:00'
date: '2026-10-08T22:47:04-07:00'
authors:
  - bendu
label: jujutsu-equivalent-of-git-stage
license: CC-BY-4.0
tags:
  - VCS
  - Jujutsu
  - jj
  - Git
  - stage
  - commit
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Git's staging area lets you pick reviewed changes first
and decide what the commit is about later.
jj has no staging area,
but the parent commit of `@` can play the same role
(`@` is the working-copy commit holding your current edits,
and `@-` is its parent).
Since a jj commit's message is optional and can be changed any time,
the "staging" commit doesn't need a message until you are done picking changes.

1. Insert an empty commit (without a message) right below `@`,
   and stay on `@`.

   ```sh
   jj new -B @ --no-edit
   ```

   - `-B @` (`--insert-before @`) puts the new commit under `@`
     instead of on top of it.
   - `--no-edit` keeps `@` as your working copy.
     Without it,
     `@` would move to the new (empty) commit
     and your edits would no longer be in the working copy
     (they would still be safe in `W`,
     but you would need `jj edit` to get back to them).

   ```text
   Before:              After:
   @  W (all edits)     @  W (all edits, unchanged)
   ○  P                 ○  S (empty)  ← "staging area"
                        ○  P
   ```

1. As you review changes,
   move them from `@` into the staging commit `@-`.

   ```sh
   jj squash path/a path/b   # like `git add path/a path/b`
   jj squash -i              # like `git add -p`
   ```

   Before running `jj squash`,
   make sure `@-` is the staging commit you just created
   (e.g., using `jj log -r @-`).
   Otherwise,
   the changes are squashed into the wrong commit.
   Notice that running step 1 again stacks another empty commit,
   which then becomes `@-`.

   Staging all changes in `@` moves `@` to a fresh empty commit
   on top of the staging commit.
   This is expected,
   and `@-` is still the staging commit.
   If both commits already have messages,
   jj opens an editor to combine them.

1. Check what is staged and what is not.

   ```sh
   jj diff -r @-   # like `git diff --cached`
   jj diff         # like `git diff`
   ```

   To unstage changes (like `git restore --staged -p`),
   move them back into `@`.

   ```sh
   jj squash -i --from @- --into @ --keep-emptied
   ```

   `--keep-emptied` keeps the staging commit even if everything is unstaged.
   Without it,
   jj abandons the emptied staging commit
   (and, if it has a message, asks you to combine it into `@`'s message),
   and the next `jj squash` would go into the commit below it.

1. When you are done,
   write the commit message
   (optionally with the help of an AI tool reading `jj diff -r @- --git`).

   ```sh
   jj describe -r @-
   ```

This approach has a few advantages over Git's staging area.

- The "staged" changes are a real commit,
  so they survive task switching and can be undone with `jj undo`.
- You can keep multiple staging commits for different topics
  and squash into each one with `jj squash --into <revision>`.

You can define aliases in your jj config
to make this workflow feel more like Git.

```toml
[aliases]
stage-init = ["new", "-B", "@", "--no-edit"]
stage = ["squash"]
staged = ["diff", "-r", "@-"]
unstage = ["squash", "-i", "--from", "@-", "--into", "@", "--keep-emptied"]
```
