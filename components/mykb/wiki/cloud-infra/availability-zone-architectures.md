---
type: "concept"
title: "Availability Zone Architectures"
description: "Placing workloads across AZs for failure independence"
tags: ["az", "availability", "architecture", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html",
  "https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview",
]
---

# Availability Zone Architectures

## Summary
Availability-zone architectures place replicated components across independent failure domains to survive facility outages. The pattern applies to databases, load balancers, and stateless compute alike. Zone-aware design is the difference between high availability and a single point of failure.

## Details
- AWS documents using regions and availability zones for fault-tolerant architecture, with resources mirrored across zones so a single facility failure does not take down the workload.
- Azure availability zones offer zonal services and zone-redundant storage.
- Stateless tiers scale across zones behind a load balancer; stateful tiers use quorum or synchronous replication.
- Cross-zone traffic costs and latency are the price of independence.
- Pod topology spread constraints bring the same idea to Kubernetes scheduling.
- Zone failures should be tested: a zone outage during game days reveals whether failover actually works.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/cloud-infra/dns-zone-transfers|DNS Zone Transfers]]
- [[wiki/infrastructure/asic-and-switching-architectures|ASIC & Switching Architectures]]
- [[wiki/cloud-infra/availability-zones|Availability Zones]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
