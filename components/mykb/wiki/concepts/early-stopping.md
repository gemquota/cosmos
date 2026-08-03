---
type: "concept"
title: "Early Stopping"
description: "Ending training when validation performance degrades"
tags: ["early-stopping", "training", "validation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Early Stopping

## Summary
Early stopping halts training when a validation metric stops improving, trading a bit of training-set fit for generalization. It is the simplest effective regularizer in deep learning: instead of deciding a priori how many epochs to run, watch a held-out validation metric and stop when it degrades, keeping the best checkpoint seen so far.

## Details
- The mechanism is a direct measurement of the bias-variance tradeoff. During training, the model first improves on both training and validation loss as it learns real structure; eventually it starts memorizing training-set idiosyncrasies, and validation loss turns upward while training loss keeps falling. Early stopping detects that turn and returns the model from the epoch before overfitting set in — the checkpoint with the best validation performance rather than the final one.
- It is simple, effective regularization with a patience hyperparameter. Patience controls how many epochs of non-improvement to tolerate before stopping, and it encodes the assumption that validation noise can hide a genuine improvement: too little patience stops prematurely on a noisy dip, too much patience lets the model overfit while you wait for an improvement that never comes. A common refinement is to restore the best checkpoint at stop time and to combine early stopping with weight decay or dropout, since the regularizers interact — early stopping plus strong weight decay can underfit.
- Modern huge runs often train to fixed schedules instead; early stopping remains for fine-tuning. Large language models are frequently trained on a precomputed token budget with a learning-rate schedule that ends at a minimum, because validation-based stopping is expensive at that scale and the schedule itself provides the regularization. But in fine-tuning, transfer learning, and small-scale training — the regime most agentic systems and fine-tuners actually operate in — early stopping remains the standard practice because overfitting is fast and cheap to measure.
- Failure modes: validation-set leakage makes the stopping signal lie; stopping on the wrong metric (a metric that does not correlate with deployment success) optimizes the wrong thing; and using the same validation set for stopping and hyperparameter selection double-dips, inflating apparent performance.
- RSIS3 relevance: pass runs stop at diminishing returns and consolidate. Each improvement cycle is a training run in miniature — iterate while the metric improves, stop when gains flatten, and consolidate the best configuration rather than the latest one.

## Related
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — what to keep when stopping
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — what it prevents
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — the broader choice
- [[wiki/decisions/eval-splits|eval-splits]] — the signal
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — existing graph context
