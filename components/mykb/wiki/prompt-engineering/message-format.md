---
type: "concept"
title: "Message Format"
description: "The typed conversation structure (system, user, assistant, tool) that chat APIs use to represent multi-turn dialogue"
tags: ["message-format", "apis", "chat", "protocols"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Message Format

## Summary
Message format is the standard conversational envelope of chat APIs: an ordered list of typed messages — system, user, assistant, and tool — each with role semantics. Getting roles right is a subtle prompt-engineering skill in itself.

## Details
- Roles carry behaviour: system sets standing instructions, user is the human, assistant is the model, tool carries tool results.
- Mistakes: putting instructions in user messages (overridable), assistant-continuation confusion, and malformed tool-result ordering.
- Some APIs allow named/developer roles and structured content blocks (text, image, tool_use).
- RSIS3 relevance: the L1 loop is a message-format machine; mykb logs canonical message traces for replay and eval.

## Related
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — The first and most persistent message
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The API endpoint that consumes message formats
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool messages extend the format
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Messages consume the window
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — Reference message-format implementation
