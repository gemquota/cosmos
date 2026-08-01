---
type: "concept"
title: "Token Budgets"
description: "Explicit allocation of the context window across system prompt, history, retrieval, and output to keep calls reliable and affordable"
tags: ["token-budgets", "context-windows", "cost", "prompt-engineering"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://docs.anthropic.com/en/docs/build-with-claude/token-counting"]
---

# Token Budgets

## Summary
A token budget is a deliberate plan for how a context window is spent: fixed caps for the system prompt, a rolling history window, a retrieval allowance, and reserved output space. Budgeting is what makes long-window models actually reliable, since unbounded context breeds cost and drift.

## Details
- Anthropic's token-counting docs show how to measure messages precisely (character-based estimates differ from real tokenizers).
- Typical split: system 1-2K, history 8-32K rolling, retrieved evidence 4-16K, output up to max_tokens, leaving headroom against truncation.
- Budgets must reserve output space: if the window is full, generation truncates or fails regardless of max_tokens settings.
- Token counting is an API-level primitive: both Anthropic (count_tokens) and OpenAI (usage fields) expose exact counts for telemetry.
- Budget drift is the #1 silent cost driver in agent loops; logging per-call usage enables regression detection.
- RSIS3 relevance: L1 tool loops can accumulate state; a budget policy (e.g., 'history capped at 20 turns, compress beyond that') keeps pulses stable.

## Related
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The capacity that budgets allocate
- [[wiki/prompt-engineering/prompt-compression|Prompt Compression]] — Compression is the budget tool for overflowing contexts
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — Budget discipline is the core of context engineering
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]] — Tokens, not characters, are the budget unit
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The API surface where budgets are enforced
- [[wiki/ml-frameworks/streaming-responses|Streaming Responses]] — Streaming exposes token usage incrementally
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Budget policy documentation lives in the wiki
- [[wiki/concepts/mykb-implementation-report|mykb Implementation Report: 6-Phase Buildout — Actual State, Architecture, and Results]] — Token accounting implemented in the buildout
