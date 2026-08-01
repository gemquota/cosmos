---
type: "concept"
title: "Reproducible Builds"
description: "Builds that produce byte-identical outputs from the same source, given the same inputs"
tags: ["builds", "reproducibility", "supply-chain", "verification"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Reproducible Builds

## Summary
A build is reproducible when the same source and inputs always yield the same artifact. This lets anyone verify that a released binary matches its source — a cornerstone of software supply chain security.

## Details
- Enemies of reproducibility: timestamps, absolute paths, network-dependent downloads, and unordered iteration.
- Tools include build determinism checkers and the Reproducible Builds project's verification infrastructure.
- RSIS3 relevance: wiki artifacts (JSON indexes) should regenerate deterministically from source notes.

## Related
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — reproducibility enables artifact verification
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — shared builds make reproducibility uniform
- [[wiki/dev-tools/lockfiles|Lockfiles]] — pinned dependency graphs stabilize inputs
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — CI is where reproducibility is enforced
