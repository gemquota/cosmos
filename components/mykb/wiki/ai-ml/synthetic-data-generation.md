---
type: "concept"
title: "Synthetic Data Generation"
description: "Creating training, eval, or retrieval data programmatically with models"
tags: ["synthetic-data", "data-generation", "training", "evaluation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2108.07258", "https://arxiv.org/abs/2005.14165"]
---

# Synthetic Data Generation

## Summary
Synthetic data generation uses models or programmatic pipelines to create training examples, evals, and retrieval corpora. It scales data production beyond human labeling and enables scenarios that are rare or sensitive in the wild. Quality control is the crux: synthetic data inherits and amplifies model biases.

## Details
- **Techniques** — self-instruct-style prompt bootstrapping, template expansion, back-translation, and domain-rule generators.
- **Uses** — instruction tuning data, preference pairs for DPO, RAG evaluation corpora, and augmentation for fine-tuning.
- **Quality controls** — filtering by model scoring, deduplication, and human spot-checks; synthetic data must be validated against real behavior.
- **Worked example** — a team generates 50k synthetic support-ticket variations from 500 real tickets, then fine-tunes a classifier and eval-scores it against 1,000 human-labeled tickets.
- **Risks** — contamination of public benchmarks, feedback loops of errors, and distribution shift from real traffic.
- **mykb relevance** — synthetic data recipes and data-labeling workflows are mykb topics for building evals without heavy labeling budgets.

## Related
- [[wiki/ai-ml/instruction-datasets|Instruction Datasets]] — target of synthetic generation
- [[wiki/ai-ml/synthetic-data-recipe|Synthetic Data Recipes]] — recipes for generation
- [[wiki/ai-ml/data-labeling-workflows|Data Labeling Workflows]] — human labeling alternative
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — measuring synthetic data quality
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — cleaning generated data
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — filtering generated data
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — fine-tuning practice
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — instruction tuning
