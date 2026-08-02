---
type: "concept"
title: "Data Poisoning of LLMs"
description: "Injecting malicious or manipulated examples into training or fine-tuning data to alter model behavior"
tags: ["security", "training-data", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Poisoning of LLMs

## Summary
Injecting malicious or manipulated examples into training or fine-tuning data to alter model behavior

## Details
- Poisoned examples can backdoor outputs or degrade safety.
- Attackers target public datasets and scraped corpora.
- Defenses: data provenance, dedup, filtering, and sandboxed evaluation.
- Supply-chain risk grows with fine-tuning on third-party data.

## Related
- [[wiki/testing/supply-chain-llm-deps|Supply Chain for LLM Dependencies]] — adjacent supply-chain risk
- [[wiki/ai-ml/data-filtering|Data Filtering]] — mitigation layer
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — quality gate
- [[wiki/testing/model-poisoning|Model Poisoning]] — downstream variant
- [[wiki/testing/red-team-processes|Red Team Processes]] — detecting planted behavior
