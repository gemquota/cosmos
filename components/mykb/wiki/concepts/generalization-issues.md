---
type: "concept"
title: "Generalization Issues"
description: "The cluster of problems in moving from training to deployment"
tags: ["generalization", "issues", "ml"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Generalization Issues

## Summary
Generalization issues are the many ways performance fails to transfer: overfitting, shortcuts, distribution shift, and goal misgeneralization. They are the central technical weakness of learned systems — a model that only performs well on training-like inputs is not actually solving the problem, and the failure modes differ enough that each needs its own detection and mitigation.

## Details
- Overfitting is the classic form: the model memorizes training-set idiosyncrasies instead of the underlying regularity, so validation and deployment performance collapse as the data diverges. It is detected by the train-validation gap and mitigated by regularization, data augmentation, and early stopping. In LLMs it shows up as memorized training text surfacing verbatim and as performance that depends on exact phrasing rather than meaning.
- Shortcut learning is the subtler form: the model finds a spurious correlation that works on the training distribution — a background cue, a watermark, a formatting artifact — and achieves high accuracy without learning the intended concept. Shortcuts are dangerous because they are invisible on the test set (which shares the artifact) and fail exactly where they matter (real deployment, where the artifact is absent or inverted). Detection requires deliberate out-of-distribution testing and failure-mode analysis; mitigation requires debiasing or dataset rebalancing.
- Distribution shift is the deployment-side issue: even a correctly learned relationship degrades when the input distribution moves, because the model's accuracy guarantee was tied to training statistics. Goal misgeneralization is the safety-critical form: the model generalizes to a different objective than intended — optimizing what it was rewarded for in training in a way that violates intent in novel settings.
- They are the central technical weakness of learned systems because they are unavoidable — any finite training set underdetermines the true function, so every model makes a bet about what generalizes, and the bet can be wrong.
- Mitigations span data, architecture, training, and evals: richer and more diverse data, inductive biases that prefer simple explanations, robustness training, and evaluation suites deliberately built to probe generalization rather than reward memorization.
- RSIS3 relevance: the wiki's ML pages map these issues to their safety consequences, and the retrieval system faces the same cluster — a retrieval model overfit to the curated corpus will fail on novel queries exactly as an overfit vision model fails on novel images.

## Related
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — the memorization side
- [[wiki/concepts/shortcut-learning|Shortcut Learning]] — the mechanism
- [[wiki/concepts/distribution-shift-ai|Distribution Shift in AI]] — the deployment side
- [[wiki/concepts/memorization-vs-generalization|Memorization vs Generalization]] — the core distinction
- [[wiki/concepts/goal-misgeneralization|Goal Misgeneralization]] — the full treatment of this theme
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — existing graph context
