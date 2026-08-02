---
type: "concept"
title: "Privacy Attacks on LLMs"
description: "Methods for extracting or inferring private information"
tags: ["privacy", "attacks", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Privacy Attacks on LLMs

## Summary
Privacy attacks on LLMs include extraction, membership inference, and prompt-based PII recovery.

## Details
- Privacy attacks on LLMs include extraction, membership inference, and prompt-based PII recovery.
- Larger models memorize more, raising the stakes.
- Defenses span training (dedup, DP), deployment (filters), and policy (data minimization).
- RSIS3 relevance: knowledge graphs holding personal data need the same threat model.

## Related
- [[wiki/concepts/extraction-attacks|Extraction Attacks]] — the main attack
- [[wiki/concepts/training-data-memorization|Training Data Memorization]] — the root
- [[wiki/testing/differential-privacy-llm|Differential Privacy Llm]] — a defense
- [[wiki/decisions/data-license-issues|Data License Issues]] — the legal frame
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
