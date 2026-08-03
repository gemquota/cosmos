---
type: "concept"
title: "Patch Management"
description: "Processes for tracking, testing, and applying security updates"
tags: ["patch", "updates", "security", "lifecycle"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Patch Management

## Summary
Patch management is the process of keeping software updated against known vulnerabilities and bugs — tracking what is installed, prioritizing what matters, testing, deploying, and verifying. "Revisited" reflects modern practice: automated, continuous patching with SBOM-driven prioritization, in place of quarterly manual maintenance windows.

## Details
- Mechanism: an inventory (agents, SBOMs, image scanners) feeds a vulnerability database; prioritization weighs severity, exploitability, exposure, and asset criticality; automation (Renovate, Dependabot, image rebuilds, patch-bake pipelines) creates and applies updates; verification runs tests after each patch; the cycle is continuous rather than windowed.
- Concrete example: Renovate opens PRs for dependency updates as they release; CI builds, tests, and scans each; container images are rebuilt weekly and redeployed; high-severity, internet-exposed CVEs get an expedited one-off patch; patches to the OS layer follow the immutable-image rebuild path.
- Failure modes: patch backlog from understaffed review (prioritize by exploitability, not severity alone); automation that updates blindly and breaks production (pin, test, and roll back); patching that is not verified — a CVE closes while the vulnerable code path still ships; the firefighting pattern where only known-exploited CVEs get patched, leaving the rest to pile up.
- Tradeoffs: continuous patching reduces the window of exposure but costs pipeline time and carries regression risk; manual windows are predictable but leave systems vulnerable in between; the mature pattern is automated updates plus test gates and fast rollback, with expedite paths for emergencies.
- Operational notes: keep an SBOM per artifact, measure time-to-patch per severity, and rehearse the expedite path.
- RSIS3 relevance: the cosmos stack (python, node, dashboard deps) should run the same continuous patch loop — RSIS3 can even treat patch cadence as one of its operational telemetry signals.

## Related
- [[wiki/os-shell/logical-volume-management|Logical Volume Management]]
- [[wiki/devops-infra/helm-and-chart-management|Helm & Chart Management]]
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
