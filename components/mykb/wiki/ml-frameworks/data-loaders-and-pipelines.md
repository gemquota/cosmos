---
type: "concept"
title: "Data Loaders and Pipelines"
description: "Infrastructure that streams, shuffles, and preprocesses training data into the training loop"
tags: ["data", "training", "pipeline"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Loaders and Pipelines

## Summary
Infrastructure that streams, shuffles, and preprocesses training data into the training loop

## Details
- Loaders shard datasets across workers, shuffle deterministically, and prefetch batches.
- Pipelines handle tokenization, augmentation, and on-the-fly filtering.
- Dataset bottlenecks are a common hidden cause of slow runs.
- Streaming loaders allow training on corpora larger than local storage.

## Related
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — dedup happens upstream
- [[wiki/ai-ml/data-filtering|Data Filtering]] — quality gates before the loader
- [[wiki/ml-frameworks/runs|Experiment Runs]] — consumers of the pipeline
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — curation step for SFT
- [[wiki/ai-ml/synthetic-data-generation|Synthetic Data Generation]] — data source feeding pipelines
