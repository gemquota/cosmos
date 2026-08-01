---
type: "concept"
title: "Multi-Cloud Strategy"
description: "Deliberate use of multiple cloud providers for resilience, best-of-breed services, or cost leverage"
tags: ["multi-cloud", "cloud", "strategy", "resilience", "lock-in"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://aws.amazon.com/what-is/multicloud/"]
---

# Multi-Cloud Strategy

## Summary
A multi-cloud strategy deliberately runs workloads across two or more cloud providers. The motivations are resilience against provider outages, access to best-of-breed services, regulatory or data-residency needs, and negotiating leverage. The price is real complexity: duplicated tooling, network plumbing, skills, and operational surface.

## Details
- Resilience pattern: active-passive keeps a full standby in a second provider (expensive but real); active-active splits traffic and requires data replication across clouds.
- Avoiding lock-in is the stated goal, but the lock-in often migrates upward into Kubernetes, Terraform, and API abstractions rather than disappearing.
- Best-of-breed trade: each provider excels somewhere (managed AI, serverless, data warehouses); multi-cloud lets teams mix, at the cost of multiple consoles and IAM models.
- Data gravity is the hard constraint: replicating databases across clouds is slow, expensive, and complicated — multi-cloud tends to work best at the stateless edge and worst at the data core.
- Cost arbitrage exists but is frequently a myth in practice: discounted committed use, egress fees, and duplicated engineering often offset savings.
- Tooling: Terraform and Kubernetes provide a portable substrate; identity, secrets, and observability must still be unified across providers.
- Worked example: mykb could serve static content from two CDN-backed providers while keeping its stateful database single-cloud — a pragmatic middle ground.

## Related
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]] — how workloads arrive in multiple clouds
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]] — the economic side of multi-cloud
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]] — resilience motivation for multi-cloud
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]] — portable substrate across providers
- [[wiki/devops-infra/terraform|Terraform]] — provisioning across clouds uniformly
- [[wiki/devops-infra/kubernetes|Kubernetes]] — portable workload layer
