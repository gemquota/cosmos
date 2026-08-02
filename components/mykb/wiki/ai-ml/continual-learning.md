---
type: "concept"
title: "Continual Learning"
description: "Training models that keep learning from new data without losing old capabilities"
tags: ["continual-learning", "training", "lifelong-learning", "forgetting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1902.10407", "https://arxiv.org/abs/2005.13201"]
---

# Continual Learning

## Summary
Continual learning updates a model over a stream of tasks or data rather than in one fixed pretraining run. It matters for personal systems like mykb that accumulate knowledge over time. The central challenge is stability-plasticity: absorb new information without erasing old.

## Details
- **Scenarios** — task-incremental, domain-incremental, and class-incremental learning with different forgetting pressures.
- **Methods** — replay buffers, regularization (EWC), architectural isolation, and adapter-based expansion.
- **Worked example** — a personal assistant fine-tunes monthly on new user notes; each round includes a replay of representative old notes to preserve prior facts.
- **Measurement** — forward and backward transfer on held-out task sets.
- **mykb relevance** — the knowledge graph should absorb new syntheses while old concepts stay intact.
- **Measurement** — forward and backward transfer on held-out task sets quantify both learning and forgetting.
- **Worked example** — a personal assistant fine-tunes monthly on new user notes; each round includes replay of representative old notes.
- **Methods** — replay buffers, regularization such as EWC, architectural isolation, and adapter-based expansion keep old capabilities alive.

## Related
- [[wiki/llm-agents/memory-consolidation-agents|Memory Consolidation for Agents]] — agent memory analog
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — regression checks
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — old-task memory
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — versioned updates
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — related concept in this cluster
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — memory consolidation research
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the curation pipeline
- [[wiki/ml-frameworks/checkpointing-training|Training Checkpointing]] — related concept in this cluster
