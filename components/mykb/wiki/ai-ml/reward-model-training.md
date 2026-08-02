---
type: "concept"
title: "Reward Model Training"
description: "Training a model to predict human preferences, which then guides RL alignment"
tags: ["reward", "training", "alignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Model Training

## Summary
Training a model to predict human preferences, which then guides RL alignment

## Details
- Trained on preference-datasets with pairwise or ranking losses.
- Reward models inherit annotator biases and can be gamed.
- Quality gates include held-out preference accuracy.
- Foundation for rlhf-stages.

## Related
- [[wiki/ai-ml/reward-modeling|Reward Modeling]] — concept umbrella
- [[wiki/ai-ml/preference-datasets|Preference Datasets]] — training data
- [[wiki/ai-ml/human-feedback-collection|Human Feedback Collection]] — feedback source
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — failure guard
- [[wiki/ai-ml/direct-preference-optimization|Direct Preference Optimization]] — reward-free alternative
