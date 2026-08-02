---
type: "concept"
title: "Contrastive Decoding"
description: "Decoding that contrasts expert and amateur model distributions to reduce errors"
tags: ["contrastive-decoding", "decoding", "quality", "techniques"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Contrastive Decoding

## Summary
Decoding that contrasts expert and amateur model distributions to reduce errors

## Details
- A small amateur model provides a baseline to penalize.
- Expert tokens favored over amateur behavior improve quality.
- Requires paired models and extra compute.
- A research-grade method for factual fluency.

## Related
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — decoding family
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — model pairing theme
- [[wiki/ai-ml/calibration-and-confidence|Calibration and Confidence]] — quality link
- [[wiki/prompt-engineering/beam-search-decoding|Beam Search Decoding]] — alternative
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — cost consideration
