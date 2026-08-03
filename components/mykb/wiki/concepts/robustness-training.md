---
type: "concept"
title: "Robustness Training"
description: "Training methods that make models resilient to variation"
tags: ["robustness", "training", "generalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Robustness Training

## Summary
Robustness training builds models that perform well across perturbations, distributions, and adversarial inputs — not just on the exact data they were trained on. Its goal is graceful, not brittle, behavior outside the training set: a robust model degrades predictably when inputs shift, while a brittle model fails suddenly and confidently on inputs barely different from what it saw.

## Details
- Robustness training builds models that perform well across perturbations, distributions, and adversarial inputs. The three targets are distinct: perturbations (small changes to otherwise valid inputs, like image noise or typos), distribution shift (a different data distribution than training, like a new domain or a new time period), and adversarial inputs (inputs deliberately crafted to fool the model).
- Methods include data augmentation, adversarial training, and domain randomization. Augmentation expands the training distribution with transformed examples (rotation, noise, paraphrasing), teaching invariance to those transformations; adversarial training generates worst-case perturbations during training (PGD and FGSM are the classic generators) so the model learns to resist them; domain randomization varies the simulated environment so a policy generalizes across appearance, physics, and layout.
- Concrete example: an image classifier trained with augmentation on rotations and lighting still fails on a rare camera's color profile; adversarial training against small perturbations makes it robust to the perturbations it was trained against but can leave it vulnerable to larger or differently-structured ones — robustness is always relative to the attack or shift family considered.
- The goal is graceful, not brittle, behavior outside the training set. Graceful behavior means calibrated confidence — the model knows when it is out of distribution and hedges — rather than a confident wrong answer; this is why robustness training is paired with calibration and out-of-distribution detection rather than treated as a standalone fix.
- Failure modes: robustness that does not transfer — a model robust to training-time attacks is often still vulnerable to transfer attacks generated on a different surrogate model; augmentation that teaches the wrong invariances (a model that ignores a feature because augmentation always varied it); and robustness at the cost of clean accuracy, where the defensive training degrades performance on the normal data it must also handle.
- Tradeoffs: adversarial training trades clean accuracy and training cost for worst-case robustness, and there is a documented accuracy-robustness tradeoff on standard benchmarks; augmentation is cheap but only covers the transformations the practitioner anticipates; the strongest practical posture combines targeted robustness training with detection and graceful degradation at inference.
- RSIS3 relevance: the bundle's tools are trained (via passes) on varied inputs and checked for consistency — robustness training is the analogy for why passes must exercise failure cases and edge conditions, so the system's behavior degrades gracefully when inputs fall outside the ones it has seen.

## Related
- [[wiki/concepts/distributional-robustness|Distributional Robustness]] — the distribution property
- [[wiki/concepts/adversarial-robustness|Adversarial Robustness]] — the adversarial property
- [[wiki/concepts/distribution-shift-ai|Distribution Shift in AI]] — the challenge
- [[wiki/concepts/brittleness-ai|AI Brittleness]] — the failure to avoid
- [[wiki/agent-systems/adversarial-self-play|Adversarial Self-Play]] — the full treatment of this theme
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — existing graph context
