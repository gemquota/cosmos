---
type: "concept"
title: "Benchmark Gaming"
description: "Optimizing for benchmark scores in ways that do not generalize to real-world performance"
tags: ["benchmark-gaming", "evaluation", "benchmarks"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Benchmark Gaming

## Summary
Benchmark gaming is the practice of inflating scores on public benchmarks — via training on test data, tuning to the metric, or exploiting benchmark quirks — without genuine capability gains. It erodes the meaning of leaderboard comparisons.

## Details
- Forms: test-set leakage, metric overfitting, exploiting multiple-choice priors, and template memorization.
- Defenses: private test sets, held-out human evaluation, and robustness checks.
- Leaderboards with contamination audits are the current partial answer.
- RSIS3 relevance: RSIS3's own evals should use private, task-specific sets rather than public leaderboards.

## Related
- [[wiki/ai-ml/data-contamination|Data Contamination]] — The leakage mechanism behind much gaming
- [[wiki/testing/eval-sets|Eval Sets]] — The artifacts that get gamed
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The discipline gaming undermines
- [[wiki/ai-ml/model-cards|Model Cards]] — Where gaming should be disclosed
- [[wiki/ai-ml/gpt-4|GPT-4]] — A model often accused and audited
