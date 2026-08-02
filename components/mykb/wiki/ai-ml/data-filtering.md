---
type: "concept"
title: "Data Filtering"
description: "Removing low-quality, toxic, or off-domain examples from training corpora"
tags: ["data", "quality", "pipeline"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Filtering

## Summary
Removing low-quality, toxic, or off-domain examples from training corpora

## Details
- Uses heuristics, classifiers, and embedding similarity for removal.
- Filtering budgets trade coverage against signal quality.
- Prevents degradation from noisy examples.
- Often precedes data-deduplication-llm.

## Related
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — quality-focused variant
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — dedup partner
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — SFT application
- [[wiki/ai-ml/content-moderation-pipelines|Content Moderation Pipelines]] — toxicity filtering
- [[wiki/testing/data-poisoning-llm|Data Poisoning of LLMs]] — security motivation
