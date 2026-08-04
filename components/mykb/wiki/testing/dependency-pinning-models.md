---
type: "concept"
title: "Dependency Pinning for Models"
description: "Locking model versions, weights, and packages to exact hashes for reproducibility"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["pinning", "dependencies", "reproducibility", "security", "supply-chain"]
status: "growing"

# Dependency Pinning for Models

## Summary
Dependency pinning for models means locking model versions, weights, and packages to exact hashes so that every deployment runs the same artifact. It matters because models drift silently: a floating "latest" tag can change behavior between runs. Pinning makes deployments reproducible, auditable, and resistant to supply-chain tampering.

## Details
- **Definition** — pinning records exact versions and content hashes for the model artifact, its tokenizer, and the runtime packages.
- **Artifact hashes** — hashing weights and configs verifies that what was tested is exactly what ships.
- **Version tags** — moving tags such as latest are resolved once and frozen, avoiding surprise upgrades.
- **Reproducibility** — a pinned environment reproduces the same inference behavior, which is essential for debugging and audits.
- **Supply chain** — pinning limits the blast radius of a compromised dependency by making the installed set explicit.
- **Verification** — hashes should be checked at load time so corrupted or swapped artifacts fail loudly.
- **Common failure modes** — pinning packages but not model weights, and upgrading a pinned version without re-running the evaluation suite.
- **Worked example** — a serving pipeline records the model hash and package lock; a deployment verifies the hash before loading, and any mismatch aborts.
- **Practical relevance** — pinning is the foundation of trustworthy model versioning and registry practice.

- **Environment pins** — the runtime, libraries, and their transitive dependencies are locked alongside the model.
- **Diff discipline** — any pin change should trigger re-evaluation, since behavior can shift with versions.
- **Inventory** — pinning pairs with SBOMs so every pinned component is known and scannable.
- **Audit trail** — recording who changed a pin and why supports review and rollback when behavior shifts.
## Related
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — versioning layer
- [[wiki/testing/supply-chain-llm-deps|Supply Chain for LLM Dependencies]] — risk context
- [[wiki/testing/sbom-for-models|SBOMs for Models]] — inventory
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — pipeline integration
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — reproducibility
- [[wiki/security/supply-chain-security|Supply Chain Security]] — broader practice
