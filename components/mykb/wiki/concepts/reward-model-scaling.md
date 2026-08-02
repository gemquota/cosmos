---
type: "concept"
title: "Reward Model Scaling"
description: "How reward model quality changes with scale and data"
tags: ["reward-model", "scaling", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Model Scaling

## Summary
Reward model scaling studies how reward quality improves with model size, data volume, and annotation diversity.

## Details
- Reward model scaling studies how reward quality improves with model size, data volume, and annotation diversity.
- Larger reward models often track human preferences better but also generalize more confidently to novel inputs.
- Scaling laws for rewards inform RLHF budget decisions.
- RSIS3 relevance: the loop scales its own evaluators (checks, rubrics) with care.

## Related
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — the quality dimension
- [[wiki/concepts/capability-jumps|Capability Jumps]] — the scaling context
- [[wiki/concepts/reward-ensemble|Reward Ensembles]] — combining models
- [[wiki/concepts/reward-uncertainty|Reward Uncertainty]] — scale and confidence
- [[wiki/ai-ml/reward-model|Reward Model]] — existing graph context
