---
type: "concept"
title: "LLMOps CI/CD"
description: "Applying continuous integration and delivery practices to prompts, models, and evaluation"
tags: ["llmops", "ci", "cd", "pipelines"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://mlflow.org/docs/latest/", "https://github.com/EleutherAI/lm-evaluation-harness"]
---

# LLMOps CI/CD

## Summary
LLMOps CI/CD treats prompts, eval suites, and model configs as code that flows through test and deployment pipelines. It matters because prompt and model changes are code changes with production impact. CI gates catch regressions; CD ships validated changes safely.

## Details
- **Pipeline stages** — lint and validate configs, run regression suites, canary in shadow mode, then promote.
- **Artifacts** — prompt versions, model registry entries, and eval reports with hashes for reproducibility.
- **Worked example** — a prompt edit triggers: golden tests, judge scoring, canary rollout to 5% traffic, then full rollout or auto-rollback.
- **Best practice** — keep deploys reversible and every change traceable to an eval delta.
- **mykb relevance** — RSIS3 iteration should be a CI loop: change knowledge, run evals, promote if no regression.
- **Worked example** — a prompt edit triggers golden tests, judge scoring, canary rollout to 5% of traffic, then full rollout or auto-rollback.
- **Reproducibility** — every promotion records artifact hashes, eval reports, and the decision rationale.

## Related
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — model artifacts
- [[wiki/agent-systems/canary-deployments-agents|Canary Deployments for Agents]] — rollout pattern
- [[wiki/agent-systems/shadow-mode-evaluation|Shadow Mode Evaluation]] — pre-promotion eval
- [[wiki/testing/evals-harness|Evals Harness]] — test runner
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/ml-frameworks/mlflow-model-registry|MLflow Model Registry]] — model registry tooling
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the curation pipeline
