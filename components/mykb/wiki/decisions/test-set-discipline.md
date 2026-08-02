---
type: "concept"
title: "Test Set Discipline"
description: "The practice of keeping test data untouched until final evaluation"
tags: ["test-set", "discipline", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Test Set Discipline

## Summary
Test set discipline means the final test data is never used for training, tuning, or decisions until the end.

## Details
- Test set discipline means the final test data is never used for training, tuning, or decisions until the end.
- It protects the credibility of reported numbers.
- Violations (even accidental peeking) invalidate results.
- RSIS3 relevance: the pass verifier runs on files the generator never tuned against.

## Related
- [[wiki/decisions/eval-splits|Eval Splits]] — the structure
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the violation
- [[wiki/concepts/test-set-leakage|Test Set Leakage]] — the leak
- [[wiki/concepts/evals-practice-ai|Evals Practice]] — the norms
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]] — existing graph context
