---
type: "concept"
title: "Terraform State Management"
description: "Storing, locking, and sharing Terraform state so plan/apply is safe in teams"
tags: ["terraform", "state", "iac", "devops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Terraform State Management

## Summary
Terraform state records the real-world resources a configuration manages; plan/apply compares desired config to this state.

## Details
- Remote backends (S3, GCS, Terraform Cloud) share state and lock it against concurrent applies.
- State is sensitive: it embeds resource metadata and sometimes secrets — encrypt and protect it.
- When state and reality diverge, import or refresh carefully; blind edits corrupt planning.
- Open question: how to split state across environments and services without coupling.

## Related
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]] — the practice state supports
- [[wiki/infrastructure/configuration-drift|Configuration Drift]] — state vs reality divergence
- [[wiki/cloud-infra/cloud-emulators|Cloud Emulators]] — local state for emulated providers
- [[wiki/devops-infra/terraform|Terraform]] — the tool whose state this manages
