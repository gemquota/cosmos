---
type: "concept"
title: "Data Deduplication for LLMs"
description: "Removing near-duplicate examples from training corpora to improve quality and reduce memorization"
tags: ["data", "quality", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Deduplication for LLMs

## Summary
Removing near-duplicate examples from training corpora to improve quality and reduce memorization

## Details
- Dedup at document, paragraph, and sentence granularity.
- Reduces redundant compute and memorization of duplicates.
- Protects eval integrity by removing test-set contamination.
- A standard early step in data-filtering.

## Related
- [[wiki/ai-ml/data-filtering|Data Filtering]] — pipeline step
- [[wiki/testing/membership-inference-attacks|Membership Inference Attacks]] — privacy link
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — sibling step
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — application
- [[wiki/ml-frameworks/data-loaders-and-pipelines|Data Loaders and Pipelines]] — downstream consumer
