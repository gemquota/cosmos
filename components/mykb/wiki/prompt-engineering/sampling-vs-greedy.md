---
type: "concept"
title: "Sampling vs Greedy Decoding"
description: "Trade-offs between deterministic greedy decoding and stochastic sampling for generation"
tags: ["sampling-vs-greedy", "decoding", "sampling", "generation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sampling vs Greedy Decoding

## Summary
Trade-offs between deterministic greedy decoding and stochastic sampling for generation

## Details
- Greedy picks the top token each step; sampling draws from the distribution.
- Sampling adds diversity; greedy is more consistent.
- Temperature and top-p shape sampling behavior.
- Choice depends on creativity versus determinism needs.

## Related
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — temperature knob
- [[wiki/prompt-engineering/top-p-sampling|Top-P Sampling]] — nucleus knob
- [[wiki/prompt-engineering/beam-search-decoding|Beam Search Decoding]] — structured alternative
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — sampling for robustness
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — when determinism matters
