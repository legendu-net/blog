---
title: Manage Your Code Repositories Using Jujutsu
created: '2026-04-30T19:49:30.593438-07:00'
date: '2026-06-15T20:02:10-07:00'
authors:
  - bendu
label: manage-your-code-repositories-using-jujutsu
license: CC-BY-4.0
tags:
  - Jujutsu
  - jj
  - Git
  - code
  - repository
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
To install Jujutsu (jj) using Homebrew, run:

## General Tips

1. jj ecourages small and frequently commits

   - easier to check local diffs
   - more flexible and granular control over changes
     You can always consolidate commits later using `jj squash`
     .

1. If you run `jj squash` and the working copy doesn't have a commit message yet,
   it will directly use the parent commit's message.
   You can also specify files to squash instead of squashing all changed files.

1. `jj squash` and `jj abandon` always create an empty working copy.
   If you are on an empty working copy,
   running those commands won't help.
   You have to either move the working copy to the (non-empty) parent commit first
   and then run those commands,
   or specify revisions manually.

## Installation Using Homebrew (Linux / macOS)

```
brew install jj
```

## Jujutsu Configuration

### Identity Configuration

After installation, you should configure your identity:

```
jj config set --user user.name "Your Name"
jj config set --user user.email "your.email@example.com"
```

### Interaction with Git Configurations

1. Jujutsu respects `.gitignore` files and also `core.excludesFile` (if defined) from `.gitignore`.

1. Settings in `.gitinore` (other than `core.excludesFile`) are not read by Jujutsu at this time.

1. In a Git-backed repo,
   jj reads remote names and URLs directly from the .git/config
   so that commands like `jj git fetch` and `jj git push` work seamlessly.

1. In "colocated" mode, jj and Git share the same underlying commit objects and branch references.

### Jujutsu Configuration Levels

Jujutsu resolves configuration in the following order (higher number overrides lower):

1. Built-in: Default settings.
1. User: `~/.config/jj/config.toml` (global for you).
1. Repo-managed: `.config/jj/config.toml` (committed to the project).
1. Repo-local: `.jj/repo/config.toml` (private to your local clone and should never be committed).
1. Workspace-local: `.jj/workspaces/<name>/config.toml` (if using multiple workspaces).
1. Command-line: arguments passed via --config-toml.

### Manage Jujutsu Configurations

1. View current config.

```
jj config list
```

2. Edit user config.

```
jj config edit --user 
```

3. Find config file path.

```
jj config path --user
```

## Use Jujutsu with a Git Repository

```
jj git init --colocate
```

## Some Useful jj Commands

1. Update the author on a commit.

```sh
jj metaedit -r @ --update-author
```

1. Moves the working copy back to the parent commit.

```sh
jj edit @-
```

1. Pushes the parent commit to the remote,
   creating a tracking branch for it automatically if needed.

```sh
jj git push --change @-
```

This is the standard jj workflow for opening a pull request —
you don't manage branch names manually; jj derives them from change IDs.

1. Pushes the parent commit to the remote under an explicit branch name you choose.

```sh
jj git push --named new-branch=@-
```
