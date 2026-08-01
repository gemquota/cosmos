---
type: "concept"
title: "LLM Evaluation"
description: "The discipline of measuring LLM output quality with benchmarks, metrics, and test harnesses instead of vibes"
tags: ["llm-evaluation", "testing", "benchmarks", "quality"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://github.com/EleutherAI/lm-evaluation-harness", "https://github.com/openai/evals"]
---

# LLM Evaluation

## Summary
LLM evaluation is the practice of scoring model or prompt output against defined datasets, metrics, and rubrics. It spans offline benchmarks, online harnesses, human ratings, and LLM-as-judge, and it is the gating mechanism that makes prompt engineering and fine-tuning scientific.

## Details
- EleutherAI's lm-evaluation-harness standardizes running academic benchmarks (MMLU, HellaSwag, GSM8K, etc.) across many models.
- OpenAI Evals provides a framework for writing custom eval runs, including model-graded and human-graded evals.
- Metric families: exact/match metrics, similarity (BLEU/ROUGE/embedding distance), task accuracy, and LLM-judge scores.
- Every improvement claim — prompt, template, fine-tune, quantization — needs a before/after eval run to be credible.
- Confounds: temperature variance, data contamination, benchmark leakage, and judge bias all distort scores.
- RSIS3 relevance: the L2 improvement loop is eval-gated; pulse outcomes and golden tests are the RSIS3-native eval harness.

## Related
- [[wiki/testing/eval-sets|Eval Sets]] — The curated datasets an evaluation runs against
- [[wiki/testing/golden-tests|Golden Tests]] — Small fixed cases for cheap, fast regression checks
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — Continuous quality monitoring across prompt changes
- [[wiki/ai-ml/benchmark-gaming|Benchmark Gaming]] — How benchmarks get gamed, and how to defend
- [[wiki/ai-ml/data-contamination|Data Contamination]] — Train/test overlap that invalidates scores
- [[wiki/ai-ml/model-cards|Model Cards]] — Where eval results are published
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Eval telemetry enriches the wiki graph
- [[wiki/syntheses/weekly-review|Weekly Review]] — Eval trends reviewed weekly
