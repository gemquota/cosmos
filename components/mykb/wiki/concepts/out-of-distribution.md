---
type: "concept"
title: "Out-of-Distribution"
description: "Inputs unlike the training distribution"
tags: ["ood", "distribution", "generalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Out-of-Distribution

## Summary
Out-of-distribution (OOD) inputs are examples that fall outside the training distribution, where model guarantees lapse.

## Details
- Out-of-distribution (OOD) inputs are examples that fall outside the training distribution, where model guarantees lapse.
- OOD performance is unpredictable; evals must include OOD sets to estimate it.
- Safety-critical systems need graceful OOD handling, not confidence in the wrong answer.
- RSIS3 relevance: OOD queries to the knowledge graph should degrade gracefully.

## Related
- [[wiki/concepts/ood-generalization|OOD Generalization]] — the ability
- [[wiki/concepts/distribution-shift-ai|Distribution Shift in AI]] — the general phenomenon
- [[wiki/concepts/brittleness-ai|AI Brittleness]] — the failure
- [[wiki/concepts/context-robustness|Context Robustness]] — the practical angle
- [[wiki/concepts/goal-misgeneralization|Goal Misgeneralization]] — the full treatment of this theme
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — existing graph context
