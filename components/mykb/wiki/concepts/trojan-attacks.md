---
type: "concept"
title: "Trojan Attacks"
description: "Models carrying hidden malicious behavior from training"
tags: ["trojan", "attacks", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Trojan Attacks

## Summary
Trojan attacks embed hidden malicious behavior into models during training or fine-tuning, activated by specific inputs.

## Details
- Trojan attacks embed hidden malicious behavior into models during training or fine-tuning, activated by specific inputs.
- Open-weight models are the main exposure: users can't fully audit them.
- Trojan detection (trigger recovery) is an active research area.
- RSIS3 relevance: third-party components in the bundle should be scanned and pinned.

## Related
- [[wiki/concepts/backdoor-attacks-llm|Backdoor Attacks on LLMs]] — the same family
- [[wiki/concepts/weight-poisoning|Weight Poisoning]] — the mechanism
- [[wiki/decisions/open-weights|Open Weights]] — the exposure
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the delivery
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]] — the full treatment of this theme
- [[wiki/ai-ml/data-poisoning|Data Poisoning]] — existing graph context
