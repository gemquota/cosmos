---
type: "concept"
title: "Traffic Shaping & QoS"
description: "Managing latency and throughput for different traffic classes"
tags: ["qos", "shaping", "networking", "bandwidth"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Traffic Shaping & QoS

## Summary
Traffic shaping and QoS manage how latency and throughput are distributed across different traffic classes on a shared link: shaping smooths bursts and enforces rate limits, while QoS marks, queues, and schedules packets so that critical traffic (voice, storage replication, control-plane) is not starved by bulk traffic. They are how a constrained link becomes a set of predictable service levels instead of a free-for-all.

## Details
- Mechanism: packets are classified and marked (DSCP/802.1p), queued into classes (typically 4–8 per interface), and served by a scheduler (strict priority, weighted fair queueing, or a mix). Shaping buffers and paces traffic to a configured rate, while policing drops or marks excess traffic at the ingress.
- Concrete examples: a WAN link where video conferencing gets priority over file downloads; a storage network class that protects replication traffic from backup bursts; and a web tier where interactive API traffic is queued ahead of batch jobs, keeping p99 latency bounded during peak load.
- Failure modes: misconfigured priority queues starving everything else (strict priority without a bandwidth guarantee for lower classes); shaping at the wrong point (ingress shaping is ineffective — you must shape at the egress of the bottleneck); marking that is stripped or ignored across administrative boundaries; and queue buffers that are too deep, adding latency to all traffic.
- Tradeoffs: QoS buys predictability on constrained links at the cost of configuration complexity and policy disputes; over-engineering QoS on an underutilized link adds nothing; and queueing always trades throughput for latency — you cannot have both on a saturated link.
- Operational practice: measure the real bottleneck before designing classes; give each class a minimum bandwidth and a cap; monitor queue drops and per-class utilization; and keep marking consistent end-to-end, because a packet stripped of its DSCP value rejoins the default class.
- RSIS3/mykb relevance: priority logic is a recurring theme in self-improvement loops that allocate scarce resources; this node supplies the queueing vocabulary loops can reuse when reasoning about scheduling attention and compute.

## Related
- [[wiki/devops-infra/traffic-shifting-and-splitting|Traffic Shifting & Splitting]] — related coverage in the same cluster
- [[wiki/devops-infra/mirroring-and-shadow-traffic|Mirroring & Shadow Traffic]] — related coverage in the same cluster
- [[wiki/infrastructure/east-west-vs-north-south-traffic|East-West vs North-South Traffic]] — related coverage in the same cluster
- [[wiki/infrastructure/traffic-engineering|Traffic Engineering]] — related coverage in the same cluster
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
