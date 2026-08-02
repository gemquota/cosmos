---
type: "concept"
title: "Evals Harness"
description: "Software that runs evaluation suites against models and reports metrics consistently"
tags: ["evals", "harness", "evaluation", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/EleutherAI/lm-evaluation-harness", "https://github.com/openai/evals"]
---

# Evals Harness

## Summary
An evals harness executes many prompts against a model, scores the outputs, and aggregates metrics into comparable reports. It matters because ad-hoc evaluation is unrepeatable. A harness standardizes datasets, sampling, and scoring so every model version gets the same test.

## Details
- **Components** — dataset loading, model runner, judge/scorer, and result store.
- **Patterns** — few-shot grading, exact-match checks, and LLM-as-judge scoring.
- **Worked example** — the EleutherAI LM Evaluation Harness runs MMLU and HellaSwag across model checkpoints, printing per-task accuracy tables.
- **Best practice** — freeze harness version for regression comparisons; changing the harness invalidates history.
- **mykb relevance** — RSIS3 quality evals should run on a fixed harness so each iteration is comparable.
- **Determinism** — fix sampling seeds and temperatures in the harness so score differences come from the model, not the run.
- **Worked example** — the EleutherAI LM Evaluation Harness runs MMLU and HellaSwag across checkpoints, printing per-task accuracy tables.
- **Best practice** — freeze the harness version for regression comparisons; changing the harness invalidates historical scores.

## Related
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — frozen inputs
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — regression use
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — scoring
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — judge scoring
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — harness in CI
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — agent evals
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
