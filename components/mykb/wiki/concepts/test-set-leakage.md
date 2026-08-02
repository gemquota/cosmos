---
type: "concept"
title: "Test Set Leakage"
description: "Test data accidentally influencing training or decisions"
tags: ["leakage", "test-set", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Test Set Leakage

## Summary
Test set leakage is any channel through which test data influences training, tuning, or reporting.

## Details
- Test set leakage is any channel through which test data influences training, tuning, or reporting.
- Channels include web scrapes, human review, and shared embeddings.
- Leakage is usually invisible in scores — it just makes them lie.
- RSIS3 relevance: leaked pass expectations would let the generator 'cheat' the verifier.

## Related
- [[wiki/concepts/train-test-contamination|Train-Test Contamination]] — the direct form
- [[wiki/decisions/eval-splits|Eval Splits]] — the barrier
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the benchmark form
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — the fix layer
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
