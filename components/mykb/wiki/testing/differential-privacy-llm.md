---
type: "concept"
title: "Differential Privacy for LLMs"
description: "Adding calibrated noise to limit what models reveal about training data"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["dp-llm", "privacy", "dp", "training", "membership-inference"]
status: "growing"

# Differential Privacy for LLMs

## Summary
Differential privacy for LLMs adds calibrated noise to training, fine-tuning, or outputs so that no single training example has a measurable influence on results. It matters because language models can memorize and repeat sensitive data. Differential privacy provides a formal bound on what a model can reveal, which is its unique value.

## Details
- **Definition** — a mechanism is differentially private if the chance of any output changes only slightly when one individual's data is added or removed.
- **Noise calibration** — the privacy budget controls how much noise is added; more noise means stronger privacy and lower utility.
- **Training-time DP** — applying noise to gradients during training bounds memorization of the training set.
- **Fine-tuning DP** — private fine-tuning protects the specific data used for adaptation, which is often the most sensitive.
- **Output filtering** — detecting and suppressing memorized text at serving time complements training-time protections.
- **Threat addressed** — the main attack is membership inference: determining whether a specific example was in the training data.
- **Common failure modes** — misinterpreting the privacy budget, and treating noised training as a substitute for data hygiene.
- **Worked example** — a fine-tuning run on customer data uses a fixed privacy budget; the resulting model passes membership-inference checks on held-out sensitive examples.
- **Practical relevance** — differential privacy is the strongest practical guarantee for protecting training data, at a real utility cost.

- **Budget management** — the privacy budget is consumed over repeated runs; teams must track it across the model's life.
- **Utility loss** — noisy training degrades quality; the budget must be sized to the task's tolerance.
- **Evaluation** — privacy claims should be validated with membership-inference probes on real data splits.
## Related
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — umbrella
- [[wiki/testing/membership-inference-attacks|Membership Inference Attacks]] — threat addressed
- [[wiki/testing/federated-learning|Federated Learning]] — complementary method
- [[wiki/ai-ml/data-deduplication-llm|Data Deduplication for LLMs]] — memorization control
- [[wiki/llm-agents/data-minimization-agents|Data Minimization for Agents]] — reducing exposure
- [[wiki/testing/encrypted-inference|Encrypted Inference]] — private serving
