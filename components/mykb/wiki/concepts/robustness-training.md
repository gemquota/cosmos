---
type: "concept"
title: "Robustness Training"
description: "Training methods that make models resilient to variation"
tags: ["robustness", "training", "generalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Robustness Training

## Summary
Robustness training builds models that perform well across perturbations, distributions, and adversarial inputs.

## Details
- Robustness training builds models that perform well across perturbations, distributions, and adversarial inputs.
- Methods include data augmentation, adversarial training, and domain randomization.
- The goal is graceful, not brittle, behavior outside the training set.
- RSIS3 relevance: the bundle's tools are trained (via passes) on varied inputs and checked for consistency.

## Related
- [[wiki/concepts/distributional-robustness|Distributional Robustness]] — the distribution property
- [[wiki/concepts/adversarial-robustness|Adversarial Robustness]] — the adversarial property
- [[wiki/concepts/distribution-shift-ai|Distribution Shift in AI]] — the challenge
- [[wiki/concepts/brittleness-ai|AI Brittleness]] — the failure to avoid
- [[wiki/agent-systems/adversarial-self-play|Adversarial Self-Play]] — the full treatment of this theme
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — existing graph context
