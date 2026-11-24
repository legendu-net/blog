---
title: Tools for Checking for Dirty Git Repositories
created: '2025-12-15T19:18:01-08:00'
date: '2026-11-23T18:35:17-08:00'
authors:
  - bendu
label: tools-for-checking-for-dirty-git-repositories
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Git
  - Jujutsu
  - jj
  - repository
  - dirty
  - check
  - reposcan
  - leave
  - Rust
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

When you have many local repositories managed by Git and/or
[Jujutsu (jj)](#manage-your-code-repositories-using-jujutsu),
you need a tool that finds uncommitted work, unpushed (ahead) changes,
unpulled (behind) updates, stashes and stale repositories.
To do this well, the tool has to understand how each version control system
tracks the working copy and remote state.

## Tools Supporting Both Git and jj

[reposcan](https://github.com/MABD-dev/reposcan) is a CLI tool written in Go.
It scans directories concurrently for both Git and jj repositories in a single pass,
and reports uncommitted changes, ahead/behind counts, stashes and stale repositories.

- **Repository discovery**: finds `.git` directories, worktree-style `.git` files
  and `.jj` directories under one or more scan roots,
  and skips directories matching ignore globs (e.g., `**/node_modules/**`).
- **Filtering & output modes**: filters with `-f` / `--filter`
  (`all`, `dirty`, `uncommitted`, `unpushed`, `unpulled`, `stash`) and `--stale-days`.
  It has an interactive TUI (`/` to filter, `c` to copy a repository path)
  and JSON output (`-o json` and `--json-output-path`), which includes a `vcsType` field.
- **jj working copy semantics**: changes in `@` count as uncommitted files,
  and commits ahead are counted up to the working-copy parent `@-`.
- **jj remote & read-only behavior**: it uses remote bookmark state that has already been fetched
  instead of running `jj fetch` itself.
  jj support only covers status/reporting:
  the TUI fetch, push and pull actions do not work for jj repositories.
- **Rewritten `@` behavior**: if you amend or rewrite `@` after pushing,
  the remote bookmark still points to the earlier version.
  reposcan might then show `1 behind` along with uncommitted edits in `@`.

## Rust Alternatives (Git Only)

None of the Rust scanners below supports jj natively.
They scan directories for dirty Git repositories,
and they can pick up the `.git` directory in a colocated jj repository.
However, the Git index and branch state do not always match jj's working copy `@` and bookmarks.

```{list-table}
---
header-rows: 1
widths: 18 50 32
---
* - Tool
  - Features
  - jj Support
* - [dirty](https://github.com/iamkaf/dirty)
  - Walks directories up to a configurable depth and checks Git repos in parallel (`git2` + `rayon`).
    Flags uncommitted/untracked changes, local-only repos, branch names (`-b`)
    and commits ahead of upstream (`-u`).
  - Skips non-colocated `.jj` repos; reads colocated repos through Git state only.
* - [git-aware](https://github.com/PaulRosset/git-aware)
  - Scans target directories (`-p`) or system paths
    to highlight dirty Git working copies (install via `cargo install gitaware`).
  - Does not parse `.jj` repositories.
* - [git-statuses](https://github.com/bircni/git-statuses)
  - Shows each repository's status, branch and clean/dirty state in a table
    (install via crates.io or GitHub Releases).
  - Does not parse `.jj` repositories.
* - [DiffCatcher](https://github.com/Teycir/DiffCatcher)
  - Finds Git repos recursively; supports fetch/pull/rebase modes, branch diffs, incremental scans,
    and JSON, Markdown or SARIF output.
  - Built for Git diff/audit workflows; does not understand jj.
```

## Other Tools

- [git-leave](https://github.com/mrnossiom/git-leave)

- [repository-check-dirty](https://www.npmjs.com/package/repository-check-dirty)

## Recommendation for Mixed Git and jj Repositories

reposcan is the recommended tool if you work with both Git and jj repositories.
This is especially true for colocated jj repositories (`jj git init --colocate`)
and for directory trees that mix plain Git repos, Git worktrees
and [jj workspaces](#jujutsu-workspace).

1. **Run a fast triage scan**: run reposcan on your root directories
   (with filters such as `-f unpushed` or `--stale-days`)
   to find repositories that need attention.
1. **Check jj state directly**: for flagged jj repositories,
   or colocated repositories where `@` was amended,
   run `jj status` and `jj log` before rewriting history or pushing.
1. **Add shell helpers if needed**: write small shell or Fish functions on top of reposcan
   for custom jj bookmark or push checks.

## Installing, Configuring and Using reposcan

### Installation

Install reposcan with the official install script
(which supports linux/amd64, darwin/amd64 and darwin/arm64),
or build it from source.
If you installed an older binary with `go install` into `$GOPATH/bin` (typically `~/go/bin/reposcan`),
remove it first.
Otherwise, it may come earlier in `PATH` and shadow the new binary.

```bash
rm -f "$(go env GOPATH)/bin/reposcan"
curl -fsSL https://raw.githubusercontent.com/mabd-dev/reposcan/main/install.sh | sh
```

### Configuration

reposcan loads its default settings first, then `~/.config/reposcan/config.toml`,
and finally CLI flags.
Later sources override earlier ones.

```toml
version = 1
debug = false
no-telemetry = false

roots = ["~/Code", "~/work"]
only = "dirty"
countStashAsDirty = false
staleDays = 0
dirIgnore = ["**/node_modules/**", "**/.cache/**", "**/.local/**"]

[output]
type = "interactive"
jsonPath = "/tmp/reposcan-report"

[tui]
showVCS = true
```

### Common Commands

```bash
# Scan multiple roots interactively
reposcan -r ~/Code -r ~/work

# Show unpushed work that has not been touched for at least 14 days
reposcan -f unpushed --stale-days 14

# Ignore additional paths, set the worker count, and export JSON
reposcan -r ~/Code -d "**/vendor/**" -w 16 -o json --json-output-path ~/reposcan-reports
```
