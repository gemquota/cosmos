---
type: "concept"
title: "Data Poisoning"
description: "Adversarial corruption of training data to implant targeted behaviours or backdoors in a model"
tags: ["data-poisoning", "security", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Data Poisoning

## Summary
Data poisoning injects malicious samples into training corpora so the model learns to misbehave on trigger inputs while appearing normal otherwise. It is a supply-chain threat for anyone fine-tuning on untrusted data.

## Details
- Backdoor triggers: specific tokens or contexts flip behaviour at inference time.
- Risks grow with web-scraped fine-tuning data and community datasets.
- Detection is hard; defenses include data provenance, filtering, and outlier analysis.
- RSIS3 relevance: mykb-curated fine-tune data is a supply chain that needs provenance and checksums.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The runtime sibling of poisoning
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — Probing for planted backdoors
- [[wiki/ai-ml/sft|SFT]] — The training stage attackers target
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — The activity that exposes the supply chain
- [[raw/archive/session-artifacts-2026-07/topics/security|security — Supply-chain security domain
