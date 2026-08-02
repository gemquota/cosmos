---
type: "concept"
title: "Differential Privacy for LLMs"
description: "Adding calibrated noise to limit what models reveal about training data"
tags: ["dp-llm", "privacy", "dp", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Differential Privacy for LLMs

## Summary
Adding calibrated noise to limit what models reveal about training data

## Details
- Guarantees bounded influence of any single example.
- Applied during training, fine-tuning, or output filtering.
- Noise reduces utility; tuning balances the trade-off.
- Mitigates membership-inference-attacks.

## Related
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — umbrella
- [[wiki/testing/membership-inference-attacks|Membership Inference Attacks]] — threat addressed
- [[wiki/testing/federated-learning|Federated Learning]] — complementary method
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — memorization control
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — family
