---
title: Web Automation
created: '2019-09-07T09:02:30-07:00'
date: '2026-11-13T07:49:26-08:00'
authors:
  - bendu
label: web-automation
license: CC-BY-4.0
tags:
  - programming
  - web
  - automation
  - Selenium
  - PlayWright
  - Puppeteer
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## AI-based Tools

For a comprehensive comparison of AI browsers and agentic web automation tools—including [BrowserOS](https://github.com/browseros-ai/browseros) (`browseros-neo`), `chrome-devtools-mcp`, Gemini in Chrome, Claude Computer Use, Perplexity Comet, Brave Leo, and HARPA AI—see [](#ai-browsers-and-agentic-web-automation).

### BrowserOS (BrowserOS neo)

[BrowserOS](https://github.com/browseros-ai/browseros) (`browseros-neo`) is an open-source (AGPL-3.0) Chromium-based AI browser for Linux, macOS, and Windows with a built-in local MCP server and `SKILL.md` support.
It is currently the best choice for complex, multi-step agentic web workflows because it:

- Queries the browser's Accessibility Tree (`snapshot`) with deterministic element refs rather than relying on slow pixel screenshots.
- Executes multi-step workflows in a single batched JavaScript `run` call (~15–30 seconds instead of ~7 minutes of turn-by-turn LLM round-trips).
- Opens and controls tabs in the background (`background: true`) with background tab throttling disabled, never stealing focus from your active browser tab.
- Reuses your persistent browser profile and live logins with local or BYOK models (Ollama, OpenRouter, Claude, Gemini, OpenAI).

See [](#ai-browsers-and-agentic-web-automation) for architectural details and benchmarks.

### Stagehand

[Stagehand](https://github.com/browserbase/stagehand-python)
is a browser automation framework used to control web browsers with natural language and code.
By combining the power of AI with the precision of code, Stagehand makes web automation flexible, maintainable, and actually reliable.

### Gemini in Chrome

[Gemini in Chrome](https://blog.google/products-and-platforms/products/chrome/gemini-3-auto-browse/) provides a built-in Chrome sidebar assistant and Auto Browse mode (requires Google AI Pro or Ultra).
While convenient for simple single-tab tasks on Windows and macOS, it is experimental on Linux, cannot save local files directly, and is much less capable than BrowserOS neo for complicated multi-step workflows.
See discussions in [](#automated-web-browsing-tasks-using-gemini-in-chrome) and [](#ai-browsers-and-agentic-web-automation).

### Claude Computer Use

[Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) can automate any desktop GUI application (not just web browsers) by taking full-screen pixel screenshots and simulating mouse coordinates and keystrokes.
However, for web automation it is significantly slower, more token-expensive, and less reliable than Accessibility Tree / DOM-based tools like BrowserOS neo (see [](#ai-browsers-and-agentic-web-automation)).

- [I Let Claude Use My Computer for 2 Days. Here's What It Can Actually Do.](https://aiblewmymind.substack.com/p/claude-computer-use-guide-6-workflows-tested)

- [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)

### [UI Vision](https://ui.vision/)

[UI Vision](https://ui.vision/)

Easy hybrid workflow automation with Selenium-style commands, Computer Vision/OCR, and AI - all from a simple browser extension.

## [playwright](https://github.com/microsoft/playwright)

Node.js library to automate Chromium, Firefox and WebKit with a single API https://playwright.dev

## Selenium

Selenium is a great web automation tool!

[Here](https://hub.docker.com/u/selenium)
are official Docker images for selenium.

## [Puppeteer](https://github.com/GoogleChrome/puppeteer)

## iMacros

## OculiX / SikuliX

OculiX / SikuliX is able to automate anything visual
but it is hard to scale and not reliable.

## [AppliTools](https://applitools.com/)

[AppliTools](https://applitools.com/)
is an expensive commercial solution.
It offers 14-day free trial though.

## References
