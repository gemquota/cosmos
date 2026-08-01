---
type: "concept"
title: "Anthropic API"
description: "Anthropic's hosted API for Claude models, with emphasis on safety, long contexts, and tool use"
tags: ["anthropic-api", "apis", "claude", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Anthropic API

## Summary
The Anthropic API serves Claude models with a documented message protocol, token counting, and tool-use support. Its docs are a reference for prompt engineering and agent patterns.

## Details
- Messages API supports system prompts, multi-turn context, and tool definitions.
- Token counting endpoint enables precise budget planning.
- Documentation includes best-practice guides for system prompts and tool use.
- RSIS3 relevance: Claude backends slot into RSIS3 via the same message/tool abstractions.

## Related
- [[wiki/ai-ml/claude|Claude]] — The model family served
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool use via the API
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — Token counting support
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — The comparable competing surface
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — Anthropic's interoperability standard
