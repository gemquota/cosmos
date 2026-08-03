---
type: "concept"
title: "Calibration"
description: "Agreement between a model's confidence and its accuracy"
tags: ["calibration", "uncertainty", "evaluation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Calibration

## Summary
Calibration is the agreement between a model's stated confidence and its actual accuracy: of all predictions made with 70% confidence, roughly 70% should be correct. A model can be accurate yet badly miscalibrated — highly capable on average while systematically overconfident on the cases that matter — which is why calibration is a core evaluation and safety metric rather than a nicety.

## Details
- The standard measurement is reliability: bin predictions by confidence and compare mean confidence to observed accuracy within each bin. A reliability diagram plots the two; points above the diagonal are underconfident (observed accuracy beats predicted confidence), points below are overconfident. Summary statistics include expected calibration error (ECE), the accuracy-weighted gap between confidence and accuracy across bins, and Brier score, which captures both calibration and sharpness.
- Why models miscalibrate: training objectives optimize accuracy, not confidence, so the network's softmax probabilities absorb dataset priors, class imbalance, and the effects of architectures that are not trained to be well-calibrated. Modern over-parameterized models trained with heavy regularization and mixed objectives are frequently overconfident on out-of-distribution inputs — the model is certain precisely where it has the least evidence.
- Fixes operate at different stages. Temperature scaling fits a single scalar to the logits on held-out data, which preserves accuracy and rank order while fixing global overconfidence; Platt scaling and isotonic regression fit richer maps but can distort rankings. At the training stage, label smoothing, focal loss, and explicit calibration objectives push the model toward better-calibrated probabilities, and ensembling or Bayesian approximations (deep ensembles, MC dropout) capture uncertainty the single forward pass cannot.
- Calibration is a measurement artifact as much as a model property: it must be evaluated on the deployment distribution, because a model calibrated in-distribution can be wildly miscalibrated under shift, and eval contamination can inflate apparent calibration by leaking test labels.
- RSIS3 relevance: every loop that makes decisions from confidence — retrieval ranking, constraint checks, proposal acceptance — should track calibration. If the system reports 90% confidence in a synthesis but its past syntheses were right 60% of the time, the next loop will misallocate its improvement effort. Logging confidence alongside outcomes is the minimal calibration dataset.

## Related
- [[wiki/concepts/evaluation-frameworks-ai|Evaluation Frameworks]] — where calibration is measured
- [[wiki/concepts/out-of-distribution|Out of Distribution]] — where calibration breaks
- [[wiki/concepts/risk-literacy|Risk Literacy]] — reading confidence claims
- [[wiki/concepts/expected-value-reasoning|Expected Value Reasoning]] — decisions from probabilities
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]]
- [[wiki/concepts/metacognition|Metacognition]]
- [[wiki/llm-agents/self-reflection-agents|Self Reflection Agents]]
- [[wiki/llm-agents/reward-hacking|Reward Hacking]]
- [[wiki/concepts/confabulation|Confabulation]]
