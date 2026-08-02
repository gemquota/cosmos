---
type: "concept"
title: "Presence Penalty"
description: "Decoding parameter that penalizes any token that has appeared at least once, encouraging topic diversity"
tags: ["sampling", "decoding", "parameters"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Presence Penalty

## Summary
Decoding parameter that penalizes any token that has appeared at least once, encouraging topic diversity

## Details
- Applies a flat penalty to every already-seen token regardless of frequency.
- Encourages the model to explore new vocabulary and themes.
- Too high a value can hurt coherence and factual consistency.
- Often paired with frequency penalty for fine-grained control.

## Related
- [[wiki/prompt-engineering/frequency-penalty|Frequency Penalty]] — frequency-based counterpart
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — how penalties mix with sampling
- [[wiki/prompt-engineering/stop-sequences|Stop Sequences]] — deterministic alternative
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — direct logit manipulation
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — what penalties change
