---
type: "concept"
title: "Chat Completions"
description: "The chat endpoint pattern (messages in, assistant message out) that most LLM APIs standardize on"
tags: ["chat-completions", "apis", "chat", "protocols"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Chat Completions

## Summary
Chat Completions is the canonical API shape: send a message list with roles, receive an assistant message (possibly with tool calls). Its message-format conventions are cloned by OpenAI-compatible servers everywhere.

## Details
- Request fields: model, messages, temperature, top_p, max_tokens, tools, response format.
- Response includes content, tool calls, finish reasons, and usage token counts.
- Streaming variants emit deltas via server-sent events.
- RSIS3 relevance: every RSIS3 model backend — hosted or local — speaks this shape.

## Related
- [[wiki/prompt-engineering/message-format|Message Format]] — The protocol it transports
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — The reference implementation
- [[wiki/ml-frameworks/ollama|Ollama]] — Local OpenAI-compatible endpoint
- [[wiki/prompt-engineering/function-calling|Function Calling]] — Tool calls in responses
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — Structured response formats
