---
type: "concept"
title: "Restraint Training"
description: "Training agents to avoid harmful or impactful actions"
tags: ["restraint", "training", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Restraint Training

## Summary
Restraint training teaches agents to avoid side effects, tampering, and excessive impact — often via curated demonstrations or penalties.

## Details
- Restraint training teaches agents to avoid side effects, tampering, and excessive impact — often via curated demonstrations or penalties.
- It is the training-time version of impact regularization.
- Generalizing restraint to novel contexts is hard; evals must test it.
- RSIS3 relevance: worker instructions (no shared-dir edits, no git) are restraint training.

## Related
- [[wiki/concepts/impact-regularization|Impact Regularization]] — the reward-side twin
- [[wiki/concepts/side-effects-problem|Side Effects Problem]] — the target
- [[wiki/agent-systems/harmless-ai|Harmless AI]] — the disposition
- [[wiki/concepts/adversarial-training-ai|Adversarial Training for AI]] — the hardening companion
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the full treatment of this theme
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — existing graph context
