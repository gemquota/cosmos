---
type: "concept"
title: "Privacy-Preserving ML"
description: "Techniques that train and serve models without exposing sensitive data"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["privacy-ml", "privacy", "ml", "security", "data-protection"]
status: "growing"

# Privacy-Preserving ML

## Summary
Privacy-preserving ML is the family of techniques that train and serve models without exposing sensitive data. It matters because data protection is a legal and ethical requirement, not just a preference. These techniques trade utility, privacy, and cost, so choosing among them requires clear priorities.

## Details
- **Federated learning** — models train across devices or sites while raw data stays local, with only updates shared.
- **Differential privacy** — calibrated noise bounds what any single example can reveal in the trained model.
- **Secure computation** — multi-party computation and homomorphic encryption let parties compute over private data jointly.
- **Encrypted inference** — models run over encrypted inputs so servers never see plaintext queries.
- **Trusted hardware** — secure enclaves protect data during processing with hardware guarantees.
- **Data minimization** — reducing what is collected and retained shrinks the exposure surface before any technique is applied.
- **Trade-offs** — every technique costs utility, latency, or engineering effort; the right mix depends on the threat model.
- **Common failure modes** — applying a technique without a threat model, and overstating protections in documentation.
- **Worked example** — a health application trains a model with federated learning across hospitals and serves predictions through encrypted inference.
- **Practical relevance** — privacy-preserving ML makes compliance and user trust engineering problems with concrete tools.

- **Threat models** — each technique protects against specific adversaries; choosing one requires naming the adversary.
- **Composition** — techniques combine, such as federated learning with differential privacy, for stronger guarantees.
- **Auditability** — documenting which technique protects what makes privacy claims checkable by reviewers.
- **Evaluation** — privacy techniques need measurement of the utility loss they impose, not just the guarantee they claim.
## Related
- [[wiki/testing/federated-learning|Federated Learning]] — distributed private training
- [[wiki/testing/differential-privacy-llm|Differential Privacy for LLMs]] — formal guarantees
- [[wiki/testing/encrypted-inference|Encrypted Inference]] — private serving
- [[wiki/testing/secure-enclaves-inference|Secure Enclaves for Inference]] — hardware trust
- [[wiki/llm-agents/data-minimization-agents|Data Minimization for Agents]] — applied privacy
- [[wiki/llm-agents/consent-and-privacy-agents|Consent and Privacy for Agents]] — consent handling
