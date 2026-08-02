---
type: "concept"
title: "Tree of Thought Variants"
description: "Extensions of tree-of-thought search with different branching, scoring, and backtracking policies"
tags: ["tot-variants", "reasoning", "search", "decoding"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tree of Thought Variants

## Summary
Extensions of tree-of-thought search with different branching, scoring, and backtracking policies

## Details
- Variants tune branching factor, depth limits, and node scoring.
- Some use verifier models, others LLM self-scoring.
- Cost grows with tree size; pruning is essential.
- Bridge to monte-carlo-tree-search-llm.

## Related
- [[wiki/ai-ml/tree-of-thought-search|Tree of Thought Search]] — base algorithm
- [[wiki/prompt-engineering/monte-carlo-tree-search-llm|Monte Carlo Tree Search for LLMs]] — rollout-based variant
- [[wiki/prompt-engineering/beam-search-decoding|Beam Search Decoding]] — scoring parallel
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — node evaluation
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — sample-based alternative
