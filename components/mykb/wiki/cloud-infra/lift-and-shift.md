---
type: "concept"
title: "Lift-and-Shift"
description: "Migrating workloads to the cloud with minimal changes, replicating the old architecture as-is"
tags: ["migration", "lift-and-shift", "cloud", "rehost"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Lift-and-Shift

## Summary

Lift-and-shift migrates workloads to the cloud without redesigning them — same VMs, same architecture, rehosted. It is the fastest migration path and the one most likely to carry over-premises habits, costs, and failure modes into the new environment.

## Details
- Mechanism: workloads are replicated to cloud VMs (agent-based replication, disk imaging, or re-deployment of artifacts), networking is extended (VPN/peering, IP preservation), and cutover happens per application; the app still runs as it did on-prem — which is the point and the trap.
- Concrete example: a legacy ERP with rigid IPs and OS-level dependencies moves to EC2 with the same topology and is live in weeks; the team then spends a year discovering that its on-prem assumptions (shared nothing over NFS, fixed IPs, no autoscaling) do not exploit cloud elasticity or its cost model.
- Failure modes: moving licensing into the cloud unchanged (per-core costs multiply); oversized VMs mirroring on-prem server sprawl; stateful assumptions (local disks, hostnames, sticky IPs) breaking automation; and skipping the optimization phase, so the migration saves no money and adds complexity.
- Operational tradeoffs: lift-and-shift buys speed and low execution risk; the follow-on phases (replatform, refactor) capture the economics. Treat it as step one with a documented optimization roadmap and a cost baseline measured before cutover, not after.
- RSIS3/mykb relevance: the wiki's migration playbook sequences lift-and-shift then right-sizing; this note records the post-migration checklist the loop applies to each workload.
- Cutover planning: run a parallel migration window with rollback, verify data consistency (checksums, row counts), and keep the source environment until the first billing cycle proves the destination is stable.
- Post-migration hygiene: retire decommissioned on-prem capacity immediately to avoid double-paying during the transition; schedule the right-sizing pass within 90 days.

## Related
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]] — one option on the migration menu
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the unit of rehosting
- [[wiki/cloud-infra/re-platforming|Re-platforming]] — the incremental upgrade path
- [[wiki/devops-infra/terraform|Terraform]] — recreating the topology as code
