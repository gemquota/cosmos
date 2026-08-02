---
type: "concept"
title: "Backdoor Attacks on LLMs"
description: "Hidden triggers that flip model behavior"
tags: ["backdoors", "attacks", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backdoor Attacks on LLMs

## Summary
Backdoor attacks plant triggers in training data that activate attacker-chosen behavior at inference.

## Details
- Backdoor attacks plant triggers in training data that activate attacker-chosen behavior at inference.
- Backdoored models behave normally until the trigger fires.
- Detection is hard at scale; provenance and differential inspection help.
- RSIS3 relevance: poisoned wiki content could trigger bad retrieval outcomes.

## Related
- [[wiki/concepts/trojan-attacks|Trojan Attacks]] — the weight-level form
- [[wiki/concepts/data-poisoning-practice|Data Poisoning in Practice]] — the delivery
- [[wiki/concepts/model-tampering|Model Tampering]] — the post-training form
- [[wiki/concepts/weight-poisoning|Weight Poisoning]] — the weight-level attack
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]] — the full treatment of this theme
- [[wiki/ai-ml/data-poisoning|Data Poisoning]] — existing graph context
