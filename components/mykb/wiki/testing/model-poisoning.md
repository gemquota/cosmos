---
type: "concept"
title: "Model Poisoning"
description: "Compromising a model through malicious training or fine-tuning data"
tags: ["model-poisoning", "security", "models", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Poisoning

## Summary
Compromising a model through malicious training or fine-tuning data

## Details
- Backdoors trigger on specific inputs while normal behavior persists.
- Fine-tuning on untrusted data is a common vector.
- Defenses: provenance, filtering, and sandboxed evaluation.
- Related to data-poisoning-llm.

## Related
- [[wiki/testing/data-poisoning-llm|Data Poisoning of LLMs]] — data-side attack
- [[wiki/testing/supply-chain-llm-deps|Supply Chain for LLM Dependencies]] — distribution risk
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — curation defense
- [[wiki/testing/model-scanning-ai-vulnerabilities|Model Scanning for AI Vulnerabilities]] — detection
- [[wiki/testing/red-team-processes|Red Team Processes]] — probing
