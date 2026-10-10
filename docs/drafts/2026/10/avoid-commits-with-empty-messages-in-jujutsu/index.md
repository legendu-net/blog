---
title: Avoid Commits with Empty Messages in Jujutsu
created: '2026-10-08T21:34:50.782468-07:00'
date: '2026-10-09T12:15:21-07:00'
authors:
  - bendu
label: avoid-commits-with-empty-messages-in-jujutsu
license: CC-BY-4.0
tags:
  - VCS
  - Jujutsu
  - jj
  - commit
  - empty
  - message
  - editor
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

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
