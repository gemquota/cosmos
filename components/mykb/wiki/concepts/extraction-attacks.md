---
type: "concept"
title: "Extraction Attacks"
description: "Recovering training data from model outputs"
tags: ["extraction", "attacks", "privacy"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Extraction Attacks

## Summary
Extraction attacks prompt or query models to recover memorized training data.

## Details
- Extraction attacks prompt or query models to recover memorized training data.
- Success depends on memorization, prompting skill, and model size.
- Membership inference is the weaker cousin: just detecting whether an example was in training.
- RSIS3 relevance: any knowledge store with sensitive records faces extraction-style risks.

## Related
- [[wiki/concepts/training-data-extraction|Training Data Extraction]] — the same problem
- [[wiki/concepts/training-data-memorization|Training Data Memorization]] — the enabler
- [[wiki/concepts/privacy-attacks-llm|Privacy Attacks on LLMs]] — the family
- [[wiki/concepts/exfiltration-evals|Exfiltration Evals]] — the agentic form
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/data-storage/data-versioning-models|Data Versioning Models]] — existing graph context
