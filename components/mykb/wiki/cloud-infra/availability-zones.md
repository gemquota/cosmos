---
type: "concept"
title: "Availability Zones"
description: "Isolated failure domains within a cloud region that make multi-AZ architectures resilient"
tags: ["availability-zones", "resilience", "regions", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Availability Zones

## Summary
Availability zones are physically separate data center clusters inside a region with independent power, cooling, and network. Spreading workloads across zones protects against facility-level failures while keeping latency low.

## Details
- AZs give low-latency (single-digit ms) redundancy that multi-region setups cannot match.
- Stateless tiers replicate easily; stateful tiers need replication (databases) or zonal snapshots.
- Cross-AZ data transfer usually costs money, so placement is a cost-vs-resilience decision.
- Open questions: zonal vs regional services, AZ-aware scheduling, and testing zonal failure.

## Related
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — instances spread across zones
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]] — zones as the first DR tier
- [[wiki/cloud-infra/subnet-design|Subnet Design]] — subnets map to zones
- [[wiki/devops-infra/replication|Replication]] — data redundancy across zones
