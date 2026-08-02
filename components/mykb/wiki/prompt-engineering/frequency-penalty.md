---
type: "concept"
title: "Frequency Penalty"
description: "Decoding parameter that reduces the probability of tokens already emitted many times"
tags: ["sampling", "decoding", "parameters"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Frequency Penalty

## Summary
Decoding parameter that reduces the probability of tokens already emitted many times

## Details
- Penalizes tokens proportionally to how often they have appeared in the generated text.
- Reduces repetitive loops and n-gram copying at moderate temperature.
- Implemented as a logit adjustment applied before sampling.
- Interacts with temperature and presence penalties, so tuning is empirical.

## Related
- [[wiki/prompt-engineering/presence-penalty|Presence Penalty]] — complementary repetition control
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — primary sampling knob it modifies
- [[wiki/prompt-engineering/top-p-sampling|Top-P Sampling]] — distribution shaping alongside penalties
- [[wiki/prompt-engineering/stop-sequences|Stop Sequences]] — harder repetition control
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — raw logit manipulation alternative
