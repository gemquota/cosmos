---
type: "concept"
title: "Model Versioning and Registry"
description: "Tracking model versions, metadata, and lifecycle stages in a central registry"
tags: ["versioning", "registry", "mlops", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://mlflow.org/docs/latest/model-registry.html", "https://github.com/mlflow/mlflow"]
---

# Model Versioning and Registry

## Summary
Model registries catalog versions of models with metadata, lineage, and promotion stages. They matter because production quality depends on knowing exactly which model is running and why. Versioning makes rollback, audit, and comparison routine.

## Details
- **Registry content** — weights, config, training data hash, eval scores, and stage (staging, production).
- **Lineage** — every version links to its training run, prompt set, and eval report.
- **Worked example** — MLflow registers a fine-tuned model with its eval delta; the CI/CD pipeline promotes it only after regression gates pass.
- **Best practice** — immutability: never overwrite a version; add a new one.
- **mykb relevance** — RSIS3 knowledge versions deserve the same discipline as model versions.
- **Worked example** — MLflow registers a fine-tuned model with its eval delta; the CI/CD pipeline promotes it only after regression gates pass.
- **Stage semantics** — staging, production, and archived labels make promotion and rollback unambiguous.
- **Lineage** — every version links to its training run, prompt set, and eval report so any behavior change is explainable.

## Related
- [[wiki/ml-frameworks/mlflow-model-registry|MLflow Model Registry]] — tooling
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — promotion pipeline
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — eval gates
- [[wiki/testing/dependency-pinning-models|Dependency Pinning for Models]] — pinning practice
- [[wiki/ai-ml/model-monitoring|Model Monitoring]] — production tracking
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — prompt analog
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the curation pipeline
