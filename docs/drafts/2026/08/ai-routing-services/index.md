---
title: AI Routing Services
created: '2026-08-04T19:44:42.449935-07:00'
date: '2026-08-04T19:44:42.449945-07:00'
authors:
  - bendu
label: ai-routing-services
license: CC-BY-4.0
tags:
  - AI
  - routing
  - gateway
  - service
  - API
  - proxy
  - OpenRouter
  - AgentRouter
  - OmniRoute
  - 9router
  - RTK
  - LiteLLm
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Local AI Gateway

```{list-table} 9Router vs OmniRoute Comparison
:header-rows: 1
:name: router-comparison-table

* - Feature / Attribute
  - 9Router
  - OmniRoute (OmniRouter)
* - Best For
  - Token efficiency and simple API failovers for coding agents.
  - Power users needing complex routing, account pooling, and maximum free-tier usage.
* - Key Optimization
  - **Token Compression:** Uses RTK Token Saver to compress tool outputs by 20–40%.
  - **Dynamic Routing:** Offers 13 routing strategies (e.g., lowest latency, cheapest, health) across 60+ providers.
* - Failover Handling
  - **Straightforward:** Automatically switches to a backup/cheaper model when hitting API limits.
  - **Account Pooling:** Chains multiple accounts and generates context handoff summaries so the next model resumes perfectly.
* - Scope & Ecosystem
  - Focused heavily as a streamlined local proxy for tools like Cursor, Cline, and Claude Code.
  - Broader scope; includes Model Context Protocol (MCP) server support and handles advanced reasoning APIs.
```

[OmniRoute](https://github.com/diegosouzapw/OmniRoute)
seems to be the best choice.

- [OmniRoute](https://github.com/diegosouzapw/OmniRoute)

flexible routing strategies

- [9router](https://github.com/decolua/9router)

- [Rust Token Killer (RTK)](https://github.com/rtk-ai/rtk)
  - integrated into 9router

- [LiteLLM](#hands-on-the-ai-gateway-litellm)

## Public AI Gateway Service

```{list-table} AgentRouter vs OpenRouter Comparison
:header-rows: 1
:name: agentrouter-vs-openrouter

* - Feature
  - OpenRouter
  - AgentRouter
* - Primary Focus
  - Commercial & Enterprise production
  - Indie developers & prototyping
* - Platform Fees
  - ~5.5% on credit top-ups
  - None (direct pass-through)
* - Model Catalog
  - 400+ models
  - Dozens (Top commercial & open-weight)
* - Sign-up Perks
  - Access to free-tier models
  - $100–$200 in free credits via GitHub OAuth
* - API Compatibility
  - OpenAI drop-in replacement
  - OpenAI drop-in replacement
```

### AgentRouter

https://agentrouter.org/

[AgentRouter](https://gist.github.com/mzaman/a9409de6ccaa19044fb564936b8c9c4f)

### OpenRouter

https://openrouter.ai/

## References

https://openrouter.ai/rankings
