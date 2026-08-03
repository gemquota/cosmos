---
type: "concept"
title: "Message Format"
description: "The typed conversation structure (system, user, assistant, tool) that chat APIs use to represent multi-turn dialogue"
tags: ["message-format", "apis", "chat", "protocols"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Message Format

## Summary
Message format is the standard conversational envelope of chat APIs: an ordered list of typed messages — system, user, assistant, and tool — each with role semantics. Getting roles right is a subtle prompt-engineering skill in itself.

## Details
- Roles carry behaviour: system sets standing instructions that persist across the conversation; user is the human input; assistant is the model's own output (and the record of what it said); tool carries tool results linked to assistant tool calls; some APIs add named or developer roles and structured content blocks (text, image, tool_use).
- Mistakes: putting standing instructions in user messages, where they compete with the human's latest input; assistant-continuation confusion — resuming a conversation by repeating assistant text instead of appending; malformed tool-result ordering, where results do not match the call they answer.
- Concrete example: a system prompt holds the agent's rules; the user message holds the task; assistant messages include tool calls; tool messages return results; the API threads them in order — a misordered or duplicated block degrades coherence and can break the loop.
- Failure modes: roles used interchangeably, blurring instruction authority; tool messages without matching assistant calls; truncated histories that drop system context; content blocks in formats the model version does not support; leaking conversation state across users or sessions.
- Tradeoffs: a well-formed message list gives the model clean signals — the alternative, prose-in-a-single-message, loses role semantics and authority; the cost is strict bookkeeping; the mature pattern is canonical message traces, logged and replayable.
- Operational notes: log canonical traces for replay and eval, validate role order, and keep system context at the top.
- RSIS3 relevance: the L1 loop is a message-format machine; mykb logs canonical message traces for replay and eval.

## Related
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — The first and most persistent message
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The API endpoint that consumes message formats
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool messages extend the format
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Messages consume the window
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — Reference message-format implementation
