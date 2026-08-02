---
type: "concept"
title: "Automated Machine Learning (AutoML)"
description: "Automating the end-to-end ML workflow"
tags: ["automl", "automation", "ml", "pipelines"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Automated_machine_learning", "https://www.automl.org/"]
---

# Automated Machine Learning (AutoML)

## Summary
Automated machine learning automates the ML workflow — data preparation, feature engineering, model selection, and hyperparameter tuning — so non-experts can build models and experts can scale experimentation. AutoML is machine learning applied to machine learning, a direct ancestor of self-improving systems.

## Details
- **Pipeline stages** — data cleaning, feature synthesis, architecture/algorithm selection, and hyperparameter optimization.
- **Tools** — open-source frameworks and commercial AutoML services; automated benchmark competitions track progress.
- **Bootstrap connection** — AutoML's search over its own pipeline is a bounded, human-supervised self-improvement loop.
- **Limits** — AutoML optimizes within a search space; it cannot yet invent new paradigms.
- **RSIS3 relevance** — the wiki daemon's automated curation pipeline (capture → link → synthesize → check) is AutoML-style automation for knowledge.

## Related
- [[wiki/concepts/hyperparameter-self-optimization|Hyperparameter Self-Optimization]] — tuning component
- [[wiki/concepts/neural-architecture-search|Neural Architecture Search]] — architecture component
- [[wiki/concepts/program-synthesis|Program Synthesis]] — model-search sibling
- [[wiki/concepts/autotuning|Autotuning]] — systems component
- [[wiki/concepts/learn-to-learn|Learn to Learn]] — the goal
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow: Open Threads]] — knowledge-side automation
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
