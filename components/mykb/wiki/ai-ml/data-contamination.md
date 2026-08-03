---
type: "concept"
title: "Data Contamination"
description: "Overlap between training data and evaluation data that inflates benchmark scores and misleads comparisons"
tags: ["data-contamination", "evaluation", "benchmarks", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Data Contamination

## Summary
Data contamination occurs when eval examples leak into pretraining or fine-tuning corpora, so the model has effectively seen the test. It silently inflates scores and corrupts the scientific value of benchmarks, and it is one of the hardest evaluation problems to detect in closed models.

## Details
Contamination happens through several concrete routes. Web-crawled training corpora routinely include benchmark repositories, LeetCode-style problem sites, and academic papers containing exam questions. Fine-tuning datasets scraped from the same sources compound the problem. Even when a benchmark is released after a model's training cutoff, mirror sites and archived copies can place it inside the corpus, which is why timing alone is not proof of cleanliness.

Detection methods include exact and n-gram overlap checks between eval items and training data, memorization probes that ask the model to continue known strings, and per-item analysis that looks for suspiciously uniform performance across difficulty levels. A model that solves obscure, hard questions while missing easy ones is a classic contamination signal. For closed training corpora the audit cannot be performed at all, so researchers fall back on behavioural signatures and controlled re-testing.

The operational consequences are severe: contaminated results mislead model selection, inflate reported capabilities, and poison downstream decisions such as which model backs an agent loop or which eval set gates a release. Mitigations include running contamination checks before publishing scores, holding out private eval sets that never enter any training pipeline, and periodically re-benchmarking on freshly written items. When contamination is suspected, the honest move is to report the overlap statistics alongside the scores.

RSIS3 relevance: any benchmark mykb uses must be checked against the training data of the models it serves. Because mykb curates and stores content that can later enter fine-tuning or prompt corpora, it should track provenance well enough to answer whether a given eval item could have leaked, and treat public benchmarks as contaminated by default until proven otherwise.

## Related
- [[wiki/ai-ml/benchmark-gaming|Benchmark Gaming]] — The behaviour contamination enables
- [[wiki/testing/eval-sets|Eval Sets]] — The datasets at risk
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The practice contamination corrupts
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — Data growth increases contamination risk
- [[wiki/ai-ml/model-cards|Model Cards]] — Contamination disclosure in cards
