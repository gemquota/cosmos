---
type: "concept"
title: "Rejection Sampling"
description: "Sampling candidates and keeping only those that pass quality or safety filters"
tags: ["sampling", "quality", "filtering"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Rejection Sampling

## Summary
Sampling candidates and keeping only those that pass quality or safety filters

## Details
- Generate many, score each, discard low-quality or unsafe outputs.
- Turns a passable model into a much better one at inference cost.
- Used in RLHF for building preference datasets.
- Filter quality determines the ceiling of the approach.

## Related
- [[wiki/ai-ml/best-of-n-sampling|Best-of-N Sampling]] — selection-based sibling
- [[wiki/ai-ml/reward-modeling|Reward Modeling]] — scoring function
- [[wiki/ai-ml/human-feedback-collection|Human Feedback Collection]] — where humans filter
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — data-side counterpart
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — automated scoring
