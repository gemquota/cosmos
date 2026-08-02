---
type: "concept"
title: "Model Stealing Attacks"
description: "Extracting a model architecture, weights, or capabilities through repeated API queries"
tags: ["security", "api", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Stealing Attacks

## Summary
Extracting a model architecture, weights, or capabilities through repeated API queries

## Details
- Attackers distill a substitute model from query outputs.
- High query volume and output diversity make stealing easier.
- Mitigations: rate limits, output watermarking, and anomaly detection.
- Economic threat that erodes proprietary model advantages.

## Related
- [[wiki/testing/api-key-theft|API Key Theft]] — credential-side attack
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — throttling defense
- [[wiki/ai-ml/model-watermarking|Model Watermarking]] — output provenance
- [[wiki/ai-ml/closed-models-moat|The Closed-Model Moat]] — what is at risk
- [[wiki/testing/quota-exhaustion-attacks|Quota Exhaustion Attacks]] — adjacent abuse pattern
