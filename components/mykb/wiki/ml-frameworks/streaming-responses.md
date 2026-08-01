---
type: "concept"
title: "Streaming Responses"
description: "Incrementally delivering LLM output as tokens are generated, reducing perceived latency"
tags: ["streaming", "apis", "latency", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Streaming Responses

## Summary
Streaming responses send generated tokens to the client as they appear instead of waiting for the full completion. It is essential for chat UX, long generations, and tool-call events.

## Details
- Server-sent events (SSE) is the standard transport for chat streaming.
- Tool-call deltas arrive as structured fragments that clients must assemble.
- Streaming interacts with usage accounting: token counts still arrive at the end.
- RSIS3 relevance: RSIS3's dashboard and L1 loop can stream long RRP outputs for progressive visibility.

## Related
- [[wiki/ml-frameworks/server-sent-events|Server-Sent Events]] — The transport used for streaming
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The endpoint that supports streaming
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool-call fragments in streams
- [[wiki/prompt-engineering/agent-state|Agent State]] — Consuming partial outputs safely
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — Reference streaming support
