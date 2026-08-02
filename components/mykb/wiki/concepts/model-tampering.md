---
type: "concept"
title: "Model Tampering"
description: "Unauthorized modification of a model after release"
tags: ["tampering", "models", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Tampering

## Summary
Model tampering is altering a deployed model's weights, config, or behavior without authorization.

## Details
- Model tampering is altering a deployed model's weights, config, or behavior without authorization.
- It includes weight swapping, quantization attacks, and runtime patching.
- Integrity checks (hashing, attestation) detect and deter it.
- RSIS3 relevance: the bundle pins scripts and schemas to detect tampering.

## Related
- [[wiki/concepts/weight-poisoning|Weight Poisoning]] — the attack form
- [[wiki/decisions/model-license-risks|Model License Risks]] — the legal form
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the delivery
- [[wiki/syntheses/patch-management-ai|Patch Management for AI]] — the defense
- [[wiki/concepts/self-modification-safety|Self-Modification Safety]] — the full treatment of this theme
- [[wiki/testing/model-scanning-ai-vulnerabilities|Model Scanning Ai Vulnerabilities]] — existing graph context
