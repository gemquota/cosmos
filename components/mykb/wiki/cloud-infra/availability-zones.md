---
type: "concept"
title: "Availability Zones"
description: "Isolated failure domains within a cloud region that make multi-AZ architectures resilient"
tags: ["availability-zones", "resilience", "regions", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html", "https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview"]
---

# Availability Zones

## Summary
Availability zones are physically separate data center clusters inside a region with independent power, cooling, and network. Spreading workloads across zones protects against facility-level failures while keeping latency low.

## Details
- AZs give low-latency (single-digit ms) redundancy that multi-region setups cannot match.
- Stateless tiers replicate easily; stateful tiers need replication (databases) or zonal snapshots.
- Cross-AZ data transfer usually costs money, so placement is a cost-vs-resilience decision.
- Open questions: zonal vs regional services, AZ-aware scheduling, and testing zonal failure.
- Availability zones are physically separate, isolated locations within a region; each has independent power, cooling, and networking, and they are connected by low-latency links.
- Deploying across zones protects against zone-level failures — a datacenter outage takes down one zone but not the whole region.
- Zone-agnostic services (like managed databases with multi-zone replication) hide the placement decision; zone-scoped resources require explicit design.
- Multi-zone design costs cross-zone data transfer and latency, so the replication strategy must justify the price.
- **Worked example / comparison** — Worked example — a wiki backend runs one replica per zone behind a load balancer; when a zone loses power, traffic shifts to the healthy replicas without downtime.
- For mykb, availability zones are documented as the regional reliability primitive that underlies the cloud-infra cluster.

## Related
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]]
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]]
- [[wiki/cloud-infra/subnet-design|Subnet Design]]
- [[wiki/devops-infra/replication|Replication]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
