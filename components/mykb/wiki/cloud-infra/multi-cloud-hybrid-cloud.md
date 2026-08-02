---
type: "concept"
title: "Multi-Cloud & Hybrid Cloud"
description: "Operating across providers and between cloud and on-prem"
tags: ["multi-cloud", "hybrid", "strategy", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://en.wikipedia.org/wiki/Hybrid_cloud",
  "https://aws.amazon.com/hybrid/",
]
---

# Multi-Cloud & Hybrid Cloud

## Summary
Multi-cloud runs workloads across multiple providers; hybrid cloud extends on-premises infrastructure into the cloud. Both increase resilience and flexibility at the cost of operational complexity. Strategy matters more than technology in either case.

## Details
- Multi-cloud avoids provider lock-in and single-provider outages but duplicates skills, tooling, and networking across clouds.
- Hybrid architectures connect on-premises systems to cloud services through VPNs, dedicated links, or managed connectors.
- AWS describes hybrid patterns including Outposts, Direct Connect, and managed connectors for on-premises links.
- Data gravity, egress costs, and latency usually decide where workloads actually run in a hybrid design.
- Consistent IaC and GitOps make multi-environment management tractable across cloud and on-premises targets.
- In mykb, multi-cloud connects to VPC peering, GitOps, and environment promotion models.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]]
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]]
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]]
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]]
