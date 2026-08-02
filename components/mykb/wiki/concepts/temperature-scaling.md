---
type: "concept"
title: "Temperature Scaling"
description: "Adjusting output sharpness for better confidence"
tags: ["temperature", "calibration", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Temperature Scaling

## Summary
Temperature scaling divides logits by a temperature to soften or sharpen probability outputs.

## Details
- Temperature scaling divides logits by a temperature to soften or sharpen probability outputs.
- It is the standard post-hoc calibration fix for classifiers.
- LLM sampling temperature trades creativity for determinism.
- RSIS3 relevance: retrieval confidence thresholds are temperature-like knobs on the graph.

## Related
- [[wiki/concepts/calibration|Calibration]] — the property
- [[wiki/concepts/label-smoothing|Label Smoothing]] — the training-side twin
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the confidence link
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — the tuning context
