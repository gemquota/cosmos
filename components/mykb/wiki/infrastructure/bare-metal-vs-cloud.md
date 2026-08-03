---
type: "concept"
title: "Bare Metal vs Cloud"
description: "Owning hardware versus renting virtualized capacity"
tags: ["bare-metal", "cloud", "hosting", "infrastructure"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Bare Metal vs Cloud

## Summary
Bare metal versus cloud is the foundational hosting decision: owning or leasing physical hardware versus renting virtualized capacity on demand. The choice is rarely about technology preference alone — it is a tradeoff between control and capital cost on one side, and flexibility and operational leverage on the other, with workload characteristics deciding which side wins.

## Details
- Bare metal means you control the full stack: physical servers (owned or leased), no hypervisor between you and the hardware, no noisy neighbors, and full access to kernel features, custom drivers, and exotic device configurations. The wins are performance (no virtualization overhead, deterministic latency), compliance (hardware in your hands), and cost at sustained high utilization (a server running 100% for years beats the equivalent cloud price). The costs are equally clear: capital or long-term lease commitments, hardware lifecycle management (procurement, refresh, failures, spare parts), and the operations team to run it.
- Cloud means renting capacity with a different cost shape: pay-as-you-go, scale on demand, and the provider absorbs hardware lifecycle, power, cooling, and most failure handling. The wins are elasticity (a burst workload that needs 10x capacity for an hour pays for an hour), agility (no procurement cycle — a new environment in minutes), and leverage (the operations burden shifts to the provider's SREs). The costs: the per-unit price premium at steady utilization, virtualization and shared-tenancy overhead, egress and data-movement fees, and the loss of low-level control.
- The decision framework is utilization and predictability: sustained, predictable workloads with high utilization favor bare metal (or reserved/long-term cloud commitments, which capture much of the discount); variable, bursty, or uncertain workloads favor cloud elasticity. Compliance and data-sovereignty requirements can force bare metal or on-prem regardless of economics, and hybrid deployments split the difference — steady-state on owned hardware, bursts in the cloud.
- Failure modes: the bare-metal bet goes wrong when utilization assumptions are wrong (underutilized hardware is dead capital; an overbooked single site is a single point of failure); the cloud bet goes wrong when cost controls are absent (unbounded egress, orphaned resources, and rightsizing neglect erode the elasticity advantage) or when the workload's determinism requirements collide with shared tenancy.
- For mykb: the node anchors the hosting cluster and connects to cloud-provider, multi-cloud, and security topics — the choice of where workloads run cascades into network design, security-group models, and cost governance.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]] — related coverage in the same cluster
- [[wiki/cloud-infra/multi-cloud-hybrid-cloud|Multi-Cloud & Hybrid Cloud]] — related coverage in the same cluster
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]] — related coverage in the same cluster
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
