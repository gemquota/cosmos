---
type: "concept"
title: "TCP Retransmission"
description: "How TCP detects loss via ACK timeouts and fast retransmit"
tags: ["tcp", "retransmission", "loss", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# TCP Retransmission

## Summary

TCP retransmission is how the protocol recovers from lost segments: timers trigger resends, fast retransmit reacts to duplicate ACKs, and the retransmission timeout (RTO) backs off exponentially. Retransmission rates are the single best network-health signal — and the most misread one.

## Details
- Mechanism: when an ACK does not arrive within the RTO, the sender resends and doubles the timeout; three duplicate ACKs trigger fast retransmit without waiting; selective ACK (SACK) narrows retransmission to missing segments; modern stacks also use ECN and RACK for finer recovery. Spurious retransmits occur when ACKs are delayed, not lost (DSACK and timestamps reveal them).
- Concrete example: a 1% packet-loss link inflates effective RTT and collapses throughput (each loss cuts the window); a retransmission spike on a specific path during an incident points to a saturated link or failing NIC; a mis-tuned proxy that duplicates ACKs causes the classic "server retransmits but the network is fine" mystery.
- Failure modes: reading retransmit counts without loss context (reordering and delayed ACKs trigger spurious retransmits); blaming the network when the server's receive buffer or app is the bottleneck; RTO minimums (200ms+) making loss feel like stalls on low-latency paths; and middleboxes that break SACK/timestamps, degrading recovery.
- Operational tradeoffs: low retransmission (<0.1%) is normal; sustained spikes warrant investigation, and zero-loss assumptions break under congestion. Measure retransmit rate per flow and path (kernel counters, tcpdump, flow telemetry) and tune window/ECN/SACK before buying more bandwidth.
- RSIS3/mykb relevance: the wiki's cross-region sync logs retransmit rates per link; the loop's replication tuning targets loss recovery settings, not just bandwidth.
- Diagnosis order: check loss before blaming throughput; a retransmit spike on one path points to a specific link, while uniform loss suggests a shared bottleneck.
- Baseline first: record the normal retransmit rate per path before an incident; without a baseline, the alert is either noise or late.

## Related
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/cloud-infra/udp-vs-tcp|UDP vs TCP]]
- [[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]]
- [[wiki/os-shell/tcp-keepalive|TCP Keepalive]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
