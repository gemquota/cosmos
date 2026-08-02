---
type: "concept"
title: "LLM Fine-Tuning"
description: "Updating a pretrained model's weights on task-specific data"
tags: ["fine-tuning", "training", "llm", "transfer-learning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/fine-tuning", "https://arxiv.org/abs/2009.01325"]
---

# LLM Fine-Tuning

## Summary
Fine-tuning updates a pretrained model's weights on curated, task-specific data, adapting its behavior beyond what prompting can achieve. It trades upfront training cost for improved reliability, format adherence, and domain knowledge. Fine-tuning is one option on a spectrum that also includes prompting, retrieval, and RLHF.

## Details
- **When to fine-tune** — when prompting and retrieval fail to hit format, tone, or domain requirements reliably, and when you have enough high-quality data.
- **Data** — instruction datasets or supervised examples, usually hundreds to tens of thousands of examples; data quality dominates results.
- **Methods** — full fine-tuning updates all weights; parameter-efficient methods like LoRA update small adapters at a fraction of the cost.
- **Worked example** — a legal summarizer fine-tunes on 5,000 expert-written case summaries so outputs follow the firm's citation format.
- **Risks** — catastrophic forgetting, overfitting to narrow styles, and evaluation contamination; evals before and after are mandatory.
- **mykb relevance** — fine-tuning and supervised fine-tuning are existing mykb topics; RSIS3 selects between prompting and tuning based on eval results.

## Related
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — efficient fine-tuning
- [[wiki/ai-ml/llm-evaluation-model-serving-llmops|LLM Evaluation, Serving, and LLMOps]] — evaluating fine-tuned models
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — instruction tuning lineage
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — existing fine-tuning concept
- [[wiki/ai-ml/catastrophic-forgetting-mitigation|Catastrophic Forgetting Mitigation]] — forgetting risks
- [[wiki/ai-ml/synthetic-data-generation|Synthetic Data Generation]] — data for tuning
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — tracking tuned models
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — related concept in this cluster
