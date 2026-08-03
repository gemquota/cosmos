---
type: "concept"
title: "Teaming & Link Aggregation"
description: "Switch-side LACP link aggregation matching host-side teaming"
tags: ["lag", "lacp", "bonding", "switching"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Teaming & Link Aggregation

## Summary
Teaming (host-side bonding) and link aggregation (switch-side LAG) bundle multiple physical links into one logical link, increasing total bandwidth and providing failover when a cable, NIC, or switch port dies. The two sides must agree on the same aggregation protocol — almost always LACP (802.3ad) — or the bundle will misbehave.

## Details
- Mechanism: LACP exchanges link aggregation control PDUs so the switch and host agree which physical ports belong to one bundle; traffic is then hashed across the member links by headers (src/dst MAC, IP, or TCP/UDP ports), not striped byte-by-byte. The hash determines which flow uses which link.
- Linux bonding modes: `mode=4` (802.3ad dynamic LACP), `mode=2` (balance-xor, static), `mode=1` (active-backup, no aggregation, pure failover), and `mode=6` (balance-alb, adaptive). Kubernetes and most production stacks use LACP with `miimon` monitoring and a fast rate.
- Concrete example: a host with two 25G links aggregated into a single 50G logical link for NFS traffic. A single large transfer still tops out at one link's speed because one flow hashes to one member; many parallel flows spread across members to reach the aggregate.
- Failure modes: mismatched LACP configuration (one side static, one side dynamic) causes flapping and packet loss; a switch port left in the wrong VLAN or trunk mode breaks the bundle; hash collisions on many same-flow connections underutilize members; and physical mis-wiring — both ends plugged into the same switch with a cross-cable — can loop traffic when spanning tree is not protecting the bundle.
- Tradeoffs: aggregation multiplies bandwidth for many flows but not for a single flow; it adds switch configuration and troubleshooting complexity; and it changes failure semantics — a dead member hides inside a bundle that still reports "up," so monitor per-member health, not just bundle state.
- Operational practice: configure both sides consistently, verify with `ethtool --show-nic` / `lacp` counters, monitor per-member utilization, and test link-down failover deliberately because most aggregation incidents are discovered during real failures.
- RSIS3/mykb relevance: for loops evaluating capacity plans, this node clarifies that LACP provides redundancy plus aggregate throughput, not per-flow speedups — a distinction retrievals need when sizing network paths.

## Related
