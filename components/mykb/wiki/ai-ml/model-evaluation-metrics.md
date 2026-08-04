---
type: "concept"
title: "Model Evaluation Metrics"
description: "Quantitative measures used to score model outputs across tasks"
tags: ["evaluation", "metrics", "benchmarks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model Evaluation Metrics

## Summary
Model evaluation metrics are quantitative measures that score model outputs across tasks, from accuracy to semantic similarity to judge-based ratings. They matter because metrics are how teams decide whether a change is an improvement, and the wrong metric leads to the wrong conclusion. Metric choice must match the task and the cost of failure. The honest metric set includes both aggregate scores and their error bars.

## Details
- **Definition** — a metric maps model outputs to scores that can be aggregated, compared, and tracked over time.
- **Families** — metrics span exact-match accuracy, F1 for classification, rouge-bleu-bert-score for text similarity, and llm-as-judge ratings for open-ended quality.
- **Matching** — the right metric depends on the task: translation needs adequacy measures, classification needs error rates, and conversational quality needs judgment.
- **Distributional failure** — averages hide failures concentrated in rare but important slices; disaggregation by segment is essential.
- **Worked example** — a summarization team tracks ROUGE for regression detection but reviews judge scores for factual quality, catching a fluency-over-fidelity trade-off.
- **Failure modes** — metric hacking, mismatched proxies, and noisy judges produce misleading conclusions.
- **Tooling** — metrics run at scale through evals-harness and golden-test-sets for continuous regression monitoring.
- **Practical relevance** — metrics are the measurement layer under every evaluation and benchmark decision in model development.
- **Confidence** — small sample sizes need confidence intervals before conclusions are drawn.
- **Segmentation** — slicing scores by domain, length, and user group exposes hidden failures.
- **Worked example** — a model's overall accuracy looks fine, but segmenting shows it fails on short queries.
- **Failure example** — reporting only the mean hides a large failure cluster in the tail.

## Related
- [[wiki/ai-ml/rouge-bleu-bert-score|ROUGE, BLEU, and BERTScore]] — text similarity metrics
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — model-based scoring
- [[wiki/testing/evals-harness|Evals Harness]] — running metrics at scale
- [[wiki/ai-ml/rubric-based-evaluation|Rubric-Based Evaluation]] — structured scoring
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — regression metrics
