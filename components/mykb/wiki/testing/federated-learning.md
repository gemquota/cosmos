---
type: "concept"
title: "Federated Learning"
description: "Training models across decentralized data without centralizing the raw data"
tags: ["federated", "privacy", "distributed", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Federated Learning

## Summary
Federated learning trains models across decentralized data without centralizing the raw data: clients (devices or organizations) train locally on their own data, and only model updates are sent to a server and aggregated. It preserves data locality at the cost of coordination complexity, and it is a core pattern in privacy-preserving machine learning.

## Details
- **How it works** — each round, the server sends the current model to a sample of clients; clients train for a few local steps on their data; the server aggregates the updates (typically by averaging) and repeats.
- **Data locality** — raw data never leaves the client, which helps with privacy regulation and with corpora that cannot be pooled; the trade-off is that the server never sees the data distribution directly.
- **Coordination costs** — clients are heterogeneous (different data sizes, compute, connectivity); stragglers, dropped clients, and non-IID data distributions complicate aggregation and convergence.
- **Privacy limits** — updates still leak information: gradients can reveal training data through attacks, so federated learning is paired with differential privacy (noise on updates) and secure aggregation (encrypted update sums) for stronger guarantees.
- **Attacks** — poisoning is a primary risk: malicious clients can inject backdoors via crafted updates; robustness measures include clipping, anomaly detection, and reputation systems.
- **Use cases** — mobile keyboard prediction and on-device personalization are canonical; cross-organization training (hospitals, banks) applies the same pattern where data cannot be shared.
- **Evaluation** — benchmark convergence against centralized training on a comparable task; performance gaps from non-IID data and communication limits should be measured and reported.

- **Communication efficiency** — updates per round are bandwidth-bound; compression, update sparsification, and fewer aggregation rounds are the standard levers, and the trade-off between local steps and global rounds is an empirical tuning question.
## Related
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — umbrella
- [[wiki/testing/differential-privacy-llm|Differential Privacy for LLMs]] — noise addition
- [[wiki/testing/data-poisoning-llm|Data Poisoning of LLMs]] — attack risk
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — deployment context
- [[wiki/llm-agents/data-minimization-agents|Data Minimization for Agents]] — data governance
- [[wiki/concepts/privacy-attacks-llm|Privacy Attacks on LLMs]] — leakage risk
