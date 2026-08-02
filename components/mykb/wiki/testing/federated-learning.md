---
type: "concept"
title: "Federated Learning"
description: "Training models across decentralized data without centralizing the raw data"
tags: ["federated", "privacy", "distributed", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Federated Learning

## Summary
Training models across decentralized data without centralizing the raw data

## Details
- Devices train locally; only updates are aggregated.
- Preserves data locality but adds coordination complexity.
- Vulnerable to poisoning and gradient leakage.
- Pairs with differential privacy for stronger guarantees.

## Related
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — umbrella
- [[wiki/testing/differential-privacy-llm|Differential Privacy for LLMs]] — noise addition
- [[wiki/testing/data-poisoning-llm|Data Poisoning of LLMs]] — attack risk
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — deployment context
- [[wiki/llm-agents/data-minimization-agents|Data Minimization for Agents]] — data governance
