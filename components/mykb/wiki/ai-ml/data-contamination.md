---
type: "concept"
title: "Data Contamination"
description: "Overlap between training data and evaluation data that inflates benchmark scores and misleads comparisons"
tags: ["data-contamination", "evaluation", "benchmarks", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Data Contamination

## Summary
Data contamination occurs when eval examples leak into pretraining or fine-tuning corpora, so the model has effectively seen the test. It silently inflates scores and corrupts the scientific value of benchmarks.

## Details
- Detected via n-gram overlap, memorization probes, and timing analyses (eval released after training cutoffs).
- Worse for closed training corpora where contamination cannot be audited.
- Mitigations: contamination checks before eval, private sets, and periodic re-benchmarking.
- RSIS3 relevance: any benchmark mykb uses must be checked against the training data of models it serves.

## Related
- [[wiki/ai-ml/benchmark-gaming|Benchmark Gaming]] — The behaviour contamination enables
- [[wiki/testing/eval-sets|Eval Sets]] — The datasets at risk
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The practice contamination corrupts
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — Data growth increases contamination risk
- [[wiki/ai-ml/model-cards|Model Cards]] — Contamination disclosure in cards
