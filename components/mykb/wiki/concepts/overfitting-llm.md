---
type: "concept"
title: "Overfitting in LLMs"
description: "Memorization at the expense of generalization in language models"
tags: ["overfitting", "llm", "generalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Overfitting in LLMs

## Summary
Overfitting in LLMs is the model fitting training specifics — exact text, formatting quirks, benchmark answers — instead of general rules.

## Details
- Overfitting in LLMs is the model fitting training specifics — exact text, formatting quirks, benchmark answers — instead of general rules.
- It surfaces as benchmark contamination and memorization of private data.
- Detection: held-out paraphrase sets and contamination audits.
- RSIS3 relevance: template memorization in the graph is its overfitting analogue.

## Related
- [[wiki/concepts/underfitting-llm|Underfitting in LLMs]] — the opposite failure
- [[wiki/concepts/memorization-vs-generalization|Memorization vs Generalization]] — the spectrum
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the benchmark symptom
- [[wiki/concepts/regularization-practice|Regularization in Practice]] — the mitigation
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/ai-ml/data-contamination|Data Contamination]] — existing graph context
