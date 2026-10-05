---
title: Manage Your Code Repositories Using Jujutsu
created: '2026-04-30T19:49:30.593438-07:00'
date: '2026-10-04T11:50:34-07:00'
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

## Installation

```
icon jj -ic
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

## Avoid Racing Conditions When Working with Multiple AI Agents

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

1. Run `jj new` first and then `jj describe @-` (minimal race window).
   `jj new` finishes in milliseconds and moves `@` to a fresh empty commit.
   Any file changed by agents while you are writing the commit message
   lands in the new `@`,
   leaving the content of `@-` untouched.

   ```sh
   jj new
   jj describe @-
   ```

1. Commit non-interactively using `jj commit -m "..."`.
   There is no editor window for agents to race against
   (though agents' half-finished edits on disk are included in the commit).

1. If agents' changes are already mixed into `@`,
   use `jj squash --into` to move only your files into the target commit
   (leaving agents' files in `@`).
   `-u` (`--use-destination-message`) avoids opening an editor to combine commit messages.
   Note that paths only separate whole files.

   ```sh
   jj squash --into @- path/to/file1 path/to/file2 -u
   ```

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

## Avoid Commits with Empty Messages

Commit descriptions are optional in jj by design.
Unlike Git,
leaving the commit message blank in the editor does NOT abort `jj commit`.
However,
jj does abort the command if the editor exits with a non-zero code
(e.g., `:cq` in Vim / Neovim).

A practical way is to configure a wrapper script as jj's `ui.editor`,
which exits with an error if the commit message is empty
(ignoring jj's `JJ:` comment lines).
For example,
create a script `~/.local/bin/jj-editor-check.fish`.

```fish
#!/usr/bin/env fish
set -l file $argv[1]
# Use the first non-blank one of $VISUAL, $EDITOR and vim
set -l editor (string match -rv '^\s*$' -- $VISUAL $EDITOR vim)[1]
# Split to allow editor commands with arguments (e.g., "code --wait")
set -l cmd (string split -n ' ' -- $editor)
$cmd $file; or exit $status

# Check whether the file contains any non-comment, non-whitespace text
if not sed '/^JJ: ignore-rest$/,$d' $file | grep -v '^JJ:' | grep -q '[^[:space:]]'
    echo "Aborting due to empty commit message." >&2
    exit 1
end
```

Make it executable.

```bash
chmod +x ~/.local/bin/jj-editor-check.fish
```

And configure jj to use it
(`~` is not expanded in `ui.editor`, so use an absolute path).

```bash
jj config set --user ui.editor /home/<user>/.local/bin/jj-editor-check.fish
```

Notes:

1. Do NOT set `$VISUAL` / `$EDITOR` to the script itself (infinite recursion).
   And `$JJ_EDITOR` (if set) overrides `ui.editor` and bypasses the script.

1. The script applies to every command that opens `ui.editor`,
   e.g., `jj commit`, `jj describe`, `jj split` and `jj squash` (when combining messages).
   Diff editors and `-m` (e.g., `jj describe -m ""`) are not affected.

1. If a commit with an empty message is created anyway,
   run `jj undo` immediately to roll it back,
   or add a message later using `jj describe`.

## Jujutsu Rebase

Please refer to [](#jujutsu-rebase)
for discussions.

## Jujutsu Workspace

Please refer to [](#jujutsu-workspace)
for discussions.

## References

- [](#jujutsu-rebase)
- [](#jujutsu-workspace)
