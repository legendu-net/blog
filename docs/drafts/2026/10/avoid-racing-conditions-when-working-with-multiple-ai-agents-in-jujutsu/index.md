---
title: Avoid Racing Conditions When Working with AI Agents in Jujutsu
created: '2026-10-08T21:50:02.923981-07:00'
date: '2026-10-08T21:52:13-07:00'
authors:
  - bendu
label: avoid-racing-conditions-when-working-with-multiple-ai-agents-in-jujutsu
license: CC-BY-4.0
tags:
  - VCS
  - Jujutsu
  - jj
  - AI
  - agent
  - concurrency
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

In jj,
the working copy (`@`) is a real commit
and changes on disk are snapshotted into it
at the start of every jj command.
If you run an interactive command (e.g., `jj commit` or `jj describe` without `-m`),
jj waits for your editor to close.
If an AI agent (or any tool) runs a jj command during that window,
it snapshots `@` in a concurrent operation
while your command finalizes based on the stale state from before the editor opened.
jj merges the concurrent operations automatically,
but `@` might end up as a divergent change.

`jj split` is NOT a good primary solution.
It only cleans up tangled changes after the fact,
the interactive `jj split` has the same race window (while the diff editor is open),
and repeatedly untangling changes adds friction.
Below are better ways (from the easiest daily habit to full isolation).

1. Create a new empty parent commit and square changes into it.

   i. Run `jj new -B @ --no-edit` to create a new empty parent commit without a commit message.
   ii. Use `jj squash -u --into @-` to move changes into the new parent commit.
   `-u` (`--use-destination-message`) avoids opening an editor to combine commit messages.
   iii. Run `jj describe --editor -r @` to change the description of the parent commit.

1. Isolate agents using separate workspaces (cleanest for multiple agents).
   Agents sharing the same working directory and working copy
   will inevitably collide (overlapping edits, linter conflicts, snapshot races).
   `jj workspace add` creates a workspace with its own independent working copy
   attached to the same repository,
   so commits are visible across workspaces
   while agents (launched inside the new workspace) never touch your working copy.
   Note that a jj workspace is not a Git worktree,
   so `git` commands might not work in it even for a colocated repository.
   Please refer to [](#jujutsu-workspace) for more discussions.

   ```sh
   jj workspace add ../agent_scratch
   ```
