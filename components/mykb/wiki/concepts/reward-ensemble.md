---
type: "concept"
title: "Reward Ensembles"
description: "Combining multiple reward models to reduce error"
tags: ["reward-ensemble", "reward-model", "robustness"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Ensembles

## Summary
Reward ensembles average several reward models (or uncertainty-aware variants) to reduce individual blind spots.

## Details
- Reward ensembles average several reward models (or uncertainty-aware variants) to reduce individual blind spots.
- Ensembles help when errors are decorrelated, but fail when all members share a bias.
- Uncertainty estimates from ensemble disagreement can gate high-stakes decisions.
- RSIS3 relevance: multi-signal checks (links + practices + word counts) are an ensemble evaluator.

## Related
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — what ensembles mitigate
- [[wiki/concepts/reward-uncertainty|Reward Uncertainty]] — the signal ensembles give
- [[wiki/concepts/reward-model-gaming|Reward Model Gaming]] — what ensembles resist
- [[wiki/concepts/impact-measures|Impact Measures]] — the ensemble use case
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — the full treatment of this theme
- [[wiki/ai-ml/reward-model|Reward Model]] — existing graph context
