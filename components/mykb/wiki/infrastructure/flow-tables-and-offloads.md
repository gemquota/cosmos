---
type: "concept"
title: "Flow Tables & Offloads"
description: "Moving flow processing to switch or NIC hardware"
tags: ["offload", "flow-table", "switching", "nic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Flow Tables & Offloads

## Summary
Flow tables and offloads move packet-processing decisions from general-purpose CPUs into switch or NIC hardware: a flow table is the match-action structure that classifies packets into flows, and offload is the act of programming that table so hardware, rather than software, handles the forwarding. This is the mechanism that makes software-defined networking fast: the controller thinks in software, but the packets never wait for software.

## Details
- The flow-table model (from OpenFlow, now generalized): a switch or NIC holds a table of entries, each with match fields (L2/L3/L4 headers, tunnel IDs, metadata) and actions (forward, drop, modify, count). Every packet is looked up against the table, and the first matching entry's actions execute in silicon. The design's power: control is software (the controller programs entries), but the per-packet cost is one hardware lookup — line rate with software semantics. The design's constraint: the table is a finite hardware resource (SRAM/TCAM), so not every flow can have its own entry.
- The lifecycle of an entry is the key operational concept: on a first packet that misses the table, the hardware punts it to software (the controller or the host stack), which decides and installs an entry; subsequent packets in the flow hit the entry and never see software again. This is exactly how SDN switches and modern NIC offloads behave — and why the flow-table size and the idle timeout (entries expire after inactivity) determine the steady-state hit ratio. A flow table that is too small, or timeouts that are too short, thrashes: packets keep punting to software, and the offload's performance advantage evaporates.
- Where offloads live: in switches (OpenFlow tables, ASIC pipelines), in NICs (flow steering, RSS, checksum and segmentation offload — the base case every NIC does — up to full TCP offload and programmable NIC pipelines), and in the kernel (flow tables like nftables' conntrack offload). Each level trades generality for speed: the more specific the hardware, the faster but the fewer packet classes it can handle.
- Failure modes: table exhaustion (a burst of flows overflows the table and the hardware falls back to punting or dropping), entry staleness (long-lived flows whose entries expired and now punt), and offload correctness bugs — the scariest class, where hardware and software disagree on a packet's fate.
- For mykb: flow tables are the mechanism under the SDN and OpenFlow cluster — they connect flow control, flow logs, and ASIC pipelines into one story.

## Related
- [[wiki/cloud-infra/flow-control|Flow Control]]
- [[wiki/cloud-infra/flow-logs-and-analysis|Flow Logs & Analysis]]
- [[wiki/os-shell/page-tables|Page Tables]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
