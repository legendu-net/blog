---
title: AI Browsers and Agentic Web Automation
created: '2026-11-13T07:46:42.210227-08:00'
date: '2026-11-13T07:50:29-08:00'
authors:
  - bendu
label: ai-browsers-and-agentic-web-automation
license: CC-BY-4.0
tags:
  - programming
  - AI
  - agents
  - browser
  - web
  - automation
  - MCP
  - BrowserOS
  - Chrome
  - Claude
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

This post compares AI-first web browsers and agentic browser automation tools across Linux, macOS, and Android, combining architecture analysis with real-world multi-step task benchmarks. For traditional programmable web automation frameworks (Playwright, Selenium, Puppeteer) see [](#web-automation), and for general browser notes see [](#tips-on-web-browsers).

## Verdict & Recommendations

- **For complex, multi-step agentic web workflows on Linux and macOS: use [BrowserOS](https://github.com/browseros-ai/browseros) (`browseros-neo`).**
  It runs a persistent local MCP server inside an open-source Chromium fork with your live logins, executes multi-step workflows in a single batched `run` call (~15–30 seconds instead of ~7 minutes of turn-by-turn LLM round-trips), always opens and controls tabs in the background without stealing focus, disables background tab throttling on agent tabs, and supports any LLM (local Ollama/LM Studio or BYOK cloud APIs) as well as standard `SKILL.md` skills.
- **For lightweight in-browser page summaries, Q&A, and daily browsing without vendor lock-in: use [Brave Leo](https://github.com/brave/brave-browser).**
  It offers native Linux/macOS/Android support, built-in ad/tracker blocking, and Bring-Your-Own-Model (BYOM) support for local Ollama and OpenAI-compatible endpoints, though its autonomous multi-step agent capabilities are limited.
- **For simple single-tab assistance inside standard Chrome on Windows/macOS: [Gemini in Chrome](https://blog.google/products-and-platforms/products/chrome/gemini-3-auto-browse/)** is convenient if you already subscribe to Google AI Pro/Ultra, but it is experimental on Linux, cannot save local files directly, and is far less capable than BrowserOS neo for complicated multi-step task flows (see [](#automated-web-browsing-tasks-using-gemini-in-chrome)).
- **For automating non-browser desktop GUI applications alongside a browser: use [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).**
  Because it relies on full-screen pixel screenshots and coordinate clicking rather than the browser's Accessibility Tree, it is significantly slower, more token-intensive, and more brittle than BrowserOS neo for pure web automation.

```{list-table} AI Browsers and Agentic Web Automation Tools Comparison
---
header-rows: 1
name: ai-browsers-agentic-web-automation-table
widths: 14 9 6 6 6 6 15 16 8 7 7
---
* - Browser / Agent Tool
  - Status
  - Linux?
  - Background Tabs?
  - Batch Scripting?
  - BYOK / Local LLM?
  - Page Perception
  - Primary Focus
  - Language
  - License
  - Popularity (Stars)
* - [BrowserOS](https://github.com/browseros-ai/browseros)
  - Active
  - Y[^lnx-browseros]
  - Y[^bg-browseros]
  - Y[^bat-browseros]
  - Y[^llm-browseros]
  - Accessibility snapshot (`[ref=eN]`) + DOM
  - Local MCP agent browser (`browseros-neo`) for complex workflows
  - Rust / C++[^lang-browseros]
  - AGPL-3.0
  - ~14.3k ★
* - [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
  - Active
  - Y[^lnx-cdmcp]
  - N[^bg-cdmcp]
  - N[^bat-cdmcp]
  - Y[^llm-cdmcp]
  - Accessibility snapshot (`uid=`) + CDP
  - Official Chrome DevTools MCP server (powers Antigravity `/browser`)
  - TypeScript
  - Apache-2.0
  - ~55.3k ★
* - [Brave Leo](https://github.com/brave/brave-browser)
  - Active
  - Y
  - N
  - N
  - Y[^llm-brave]
  - Page text & DOM context
  - Privacy-first daily browser with BYOM chat & summarization
  - C++
  - MPL-2.0
  - ~24.2k ★
* - [HARPA AI](https://harpa.ai/)
  - Active
  - Y[^lnx-harpa]
  - N
  - Y[^bat-harpa]
  - Y[^llm-harpa]
  - Hybrid DOM + CSS/XPath selectors
  - Chromium extension for web scraping, monitoring & macros
  - TypeScript / JS
  - Proprietary
  - N/A
* - [Gemini in Chrome](https://blog.google/products-and-platforms/products/chrome/gemini-3-auto-browse/)
  - Active
  - N[^lnx-glic]
  - N[^bg-glic]
  - N
  - N[^llm-glic]
  - Built-in Chrome DOM / Gemini context
  - Native Chrome sidebar assistant & Auto Browse
  - C++
  - Proprietary
  - N/A
* - [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)
  - Active
  - Y[^lnx-claude]
  - N[^bg-claude]
  - N
  - N[^llm-claude]
  - Pixel screenshots + `(x, y)` coordinates
  - Full desktop GUI & OS-level visual automation
  - N/A
  - Proprietary
  - N/A
* - [Perplexity Comet](https://www.perplexity.ai/comet)
  - Active
  - N[^lnx-comet]
  - Y
  - N
  - N[^llm-comet]
  - Cloud-assisted DOM & tab context
  - Commercial AI-first research & assistant browser
  - C++
  - Proprietary
  - N/A
```

## Deep Technical Comparison from Real-World Testing

When automating a realistic multi-step workflow—such as logging into a healthcare portal, selecting a patient, traversing a multi-screen scheduling wizard, inspecting available dates/times across providers, and stopping cleanly before final submission—four architectural differences separate **BrowserOS neo** from **`chrome-devtools-mcp`** (Antigravity's built-in `/browser` tool), **Gemini in Chrome**, and **Claude Computer Use**.

### 1. Snapshot (Accessibility Tree) vs. Screenshot (Pixel Image)

A common misconception is that `snapshot` and `screenshot` are synonyms. In agentic browser tools, they are fundamentally different operations:

- **Snapshot (`page.snapshot()` in BrowserOS neo / `take_snapshot` in `chrome-devtools-mcp`)**:
  Queries the browser's **Accessibility Tree** (`Accessibility.getFullAXTree` over CDP) and returns a compact, structured plain-text tree of interactive roles, labels, and short element references:
  ```text
  [ref=e3] button "Schedule an Appointment"
  [ref=e4] button "Check-up, Well Child or Physical"
  [ref=e9] link "Next week"
  ```
  The agent then acts deterministically by reference (`await page.click('e4')`), which resolves directly to the underlying DOM node.
- **Screenshot (`page.screenshot()` / `take_screenshot` / Claude Computer Use)**:
  Renders the visual viewport into a PNG/JPEG bitmap. Vision-based agents like **Claude Computer Use** must encode and upload full-resolution screenshots on every step, visually infer where buttons are, and emit pixel coordinates like `mouse_move(x=412, y=285)`.

**Why Snapshot Wins for Web Automation:**

1. **Deterministic targeting**: Clicking `ref=e4` targets the exact DOM element regardless of window size, DPI scaling, or minor layout shifts. Coordinate clicking frequently misclicks when sticky headers, dynamic banners, or scrollbars shift the page.
1. **Speed and token efficiency**: A filtered interactive snapshot (`page.snapshot()`) is a few hundred tokens of text generated in milliseconds; a sequence of high-resolution screenshots consumes tens of thousands of vision tokens and adds seconds of encoding/inference latency per click.
1. **No visual occlusion required**: Querying the Accessibility Tree does not require the browser window to be visible on the physical monitor, whereas desktop screenshot tools capture whatever window happens to be on top.

### 2. Batch Scripting (`run`) vs. Step-by-Step LLM Round-Trips

Even though both **BrowserOS neo** and **`chrome-devtools-mcp`** use accessibility snapshots, their execution models differ drastically:

- **BrowserOS neo (`run` tool — Batch JS Sandbox)**:
  Exposes a single `run` MCP tool that executes a multi-line JavaScript function inside a sandbox with direct bindings to `browser`, `page`, `snapshot()`, `click()`, `fill()`, and `evaluate()`. A single tool call can open a tab, navigate through five wizard screens, inspect DOM state, and return a compact JSON summary—completing a complex medical scheduling check in **1–3 LLM turns (~15–30 seconds)**.
- **`chrome-devtools-mcp` (`/browser` — One Action per LLM Turn)**:
  Exposes granular single-action tools (`click`, `fill`, `take_snapshot`, `wait_for`). Every time `click` is called (even with `includeSnapshot: false`), `chrome-devtools-mcp` appends the list of all open pages (`# Pages ...`) and requires another LLM round-trip to inspect the next screen. For a multi-step wizard with dropdowns and date pickers, this results in **15–30 sequential LLM turns (~7 minutes)** and floods the context window with repeated full-page snapshots.

### 3. Background Execution vs. Foreground Tab Focus (`bringToFront`)

Can an agent work in a background tab while you keep reading or working in your active tab?

- **Why `chrome-devtools-mcp` steals focus**:
  Although CDP's `Accessibility.getFullAXTree` can read an unfocused tab, `chrome-devtools-mcp` sets `background: false` by default in `new_page` and explicitly calls `Page.bringToFront()` inside `select_page`. Furthermore, standard Chrome heavily throttles background tabs (`requestAnimationFrame` pauses, timers are throttled, and layout/scroll visibility checks in Puppeteer's `element.click()` can stall on occluded tabs).
- **How BrowserOS neo stays in the background**:
  1. **Forced background tab creation**: Both `browser.open(url)` inside `run` and `tabs` (`action: "new"`) hardcode `{ background: true }`, opening tabs in an isolated `<client>/<task>` tab group without switching your active tab.
  1. **Explicit `pageId` targeting**: Every command addresses a specific `pageId` via CDP target session attachment (`browser.getPage(pageId)`) rather than relying on whichever tab is visually active.
  1. **No background throttling on agent tabs**: BrowserOS disables background timer/rendering throttling on agent-controlled tabs so SPA state transitions and `.click()` calls complete at full speed out of sight.

### 4. Connection Reliability on Linux (Flatpak Chrome & Modal Prompts)

On Linux—especially immutable distributions like Fedora Silverblue/Bluefin where Google Chrome runs inside Flatpak (`com.google.Chrome`)—attaching via Chrome DevTools Protocol has sharp edges:

- **`chrome-devtools-mcp` path & permission friction**:
  1. `--autoConnect` looks for `~/.config/google-chrome/DevToolsActivePort`, whereas Flatpak Chrome writes to `~/.var/app/com.google.Chrome/config/google-chrome/DevToolsActivePort` (and Flatpak sandboxes can reject cross-directory symlinks with `ELOOP`).
  1. Every new CDP session triggers Chrome's interactive **"Allow remote debugging?"** modal popup, which times out after 60 seconds if you are away from the keyboard or looking at another workspace.
- **BrowserOS neo zero-prompt local MCP**:
  BrowserOS runs a persistent built-in MCP HTTP server (`http://127.0.0.1:9108/mcp`) directly inside the browser binary. Agents connect instantly with zero modal prompts and full access to your persistent profile and logged-in sessions.

### 5. BrowserOS neo vs. Gemini in Chrome & Claude Computer Use

- **BrowserOS neo vs. Gemini in Chrome (Auto Browse)**:
  - **Platform & Cost**: Gemini in Chrome is officially Windows/macOS-only (experimental Glic flag on Linux) and requires a paid **Google AI Pro or Ultra** subscription for Auto Browse, whereas BrowserOS is open-source (AGPL-3.0), runs natively on Linux x64 and macOS, and works with any local or cloud LLM.
  - **Complex Task Flows**: Gemini in Chrome lives in a single-tab sidebar, cannot save files directly to disk (requiring manual intervention for batch downloads like paychecks or tax PDFs; see [](#automated-web-browsing-tasks-using-gemini-in-chrome)), and cannot be scripted via multi-step JS batches (`run`) or called as an MCP server from terminal coding agents (Claude Code, Antigravity, Gemini CLI, OpenCode). **BrowserOS neo is a much better choice for complicated task flows.**
- **BrowserOS neo vs. Claude Computer Use**:
  - **Scope**: Claude Computer Use can control any desktop application (spreadsheets, native OS dialogs, terminal windows), whereas BrowserOS neo is specialized for web applications.
  - **Web Reliability & Ergonomics**: Because Claude Computer Use operates via full-screen pixel screenshots and simulated mouse/keyboard events, it takes over the visible cursor/display (unless isolated in a container/VM) and struggles with dynamic web dropdowns, scrolling containers, and slow-loading SPAs that BrowserOS neo handles effortlessly via DOM/Accessibility Tree refs.

## Commercial & Alternative AI Browsers

### Perplexity Comet Overview & Security Considerations

**[Perplexity Comet](https://www.perplexity.ai/comet)** is a commercial AI-first browser built on Chromium/Blink that acts as a sidecar personal assistant:

- **Capabilities**: Monitors open tabs, maintains cross-page/cross-session context, connects to Gmail/Outlook/Google Drive/LinkedIn, includes a built-in ad blocker and voice mode, and executes multi-step web tasks (booking travel, comparing products, filling forms).
- **Platform Availability & Pricing**: Available on Windows, macOS, Android, and iOS, with **no official Linux support**. Basic browsing is free; expanded research and agentic workflows require Perplexity Pro (\$20/month) or higher.
- **Privacy, Lock-In & "CometJacking" Risks**:
  - While local history and cookies stay on-device by default, invoking summaries or agentic actions transmits page content and tab context to Perplexity's servers (retained up to 30 days).
  - **Vendor Lock-In**: Requires a Perplexity account and routes all requests through Perplexity's cloud with no local model or BYOK support.
  - **Prompt Injection ("CometJacking")**: Security researchers have demonstrated that hidden instructions embedded in untrusted webpages can hijack the sidecar agent into reading sensitive data from other open tabs or connected services like Gmail and exfiltrating it.

### Other Standalone & Open-Source AI Browsers

- **[ChatGPT Atlas](https://chatgpt.com/atlas/)**: OpenAI's macOS browser designed to autonomously navigate websites and execute multi-step tasks within the ChatGPT ecosystem.
- **[Dia Browser](https://www.diabrowser.com/)**: Focuses on chatting directly with open tabs, drafting text, and planning projects inside the browser (see [](#tips-on-the-dia-browser)).
- **[Opera Neon](https://www.operaneon.com/)**: Commercial subscription browser for Windows and macOS built for deep research, automated shopping, and web projects with offline workflow support.
- **Genspark AI Browser**: Full-agentic browser tailored for automated deep research and multi-step workflows.
- **Sessional**: macOS-only open-source browser integrating Model Context Protocol (MCP) to connect external clients like Claude Desktop.
- **[Moli Browser](https://github.com/lexmount/moli)**: Lightweight Rust-based headless browser designed for fast, low-memory AI agent crawling (see [](#tips-on-the-moli-browser-for-agents)).

## Android Support & Mobile Workarounds

**BrowserOS does not support Android** (and mobile support is not on its roadmap due to its desktop Chromium + local MCP server architecture). Practical ways to run BYOK/local-LLM agentic web tasks from Android include:

```{list-table} Android Agentic Web Automation Workarounds
---
header-rows: 1
name: android-agentic-web-workarounds-table
widths: 22 24 26 28
---
* - Approach
  - Tool
  - BYOK / Custom Endpoints
  - Autonomous Web Control
* - Remote Desktop Trigger
  - BrowserOS + OpenClaw
  - Full desktop BYOK / local Ollama routing
  - Triggers autonomous tasks on Linux/macOS via Telegram, WhatsApp, or Slack
* - Native Android Agent App
  - AIOPE (open-source) or BYOA AI Agent
  - Yes (OpenRouter, Ollama, OpenAI-compatible APIs)
  - Yes (built-in WebView automation & MCP in AIOPE)
* - Browser + Extension
  - Quetta / Mises + Nanobrowser
  - Yes (OpenRouter, OpenAI, Claude, Gemini, Ollama)
  - Yes (clicks, types, and navigates across tabs)
* - Local Terminal
  - Termux + OpenClaw
  - Yes (full local or BYOK API routing)
  - Yes (scripted & agentic browser tasks)
```

## Standard AI Agent Skills (`SKILL.md`) in BrowserOS

BrowserOS natively supports the open `SKILL.md` standard in two complementary directions:

1. **Exposing BrowserOS as a Skill for External Coding Agents**:
   BrowserOS ships official `SKILL.md` bundles—installable via `npx skills add browseros-ai/browseros --skill browseros-neo`—backed by its local MCP server and `browseros-cli`. This exposes over 25 high-level MCP tools (and 50+ browser-control actions) to external coding agents such as Antigravity, Claude Code, Codex, Gemini CLI, Cursor, and OpenCode.
1. **Running Reusable Skills Inside BrowserOS**:
   BrowserOS natively executes reusable `SKILL.md` workflow definitions (shipping with built-in skills for deep research, comparisons, and form automation) and allows saving deterministic `run` scripts via `save_skill` and replaying them via `run_skill`.

## References

- [Web Automation](#web-automation)
- [Automated Web Browsing Tasks Using Gemini in Chrome](#automated-web-browsing-tasks-using-gemini-in-chrome)
- [Tips on Web Browsers](#tips-on-web-browsers)
- [Tips on the Moli Browser for Agents](#tips-on-the-moli-browser-for-agents)
- [Tips on the Dia Browser](#tips-on-the-dia-browser)
- [BrowserOS GitHub Repository](https://github.com/browseros-ai/browseros)
- [Chrome DevTools MCP GitHub Repository](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Claude Computer Use Documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)

[^lnx-browseros]: Native Linux x64 AppImage/deb packages and macOS builds.

[^bg-browseros]: `browser.open(url)` and `tabs` (`action: "new"`) hardcode `background: true` in an isolated agent tab group (`<client>/<task>`) with background tab throttling disabled.

[^bat-browseros]: The `run` MCP tool executes multi-step async JavaScript workflows (`open` -> `snapshot` -> `click` -> `fill` -> `evaluate`) in a single tool call.

[^llm-browseros]: Supports Ollama, LM Studio, OpenRouter, Anthropic Claude, Google Gemini, OpenAI, and any external agent via MCP.

[^lang-browseros]: Companion services and CLI in Rust/TypeScript on top of a C++ Chromium fork.

[^lnx-cdmcp]: Works on Linux, but Flatpak Chrome requires pointing `--wsEndpoint` or symlinking `~/.var/app/com.google.Chrome/config/google-chrome/DevToolsActivePort`, and each connection triggers Chrome's remote-debugging confirmation modal.

[^bg-cdmcp]: `new_page` defaults to `background: false` and `select_page` calls `Page.bringToFront()`, stealing focus in the active browser window.

[^bat-cdmcp]: Each `click`, `fill`, or `take_snapshot` requires a separate MCP tool call and LLM turn.

[^llm-cdmcp]: Model-agnostic MCP server; uses whatever LLM powers the host MCP client.

[^llm-brave]: Supports built-in models plus Bring-Your-Own-Model (BYOM) for local Ollama and custom OpenAI-compatible endpoints on desktop.

[^lnx-harpa]: Runs as a Chromium extension inside Chrome, Brave, or Edge on Linux, macOS, and Windows.

[^bat-harpa]: Supports multi-step YAML/visual macros, scheduled monitors, and webhooks.

[^llm-harpa]: Supports BYOK for OpenAI, Claude, Gemini, OpenRouter, and local Ollama.

[^lnx-glic]: Officially Windows and macOS only; requires enabling experimental `Glic` flags on Linux.

[^bg-glic]: Operates as a sidebar bound to the active tab and requires user confirmation for sensitive actions.

[^llm-glic]: Locked to Google Gemini models; Auto Browse requires a Google AI Pro or Google AI Ultra subscription.

[^lnx-claude]: Typically run inside a Linux Docker container with a virtual X11/Xvfb display or on macOS/Linux desktop.

[^bg-claude]: Controls the visible desktop screen and mouse cursor unless isolated inside a virtual display or container.

[^llm-claude]: Locked to Anthropic Claude models supporting the `computer` tool.

[^lnx-comet]: Available on Windows, macOS, Android, and iOS; no official Linux release.

[^llm-comet]: Locked to Perplexity's cloud infrastructure and account; no local LLM or BYOK support.
