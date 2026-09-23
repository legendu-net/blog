---
title: Great Command Line Tools Developed in Rust
created: '2022-12-21T10:14:53-08:00'
date: '2026-09-23T01:28:36-07:00'
authors:
  - bendu
label: great-command-line-tools-developed-in-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - alternative
  - command line
  - rewrite
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

(great-command-line-tools-developed-in-rust-git-tools)=

:::\{list-table}
:header-rows: 1
:widths: 15 20 65

- - Category
  - Tool
  - Description
- - General
  - [GQL](https://github.com/AmrDeveloper/GQL)
  - Is a query language with a syntax very similar to SQL with a tiny engine to perform queries on .git files instance of database files, the engine executes the query on the fly without the need to create database files or convert .git files into any other format, note that all Keywords in GQL are case-insensitive similar to SQL.
- - General
  - [tealdeer](https://crates.io/crates/tealdeer)
  - Is a very fast implementation of tldr in Rust: simplified, example based and community-driven man pages.
- - General
  - [halp](https://github.com/orhun/halp)
  - Aims to help find the correct arguments for command-line tools by checking the predefined list of commonly used options/flags. Additionally, it provides a prompt for quick access to the manual page or cheat sheet of the given command.
- - General
  - [Atuin](https://github.com/ellie/atuin)
  - Replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.
- - General
  - [see](https://github.com/guilhermeprokisch/see)
  - Is a powerful file visualization tool for the terminal, offering advanced code viewing capabilities, Markdown rendering, and more. It provides syntax highlighting, emoji support, and image rendering capabilities, offering a visually appealing way to view various file types directly in your console.
- - General
  - [bat](bat-is-a-better-alternative-to-cat)
  - Is a cat clone with syntax highlighting and Git integration.
- - General
  - [exa](https://github.com/ogham/exa)
  - Is a modern replacement for ls.
- - General
  - [procs](https://github.com/dalance/procs)
  - Is a modern replacement for ps written in Rust.
- - General
  - [sd](https://github.com/chmln/sd)
  - Is an intuitive find & replace CLI (sed alternative).
- - General
  - [skim](https://github.com/skim-rs/skim)
  - Is a fuzzy finder implemented in rust!
- - System Monitoring
  - [bottom](https://crates.io/crates/bottom)
  - Is a customizable cross-platform graphical process/system monitor for the terminal. It supports Linux, macOS, and Windows.
- - System Monitoring
  - [sniffnet](https://crates.io/crates/sniffnet)
  - Is an application to comfortably monitor your network traffic.
- - System Monitoring
  - [trippy](https://github.com/fujiapple852/trippy)
  - Combines the functionality of traceroute and ping and is designed to assist with the analysis of networking issues.
- - System Monitoring
  - [gping](https://github.com/orf/gping)
  - Is ping with a graph.
- - System Monitoring
  - [bandwhich](https://crates.io/crates/bandwhich)
  - Is a CLI utility for displaying current network utilization by process, connection and remote IP/hostname.
- - System Monitoring
  - [below](https://github.com/facebookincubator/below)
  - Is an interactive tool to view and record historical system data.
- - Disk Usage
  - [dust](https://github.com/bootandy/dust)
  - Is a more intuitive version of du in rust.
- - Disk Usage
  - [dua-cli](https://crates.io/crates/dua-cli)
  -
- - Navigation and Searching
  - [ripgrep](the-ripgrep-command-is-a-better-alternative-to-the-find-command)
  - Recursively searches directories for a regex pattern while respecting your gitignore.
- - Navigation and Searching
  - [igrep](https://github.com/konradsz/igrep)
  - Runs grep (ripgrep's library) in the background, allows interactively pick its results and open selected match in text editor of choice (vim by default).
- - Navigation and Searching
  - [broot](https://github.com/Canop/broot)
  - Provides a new better way to see and navigate directory trees.
- - Git Tools
  - [gitui](https://github.com/extrawurst/gitui)
  - Provides you with the comfort of a git GUI but right in your terminal.
- - Git Tools
  - [gitoxide](https://github.com/Byron/gitoxide)
  - Is an implementation of git written in Rust for developing future-proof applications which strive for correctness and performance while providing a pleasant and unsurprising developer experience.
- - Git Tools
  - [git-leave](https://crates.io/crates/git-leave)
  - Checks for unsaved or uncommitted changes on your machine.
- - Git Tools
  - [Stacked Git](https://github.com/stacked-git/stgit)
  - StGit for short, is an application for managing Git commits as a stack of patches.
- - Git Tools
  - [delta](https://github.com/dandavison/delta)
  - Is a syntax-highlighting pager for git, diff, and grep output.
- - Git Tools
  - [difftastic](https://github.com/Wilfred/difftastic)
  - Is a structural diff tool that compares files based on their syntax.
- - Git Tools
  - [git-cliff](https://github.com/orhun/git-cliff)
  - Can generate changelog files from the Git history by utilizing conventional commits as well as regex-powered custom parsers. The changelog template can be customized with a configuration file to match the desired format.
- - Git Tools
  - [tokei](https://github.com/XAMPPRocky/tokei)
  - Is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language.
- - Git Tools
  - [onefetch](https://github.com/o2sh/onefetch)
  - Is a command-line Git information tool written in Rust that displays project information and code statistics for a local Git repository directly to your terminal. The tool is completely offline - no network access is required.
- - Misc
  - [grex](https://github.com/pemistahl/grex)
  - Is a command-line tool and Rust library for generating regular expressions from user-provided test cases.
- - Misc
  - [ruff](https://github.com/charliermarsh/ruff)
  - Is an extremely fast Python linter, written in Rust.
- - Misc
  - [Rome](https://github.com/rome/tools)
  - Provides unified developer tools for JavaScript, TypeScript, and the web.
- - Misc
  - [carbonyl](https://github.com/fathyb/carbonyl)
  - Is a Chromium based browser built to run in a terminal.
- - Misc
  - [speedtest-rs](https://github.com/nelsonjchen/speedtest-rs)
  - A tool like speedtest-cli, but in Rust.
- - Misc
  - [mprocs](https://github.com/pvolok/mprocs)
  - Runs multiple commands in parallel and shows output of each command separately.
- - Security
  - [Nosey Parker](https://github.com/praetorian-inc/noseyparker)
  - Is a command-line program that finds secrets and sensitive information in textual data and Git history.
- - Security
  - [rtx](https://github.com/jdxcode/rtx)
  - Is a version manager for multiple programming languages.
- - Good Ones but Which I Won't Use
  - nushell
  -

:::

## References

- [Rewritten in Rust: Modern Alternatives of Command-Line Tools](https://zaiste.net/posts/shell-commands-rust/)

- [Awesome Alternatives in Rust](https://github.com/TaKO8Ki/awesome-alternatives-in-rust)
