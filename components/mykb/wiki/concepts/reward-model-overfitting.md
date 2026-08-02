---
type: "concept"
title: "Reward Model Overfitting"
description: "Reward models fitting training quirks instead of true preferences"
tags: ["reward-model", "overfitting", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Model Overfitting

## Summary
Reward models overfit when they memorize annotator quirks or dataset artifacts instead of general preferences.

## Details
- Reward models overfit when they memorize annotator quirks or dataset artifacts instead of general preferences.
- Overfit reward models assign high scores to surface features the policy then exploits.
- Detection: hold-out preference accuracy and adversarial probing of reward scores.
- RSIS3 relevance: overfit checkers would rubber-stamp the loop instead of guarding it.

## Related
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — the umbrella
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — the general failure
- [[wiki/concepts/reward-model-gaming|Reward Model Gaming]] — the consequence
- [[wiki/concepts/eval-contamination|Eval Contamination]] — data leak
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — the full treatment of this theme
- [[wiki/ai-ml/reward-model-training|Reward Model Training]] — existing graph context
