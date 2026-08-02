---
type: "concept"
title: "Double Descent"
description: "Error curves that rise then fall with model size"
tags: ["double-descent", "interpolation", "theory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Double Descent

## Summary
Double descent describes error curves that decrease, increase near the interpolation threshold, then decrease again as models overparameterize.

## Details
- Double descent describes error curves that decrease, increase near the interpolation threshold, then decrease again as models overparameterize.
- It overturned the bias-variance intuition that bigger models overfit monotonically.
- Implications for training: very large models can generalize where medium ones fail.
- RSIS3 relevance: the wiki's coverage-vs-precision tradeoffs may show the same shape.

## Related
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — the traditional worry
- [[wiki/concepts/grokking|Grokking]] — another non-monotonic curve
- [[wiki/concepts/simplicity-bias|Simplicity Bias]] — the inductive side
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — the practical impact
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — existing graph context
