---
type: "concept"
title: "Model Cards"
description: "Structured documentation of a model's training data, intended use, limitations, and evaluation results"
tags: ["model-cards", "documentation", "governance"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Model Cards

## Summary
Model cards are the standard format for documenting machine-learning models: what they are for, how they were trained, what they fail at, and how they were evaluated. They are the trust contract between model publishers and users.

## Details
- Originated with 'Model Cards for Model Reporting' (2019) and are now common practice for frontier labs.
- Sections: intended use, training data, evaluation, limitations, ethical considerations.
- Good cards disclose eval scores, biases, and failure modes; they are not marketing.
- RSIS3 relevance: mykb should attach a model card to every model it benchmarks or serves locally.

## Related
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The results model cards report
- [[wiki/ai-ml/data-contamination|Data Contamination]] — A disclosure model cards should make
- [[wiki/ai-ml/benchmark-gaming|Benchmark Gaming]] — Why cards must report eval methodology
- [[wiki/ai-ml/llama|Llama]] — A family published with model cards
- [[wiki/ai-ml/claude|Claude]] — Frontier family with extensive cards
