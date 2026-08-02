---
type: "concept"
title: "Long Context Techniques"
description: "Methods for extending or effectively using very long model contexts"
tags: ["long-context", "context", "architecture", "techniques"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Long Context Techniques

## Summary
Methods for extending or effectively using very long model contexts

## Details
- Include RoPE scaling, sliding windows, and sparse attention.
- Effective use also needs retrieval and summarization strategies.
- Long context raises cost and attention complexity.
- Practical systems still rely on context engineering.

## Related
- [[wiki/ml-frameworks/rope-embeddings-sliding-window|RoPE and Sliding Window Attention]] — positional methods
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — attention efficiency
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — usage strategy
- [[wiki/prompt-engineering/context-compression|Context Compression]] — shrinking what fits
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — memory for long context
