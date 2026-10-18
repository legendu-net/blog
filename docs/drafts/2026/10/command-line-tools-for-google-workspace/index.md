---
title: Command Line Tools for Google Workspace
created: '2026-10-14T10:06:34.010747-07:00'
date: '2026-10-17T23:05:34-07:00'
authors:
  - bendu
label: command-line-tools-for-google-workspace
license: CC-BY-4.0
tags:
  - programming
  - command
  - line
  - Google
  - workspace
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Comparison of gog, GAM7 and gws

- For working with your own Gmail, Calendar, Drive, Docs and Sheets
  from the terminal, in scripts or by AI agents, gog is the best fit.
  It is actively developed, has curated task-oriented commands and strong safety controls,
  and works with consumer Google accounts.
- For administering a Google Workspace domain, use GAM7.
  It only works with paid (or Education/Non-profit) Google Workspace editions.
- gws covers every Google Workspace API (its commands are generated from Google Discovery Service),
  but it is pre-1.0 and has had no commits since March 2026.

```{list-table} Command Line Tools for Google Workspace
---
header-rows: 1
name: google-workspace-clis-table
widths: 16 28 28 28
---
* - Aspect
  - [gog](https://github.com/openclaw/gogcli)
  - [GAM7](https://github.com/GAM-team/GAM)
  - [gws](https://github.com/googleworkspace/cli)
* - Status
  - Active
  - Active
  - Low activity (last commit 2026-03)[^st-gws]
* - Target users
  - Individuals, scripts and AI agents
  - Google Workspace administrators
  - Developers and AI agents
* - Command design
  - Curated, task-oriented commands (e.g., `gog gmail search`), with a Discovery API fallback (`gog api call`)
  - Its own admin-oriented grammar (e.g., `gam print users`, `gam user <email> ...`)
  - Generated at runtime from Google Discovery Service (e.g., `gws drive files list --params '{...}'`), plus `+` helper commands
* - Consumer Google account?
  - Y
  - N[^ca-gam]
  - Y
* - Workspace administration?
  - Partial[^ad-gog]
  - Y[^ad-gam]
  - Y[^ad-gws]
* - Bulk processing?
  - Unknown
  - Y[^bk-gam]
  - Unknown
* - Multiple accounts?
  - Y[^ma-gog]
  - Y[^ma-gam]
  - Unknown[^ma-gws]
* - Output formats
  - JSON (`--json`), TSV (`--plain`), human-readable
  - CSV, optionally uploaded to Google Sheets (`todrive`)
  - JSON (default), table, YAML, CSV (`--format`)
* - AI agent support
  - Agent skills, `gog schema`, MCP server (`gog mcp`)
  - N
  - 100+ agent skills, Gemini CLI extension, `gws schema`[^ag-gws]
* - Safety controls
  - `--readonly`, command allowlists, `--gmail-no-send`, dry-run plans
  - Unknown
  - `--dry-run`, Model Armor (`--sanitize`)
* - Installation
  - Homebrew, `go install`, prebuilt binaries, Docker
  - Install script, Windows installer, `pip install gam7`
  - Prebuilt binaries, npm, Homebrew, `cargo install`, Nix
* - Best fit
  - Personal Google Workspace work and AI agents
  - Domain administration and bulk user/data management
  - Raw access to any Google Workspace API
* - Language
  - Go
  - Python
  - Rust
* - License
  - MIT
  - Apache 2.0
  - Apache 2.0
* - Popularity (Stars)
  - ~8.5k ★
  - ~4.3k ★
  - ~31.6k ★
```

## Other Realted Tools

- [GitHub - google/clasp: 🔗 Command Line Apps Script Projects · GitHub](https://github.com/google/CLASP)

- [GitHub - rclone/rclone: "rsync for cloud storage"](https://github.com/rclone/rclone)

## References

- [gog and gws evaluation — gog](https://gogcli.sh/gws-comparison.html)

- [Gemini Chat - Google Workspace Command Line Tools](https://share.gemini.google/jWkzbiffe76r)

[^st-gws]: Latest release v0.22.5 (2026-03-31). The README warns of breaking changes before v1.0 and says it is not an officially supported Google product.

[^ca-gam]: Requires a paid, or Education/Non-profit, edition of Google Workspace.

[^ad-gog]: `gog admin` and `gog groups`; requires a Workspace domain and a service account with domain-wide delegation.

[^ad-gam]: Core purpose: users, groups, org units, ChromeOS and mobile devices, reports, Vault, etc.

[^ad-gws]: Via the Admin SDK APIs exposed through Discovery.

[^bk-gam]: `gam csv <file> gam ...` runs a command per CSV row; `gam batch`/`gam tbatch` run command files.

[^ma-gog]: Multiple accounts, account aliases (`gog auth alias set`) and `--account`.

[^ma-gam]: Multiple customers/domains via sections in `gam.cfg`.

[^ma-gws]: Not documented in the README; credentials are selected via environment variables such as `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`.

[^ag-gws]: The built-in MCP server (`gws mcp`) was removed.
