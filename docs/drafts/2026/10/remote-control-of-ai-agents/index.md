---
title: Remote Control of AI Agents
created: '2026-10-17T17:00:35.675043-07:00'
date: '2026-11-02T08:15:51-08:00'
authors:
  - bendu
label: remote-control-of-ai-agents
license: CC-BY-4.0
tags:
  - programming
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

AI agent CLIs frequently block waiting for the user's input
(approving a command, answering a clarifying question, etc.).
Ideally,
you get notified when an agent is waiting
and reply directly from your phone
without opening the terminal or even the session.

## First-party Support

1. Antigravity CLI/IDE sessions can be viewed and controlled at
   [Antigravity Web/Hub](https://antigravity.google.com/)
   .

1. Claude Code has the most complete first-party support.
   See [Remote Control vs cloud sessions](https://code.claude.com/docs/en/remote-control#remote-control-vs-cloud-sessions)
   for a comparison of all options.

   - [Remote Control](https://code.claude.com/docs/en/remote-control)
     connects [claude.ai/code](https://claude.ai/code)
     or the Claude mobile app (iOS/Android)
     to a Claude Code session running on your machine.
     Code execution and filesystem access stay local.
     Start it with `claude remote-control` (server mode),
     `claude --remote-control` (`--rc`),
     or `/remote-control` (`/rc`) inside a running session.
     Press spacebar (in server mode) to show a QR code
     for opening the session in the Claude app.
     Run `/config` and set **Enable Remote Control for all sessions** to `true`
     to turn it on automatically.
     Available on Pro, Max, Team and Enterprise plans (not with API keys).
     On Team/Enterprise, an admin must enable it first.

   - Mobile push notifications:
     when Remote Control is active,
     run `/config` and enable **Push when actions required**
     (permission prompts and questions)
     and/or **Push when Claude decides**
     (e.g., a long-running task finishes).
     You can then approve or reply from the Claude app.

   - [Channels](https://code.claude.com/docs/en/channels)
     (research preview)
     push events from chat apps (Telegram, Discord, iMessage)
     into a running Claude Code session,
     and Claude can reply back through the same chat.
     Channels supporting
     [permission relay](https://code.claude.com/docs/en/channels-reference#relay-permission-prompts)
     forward permission prompts to the chat
     so that you can approve or deny there.
     This is exactly "reply to a chat message to unblock the agent".
     E.g., `claude --channels plugin:telegram@claude-plugins-official`.

   - [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch)
     lets you message a task from the Claude mobile app
     to the Claude Desktop app on your machine.

   - [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)
     (cloud sessions) runs tasks on cloud infrastructure,
     which can be started and monitored from the browser or the Claude mobile app.

   - [Claude Code in Slack](https://code.claude.com/docs/en/slack):
     mention `@Claude` in a channel to start a cloud session.

1. OpenAI [Codex is available in the ChatGPT mobile app](https://sdtimes.com/ai/openai-announces-codex-for-mobile-devices/) (iOS/Android).
   Pair your phone with the Codex app on your computer by scanning a QR code,
   and then you can monitor threads, approve commands and start new tasks from the phone.
   The host machine has to stay awake and online.

## Third-party Tools

1. [Happy](https://github.com/slopus/happy)
   is an open-source, end-to-end encrypted mobile/web client
   for Claude Code, Codex and other agent CLIs (Antigravity, any ACP CLI, etc.).
   Run `happy` (or `happy claude`) in place of `claude`,
   or `happy codex` for Codex,
   and scan the QR code to connect from your phone or browser.

1. [Clawless](https://github.com/HainanZhao/clawless)
   bridges local agent CLIs (Gemini CLI, OpenCode, Claude Code)
   to Telegram or Slack via ACP (Agent Client Protocol).
   You chat with the agent directly in Telegram/Slack.

1. [HumanLayer](https://github.com/humanlayer/humanlayer)
   used to provide approval workflows (e.g., an MCP server for Claude Code)
   which route approval requests to Slack, email, etc.
   The repo is deprecated now
   and the product has pivoted to a multiplayer coding agent IDE/cloud
   ([humanlayer.com](https://www.humanlayer.com/)).

## Through an Always-on Agent via MCP

Another approach is to connect the coding agent to an always-on agent
through MCP (Model Context Protocol).
You message the always-on agent from your phone;
it relays instructions to the coding agent and brings results back to you.
This requires a bridge that exposes agent-control tools
or a shared message space that both agents check.

1. [Crosswalk](https://crosswalk.to/)
   provides a shared MCP server where agents can post messages and read replies.
   Connect both the coding agent and the always-on agent to the same shared space
   to exchange task requests, progress updates and follow-up instructions.
   Its [agent connection guide](https://crosswalk.to/agents)
   explains that active agents check on a schedule,
   while passive agents catch up when opened.
   Crosswalk carries messages; it does not run or wake the coding agent itself.

1. [Gemini Antigravity Bridge](https://github.com/nandhakumar-murugan/gemini-antigravity-bridge)
   describes an MCP bridge between cloud-based Gemini Spark and local Antigravity.
   Its tools include dispatching coding tasks, checking task status,
   injecting messages into Antigravity conversations,
   and retrieving execution reports.
   This provides a more direct control path than exchanging messages alone.

The coding agent's host must remain awake and reachable for local work to continue.
Whether you can answer a pending question or approve a command remotely
depends on the tools exposed by the bridge and the target agent's integration;
an MCP connection alone does not provide permission-prompt forwarding.

## DIY Approaches

1. [ntfy](https://ntfy.sh/) supports
   [action buttons](https://docs.ntfy.sh/publish/#action-buttons)
   in push notifications.
   An `http` action button can call a webhook you run
   which then feeds the response to the agent.
   Anyone knowing the topic can trigger the webhook,
   so use a hard-to-guess topic and authenticate the webhook.

   ```bash
   curl \
       -H "Actions: http, Approve, https://your-webhook.example/approve; http, Deny, https://your-webhook.example/deny" \
       -d "Agent is requesting permission to run: rm -rf ./cache" \
       ntfy.sh/your-secret-topic
   ```

1. Use hooks of AI agent CLIs (e.g., the `Notification` hook of Claude Code)
   to send a message to Telegram/Slack/ntfy when the agent is waiting for input.
   Note that this is one-way only.
   You need something else (e.g., a bot listening for replies) to send responses back.

1. Run agents in a terminal multiplexer (tmux, Zellij)
   and have a background bot watch pane output for prompts
   (e.g., `(y/n)`).
   The bot notifies you
   and types your reply into the pane,
   e.g., via `tmux send-keys -t agent:0 "your response" Enter`.
   This works with any CLI tool but is fragile.

## References

- [Continue local sessions from any device with Remote Control - Claude Code Docs](https://code.claude.com/docs/en/remote-control)

- [Clawless: Bring Your Own Agent to Telegram & Slack - DEV Community](https://dev.to/hainanzhao/clawless-bring-your-own-agent-to-telegram-slack-291m)

- [Human-in-the-Loop for AI Agents: Best Practices, Frameworks, Use Cases, and Demo - Permit.io](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)

- [OpenAI announces Codex for mobile devices - SD Times](https://sdtimes.com/ai/openai-announces-codex-for-mobile-devices/)
