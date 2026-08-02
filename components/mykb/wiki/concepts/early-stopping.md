---
type: "concept"
title: "Early Stopping"
description: "Ending training when validation performance degrades"
tags: ["early-stopping", "training", "validation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Early Stopping

## Summary
Early stopping halts training when a validation metric stops improving, trading fit for generalization.

## Details
- Early stopping halts training when a validation metric stops improving, trading fit for generalization.
- It is simple, effective regularization with a patience hyperparameter.
- Modern huge runs often train to fixed schedules instead; early stopping remains for fine-tuning.
- RSIS3 relevance: pass runs stop at diminishing returns and consolidate.

## Related
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — what to keep when stopping
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — what it prevents
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — the broader choice
- [[wiki/decisions/eval-splits|eval-splits]] — the signal
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — existing graph context
