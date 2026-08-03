---
type: "concept"
title: "Datacenter Redundancy & Failover"
description: "N+1 power, dual paths, and failover design across facilities"
tags: ["redundancy", "failover", "datacenter", "availability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Datacenter Redundancy & Failover

## Summary
Datacenter redundancy is the discipline of having no single points of failure in the facility: N+1 (or 2N) power paths, dual network feeds, redundant cooling, and — at the top level — multiple facilities so that a whole datacenter can fail without ending the service. Failover is the other half: redundancy only helps if the failover actually works, which is why the practice is as much about testing the failover paths as about building them.

## Details
- The redundancy ladder inside a facility: power (dual utility feeds, N+1 UPS modules, generators sized to the load, A/B power paths to every rack — so a UPS module, a feeder, or a generator can fail without dropping a rack), cooling (N+1 chillers and pumps, dual water loops, sufficient airflow redundancy that a fan or pump failure does not create hot spots), and network (dual carriers, diverse fiber entrances, redundant spine paths). The naming convention matters: N+1 means one spare beyond the required count (a single component failure is absorbed), 2N means two full independent systems (one entire system can fail; the other carries everything), and 2(N+1) means two full systems each with their own spares — the tier ladder again, with cost rising steeply per level.
- Failover across facilities: the availability boundary moves from the facility to the application. Single-datacenter designs fail when the datacenter fails (power event, fire, flood, network cut); the fix is either active-passive DR (a standby site with data replication and a runbook to bring it up — recovery time is hours) or active-active (both sites serve traffic, data replicates synchronously or nearly so — a site loss is a routing and failover event, not an outage). The design decisions: how much data loss is acceptable (the RPO — recovery point objective: synchronous replication loses nothing, async loses seconds-to-minutes), how fast recovery must be (RTO — recovery time objective), and whether the second site can actually absorb the load (a DR site that was never load-tested fails when it is needed).
- The failure modes of redundancy: shared fate (the "redundant" paths that share a single failure domain — two power feeds from the same transformer, two fiber paths in the same conduit — redundancy on paper, one event kills both), failover paths never exercised (the standby that has never been failed over to, discovered broken at the moment of need), and the failover storm (a healthy system whose automated failover triggers on a blip and causes more damage than the blip).
- The practice: test the failover — quarterly failover drills, generator load tests, circuit-breaker tests — and treat the untested failover path as nonexistent.
- For mykb: the node anchors the availability branch of the infrastructure cluster — DR replication, database failover automation, and time synchronization all connect here.

## Related
- [[wiki/devops-infra/replication-and-failover-dr|Replication & Failover DR]]
- [[wiki/devops-infra/database-failover-automation|Database Failover Automation]]
- [[wiki/infrastructure/time-synchronization-in-dc|Time Synchronization in the Datacenter]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
