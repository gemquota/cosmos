---
type: "concept"
title: "Best-of-N Sampling"
description: "Generating several candidate outputs and selecting the best by a reward model or judge"
tags: ["sampling", "reward", "alignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Best-of-N Sampling

## Summary
Generating several candidate outputs and selecting the best by a reward model or judge

## Details
- Increases output quality beyond single sampling at Nx inference cost.
- Selection uses a reward model, LLM judge, or task metric.
- Common in RLHF pipelines for preference data collection.
- The simple baseline that rejection-sampling generalizes.

## Related
- [[wiki/ai-ml/rejection-sampling|Rejection Sampling]] — filtering variant
- [[wiki/ai-ml/reward-modeling|Reward Modeling]] — selection signal
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — judge-based selection
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — voting variant
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — sampling family
