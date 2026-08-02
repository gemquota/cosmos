---
type: "concept"
title: "Induction Heads"
description: "Attention heads that copy and complete repeated patterns"
tags: ["induction-heads", "circuits", "attention"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Induction Heads

## Summary
Induction heads are attention heads that detect a repeated token and attend to its next occurrence, enabling copying and in-context learning.

## Details
- Induction heads are attention heads that detect a repeated token and attend to its next occurrence, enabling copying and in-context learning.
- Their discovery in 2021-2022 was a landmark for mechanistic interpretability.
- They appear to be a general circuit for pattern completion in transformers.
- RSIS3 relevance: understanding induction-like circuits informs how in-context knowledge retrieval works.

## Related
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — the framework
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — the behavior
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]] — the substrate
- [[wiki/concepts/circuit-tracing|Circuit Tracing]] — how they were found
- [[wiki/concepts/emergence-in-llms|Emergence in LLMs]] — the full treatment of this theme
