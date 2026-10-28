---
title: Sidecars, Daemons, and Schedulers in AI Coding Agents
created: '2026-10-27T08:44:50.576100-07:00'
date: '2026-10-27T08:48:07-07:00'
authors:
  - bendu
label: sidecars-daemons-and-schedulers-in-ai-coding-agents
license: CC-BY-4.0
tags:
  - programming
  - AI
  - agent
  - CLI
  - Antigravity
  - Claude Code
  - automation
  - cron
  - sidecar
  - Linux
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Modern AI coding agents (such as Google Antigravity / Jetski and Anthropic Claude Code) have transitioned from simple conversational REPLs into autonomous engineering systems capable of executing recurring maintenance tasks, reacting to real-time events, and operating in headless background environments.

Accomplishing these workflows requires understanding three distinct execution models:

1. **Scheduled Cron Tasks** (ephemeral batch executions)
1. **Continuous Background Daemons** (long-running sidecar processes)
1. **Headless System-Level Schedulers** (Linux `cron` / `systemd` timers)

This article breaks down their architectural underpinnings, examines the Go-based Sidecar implementation in Antigravity, contrasts Anthropic's cloud and desktop execution models, and provides practical guidance on orchestrating autonomous agents reliably.

______________________________________________________________________

## 1. Scheduled Cron Tasks vs. Continuous Background Processes

When designing automated workflows for AI agents, developers frequently conflate **continuous background processes** with **scheduled tasks**. While both operate without interactive human intervention, their lifecycle models and resource profiles differ fundamentally.

### Ephemeral Scheduled Batch Jobs (`builtin: schedule`)

Scheduled tasks are discrete, time-triggered batch jobs:

- **Execution pattern**: The agent wakes up at specified cron intervals (e.g., `0 8 * * *` for daily 8:00 AM runs), initializes a workspace session, executes a multi-step state machine (such as analyzing bank alerts, running test sweeps, or reconciling monthly bills), writes logs or artifacts, and immediately terminates.
- **Resource consumption**: **Zero** CPU and memory footprint between executions. The agent runtime process does not stay active while waiting.
- **State management**: State must be externalized in persistent files (such as YAML/JSON databases, git commits, or transactional logs) so subsequent invocations can reconstruct context.

### Continuous Background Processes (Long-Running Daemons)

Continuous background processes are persistent services running indefinitely:

- **Execution pattern**: Long-running daemons (`restart_policy: always`), useful for filesystem watchers (`inotify`/`fsnotify`), IPC domain socket listeners, local HTTP/gRPC servers, or message queue consumers.
- **Resource consumption**: Continuous baseline memory and event-loop CPU consumption.
- **State management**: Can maintain in-memory state, active connection pools, and long-lived subscriptions.

### The Supervisor Paradox: Why `schedule` Sidecars Use `restart_policy: always`

In supervisor-based architectures (such as Antigravity's `sidecar.json`), a scheduled cron task is configured with:

```json
{
  "builtin": "schedule",
  "restart_policy": "always"
}
```

At first glance, setting `"restart_policy": "always"` on a scheduled job appears contradictory. However, this separates the **supervisor daemon** from the **agent worker**:

1. The **Sidecar Supervisor** is a continuous background daemon that must stay alive `24/7` to monitor the clock, parse cron expressions, and survive host sleep/wake cycles. If this supervisor crashes, it must be restarted immediately (`restart_policy: always`).
1. The **Agent Worker** dispatched by the supervisor is an ephemeral process spawned via IPC/API when the cron trigger fires, completing its prompt turn and exiting.

______________________________________________________________________

## 2. Antigravity / Jetski Sidecar Architecture

Google Antigravity (and its internal Jetski engine) features a modular sidecar architecture designed for headless task automation.

### Go-Based `SidecarManager` Backend

The `SidecarManager` is implemented in **Go** in the backend (`google3/third_party/jetski/cortex/sidecars`) and compiled directly into the unified `agy` / `jetski` binary.

- It is a core daemon capability of the CLI engine, not a feature exclusive to the Electron GUI app.
- It manages child process lifecycles, health checks, cron evaluation, and inter-process communication with agent workspaces.

```
+-------------------------------------------------------------+
|                      agy / jetski Host                      |
|                                                             |
|  +--------------------+             +--------------------+  |
|  |   SidecarManager   |             |   Language Server  |  |
|  |     (Go Engine)    |             | (tryPostAuthInit)  |  |
|  +---------+----------+             +---------+----------+  |
|            |                                  |             |
|            | spawns / monitors                | gates       |
|            v                                  v             |
|  +--------------------+             +--------------------+  |
|  | Sidecar Supervisor |             | Authenticated User |  |
|  | (builtin:schedule) |             |      Session       |  |
|  +---------+----------+             +--------------------+  |
|            |                                                |
|            | cron trigger                                   |
|            v                                                |
|  +-------------------------------------------------------+  |
|  | agentapi new-conversation / send-message              |  |
|  | -> Invokes Ephemeral Antigravity Agent Session        |  |
|  +-------------------------------------------------------+  |
+-------------------------------------------------------------+
```

### Configuration Hierarchy

Automated sidecars in Antigravity are configured across three locations:

1. **Sidecar Definition** (`~/.gemini/config/sidecars/<id>/sidecar.json`):
   Defines the task metadata, schedule arguments, and execution target.

   ```json
   {
     "display_name": "Verizon Bill Analyzer",
     "description": "Runs daily at 8:00 AM to check Bank of America Zelle payment alerts, re-notify unsettled owners after 7 days, or process any new monthly Verizon statement PDF.",
     "builtin": "schedule",
     "args": [
       "0 8 * * *",
       "agentapi",
       "new-conversation",
       "/verizon-bill-analyzer Run the daily automated workflow in /var/home/dclong/archives/verizon: if the latest month in bill.yaml has any owner with payment.settled: false, run Step 7 (check_payments.py) to check Zelle payments, and re-notify any owner unsettled for >= 7 days via Step 6; otherwise, if all owners are settled and a newer monthly statement PDF exists, process the new statement in prod mode."
     ],
     "restart_policy": "always"
   }
   ```

1. **Project Linkage** (`~/.gemini/config/config.json`):
   Enables the sidecar and binds it to a target project ID:

   ```json
   {
     "sidecars": {
       "verizon-bill-analyzer": {
         "enabled": true,
         "projectId": "verizon",
         "schemaVersion": 1
       }
     }
   }
   ```

1. **Project Registry** (`~/.gemini/config/projects/<id>.json` or `~/.gemini/projects.json`):
   Maps the `projectId` to the filesystem path and workspace resources:

   ```json
   {
     "id": "verizon",
     "name": "Verizon (/var/home/dclong/archives/verizon)",
     "projectResources": {
       "resources": [
         {
           "folderUri": "file:///var/home/dclong/archives/verizon"
         }
       ]
     }
   }
   ```

### The `agentapi` Dispatch Protocol

When a cron expression triggers, the supervisor invokes the `agentapi` CLI tool:

- `agentapi new-conversation`: Spawns a clean agent thread in the associated project workspace.
- `agentapi send-message`: Injects prompts or commands into an existing conversation.

### Lifecycle & Prerequisites

For automated sidecars to operate:

- **Project Registration**: A valid `projectId` must exist in `config.json` and match an entry in `projects/<id>.json`.
- **Authentication Gate**: In CLI mode, `SidecarManager` initialization is gated inside the language server method `tryPostAuthInit()`. An active, authenticated user session is required before background sidecars are started.

______________________________________________________________________

## 3. Comparison with Claude Code Automation

Anthropic approaches background automation and scheduling with a different architecture, distributing capabilities across cloud infrastructure, local desktop instances, and interactive sessions.

### Claude Cloud Scheduled Tasks (Routines)

Claude Code supports scheduled tasks executed directly on Anthropic's managed cloud infrastructure:

- **Cloud-Native**: Tasks run in containerized cloud sandboxes without requiring a local workstation or laptop to remain powered on.
- **Plan Quotas**: Cloud scheduled tasks are bundled with paid Claude subscription tiers, with daily run allocations (e.g., 5 runs/day on Pro, 15 runs/day on Max/Team).
- **Ideal Use Case**: Off-hours repo triage, nightly documentation validation, dependency vulnerability scanning, and daily issue summaries.

### Claude Desktop Local Tasks

For workflows requiring local hardware, proprietary network access, or private filesystem manipulation:

- Tasks run directly on the host machine managed by the Claude Desktop application.
- **Limitation**: The host machine must be awake, and the desktop application must be running.

### Interactive Session-Level Polling (`/loop`)

For short-term background monitoring inside an active terminal session, Claude Code provides the `/loop` command:

```sh
# Poll CI status every 5 minutes until finished
/loop 5m check if GitHub Actions CI checks have completed on current PR
```

- **Scope**: Tied to the lifespan of that specific interactive terminal session.
- **Behavior**: Periodically wakes the agent to run the prompt and presents findings in the console.

### Event-Driven vs. Scheduled Tasks: Demystifying `@claude`

A frequent point of confusion is how GitHub PR and issue triggers relate to scheduled tasks:

- **Event-Driven Webhook**: Mentioning `@claude` in a GitHub PR comment or issue does **not** consume Claude Cloud scheduled task quotas.
- Instead, it triggers an event-driven webhook workflow executed inside GitHub Actions runners via [`claude-code-action`](https://github.com/anthropics/claude-code-action).
- The compute and token consumption are billed under GitHub Actions compute minutes and Claude API usage, completely independent of the daily cloud routine allowances.

______________________________________________________________________

## 4. Linux System Cron / Systemd vs. Native Agent Schedulers

When deploying autonomous agents on Linux workstations or servers, developers can choose between **Native Agent Schedulers** (Sidecars or Claude Cloud Routines) and **Operating System-Level Schedulers** (`cron` or `systemd` timers).

### Feature Comparison

```{list-table} Agent Automation Architecture Comparison
---
header-rows: 1
---
- - Architecture
  - Execution Host
  - Uptime Requirement
  - Resumption & Transcript
  - Notification & UI
- - **Antigravity Sidecar**
  - Local Host (`agy`)
  - Signed-in CLI / IDE active
  - SQLite & disk transcripts; interactive resume
  - Desktop notifications, IDE badges, thinking logs
- - **Claude Cloud Routines**
  - Anthropic Cloud
  - 24/7 cloud (zero local uptime)
  - Cloud dashboard logs; quota-capped
  - Email / Claude web notifications
- - **Claude Desktop Tasks**
  - Local Host
  - Desktop App active
  - Desktop session storage
  - Desktop app notifications
- - **System Cron / Systemd**
  - Local / Server OS
  - OS running (headless, survives reboots)
  - Full disk transcripts; CLI `--resume`
  - System logs (`journalctl`), mail, or webhook
```

### Advantages of Native Schedulers

1. **Rich Interactive History**: Native schedulers preserve structured reasoning steps, tool invocation outputs, and diff previews in the agent's native visual interface.
1. **Seamless Human-in-the-Loop Resumption**: If an automated task encounters an ambiguous condition (e.g., an unexpected merge conflict or unverified invoice), a human engineer can jump into the conversation and provide guidance without losing prior context.
1. **Turn-by-Turn Thinking Logs**: Full visibility into internal chain-of-thought tokens and subagent handoffs.

### Advantages of Linux System Cron / Systemd Timers

Executing headless CLI runs via `cron` or `systemd` timers (`agy --prompt "..."` or `claude -p "..."`) provides operational guarantees that GUI apps cannot:

1. **True Headless Independence**: Eliminates reliance on whether VS Code, Electron, or a terminal window is currently open.
1. **Reboot Resilience**: A `systemd` timer configured with `Persistent=true` will trigger missed runs if the machine was offline during the scheduled interval.
1. **Resource Determinism**: Guaranteed clean process exit without background memory leaks.

### Headless Session Persistence & Resumption

A common misconception is that headless runs (`agy --prompt` or `claude -p`) discard conversational history. In reality:

- **Antigravity CLI**: Persists complete conversation sessions, tool invocation records, and artifacts under `~/.gemini/antigravity-cli/brain/<conversation-id>/`. Any automated headless run can be resumed interactively using:
  ```sh
  agy --resume <conversation-id>
  ```
- **Claude Code CLI**: Stores project transcripts under `~/.claude/projects/`. Headless runs executed with `claude -p "..."` can be resumed in terminal mode using:
  ```sh
  claude --resume
  ```

______________________________________________________________________

## 5. Practical Implementation Guidelines

To maximize reliability when deploying autonomous AI coding agents:

1. **Choose Ephemeral Batch Tasks by Default**:
   Unless you explicitly need sub-second reaction to filesystem changes or socket events, implement workflows as ephemeral cron tasks rather than persistent daemons. This prevents memory leaks and ensures clean token context windows.

1. **Always Externalize State**:
   Never rely on agent memory between scheduled executions. Persist state in structured files (`state.yaml`, SQLite, or Git commits). Each run should follow this lifecycle:

   - Read persistent state
   - Perform atomic checks or updates
   - Write updated state
   - Commit changes or notify stakeholders

1. **Set Hard Execution Timeouts**:
   Headless autonomous agents can get caught in retry loops if a tool command blocks. Always enforce command-level or timer-level timeouts:

   ```ini
   # systemd service unit snippet
   [Service]
   Type=oneshot
   TimeoutStartSec=600
   ExecStart=/usr/local/bin/agy --prompt "Run daily repo lint and test audit"
   ```

1. **Combine OS Timers with Native Resumption**:
   For mission-critical production maintenance, the most robust architecture pairs **Linux `systemd` timers** with **native CLI session resumption**. The systemd timer guarantees reliable headless execution, while `agy --resume` / `claude --resume` allows human operators to inspect and continue any run that requires manual intervention.

______________________________________________________________________

## References

- [](#develop-with-google-antigravity)
- [](#tips-on-claude)
- [](#ai-agent-code-cli)
- [Antigravity Documentation](https://antigravity.google/docs/home)
- [Claude Code Documentation](https://code.claude.com/docs/en/quickstart)
- [Claude Code Action for GitHub](https://github.com/anthropics/claude-code-action)
- [systemd.timer Documentation](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)
