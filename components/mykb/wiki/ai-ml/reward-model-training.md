---
type: "concept"
title: "Reward Model Training"
description: "Training a model to predict human preferences, which then guides RL alignment"
tags: ["reward", "training", "alignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Reward Model Training

## Summary
Reward model training teaches a model to predict human preferences, producing the reward signal that guides reinforcement-learning alignment. It matters because preferences are the bridge between human judgment and optimization, and a flawed reward model propagates its flaws into the aligned policy. Training quality gates everything downstream. Reward models are learned preferences, complete with their flaws.

## Details
- **Definition** — a reward model takes an input and candidate response and outputs a score predicting human preference.
- **Training** — reward models are trained on preference-datasets using pairwise or ranking losses that maximize agreement with human choices.
- **Bias inheritance** — reward models absorb annotator biases and dataset artifacts, so data quality is the dominant determinant of model quality.
- **Gaming risk** — reward models can be exploited by outputs that score well without being good, motivating reward-hacking-prevention.
- **Validation** — held-out preference accuracy and calibration checks gate whether a reward model is fit for use.
- **Worked example** — a team trains a reward model on cleaned pairwise votes, validates it on a reserved set, and uses it to score rollouts in rlhf-stages.
- **Failure modes** — overfitting to annotator quirks, reward hacking, and distribution shift between training and deployment corrupt the signal.
- **Alternatives** — direct-preference-optimization and related methods train from preferences without a separate reward model.
- **Practical relevance** — reward models are the preference-to-optimization converter at the center of modern alignment pipelines.
- **Data hygiene** — preference pairs must be clean, since the reward model inherits every artifact.
- **Regularization** — limiting reward model capacity and training length reduces overfitting to the dataset.
- **Worked example** — a reward model is validated on a held-out preference set before powering RL training.
- **Failure example** — a reward model that overvalues politeness steers the policy toward empty agreeable answers.

## Related
- [[wiki/ai-ml/reward-modeling|Reward Modeling]] — the concept umbrella
- [[wiki/ai-ml/preference-datasets|Preference Datasets]] — the training data
- [[wiki/ai-ml/human-feedback-collection|Human Feedback Collection]] — the feedback source
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — guarding the signal
- [[wiki/ai-ml/direct-preference-optimization|Direct Preference Optimization]] — the reward-free alternative
