---
type: "concept"
title: "Data Poisoning in Practice"
description: "Attacks that corrupt training data to steer models"
tags: ["poisoning", "attacks", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Poisoning in Practice

## Summary
Data poisoning injects crafted examples into training data so the model learns attacker-chosen behavior.

## Details
- Data poisoning injects crafted examples into training data so the model learns attacker-chosen behavior.
- Backdoors are the targeted form; general poisoning degrades quality.
- Defenses: data provenance, filtering, robust aggregation, and audits.
- RSIS3 relevance: unvetted sources in the wiki are a poisoning vector for its embeddings.

## Related
- [[wiki/concepts/backdoor-attacks-llm|Backdoor Attacks on LLMs]] — the targeted form
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the delivery path
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — the defense
- [[wiki/concepts/red-teaming-ai|Red Teaming AI]] — the detection
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]] — the full treatment of this theme
