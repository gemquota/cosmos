---
type: "concept"
title: "Quality Filtering"
description: "Selecting training data by learned or heuristic quality scores rather than raw availability"
tags: ["data", "quality", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Quality Filtering

## Summary
Selecting training data by learned or heuristic quality scores rather than raw availability

## Details
- Scores come from classifiers, heuristics, and model-based judgments.
- High-quality subsets often train better than larger noisy sets.
- Applies to both pretraining and fine-tuning corpora.
- Feeds synthetic-data-recipe and instruction datasets.

## Related
- [[wiki/ai-ml/data-filtering|Data Filtering]] — broader filtering family
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — scoring mechanism
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — consumer
- [[wiki/ai-ml/data-labeling-workflows|Data Labeling Workflows]] — human scoring
- [[wiki/ai-ml/instruction-datasets|Instruction Datasets]] — beneficiary
