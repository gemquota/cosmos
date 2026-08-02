---
type: "concept"
title: "Context Compression"
description: "Reducing the size of context through summarization, extraction, or dropping low-value content"
tags: ["context", "summarization", "tokens"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Context Compression

## Summary
Reducing the size of context through summarization, extraction, or dropping low-value content

## Details
- Compression keeps information while cutting tokens: summaries, key-value extraction, pruning.
- Long conversations are the main target.
- Trade-off: information loss versus cost and latency savings.
- Should be evaluated against task accuracy, not just token counts.

## Related
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — governs when to compress
- [[wiki/prompt-engineering/prompt-compression|Prompt Compression]] — prompt-level variant
- [[wiki/ml-frameworks/context-distillation|Context Distillation]] — training-time compression
- [[wiki/agent-systems/summarization-agents|Summarization Agents]] — summarization tooling
- [[wiki/ml-frameworks/long-context-techniques|Long-Context Techniques]] — alternative to compression
