---
type: "concept"
title: "Model Evaluation Metrics"
description: "Quantitative measures used to score model outputs across tasks"
tags: ["evaluation", "metrics", "benchmarks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Evaluation Metrics

## Summary
Quantitative measures used to score model outputs across tasks

## Details
- Accuracy, F1, ROUGE, BLEU, and newer LLM-judge scores.
- Metric choice must match task and failure costs.
- Averages hide distributional failures.
- Underpin evals-harness and golden-test-sets.

## Related
- [[wiki/ai-ml/rouge-bleu-bert-score|ROUGE, BLEU, and BERTScore]] — text similarity metrics
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — model-based scoring
- [[wiki/testing/evals-harness|Evals Harness]] — running metrics at scale
- [[wiki/ai-ml/rubric-based-evaluation|Rubric-Based Evaluation]] — structured scoring
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — regression metrics
