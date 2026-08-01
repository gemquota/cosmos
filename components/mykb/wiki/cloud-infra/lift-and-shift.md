---
type: "concept"
title: "Lift-and-Shift"
description: "Migrating workloads to the cloud with minimal changes, replicating the old architecture as-is"
tags: ["migration", "lift-and-shift", "cloud", "rehost"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Lift-and-Shift

## Summary
Lift-and-shift (rehost) moves an application to the cloud with its architecture essentially unchanged — same VMs, same topology, now running in the cloud.

## Details
- Speed wins: the shortest path to retiring a data center, ideal when leases or capacity force the move.
- You inherit the old architecture's weaknesses: no autoscaling, no managed services, same single points of failure.
- Plan a second wave of optimization once migration pressure is gone.
- Open question: how to stop lift-and-shift from becoming permanent technical debt.

## Related
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]] — one option on the migration menu
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the unit of rehosting
- [[wiki/cloud-infra/re-platforming|Re-platforming]] — the incremental upgrade path
- [[wiki/devops-infra/terraform|Terraform]] — recreating the topology as code
