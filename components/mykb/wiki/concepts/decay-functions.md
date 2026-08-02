---
type: "concept"
title: "Decay Functions"
description: "Mathematical models of how knowledge loses currency"
tags: ["decay", "functions", "metrics", "policy"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Decay Functions

## Summary
Decay functions model how knowledge loses currency over time: exponential decay, half-life models, or step functions for version-validity.

## Details
- They turn 'this is getting stale' into a number: at time t, how much of this article's value should still count.
- Decay parameters are topic-specific — Android API knowledge decays faster than git fundamentals.
- For mykb, decay functions are the engine under recency-weighting and the timeliness score.

## Related
- [[wiki/concepts/decay-functions|Decay Functions]]
- [[wiki/concepts/half-life-knowledge|Half-Life of Knowledge]]
- [[wiki/concepts/recency-weighting|Recency Weighting]]
- [[wiki/concepts/freshness-signals|Freshness Signals]]
- [[wiki/concepts/knowledge-temperature|Knowledge Temperature]]
- [[wiki/concepts/timeliness-score|Timeliness Score]]
