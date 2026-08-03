---
type: "concept"
title: "Out-of-Distribution"
description: "Inputs unlike the training distribution"
tags: ["ood", "distribution", "generalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Out-of-Distribution

## Summary
Out-of-distribution (OOD) inputs are examples that fall outside the training distribution, where model guarantees lapse. The training distribution is a promise — "the model is good here" — and OOD is everything outside that promise, where the model's behavior is not covered by its performance statistics and cannot be predicted from them.

## Details
- OOD performance is unpredictable; evals must include OOD sets to estimate it. The uncomfortable fact is that a model can be excellent in distribution and arbitrary out of it — accuracy can collapse, remain high by luck, or flip in perverse ways (a vision model that classifies OOD images with high confidence into the wrong classes). Because the behavior is not governed by the training objective, it cannot be extrapolated; the only way to estimate it is to test on deliberately shifted data, which is why robustness evaluation always includes OOD suites constructed by perturbation, domain transfer, and held-out environments.
- The danger is confidence: OOD inputs do not reliably trigger low confidence. Neural networks are famously overconfident on OOD data — they output high softmax probabilities for inputs they have no evidence about — so "the model seems sure" is not evidence the input is in distribution. This is why OOD detection is a separate research area: distinguishing "input is OOD" (via density estimates, distance to training data, or specialized detectors) from "input is normal", so the system can route OOD inputs to fallback handling instead of trusting the prediction.
- Safety-critical systems need graceful OOD handling, not confidence in the wrong answer. The design goal is a system that knows when it is out of its depth and responds appropriately — refuse, ask, escalate to a human, or return "unknown" — rather than one that confidently proceeds. Graceful degradation is an explicit property to engineer: uncertainty signaling, abstention options, and conservative defaults on the OOD path.
- The deeper lesson: OOD is not an edge case but the default in deployment. Every real system meets inputs its training never anticipated, so "in distribution" is the special case, and robustness to OOD is part of the core spec, not a nice-to-have.
- RSIS3 relevance: OOD queries to the knowledge graph should degrade gracefully. A query outside the curated corpus should return low-confidence, partial results with an honest "this is beyond my knowledge" signal rather than a confident synthesis built from nearest-neighbor noise.

## Related
- [[wiki/concepts/ood-generalization|OOD Generalization]] — the ability
- [[wiki/concepts/distribution-shift-ai|Distribution Shift in AI]] — the general phenomenon
- [[wiki/concepts/brittleness-ai|AI Brittleness]] — the failure
- [[wiki/concepts/context-robustness|Context Robustness]] — the practical angle
- [[wiki/concepts/goal-misgeneralization|Goal Misgeneralization]] — the full treatment of this theme
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — existing graph context
