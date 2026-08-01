---
type: "concept"
title: "OpenAI API"
description: "OpenAI's hosted API surface: chat completions, embeddings, fine-tuning, and tool calling"
tags: ["openai-api", "apis", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# OpenAI API

## Summary
The OpenAI API is the most widely used hosted LLM interface, defining conventions — messages, tokens, temperature, tool calls — that other providers clone. It is the reference implementation for prompt-system integrations.

## Details
- Chat Completions is the core endpoint; Responses and Assistants layers add state and tools.
- Usage fields return exact token counts, enabling budget telemetry.
- Fine-tuning, embeddings, and structured outputs are first-class API features.
- RSIS3 relevance: RSIS3's L1 loop can target OpenAI-compatible endpoints across many local and hosted runtimes.

## Related
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The core endpoint
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — Vector retrieval endpoint
- [[wiki/ai-ml/gpt-4|GPT-4]] — The flagship models served
- [[wiki/prompt-engineering/function-calling|Function Calling]] — Tool support in the API
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — Structured output modes
