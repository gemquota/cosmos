---
type: "concept"
title: "Configuration Drift"
description: "When running systems diverge from declared state due to manual edits and failed automation"
tags: ["configuration", "drift", "iac", "governance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Configuration Drift

## Summary
Configuration drift is the gap between what infrastructure should be (per code) and what it actually is, caused by manual changes, failed applies, and time.

## Details
- Sources: out-of-band edits, partial applies, human debugging sessions, and expired secrets.
- Detection: plan output in IaC, config audits, and immutable infrastructure that cannot drift.
- Prevention: single source of truth, change approval, and reconciliation loops.
- Open question: how aggressively to auto-remediate drift vs alert on it.

## Related
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]] — declared state drift measures
- [[wiki/infrastructure/configuration-management|Configuration Management]] — convergence as the fix
- [[wiki/devops-infra/tfstate-management|Terraform State Management]] — state as the drift record
- [[wiki/devops-infra/terraform|Terraform]] — plan output shows drift
