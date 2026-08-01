---
type: "concept"
title: "Re-platforming"
description: "Migrating with targeted upgrades to managed services without rewriting application code"
tags: ["migration", "replatform", "managed-services", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Re-platforming

## Summary
Re-platforming moves a workload to the cloud and swaps a few components for managed equivalents — a database becomes a managed service, a VM fleet becomes containers.

## Details
- Typical swaps: self-managed databases to managed services, VMs to containers or PaaS, storage to object storage.
- Code stays mostly intact, so risk stays low; operations load drops sharply.
- Choose swaps by leverage: the biggest operational pain points first.
- Open question: when does replatforming cross the line into a full refactor?

## Related
- [[wiki/infrastructure/containerization|Containerization]] — replatforming destination for VM apps
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]] — the strategy family it belongs to
- [[wiki/cloud-infra/lift-and-shift|Lift-and-Shift]] — the minimal-change alternative
- [[wiki/devops-infra/docker-compose|Docker Compose]] — local container replatforming
