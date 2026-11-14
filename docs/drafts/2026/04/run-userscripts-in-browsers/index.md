---
title: Run UserScripts in Browsers
created: '2026-04-07T00:39:53.808131-07:00'
date: '2026-11-14T08:02:45-08:00'
authors:
  - bendu
label: run-userscripts-in-browsers
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - browser
  - UserScript
  - JavaScript
  - TamperMonkey
  - ViolentMonkey
  - ScriptCat
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## AI Agents

AI agents connected to Chromium-based browsers via the **Chrome DevTools Protocol (CDP)** (`Runtime.evaluate`) can execute arbitrary JavaScript in the page's main world (`window`, `document`, etc.) and mutate the DOM on the fly—achieving the same page-modification capabilities as a userscript extension without installing one:

- **[BrowserOS](https://github.com/browseros-ai/browseros) (`browseros-neo`)**:
  Provides `page.evaluateInPage(fn, arg)` (inside batched `run` scripts) and the `evaluate_in_page` MCP tool to run custom JavaScript directly in the page context.
  Furthermore, `page.saveHelper(name, fn)` persists reusable JavaScript helpers scoped to the current hostname (`location.hostname`), and `save_skill` / `run_skill` save and replay parameterized host-scoped scripts—functioning much like `@match` rules in userscript managers (see [](#ai-browsers-and-agentic-web-automation)).
- **Google Chrome (and other Chromium browsers)**:
  Agents using [`chrome-devtools-mcp`](https://github.com/ChromeDevTools/chrome-devtools-mcp) (`evaluate_script`), Playwright (`page.evaluate()`), or Puppeteer connected over CDP (`chrome://inspect/#remote-debugging` or `--remote-debugging-port`) can similarly inject and execute JavaScript to modify any open tab.

### Example: Bypassing Chrome's Built-in PDF Viewer "Save As" Dialog

When automating document downloads (such as paychecks or statements), clicking the "Download" button inside Chrome's built-in PDF viewer invokes Chrome's internal `SavePackage` / file-picker API, which **always** opens a native OS "Save As" dialog (even when *"Ask where to save each file before downloading"* is disabled) and stalls unattended automation.

An AI agent can bypass the PDF viewer entirely by mutating the page DOM on the fly—injecting a temporary same-origin `<a href="..." download="filename.pdf">` anchor into `document.body` and triggering a direct download to `~/Downloads` (e.g., via `page.download(ref)` in BrowserOS neo):

```javascript
// Inside a BrowserOS neo `run` script:
await page.evaluateInPage(({ url, filename }) => {
  let a = document.getElementById('__agent_dl');
  if (!a) {
    a = document.createElement('a');
    a.id = '__agent_dl';
    a.textContent = 'Agent Direct Download';
    document.body.appendChild(a);
  }
  a.href = url;
  a.setAttribute('download', filename);
}, { url: pdfUrl, filename: 'statement.pdf' });

const snap = await page.snapshot();
// Locate the injected link ref from `snap` and download directly:
const result = await page.download(dlRef);
```

### AI Agents vs. Userscript Extensions

- **Trigger model**: Userscript extensions (like ScriptCat or Tampermonkey) inject scripts **automatically on every page load** matching `@match` / `@include` rules. AI agents mutate the DOM **on demand** during a task, and those mutations only persist until the tab reloads or navigates.
- **Stealth by default**: In BrowserOS neo, standard accessibility and CDP primitives (`snapshot`, `read`, `grep`, `act`, `download`) operate from the browser process without injecting JavaScript into the page's main world; `evaluateInPage` is only invoked selectively when custom DOM manipulation is needed.

## Browser Extensions

[ScriptCat](https://docs.scriptcat.org/en/docs/use/install_comple/)
is preferred to TamperMonkey and ViolentMonkey
as ScriptCat is opensource and support latest versions of Chrome.
TamperMonkey is close sourced
while ViolentMonkey doesn't support the latest version of Chrome (due to Manifest V3).
