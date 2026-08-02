---
type: "concept"
title: "Train-Test Contamination"
description: "Training data overlapping with evaluation data"
tags: ["contamination", "evals", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Train-Test Contamination

## Summary
Train-test contamination occurs when evaluation examples appear (directly or near-duplicate) in training data.

## Details
- Train-test contamination occurs when evaluation examples appear (directly or near-duplicate) in training data.
- It inflates benchmark scores and masks true generalization.
- Detection uses duplicate and near-duplicate search against training corpora.
- RSIS3 relevance: the wiki's eval of retrieval quality must exclude pages used to build the index.

## Related
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the benchmark form
- [[wiki/concepts/eval-contamination|Eval Contamination]] — the broad form
- [[wiki/concepts/test-set-leakage|Test Set Leakage]] — the mechanism
- [[wiki/concepts/memorization-vs-generalization|Memorization vs Generalization]] — the consequence
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/ai-ml/data-contamination|Data Contamination]] — existing graph context
