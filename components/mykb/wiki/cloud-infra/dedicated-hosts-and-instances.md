---
type: "concept"
title: "Dedicated Hosts & Instances"
description: "Single-tenant servers for compliance and performance isolation"
tags: ["dedicated-hosts", "tenancy", "cloud", "compliance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Dedicated Hosts & Instances

## Summary

Dedicated hosts and instances give a customer exclusive use of a physical server: for licensing (per-core/per-socket), compliance (no noisy neighbors), or predictable placement. They cost more than shared tenancy and matter only when those constraints are real.

## Details
- Mechanism: dedicated hosts (AWS) and isolated VMs (GCP sole-tenant nodes, Azure dedicated hosts) guarantee an entire physical machine: instance placement is controlled, host affinity can pin instances, and capacity is reserved on that host; dedicated instances (AWS) give exclusive tenancy of the host without placement control, costing the same premium with fewer features.
- Concrete example: an Oracle or Windows Server license tied to sockets/cores forces dedicated hosts so the physical core count matches licensing; a regulated workload demands sole tenancy to exclude other customers; a latency-critical pair wants host affinity so instances share the same NUMA/network path.
- Failure modes: paying for dedicated tenancy without a licensing or compliance driver (pure cost); confusing dedicated instances with dedicated hosts and losing placement control; host-level maintenance events taking down all pinned instances at once (plan for host replacement); and capacity assumptions — dedicated hosts reserve a whole host, wasting unused vCPUs.
- Operational tradeoffs: the premium buys isolation and placement control, not performance (shared tenancy is usually equal or better price-performance); use savings plans/reserved coverage on hosts and keep host pools sized for failover. Re-evaluate annually — licensing deals change.
- RSIS3/mykb relevance: the wiki's compliance-sensitive workloads are on dedicated hosts with a placement diagram; this note documents the justification so the loop does not spread dedicated tenancy by default.
- Utilization: track host-level vCPU utilization; a dedicated host at 20% utilization is the clearest sign the licensing rationale should be re-audited.

## Related
- [[wiki/infrastructure/bastion-hosts-and-jump-boxes|Bastion Hosts & Jump Boxes]]
- [[wiki/cloud-infra/reserved-instances-vs-on-demand|Reserved vs On-Demand Instances]]
- [[wiki/cloud-infra/spot-instances|Spot Instances]]
- [[wiki/cloud-infra/burstable-instances|Burstable Instances]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
