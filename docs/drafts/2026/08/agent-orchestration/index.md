---
title: Agent Orchestration
created: '2026-08-08T22:19:59.650925-07:00'
date: '2026-11-03T09:37:03-08:00'
authors:
  - bendu
label: agent-orchestration
license: CC-BY-4.0
tags:
  - AI
  - agent
  - harness
  - orchestration
  - graph
  - engineering
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Agent orchestration can mean managing existing coding agents or building an application
whose agents coordinate through code. For running a fleet of Claude Code, Codex,
OpenCode, or other installed agents, start with a session manager or agent workspace.
A multi-agent application framework serves a different purpose.

## Coding Agent Managers

The comparison below focuses on launching, monitoring, and steering existing agents.
Capabilities were checked against the linked official documentation on November 3, 2026.
Development activity is marked Unknown where a recent commit date could not be verified.

```{list-table} Coding Agent Manager Comparison
---
header-rows: 1
name: coding-agent-manager-comparison
widths: 15 10 22 18 18 17
---
* - Agent Manager
  - Development Status
  - Agents and Authentication
  - Parallel Work
  - Mobile and Remote Access
  - Best Fit
* - [Orca](https://github.com/stablyai/orca)
  - Unknown
  - Terminal agents; existing subscriptions
  - Isolated Git worktrees; compare results
  - Mobile companion; SSH workspaces
  - Integrated fleet workspace
* - [Paradev](https://github.com/ParadevAI/Paradev)
  - Unknown
  - CLI agents; existing subscriptions
  - Worktrees; monitoring; diff review
  - Remote hosts; cloud; iOS[^mobile-paradev]
  - Closest overall Orca alternative
* - [Happy](https://github.com/slopus/happy)
  - Unknown
  - Claude, Codex, Grok, Gemini; existing subscriptions[^auth-happy]
  - Multi-provider tasks and subagents
  - Encrypted phone access; own server
  - Phone access and shared sessions
* - [Agent of Empires](https://github.com/agent-of-empires/agent-of-empires)
  - Unknown
  - Installed agent CLIs and their authentication
  - Persistent tmux sessions; worktrees; containers
  - TUI and web dashboard; phone browser
  - Linux and self-hosted servers
* - [Emdash](https://github.com/generalaction/emdash)
  - Unknown
  - Installed CLI agents
  - Worktrees; issue intake; diff review
  - Linux/macOS/Windows desktop; SSH/SFTP
  - Cross-platform desktop and ticket workflows
* - [Agentastic](https://www.agentastic.dev/)
  - Unknown
  - CLI agents; provider subscriptions or keys
  - Worktrees; containers; manager agents
  - Native macOS; iPhone beta; SSH/cloud
  - Native Mac workspace and delegated work
* - [Conductor](https://www.conductor.build/)
  - Active (October 2026 releases)
  - Claude Code, Codex, Cursor, OpenCode; subscriptions or keys
  - Cloud microVMs; shared workspaces
  - macOS; iOS; API
  - Cloud execution and team collaboration
* - [Nimbalyst](https://github.com/Nimbalyst/nimbalyst)
  - Active (October 2026 releases)
  - Claude Code, Codex; OpenCode/Copilot in alpha
  - Worktrees; visual editing; task board
  - Linux/macOS/Windows; iOS companion
  - Specs, diagrams, and rendered diff review
* - [Herdr](https://github.com/herdrdev/herdr)
  - Unknown
  - Existing agents in their own terminals
  - Persistent panes; status; socket API
  - Linux/macOS/Windows terminal; SSH hosts
  - Terminal-based fleet control
* - [Paseo](https://github.com/getpaseo/paseo)
  - Unknown
  - Installed agent CLIs and credentials
  - Worktrees; cross-provider orchestration
  - Daemon; desktop/web/CLI; iOS/Android
  - Self-hosted runtime across devices
* - [OpenChamber](https://github.com/openchamber/openchamber)
  - Unknown
  - OpenCode runtime and its provider configuration
  - Multi-run; optional worktrees; scheduled goals
  - Desktop/web/VS Code; iOS/Android; remote access
  - Visual workspace for OpenCode
* - [CLI Agent Orchestrator](https://github.com/awslabs/cli-agent-orchestrator)
  - Unknown
  - External CLI providers; supervisor/worker profiles
  - tmux windows; handoffs; assignments; messaging
  - CLI; API/MCP; browser dashboard
  - Programmatic delegation across CLI agents
* - [Vibe Kanban](https://github.com/BloopAI/vibe-kanban)
  - Sunsetting
  - Multiple authenticated coding-agent CLIs
  - Task board; branches; inline review
  - Web UI; remote deployment
  - Existing installations; evaluate sunset plans first
```

### Choosing a Manager

**Orca** combines terminals, worktrees, agent monitoring, and diff review in one
workspace. Its SSH workspaces run agents on another machine, and its mobile
companion lets you monitor progress and send follow-ups. Its terminal-based approach
accommodates agents beyond a fixed provider list. See the
[official feature overview](https://github.com/stablyai/orca#features).

**Paradev**, formerly Superset, is the closest overall alternative in this shortlist.
It supports independent worktrees, persistent terminals, agent status indicators,
and reviewing changes before merging. Its CLI, SDK, and MCP server allow scripts
and agents to manage workspaces; automations add scheduled or event-triggered work.
Desktop support prioritizes macOS, with experimental Linux builds and no Windows
build at the time checked. See the
[official README](https://github.com/ParadevAI/Paradev).

**Happy** is a strong choice when phone access matters. Its mobile app can send
prompts, answer permission requests, stop turns, and inspect changes. Session
synchronization between devices is end-to-end encrypted. Happy Agent can run on
your own server so work continues while your laptop sleeps. The original Happy CLI
also offers remote access to terminal Claude Code and Codex sessions. See the
[mobile guide](https://happy.engineering/mobile-app/) and
[remote-server guide](https://happy.engineering/guides/remote-server/).

**Agent of Empires** is particularly suitable for Linux and server workflows.
It is written in Rust and uses tmux for persistent agent sessions, with optional
Git worktrees and container isolation. Its terminal and browser interfaces manage
the same sessions, including a phone-friendly web view. See the
[official documentation](https://github.com/agent-of-empires/agent-of-empires/blob/main/docs/index.md).

**Vibe Kanban** combines task planning, multiple coding-agent backends, workspace
isolation, and inline feedback. However, its
[README](https://github.com/BloopAI/vibe-kanban) explicitly announces that it is
sunsetting. Prefer another candidate for a new setup unless you intend to maintain
your own deployment.

### Additional Alternatives

**Emdash** is an Apache-2.0 desktop app for Linux, macOS, and Windows. It detects
installed coding-agent CLIs, gives tasks separate worktrees and branches, and
imports tickets from services including Linear, GitHub, and Jira. SSH/SFTP support
extends the workflow to remote projects. It is a strong candidate for cross-platform
desktop use. See its [official README](https://github.com/generalaction/emdash).

**Agentastic.dev** provides a native macOS workspace for coding agents, code review,
and an embedded browser. Agents can use Git worktrees or Docker/Apple containers;
Manager Agents can assign and steer workers. SSH and cloud execution support
remote work, and an iPhone TestFlight companion supports approvals and follow-ups.
See the [official product overview](https://www.agentastic.dev/).

**Conductor** at conductor.build runs Claude Code, Codex, Cursor, and OpenCode using
your subscriptions or keys. Its cloud workspaces use isolated microVMs, and teams
can share a workspace and prompt agents together. macOS, iOS, and API access make
it a candidate for hosted execution and collaborative work. See the
[official overview](https://www.conductor.build/). This is distinct from Microsoft's
Conductor CLI and the Conductor workflow engine.

**Nimbalyst** is an MIT-licensed visual workspace for Linux, macOS, and Windows,
with an iOS companion. It combines parallel agent worktrees with Markdown,
Mermaid, Excalidraw, and mockup editors, plus rendered diff review and task tracking.
Claude Code and Codex are supported; its README labels OpenCode and Copilot
integrations alpha. Prefer it when planning documents and visual artifacts are
central. See the [README](https://github.com/Nimbalyst/nimbalyst) and
[recent releases](https://github.com/Nimbalyst/nimbalyst/releases).

**Herdr** is an Apache-2.0 Rust runtime that manages agents' terminals through a
background server. Its terminal interface shows agent status and supports
persistent sessions, remote SSH machines, and CLI/socket control by other agents.
The project also offers a [separate desktop app](https://github.com/herdrdev/herdr-app);
the terminal runtime is the relevant option for avoiding a GUI. See the
[upstream README](https://github.com/herdrdev/herdr).

**Paseo** uses a daemon to manage installed agent CLIs on your workstation or server.
Desktop, web, CLI, iOS, and Android clients connect to the same runtime. Agents can
create worktrees, launch other agents, and communicate across providers; a
TypeScript SDK supports custom orchestration. An optional encrypted relay helps
pair devices. Its desktop client uses Electron, so the daemon/web/CLI deployment
is the option for avoiding a desktop GUI. See the
[official README](https://github.com/getpaseo/paseo).

**OpenChamber** is an MIT-licensed workspace built around OpenCode, with desktop,
web, VS Code, iOS, and Android interfaces. Multi-run sends a task to several models
in separate sessions, optionally with separate worktrees. Session Goals and
scheduled prompts support continued work, while remote access connects other
devices to the host. Model access comes through OpenCode's provider configuration;
shell access alone does not establish native supervision of arbitrary external
agent CLIs. See the [official README](https://github.com/openchamber/openchamber).

**CLI Agent Orchestrator (CAO)** from AWS Labs coordinates supervisor and worker
agents in separate tmux windows. It supports synchronous handoffs, asynchronous
assignments, direct messaging, scheduled flows, MCP tools, and a browser dashboard.
Documented CLI providers include Claude Code, Codex, Kiro, OpenCode, and Copilot.
Its supervisor is itself backed by a CLI provider; the documentation does not
establish a separate raw-model API supervisor. Terminal/context isolation also
should not be confused with separate working files. See the
[official introduction](https://awslabs.github.io/cli-agent-orchestrator/docs/intro/).

Existing subscriptions authenticate the underlying agents; they do not imply that
all manager features or hosted runtimes are free. Also distinguish a remote control
from a remote runtime: controlling a laptop from a phone still requires the laptop
to stay awake. Running the agent on a server removes that dependency.

## Frameworks and Other Related Projects

**[Aider](https://github.com/Aider-AI/aider)** is a coding agent that can serve as
a worker in a scripted orchestration workflow. It connects to hosted model APIs
and local models through Ollama or OpenAI-compatible endpoints. Its
[`--message` option](https://aider.chat/docs/scripting.html) performs one task and
exits, making it usable from supervisor scripts. Parallel worktree creation,
scheduling, and fleet monitoring belong to the surrounding manager or scripts.
See its [model connection documentation](https://aider.chat/docs/llms.html).

The following links cover building agent systems and harnesses beyond the fleet
management comparison above. They are retained as further research candidates.

- [MetaGPT](https://github.com/FoundationAgents/MetaGPT)
- [AutoGen](https://github.com/microsoft/autogen)
- [CrewAI](https://github.com/crewaiinc/crewai)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [OpenHarness](https://github.com/HKUDS/OpenHarness)
- [Omnigent](https://github.com/omnigent-ai/omnigent), which describes itself as an
  agent framework and meta-harness for orchestrating existing coding agents.
- [Restate](https://github.com/restatedev/restate)

## References

- [Agentastic: Orca Alternatives](https://www.agentastic.dev/alternatives/orca)
- [Paradev: Orca Alternative](https://paradev.com/compare/orca-alternative)
- [Agent Orchestration Tools Explained](https://share.gemini.google/ge87HRlhor2p)
- [我用 Rust 撸了个自编排的 Agent，它拥有了"自我完善"的能力，群友：这难道是传说中的Graph Engineering ？](https://mp.weixin.qq.com/s/YECoz0HODWz3CqC6D4SCDw?poc_token=HN8TeGqjUsi2tX34IA8ztkasvAfF_ZoLNYVMHHfg)

[^mobile-paradev]: [Paradev's README](https://github.com/ParadevAI/Paradev)
    documents iPhone/iPad support requiring Pro and iOS/iPadOS 26 or later.
    Access to a workspace on your own machine requires that host to remain online.

[^auth-happy]: [Happy's overview](https://happy.engineering/) documents Claude,
    Codex, and Grok subscription sign-in, plus Gemini through Google sign-in via
    Antigravity. Support depends on the provider and harness integration.
