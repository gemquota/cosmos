---
type: "concept"
title: "Reproducible Builds"
description: "Builds that produce byte-identical outputs from the same source, given the same inputs"
tags: ["builds", "reproducibility", "supply-chain", "verification"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://reproducible-builds.org/", "https://reproducible-builds.org/specs/"]
---

# Reproducible Builds

## Summary
A build is reproducible when the same source and inputs always yield the same artifact. This lets anyone verify that a released binary matches its source — a cornerstone of software supply chain security.

## Details
- Enemies of reproducibility: timestamps, absolute paths, network-dependent downloads, and unordered iteration.
- Tools include build determinism checkers and the Reproducible Builds project's verification infrastructure.
- RSIS3 relevance: wiki artifacts (JSON indexes) should regenerate deterministically from source notes.
- A build is reproducible when the same inputs deterministically produce the same output, verified by byte-identical artifacts.
- The enemies of reproducibility are timestamps, random seeds, absolute paths, locale, and ambient network state; each must be pinned or removed.
- Reproducible builds strengthen the supply chain: independent rebuilds can verify that a released artifact matches its source.
- The practice is a spectrum — full byte-reproducibility is a goal, and partial gains still improve debugging and caching.
- **Worked example / comparison** — Worked example — the wiki bundle build fixes timestamps and locale, vendors dependencies, and emits a manifest of artifact hashes; a CI rebuild matches the released bundle byte-for-byte.
- For mykb, reproducible-builds is documented as the outcome that devcontainers, pinned toolchains, and hermetic builds together produce.

## Related
- [[wiki/security/supply-chain-security|Software Supply Chain Security]]
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/deep-dives|Deep Dives]]
