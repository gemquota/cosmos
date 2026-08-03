---
type: "concept"
title: "Regularization in Practice"
description: "Practical techniques for controlling model complexity"
tags: ["regularization", "practice", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Regularization in Practice

## Summary
Regularization in practice includes weight decay, dropout, label smoothing, early stopping, and data augmentation. The unifying goal is controlling model complexity so that the model learns the task's true structure rather than memorizing training specifics — and in practice, the choice and strength of regularizers is where much of a model's generalization quality is actually decided.

## Details
- Weight decay is the workhorse: it adds a penalty proportional to the squared norm of the weights, pushing parameters toward zero and preferring simpler functions. In modern optimizers (AdamW), weight decay is decoupled from the adaptive learning-rate scaling, which fixed a long-standing interaction bug and made it predictable again. It is the regularizer that survives at scale because it is cheap, stable, and interacts cleanly with normalization.
- Dropout randomly zeroes a fraction of activations during training, forcing the network to be robust to missing units — an ensemble-like effect at training time. Its practice lesson: it is powerful for smaller networks and fully connected layers, but modern large-scale training has largely moved away from it in favor of normalization and weight decay, because at scale the robustness it provides is bought at the cost of slower convergence. Label smoothing replaces hard 0/1 targets with soft targets (e.g., 0.9/0.1), which prevents the network from becoming overconfident and, as a side effect, improves calibration.
- Early stopping halts training when validation performance degrades, directly measuring the bias-variance tradeoff instead of trusting a predetermined schedule. Data augmentation expands the training distribution with transformed examples (cropping, flipping, noise, paraphrases), which regularizes by teaching invariance — the model cannot overfit surface features it has seen varied.
- Modern LLM training leans on weight decay, AdamW defaults, and scale rather than aggressive regularizers. The empirical finding at scale is that careful data, normalization, and a modest weight decay beat the heavy regularizer stacks of the small-model era; dropout and label smoothing are used selectively (label smoothing is common, dropout mostly in specific components). The lesson is that regularization choices are scale-dependent — techniques that are essential at one size are harmful at another.
- Regularization choices interact with scaling; there is no free lunch. Every regularizer trades training fit for generalization, and the correct strength depends on model size, data size, and task — which is why regularization strength is a tuned hyperparameter, not a constant.
- RSIS3 relevance: the bundle's own regularization is structural (templates, links, checks) — the wiki prevents its own overfitting by enforcing consistent structure, linking discipline, and verification checks, which play the role that weight decay plays for a model.

## Related
- [[wiki/concepts/weight-decay|Weight Decay]] — the workhorse
- [[wiki/concepts/dropout-practice|Dropout in Practice]] — the classic
- [[wiki/concepts/early-stopping|Early Stopping]] — the patience tool
- [[wiki/concepts/label-smoothing|Label Smoothing]] — the calibration tool
- [[wiki/concepts/grokking|Grokking]]
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]]
