---
type: "concept"
title: "Fine-Tuning Data Curation"
description: "Selecting and preparing high-quality training examples for supervised fine-tuning"
tags: ["fine-tuning", "data", "curation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fine-Tuning Data Curation

## Summary
Selecting and preparing high-quality training examples for supervised fine-tuning

## Details
- Quality and diversity beat raw volume for instruction tuning.
- Includes dedup, filtering, and label auditing.
- Curation pipelines feed instruction-datasets and preference-datasets.
- Directly determines downstream model behavior.

## Related
- [[wiki/ai-ml/instruction-datasets|Instruction Datasets]] — main output
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — dedup step
- [[wiki/ai-ml/data-filtering|Data Filtering]] — noise removal
- [[wiki/ai-ml/data-labeling-workflows|Data Labeling Workflows]] — labeling step
- [[wiki/ai-ml/supervised-fine-tuning|Supervised Fine-Tuning]] — training consumer
