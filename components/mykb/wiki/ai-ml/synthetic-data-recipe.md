---
type: "concept"
title: "Synthetic Data Recipes"
description: "Reproducible procedures for generating synthetic training or eval data with LLMs"
tags: ["synthetic-data", "data-generation", "recipes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Synthetic Data Recipes

## Summary
Synthetic data recipes are reproducible procedures for generating synthetic training or evaluation data with LLMs, specifying models, prompts, filters, and diversity controls. They matter because high-quality data is the scarcest resource in model development, and recipes make data production systematic instead of accidental. A good recipe produces data that improves rather than degrades the model. A recipe's worth is proven by the model it produces, not the volume of data.

## Details
- **Definition** — a recipe is a documented pipeline that turns seed ideas into synthetic examples: generator selection, prompts, transformations, filtering, and validation.
- **Components** — recipes specify the generator model, instruction templates, diversity controls, quality gates, and deduplication steps.
- **Quality risk** — synthetic data can amplify model weaknesses and introduce repetitive artifacts; filtering and diversity control are mandatory.
- **Auditability** — documented recipes make synthetic pipelines reproducible and reviewable, which matters for compliance and debugging.
- **Use cases** — recipes produce instruction-datasets, preference data, eval sets, and augmentation examples for fine-tuning-data-curation.
- **Worked example** — a recipe generates ten thousand math word problems with varied difficulty, filters failures with an llm-as-judge check, and deduplicates near-duplicates.
- **Failure modes** — generator bias, distribution collapse, and unfiltered errors all degrade the resulting training data.
- **Practical relevance** — recipes are the production unit of synthetic data, sitting at the center of modern instruction-data production.
- **Seed diversity** — varied seed prompts prevent the generator from collapsing into a few templates.
- **Human review** — small human audits of generated batches catch systematic errors early.
- **Worked example** — a recipe is versioned and re-run monthly with a fixed seed set to keep a training pipeline stable.
- **Failure example** — a recipe that never changes produces data the model has already memorized.

## Related
- [[wiki/ai-ml/synthetic-data-generation|Synthetic Data Generation]] — the umbrella concept
- [[wiki/ai-ml/instruction-datasets|Instruction Datasets]] — the common output
- [[wiki/ai-ml/data-filtering|Data Filtering]] — post-generation gates
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — quality control scoring
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — the integration point
