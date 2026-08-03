---
type: "concept"
title: "Dependency Management"
description: "The practice of controlling what your software depends on and when it changes"
tags: ["dependencies", "management", "updates", "supply-chain"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Dependency_management", "https://en.wikipedia.org/wiki/Package_manager"]
---

# Dependency Management

## Summary
Dependency management is the discipline of knowing, controlling, and updating everything your software relies on: direct and transitive packages, tools, and runtimes. It balances stability against freshness and treats dependencies as risk to be inventoried and scanned.

## Details
- Know your full graph: lockfiles expose transitive dependencies, and SBOMs record them for auditing.
- Update with cadence, not chaos: automated PRs, grouped updates, and CI verification keep upgrades small.
- Security is a dependency problem: scanning, pinning, and fast response to advisories.
- Version policy matters: ranges for flexibility, pins for reproducibility — pick per context and document it.
- The transitive blight is real: a tiny package deep in the graph can be the critical vulnerability.
- For the mykb bundle, dependency management covers tooling and sources: pinned builds, scanned packages, and tracked source URLs.

Worked example — the wiki's dependency review: Renovate would open grouped PRs weekly, CI would scan each for CVEs, and the SBOM would regenerate per release so the audit trail is current.

- Cadence design: automated PRs, grouped updates, and CI verification keep upgrades small and reviewable; the standing rule is that every update is verified before merge and rolled back on failure.
- Inventory value: lockfiles expose transitive dependencies and SBOMs record them for auditing, so the audit trail can answer what was running when, even after upgrades.
- Scope for the bundle: dependency management would cover tooling and sources — pinned builds, scanned packages, and tracked source URLs — so corpus reproducibility does not depend on a moving toolchain.
- Response discipline: when an advisory arrives, the fix should be prepared on a branch, verified by CI, and merged as a priority update rather than waiting for the next grouped cycle.
- Renewal review: dependencies that are no longer maintained should be flagged for replacement rather than pinned forever; maintenance status is part of the inventory.
## Related
- [[wiki/communities/dependency-updates|Dependency Updates]]
- [[wiki/communities/dependency-graphs|Dependency Graphs]]
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
- [[wiki/communities/renovate-bot|Renovate Bot]]
- [[wiki/dev-tools/package-managers|Package Managers]]
