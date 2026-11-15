---
title: Prompt Engineering for LLM Tools
created: '2025-05-30T08:26:03-07:00'
date: '2026-11-15T12:20:40-08:00'
authors:
  - bendu
label: prompt-engineering-for-llm-tools
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - LLM
  - prompt
  - engineering
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Most things on this page are obsolete given the development of agent and skills.
In general,
skills are preferred to plain prompts.
However,
sometimes you do still want to manage prompts.
And in that case,
[fabric](manage-ai-prompts-using-fabric)
is a great tool.

- [Gemini API - Prompt Gallery](https://ai.google.dev/gemini-api/prompts)

- [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts)

- [Awesome Awesome Prompts](https://github.com/dukeluo/awesome-awesome-prompts)

- [Prompt Programming](https://github.com/ai-boost/awesome-prompts?tab=readme-ov-file#prompt-programming)

## Tips and Traps

1. Set temporature (if using LLMs in Google AI Studio).

1. Give examples in a prompt can help.

1. Leverage built-in tools provided by LLM products.
   For example,
   Google AI Studio provides the tool "grounding with google search" (obsolete with agent/skills).

1. A single comprehensive prompt including all details is better than interactively improving your prompt.

   - Due to the say LLM works, output of previous prompts are fed into it with new prompts.
     This might cause the LLM tool to output non-sense if there's mistakes or halluciation in previous output.

   - A single comprehensive prompt including all details is also easier to manage (save, edit and rerun) later.

1. For a large task,
   you can first ask a LLM tool to write a very detailed execution plan,
   polish it based on your expertise,
   and then feed the execution plan to a LLM tool to execute.

## Tools for Generating and Managing Prompts

```{list-table}
---
header-rows: 1
---
- - Feature/Tool
  - Vellum.ai
  - PromptPerfect (Jina AI)
  - Humanloop
  - Dust.tt
  - LangChain (+LangSmith)
  - LlamaIndex
  - LiteLLM
  - Spreadsheets (Sheets/Excel)
  - Text Editors + Git
  - AI Model Playgrounds
  - Meta-Prompting (LLMs)
- - **Primary Focus**
  - End-to-end Platform
  - Prompt Optimization
  - Feedback & Iteration Platform
  - Building LLM Apps
  - Developer Framework
  - RAG Developer Framework
  - LLM API Abstraction
  - Simple Org & Variation
  - Flexible Text & Versioning
  - Interactive Experimentation
  - AI-Assisted Prompt Creation
- - **Prompt Generation**
  - Playground, Templating
  - AI-driven optimization, Variations
  - Playground, Templating
  - Templating, Chaining
  - Advanced Templating, Parsers
  - Templating (RAG-focused)
  - N/A (tests same prompt)
  - Component Combination
  - Manual Text Entry
  - Direct Iteration
  - LLM-generated suggestions
- - **Prompt Management**
  - Versioning, A/B, Eval, Deploy
  - Limited
  - Versioning, A/B, Feedback Loop
  - App Versioning, Collab
  - Code (Git), LangSmith (Observability)
  - Code (Git)
  - Model Routing
  - Manual
  - Git for Versioning, Folders
  - Basic Saving/Presets
  - N/A
- - **Collaboration**
  - Yes
  - Limited
  - Yes
  - Yes
  - Via Git, LangSmith
  - Via Git
  - N/A
  - Basic Sharing
  - Via Git
  - Limited
  - N/A
- - **A/B Testing**
  - Yes
  - No
  - Yes
  - Via app versions
  - Manual or via LangSmith
  - Manual
  - Facilitates
  - Manual
  - Manual
  - Manual
  - N/A
- - **Versioning**
  - Yes
  - No
  - Yes
  - Yes (for apps)
  - Yes (Git)
  - Yes (Git)
  - N/A
  - Manual
  - Yes (Git)
  - Limited
  - N/A
- - **Key LLM Integrations**
  - OpenAI, Anthropic, etc.
  - Many models
  - OpenAI, Anthropic, etc.
  - OpenAI, Anthropic, etc.
  - All major LLMs
  - All major LLMs
  - 100+ LLMs
  - N/A (manual)
  - N/A (manual)
  - Provider-specific
  - Via API
- - **Target User**
  - Teams, Production
  - Individuals, Teams (Refinement)
  - Teams, Product Builders
  - Devs, Internal Tools
  - Developers
  - Developers (RAG)
  - Developers
  - Individuals, Simple Needs
  - Individuals, Devs
  - Individuals, Quick Tests
  - Anyone
- - **Pricing Model**
  - Paid
  - Freemium
  - Paid
  - Open Source, Paid Cloud
  - OS (LangChain), LangSmith (Paid)
  - Open Source
  - Open Source
  - Free
  - Free (most tools)
  - Usage-based (API)
  - Usage-based (API)
- - **Learning Curve**
  - Moderate
  - Easy
  - Moderate
  - Moderate-Steep
  - Moderate-Steep
  - Moderate-Steep
  - Easy-Moderate
  - Easy
  - Easy (Editors), Mod (Git)
  - Easy
  - Easy
- - **Key Strength**
  - Comprehensive, Prod-ready
  - Optimizes existing prompts
  - Evaluation & Feedback Loop
  - Building internal LLM apps
  - Versatility, Ecosystem, Observability
  - Best for RAG
  - Multi-model API ease
  - Accessible, No cost
  - Flexible, Robust Versioning
  - Immediate Feedback
  - Idea generation, Phrasing
- - **Potential Weakness**
  - Paid, Overkill for solo
  - Not full management suite
  - Paid
  - Steeper curve
  - Code-heavy, LangSmith setup
  - RAG-specific
  - Not prompt content itself
  - Manual, Not scalable
  - Manual setup for mgmt
  - Basic mgmt, Not for teams
  - Output quality varies
```

## Examples of Prompt

> You are an expert at making ascii art. Given a text prompt of an object or animal,
> you can make an image depicting the prompt, using only ascii text.
> Please be creative, and make liberal use of whitespace characters.
> Please use code blocks as needed.
> Avoid repeating the same lines.
> Prefer profile reviews, not top down views or face views.
> Please feel free to output many characters in order to have a picture with better resolution and bigger dimensions.

> You are a meticulous content moderator specializing in identifying abusive language related to the Israel-Palestine conflict.\
> Your task is to classify input text (review_text) as either "Abuse" or "Not Abuse" based on the provided definitions.\
> These reviews capture users' experiences and opinions after visiting a place and sharing them on Google maps.
> "Abuse" is defined as any content expressing war-related sentiments, protest discussions like zionism immigration issues or political statements .
> "Not Abuse" encompasses all other content not related to the conflict. Provide the Label: [Abuse or Not Abuse]

> You are the best sales man at a kia ev9 dealership.
> I'm interested in kia ev9, either the land or the gt-line trim.
> Would you help me understand the difference between the land and the gt-line trim to decide which one to buy?

# Step by Step Instructions

1. **Read the input:** Carefully review the provided review_text variable. The review_text contains the text to be classified.

1. **Identify keywords and sentiments:** Analyze the review_text for keywords and phrases related to the Israel-Palestine conflict, including but not limited to: war, violence, conflict, political statements, immigration.

1. **Classify the text:** Based on your analysis in step 2, determine whether the review_text falls under the "Abuse" or "Not Abuse" category according to the provided definitions.

1. **Format the output:** Label: [Abuse or Not Abuse]

## References

- [I save every great ChatGPT prompt I find. Here are the 15 that changed how I work.](https://www.reddit.com/r/ChatGPT/comments/1qblp9j/i_save_every_great_chatgpt_prompt_i_find_here_are/)
