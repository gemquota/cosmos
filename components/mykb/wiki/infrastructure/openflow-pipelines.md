---
type: "concept"
title: "OpenFlow Pipelines"
description: "Match-action flow tables that program switches from a controller"
tags: ["openflow", "sdn", "switching", "flows"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# OpenFlow Pipelines

## Summary
OpenFlow pipelines are the match-action flow-table architecture that lets a software controller program switches: the switch exposes its forwarding tables through a protocol, and the controller populates them with flow entries — match fields, actions, counters — so forwarding behavior is defined in software and executed in hardware. OpenFlow was the first standardized expression of the SDN idea, and its pipeline model is the ancestor of every modern programmable-switch design.

## Details
- The model: a switch's forwarding path is a pipeline of flow tables. Each table contains flow entries: a match (header fields — L2/L3/L4, plus metadata), actions (forward out a port, drop, modify headers, push/pop MPLS/VLAN, go to another table), and counters. A packet enters the pipeline, is matched against table 0, executes the first match's actions (possibly jumping to the next table), and continues until a terminal action or table-miss — the miss behavior being programmable too (drop, forward to controller, or continue). The pipeline's multi-table structure is what makes it powerful: coarse classification in early tables, fine-grained policy in later ones, with metadata passing context between tables.
- The control relationship: a controller (ONOS, ODL, Ryu, or production SDN controllers) maintains the network-wide view and programs every switch's tables through the OpenFlow protocol — installing flows reactively (on the first packet of a flow, the switch forwards it to the controller, which decides and installs an entry) or proactively (the controller pre-installs the full policy). The switch is a dumb executor; the intelligence lives in software. The match-action model is why the SDN architecture (control plane separated from data plane) is implementable — the control plane's decisions are exactly the flow entries it writes.
- The legacy and the successor: OpenFlow's history is a lesson in protocol design. Version churn (1.0 → 1.3 → 1.4+) fragmented vendor support, the protocol's fixed match fields constrained innovation (you can only match what the spec defines), and the industry moved to programmable pipelines (P4) — where the pipeline itself is user-defined, compiled onto the silicon, and the control protocol is the general-purpose one the switch's vendor provides. The concepts carried over: match-action processing, table-miss behavior, and controller-programmed forwarding are all still the architecture, just with a user-defined pipeline instead of a fixed one.
- Failure modes: controller dependency (a switch with empty tables and a dead controller forwards nothing — hence proactive flow installation and fallback), table exhaustion (a reactive controller that installs per-flow entries overflows the table under a flow burst), and the version/feature mismatch between controller and switch.
- For mykb: OpenFlow pipelines are the mechanism node of the SDN cluster — flow tables and offloads (the hardware), SDN controllers (the software), and programmable pipelines (the successor) all connect here.

## Related
- [[wiki/devops-infra/log-aggregation-pipelines|Log Aggregation Pipelines]]
- [[wiki/devops-infra/continuous-delivery-pipelines|Continuous Delivery Pipelines]]
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]]
