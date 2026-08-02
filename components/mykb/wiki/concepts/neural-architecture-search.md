---
type: "concept"
title: "Neural Architecture Search"
description: "Automating the design of neural network architectures"
tags: ["nas", "architecture-search", "automl", "self-improvement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Neural_architecture_search", "https://arxiv.org/abs/1611.01578"]
---

# Neural Architecture Search

## Summary
Neural architecture search (NAS) automates network design: a controller proposes architectures, they are trained and scored, and the search updates toward better ones. The 2017 NAS paper achieved human-expert-level results on image benchmarks, establishing AutoML's credibility.

## Details
- **Methods** — RL-based controllers, evolutionary search, weight-sharing (one-shot NAS), and differentiable search.
- **Cost problem** — naive NAS trains thousands of candidates; weight sharing and proxy tasks make it tractable.
- **Relevance to RSI** — NAS is architectural self-improvement: the system redesigns part of its own brain.
- **Safety angle** — searched architectures are less interpretable; verification must cover the search, not just the winner.
- **RSIS3 relevance** — the bundle's own 'architecture' (loop stack, knowledge schema) is revised via syntheses and practice passes.

## Related
- [[wiki/concepts/automated-machine-learning|Automated Machine Learning (AutoML)]] — the field
- [[wiki/concepts/hyperparameter-self-optimization|Hyperparameter Self-Optimization]] — configuration sibling
- [[wiki/concepts/emergence-in-llms|Emergence in LLMs]] — what search can discover
- [[wiki/concepts/self-modification-safety|Self-Modification Safety]] — governing self-redesign
- [[wiki/concepts/capability-jumps|Capability Jumps]] — search as jump source
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — tuning layer
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
