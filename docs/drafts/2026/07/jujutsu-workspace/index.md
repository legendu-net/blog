---
title: Jujutsu Workspace
created: '2026-07-28T19:53:35.732610-07:00'
date: '2026-07-28T20:04:38-07:00'
authors:
  - bendu
label: jujutsu-workspace
license: CC-BY-4.0
tags:
  - VCS
  - Jujutsu
  - jj
  - workspace
  - parallel
  - work
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The best way to do multiple parallel work on the same repository
(e.g., if there are 2 independent changes you'd like to make in 2 separate PRs,
or if an AI agent is working on one change while you work on another)
is by using Workspaces (`jj workspace`),
which is the native equivalent of `git worktree`.

Workspaces allow you to create a separate physical directory on your file system
that shares the exact same underlying repository state (the `.jj` and `.git` data)
but maintains its own independent working copy.
This means your AI agent can continue mutating files in your primary directory while you work entirely unbothered in the second one.

## How to set it up and manage it

1. **Create a New Workspace**
   From within your current repository directory, add a new workspace pointing to a new directory path (usually placed right next to your current repo):

   ```sh
   jj workspace add ../my-repo-pr2
   ```

   *Note: By default, the workspace name will match the directory name (`my-repo-pr2`).*

1. **Switch and Start Working**
   Navigate into the new directory. You will notice it has the files from your repository, but it is a completely independent working copy:

   ```sh
   cd ../my-repo-pr2
   ```

   By default, `jj workspace add` creates a new working copy based on the current commit of the workspace you ran it from. If you want this second PR to branch off `main` instead, just create a new revision off your main branch:

   ```sh
   jj new main -m "Independent changes for PR 2"
   ```

1. **Work in Parallel**
   You now have two directories attached to the exact same repository backend.

   Any `jj git fetch` or `jj git push` you run in one directory will instantly update the repository state for both.

   The AI agent can continue running tasks, building, or modifying the working tree in the first directory without any collision with your work in the second.

1. **Clean Up**
   When your second PR is merged and you no longer need the parallel directory, you can simply delete it and tell `jj` to remove it from its tracking:

   ```sh
   # Move out of the workspace directory
   cd ../my-repo

   # Delete the physical directory
   rm -rf ../my-repo-pr2

   # Tell jj to forget the workspace
   jj workspace forget my-repo-pr2
   ```

   If you ever forget which workspaces you have active, you can run `jj workspace list` to see all directories currently attached to your repository.

## `jj workspace` vs Independent Clone

While doing an independent clone will also give you a separate directory to work in, using `jj workspace` (or `git worktree`) is significantly faster, lighter, and keeps your local workflow perfectly synchronized.

The core difference is **Shared State vs. Isolated State**. A clone duplicates the entire repository, while a workspace shares the exact same underlying database (`.git` and `.jj` folders).

Here is how that impacts your workflow practically:

1. **Instant Visibility (No Pushing/Pulling Locally)**

   - **With a Clone**: If your AI agent finishes a task and creates a commit in directory A, directory B knows nothing about it. To see that commit in directory B, the agent must push to the remote server, and you must `jj git fetch` in directory B.
   - **With a Workspace**: Because they share the same backend, a commit made by the AI agent in directory A is instantly visible in directory B when you run `jj log`. You can immediately rebase your work on top of the agent's work without involving the network.

1. **Single Point of Maintenance**

   - **With a Clone**: You have two completely separate repositories to maintain. You have to run `jj git fetch` in both directories independently to keep them up to date with `main`.
   - **With a Workspace**: You only need to fetch once. If you run `jj git fetch` in your workspace, the new remote commits are instantly available to your primary directory as well.

1. **Disk Space and Speed**

   - **With a Clone**: You duplicate the entire history of the repository. For a large codebase, this takes up significant disk space and requires waiting for a full network download.
   - **With a Workspace**: It is nearly instantaneous. You are only duplicating the physical files of the working copy (the code you actually see), not the decades of Git history.

**Summary**

Cloning is best when you need complete, total isolation (e.g., you want to experiment with highly destructive Git operations without risking your primary repo's history). For parallel development—like you and an AI working on two different PRs simultaneously—workspaces are the native, frictionless solution.
