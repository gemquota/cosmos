---
type: "concept"
title: "ASIC & Switching Architectures"
description: "Fixed-function silicon and the pipeline inside switches"
tags: ["asic", "switching", "hardware", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# ASIC & Switching Architectures

## Summary
ASIC-based switching architectures use fixed-function silicon — application-specific integrated circuits — to forward packets at line rate, in contrast to CPU-based switches that process packets in software. The tradeoff at the heart of the topic: ASICs deliver the raw throughput and determinism that datacenter fabrics require, but their behavior is fixed at design time, so every feature (tables, pipelines, telemetry) is a silicon decision.

## Details
- The classic switching ASIC pipeline mirrors the forwarding path: parse the packet header, classify it (match against ACLs and forwarding tables), edit it (rewrite MACs, decrement TTL, set QoS fields), and queue it for transmission. These stages run in fixed hardware on every packet, which is why an ASIC switch forwards at multi-terabit rates with nanosecond-scale, predictable latency. The pipeline is the architecture: the number of table entries, the width of the longest-prefix-match lookup, and the depth of the queues are all physical resources.
- The modern evolution is the programmable pipeline (P4-capable ASICs): instead of a fixed parse-and-match structure, the pipeline is configured at deployment time — the operator compiles a P4 program that defines the headers to parse, the tables to match, and the actions to take. This recovers much of the flexibility of software switches while keeping the ASIC's line-rate performance, at the cost of a compiler toolchain and careful resource budgeting: the program must fit the silicon's stages, tables, and SRAM.
- Key design dimensions: forwarding tables (exact-match and LPM entries stored in TCAM and SRAM — TCAM is fast and flexible but power-hungry and small), buffer memory (shared vs dedicated packet buffers; deep buffers absorb bursts but add latency), and offloads (VXLAN encap/decap, ECMP hashing, ACL filtering done in silicon rather than in the host CPU).
- Failure modes: table exhaustion (a full TCAM silently degrades to best-effort forwarding or drops), buffer exhaustion under incast (microbursts overflow shallow buffers and cause TCP retransmits), and firmware bugs in the forwarding silicon that produce subtle packet corruption or incorrect lookups — the hardest class to debug because the packets look fine until they do not.
- For mykb: switching architecture knowledge grounds the adjacent topics — flow tables and offloads, VXLAN overlays, and software-defined networking all assume a particular ASIC pipeline, and understanding the silicon explains why certain SDN features are cheap and others impossible.

## Related
- [[wiki/cloud-infra/availability-zone-architectures|Availability Zone Architectures]]
- [[wiki/os-shell/context-switching|Context Switching]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
