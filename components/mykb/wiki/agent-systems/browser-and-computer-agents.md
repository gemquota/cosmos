---
type: "concept"
title: "Browser and Computer Agents"
description: "Agents that operate web browsers or entire computer interfaces to complete tasks"
tags: ["agents", "browser", "computer-use", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.anthropic.com/en/docs/build-with-claude/vision", "https://platform.openai.com/docs/guides/vision"]
---

# Browser and Computer Agents

## Summary
Browser and computer agents interact with the world through human interfaces — clicking, typing, and reading screens — rather than APIs. They unlock tasks where no API exists. Reliability is hard: the interface is noisy, visual, and slow, so these agents lean on vision models, structured DOM observations, and careful verification.

## Details
- **Browser agents** — driven via CDP or browser automation, reading accessibility trees or screenshots, acting through structured tool calls.
- **Computer-use agents** — operate the full OS (mouse, keyboard, screenshots), as demonstrated by computer-use models; higher risk, broader reach.
- **Observation strategies** — DOM/text observations are more reliable and cheaper than pixels; screenshots help when layout matters.
- **Verification** — after each action the agent checks the resulting page state; confirmations and screenshots are logged for audit.
- **Worked example** — a form-filling agent logs in (via injected session, never passwords), fills fields, submits, and verifies the success page.
- **mykb relevance** — relevant to RSIS3 workflows that must interact with web dashboards and external tools without APIs.

## Related
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — sandboxing browser agents
- [[wiki/llm-agents/grounding-vision-to-text|Grounding Vision to Text]] — vision observations
- [[wiki/llm-agents/user-confirmation-flows|User Confirmation Flows]] — confirmations before risky clicks
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — structured tool use
- [[wiki/llm-agents/ocr-and-document-ai|OCR and Document AI]] — reading document content
- [[wiki/agent-systems/session-replay-agents|Session Replay for Agents]] — replaying browser sessions
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
