---
type: "concept"
title: "Beam Search Decoding"
description: "Decoding that keeps the top-k partial sequences at each step to find better outputs"
tags: ["beam-search", "decoding", "search", "generation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Beam Search Decoding

## Summary
Decoding that keeps the top-k partial sequences at each step to find better outputs

## Details
- Beam width k trades diversity and compute against quality.
- Better for structured outputs like translations.
- Prone to repetitive or less diverse text.
- Compare with sampling-vs-greedy strategies.

## Related
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — decoding family
- [[wiki/prompt-engineering/constrained-decoding|Constrained Decoding]] — structural constraints
- [[wiki/agent-systems/translation-agents|Translation Agents]] — classic use
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — sampling alternative
- [[wiki/ai-ml/best-of-n-sampling|Best-of-N Sampling]] — scoring alternative
