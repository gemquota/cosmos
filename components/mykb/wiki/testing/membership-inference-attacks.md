---
type: "concept"
title: "Membership Inference Attacks"
description: "Determining whether a specific example was in a model training set by observing outputs"
tags: ["security", "privacy", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Membership Inference Attacks

## Summary
Determining whether a specific example was in a model training set by observing outputs

## Details
- Overconfident outputs on training-like inputs reveal membership.
- More feasible for smaller or overtrained models.
- Privacy defenses: differential privacy, dedup, and output calibration.
- A core concern for privacy-preserving-ml.

## Related
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — defense umbrella
- [[wiki/testing/differential-privacy-llm|Differential Privacy for LLMs]] — formal privacy tool
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — reduces memorized duplicates
- [[wiki/ai-ml/calibration-and-confidence|Calibration and Confidence]] — overconfidence link
- [[wiki/testing/model-scanning-ai-vulnerabilities|Model Scanning for AI Vulnerabilities]] — testing for exposure
