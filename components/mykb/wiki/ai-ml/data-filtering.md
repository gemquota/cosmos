---
type: "concept"
title: "Data Filtering"
description: "Removing low-quality, toxic, or off-domain examples from training corpora"
tags: ["data", "quality", "pipeline"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Filtering

## Summary
Data filtering removes low-quality, toxic, or off-domain examples from training corpora before they can degrade a model. It matters because raw web-scale data is mostly noise, and models trained on garbage inherit garbage behavior. Filtering is the first and cheapest quality gate in the data pipeline. Filtering decides what a model will never learn.

## Details
- **Definition** — filtering is the application of rules, classifiers, or similarity signals to exclude examples that do not meet quality, safety, or relevance bars.
- **Techniques** — heuristics such as length and repetition rules, classifier-based toxicity and quality scoring, and embedding-similarity deduplication are common tools.
- **Placement** — filtering runs before and alongside data-deduplication-llm and before curation into instruction or fine-tuning sets.
- **Trade-offs** — aggressive filtering can remove useful minority content and shrink diversity; budgets balance coverage against signal quality.
- **Motivations** — filtering prevents degradation from noisy examples and defends against data-poisoning attacks on training corpora.
- **Worked example** — a pretraining pipeline drops pages with high boilerplate ratios, adult content scores above a threshold, and near-duplicate text blocks.
- **Failure modes** — overly narrow filters bias the corpus, miscalibrated classifiers miscategorize content, and filtering logs that are not reviewed hide systemic losses.
- **Practical relevance** — filtering is the quality-control foundation beneath quality-filtering and fine-tuning-data-curation.
- **Audit** — filter decisions should be sampled and reviewed to catch systematic over-removal.
- **Domain nuance** — filters must respect language and cultural variation rather than applying one global rule.
- **Worked example** — a corpus pipeline drops near-duplicate paragraphs, then audits a sample of removed text for false positives.
- **Failure example** — a filter tuned on one language silently removes valid multilingual content.

## Related
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — the quality-focused variant
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — the deduplication partner
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — the downstream curation stage
- [[wiki/ai-ml/content-moderation-pipelines|Content Moderation Pipelines]] — toxicity filtering
- [[wiki/testing/data-poisoning-llm|Data Poisoning of LLMs]] — the security motivation
