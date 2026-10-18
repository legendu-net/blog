---
title: Comparison of Google Gemini Products
created: '2026-10-18T00:06:41.898266-07:00'
date: '2026-10-18T00:23:43-07:00'
authors:
  - bendu
label: comparison-of-google-gemini-products
license: CC-BY-4.0
tags:
  - AI
  - Gemini
  - Google
  - Antigravity
  - Chrome
  - workspace
  - MCP
  - agent
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Summary

- For coding and anything that needs your local files,
  use Antigravity CLI (`agy`) or the Antigravity App / IDE (the Antigravity 2.0 desktop app, the original IDE or the IDE extensions).
  They work directly on local files.
  They reach Google Workspace only through MCP servers you configure
  or command line tools such as gog and gws
  (see [](#command-line-tools-for-google-workspace)).
- For questions about your Gmail, Docs, Drive and Calendar,
  Gemini Chat (gemini.google.com) is the easiest.
  Workspace apps are built-in "Connected Apps" that only need a toggle.
  It cannot reach your disk: it only reads copies of the files you upload.
- The Gemini desktop app is Gemini Chat plus a system-wide shortcut, screen sharing,
  Gemini Spark and, on macOS only, Spark's "Connected folders" for local files.
- Gemini Spark is a 24/7 agent running on Google Cloud.
  It has the deepest Workspace integration (it acts on Gmail, Docs, Sheets, Slides, etc.)
  and supports third-party and custom MCP servers.
  It touches local files only via connected folders in the macOS desktop app.
- Gemini in Chrome is the best choice for tasks on web pages (Auto Browse).
  It connects to Gmail and Calendar, but it cannot save files to your computer.

```{list-table} Comparison of Google Gemini Products
---
header-rows: 1
name: google-gemini-products-table
widths: 14 15 14 15 14 14 14
---
* - Aspect
  - Antigravity App / IDE
  - Antigravity CLI
  - Gemini Chat
  - Gemini Desktop App
  - Gemini Spark
  - Gemini in Chrome
* - Form
  - Desktop app (Antigravity 2.0)[^ag-ide] and IDE extensions
  - Terminal app (`agy`)
  - Web app (gemini.google.com) and mobile apps
  - Native app for macOS and Windows
  - Cloud agent, used from the Gemini web, mobile and desktop apps
  - Side panel in the Chrome browser
* - Main use
  - Agentic coding
  - Agentic coding in terminals, SSH sessions and scripts
  - Chat, research, Workspace questions
  - Chat without switching to a browser
  - Long-running and recurring tasks in the background
  - Tasks on web pages
* - Workspace (built-in)?
  - N
  - N
  - Y[^ws-chat]
  - Y[^ws-desktop]
  - Y[^ws-spark]
  - Partial[^ws-chrome]
* - Workspace via MCP?
  - Y[^mcp-ag]
  - Y[^mcp-ag]
  - N[^mcp-chat]
  - N
  - Not needed[^mcp-spark]
  - N
* - Workspace via command line tools?
  - Y[^cli-ag]
  - Y[^cli-ag]
  - N
  - N
  - N
  - N
* - Read local files?
  - Y
  - Y[^lf-cli]
  - Upload only[^lf-chat]
  - macOS: via Spark connected folders[^lf-desktop]; Windows: upload only
  - Only via connected folders (macOS app)[^lf-spark]
  - Only pages open in tabs
* - Write local files?
  - Y
  - Y
  - N
  - macOS: via Spark connected folders; Windows: N
  - Only via connected folders (macOS app)
  - N[^lf-chrome]
* - Run commands?
  - Y
  - Y (optional `--sandbox`)
  - N
  - N
  - On its cloud computer only (not locally)
  - N
* - Support skills?
  - Y[^sk-ag-app]
  - Y[^sk-ag-cli]
  - Y[^sk-chat]
  - Likely[^sk-desktop]
  - Y[^sk-spark]
  - Y[^sk-chrome]
* - Runs when your computer is off?
  - N
  - N[^bg-cli]
  - N
  - N
  - Y (except connected-folder tasks)[^bg-spark]
  - N
* - Linux?
  - Y
  - Y
  - Y (browser)
  - N
  - Y (via web app)
  - Experimental[^linux-chrome]
* - Plan
  - Free, AI Plus, AI Pro, AI Ultra
  - Free, AI Plus, AI Pro, AI Ultra
  - Free, AI Pro, AI Ultra
  - Free, AI Pro, AI Ultra
  - AI Ultra (US first)[^plan-spark]
  - Free; Auto Browse needs AI Pro or Ultra (US)
```

## Antigravity App / IDE

Antigravity now ships as the Antigravity 2.0 desktop app
(which evolved from the Agent Manager of the original VS Code–fork IDE),
the original IDE,
and agent panels as extensions for VS Code and Visual Studio
(JetBrains, Zed and Xcode are in preview).

- **Local files:** Full access to the workspace directory, plus terminal sessions.
  The desktop app also offers sandboxed Chromium browser automation.
- **Google Workspace:** No built-in integration.
  Google publishes official (developer preview) remote MCP servers for Workspace,
  e.g., `https://gmailmcp.googleapis.com/mcp/v1`, `drivemcp`, `docsmcp`, `sheetsmcp`,
  `slidesmcp`, `calendarmcp`, `chatmcp`, the universal `workspacemcp`
  and `https://people.googleapis.com/mcp/v1`.
  Antigravity 2.0, the IDE and the CLI share the MCP configuration file `~/.gemini/config/mcp_config.json`,
  but OAuth tokens are not shared, so you have to authenticate each server in each surface.
  Setting it up requires enrolling in the Developer Preview Program
  and creating your own OAuth client.
  Since the agent can run commands,
  a command line tool such as gog or gws is often a simpler alternative to MCP.

## Antigravity CLI

Antigravity CLI (`agy`) replaces Gemini CLI,
which stopped serving personal accounts (free, AI Pro and AI Ultra) on 2026-06-18
(see [](#develop-with-google-antigravity)).
Enterprise (Code Assist Standard/Enterprise) and paid API key users can still use Gemini CLI.

- **Local files:** The directory where you run `agy` is the workspace.
  Files inside it are allowed and files outside it require your approval.
  You can reference files, directories and glob patterns with `@`,
  and add more directories with `--add-dir`.
- **Google Workspace:** Same as Antigravity App / IDE: MCP servers (stdio or remote HTTP)
  configured in `~/.gemini/config/mcp_config.json` (global) or `.agents/mcp_config.json` (project),
  or command line tools such as gog (which also has an MCP server `gog mcp`) and gws.
  Gemini CLI extensions (e.g., the Google Workspace extension) can be migrated using `agy plugin import gemini`.
- It is the best fit if you work on Linux, over SSH or in scripts.

## Gemini Chat (gemini.google.com)

- **Google Workspace:** Built-in "Connected Apps" for Gmail, Docs, Drive, Calendar, Keep and Tasks.
  You toggle them on in Settings.
  For Workspace accounts, admins allow them by default but can turn them off.
  Third-party apps (e.g., Canva and Instacart) are available too.
  Custom MCP servers can be added under Connected Apps,
  but they are only usable in Gemini Spark tasks.
- **Local files:** No direct access.
  You upload files (up to 10 files per prompt and 100 MB per file)
  and Gemini reads copies of them, so it won't see later edits.
  The same applies to the mobile apps.
- **Skills:** Reusable instructions added via the Customize menu
  (rolling out since 2026-10-13); they will eventually replace Gems.
- Gemini Notebook (formerly NotebookLM) can't reach your disk either.

## Gemini Desktop App

The Gemini app launched on macOS first
and on Windows 10/11 in September 2026.
There is no Linux version.

- **Google Workspace:** Same Connected Apps as Gemini Chat,
  e.g., drafting a summary from Gmail and Google Drive.
- **Local files:**
  - macOS: Yes, via Gemini Spark (version 1.80.15.516+, Apple Silicon, macOS 15+).
    You add folders under "Connected folders" in the Spark tab,
    and Spark can open, edit, rename and reorganize files in them.
    It alerts you (on by default) when it cannot back up a file in a connected folder.
    You can also keep your Mac awake while tasks run.
    Connect only the narrowest folders you need.
  - Windows: Connected folders are not available yet.
    You can attach files and share your screen.
- Other features: a system-wide shortcut (`Alt + Space` on Windows) that opens a floating overlay,
  screen sharing and image generation.

## Gemini Spark

Gemini Spark, announced at Google I/O 2026, is a 24/7 personal agent
built on Gemini 3.5 and the Antigravity harness.
It runs in the cloud (a remote browser and cloud computer),
so tasks continue after you close your laptop.
It supports recurring tasks, triggers, custom skills and multi-step workflows.
It asks for confirmation before high-stakes actions such as spending money or sending emails.

- **Google Workspace:** The deepest built-in integration among all products here.
  It acts on Gmail, Docs, Sheets, Slides, Calendar, etc.,
  e.g., summarizing meeting notes into a Google Doc and drafting a follow-up email.
- **MCP:** Third-party integrations (e.g., Canva, Dropbox, Instacart, OpenTable and Zillow)
  and custom HTTPS MCP servers (personal accounts, 18+, US and English only, Keep Activity on).
- **Local files:** Only via connected folders in the macOS desktop app,
  e.g., turning invoices saved locally into a budget spreadsheet in Google Sheets
  that updates on a schedule.
  Starting tasks on your Mac from the web or mobile apps is announced as "coming soon".

## Gemini in Chrome

Gemini in Chrome is a side panel in Chrome (Windows, macOS, Chromebook Plus, Android and iOS)
that reads the current page and the tabs you add.
Auto Browse clicks, scrolls, types and fills in forms for you
(see [](#automated-web-browsing-tasks-using-gemini-in-chrome)).

- **Google Workspace:** Connected apps for Gmail and Calendar (and Keep on Android),
  plus YouTube, Maps, Shopping and Flights.
  Drive and Docs are not listed,
  though it can of course read a Google Doc open in a tab.
  It asks before sending emails or creating events.
  No MCP support (WebMCP, which lets websites expose tools to Gemini, is upcoming).
- **Local files:** It cannot save files to your computer,
  so downloading files still needs manual help.
  It only sees local files that are open in tabs.
- **Skills:** Since 2026-04, you can save a prompt as a skill
  and run it on the current page (and selected tabs) by typing `/`.
  Prebuilt skills are available in the Skills library (type `/`, then click the compass icon).
- **Linux:** Chrome on Linux lags behind in Gemini features.
  Gemini in Chrome is only experimental on Linux,
  and Skills officially support only macOS, Windows and ChromeOS (with Chrome set to US English).

## References

- [The Gemini app becomes more agentic, delivering proactive, 24/7 help](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)

- [Gemini Spark rolling out to macOS app for local tasks, automation](https://9to5google.com/2026/06/30/gemini-spark-mac-app/)

- [Gemini Spark adds third-party apps, including MCP](https://9to5google.com/2026/06/30/gemini-spark-apps-more/)

- [The Gemini app is now available for Windows](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-windows/)

- [Can Gemini Access Local Files? It Depends Which Gemini](https://stashbase.ai/blog/can-gemini-access-local-files/)

- [Antigravity Overview](https://antigravity.google/docs/overview)

- [Antigravity MCP](https://antigravity.google/docs/mcp)

- [Antigravity Skills](https://antigravity.google/docs/skills)

- [Google Workspace MCP servers in Google Antigravity 2.0, IDE, and/or CLI](https://codelabs.developers.google.com/google-workspace-mcp-antigravity)

- [Antigravity CLI: A Hands-On Guide to Google's Terminal Coding Agent](https://dev.to/arindam_1729/antigravity-cli-a-hands-on-guide-to-googles-terminal-coding-agent-5bc7)

- [Control Gemini App access to Workspace services](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-google-apps-in-gemini-on-or-off)

- [Gemini in Chrome: AI Features Explained (2026 Guide)](https://chromestory.com/2026/10/gemini-in-chrome-ai-features-guide/)

- [Turn your best AI prompts into one-click tools in Chrome](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

- [Introducing skills in the Gemini app and Workspace, plus what's next for Gems](https://workspaceupdates.googleblog.com/2026/09/skills-gemini-app-workspace.html)

- [An update on the launch of skills in the Gemini app and Workspace](https://workspaceupdates.googleblog.com/2026/10/an-update-on-launch-of-skills-in-gemini-app-and-workspace.html)

- [](#command-line-tools-for-google-workspace)

- [](#develop-with-google-antigravity)

- [](#automated-web-browsing-tasks-using-gemini-in-chrome)

[^ag-ide]: See the section Antigravity App / IDE below.

[^ws-chat]: Connected Apps: Gmail, Docs, Drive, Calendar, Keep and Tasks. Admins can turn them off for Workspace accounts.

[^ws-desktop]: Same Connected Apps as Gemini Chat.

[^ws-spark]: Acts on (not just reads) Gmail, Docs, Sheets, Slides, Calendar, etc.

[^ws-chrome]: Gmail and Calendar (plus Keep on Android); Drive and Docs are not listed.

[^mcp-ag]: Official (developer preview) remote MCP servers such as `gmailmcp.googleapis.com` and `drivemcp.googleapis.com`, configured in `~/.gemini/config/mcp_config.json`; or `gog mcp`.

[^mcp-chat]: Custom MCP servers can be added under Connected Apps, but they are only usable in Gemini Spark tasks.

[^mcp-spark]: Workspace is built in. Custom HTTPS MCP servers (added under Connected Apps) are for third-party apps.

[^cli-ag]: The agent can run tools such as gog and gws in a terminal.

[^lf-cli]: The current directory is the workspace; files outside it require approval. Use `--add-dir` to add more directories.

[^lf-chat]: Up to 10 files per prompt and 100 MB per file. Gemini reads copies, so it won't see later edits.

[^lf-desktop]: Via Gemini Spark and "Connected folders" (Apple Silicon, macOS 15+).

[^lf-spark]: Only folders connected in the macOS desktop app; otherwise Spark works on a cloud computer.

[^lf-chrome]: Gemini in Chrome cannot save files to your computer due to security concerns.

[^sk-ag-app]: Agent Skills (`SKILL.md` files) in `.agents/skills/` (project) or `~/.gemini/config/skills/` (global).

[^sk-ag-cli]: Agent Skills (`SKILL.md` files) in `.agents/skills/` (project) or `~/.gemini/antigravity-cli/skills/` (global).

[^sk-chat]: Skills (reusable instructions) began rolling out on 2026-10-13 for personal and Workspace accounts and will eventually replace Gems; Gems move to Settings on 2026-11-17. Skills inside Workspace apps (Docs, Gmail, etc.) are delayed until further notice.

[^sk-desktop]: Skills belong to the Gemini app, so they should be available in the desktop app too, but I could not confirm that.

[^sk-spark]: Custom skills, e.g., checking your inbox for school updates and sending a daily digest.

[^sk-chrome]: Skills are saved prompts invoked with `/`. Officially available on macOS, Windows and ChromeOS (with Chrome set to US English) only, not Linux.

[^bg-cli]: Unless you run it on a remote server, e.g., over SSH.

[^bg-spark]: Tasks on connected folders need the Mac awake ("Keep this Mac awake to run tasks").

[^linux-chrome]: Gemini in Chrome is not officially available on Linux, but it can be enabled experimentally (Glic).

[^plan-spark]: Launched as a beta for Google AI Ultra subscribers in the US. Google's Windows announcement only says it "requires a Google AI subscription", and some sources report that AI Pro is included now. Some sources also report that Google is folding Spark into a "Task mode" in the Gemini app, which I could not confirm.
