---
type: "concept"
title: "Weight Poisoning"
description: "Directly corrupting model weights with malicious behavior"
tags: ["weights", "poisoning", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Weight Poisoning

## Summary
Weight poisoning modifies model weights directly to implant behavior, bypassing training-data defenses.

## Details
- Weight poisoning modifies model weights directly to implant behavior, bypassing training-data defenses.
- Open-weights distribution makes poisoned weights easy to spread.
- Verification (reproducible builds, hashes) is the main defense.
- RSIS3 relevance: reproducible scripts and pinned dependencies are the bundle's hash-based integrity.

## Related
- [[wiki/concepts/model-tampering|Model Tampering]] — the generic act
- [[wiki/concepts/trojan-attacks|Trojan Attacks]] — the behavior
- [[wiki/decisions/open-weights|Open Weights]] — the distribution channel
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the attack class
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]] — the full treatment of this theme
- [[wiki/testing/model-poisoning|Model Poisoning]] — existing graph context
