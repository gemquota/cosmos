---
type: "concept"
title: "Bandwidth vs Throughput"
description: "Theoretical link capacity versus realized application data rate"
tags: ["bandwidth", "throughput", "networking", "capacity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Bandwidth vs Throughput

## Summary

Bandwidth is the capacity of a link (bits per second); throughput is what actually transfers after overhead, loss, and protocol limits. Confusing the two causes both over-provisioned bills and underperforming claims.

## Details
- Mechanism: bandwidth is the negotiated or advertised link rate; throughput = bandwidth × efficiency, where efficiency loses to TCP window/round-trip time limits, congestion loss, protocol overhead (headers, TLS), and application behavior. The theoretical max for a TCP flow is roughly window size ÷ RTT, which is why high-RTT links need large windows (BDP).
- Concrete example: a 1 Gbps link with 100ms RTT and a 64KB TCP window tops out near 5 Mbps without window scaling — a classic WAN surprise; the same link carries 900+ Mbps with HTTP/2 + congestion control tuned and multiple flows. Cloud egress bills on bytes actually moved, so "10 Gbps" networking rarely moves 10 Gbps of application data.
- Failure modes: sizing links by bandwidth while the bottleneck is latency or loss (packet loss halves throughput via TCP backoff); saturating one flow while others starve (fairness); ignoring duplex mismatches and NIC offload settings in physical contexts; and measuring throughput with small transfers that never reach steady state.
- Operational tradeoffs: raise throughput by removing loss, increasing window/BDP, parallelizing flows, and compressing — not just buying bandwidth; monitor both utilization and achieved throughput per path, and use TCP-friendly tuning for high-latency interconnects.
- RSIS3/mykb relevance: the wiki's cross-region sync measurements would record achieved throughput vs link rate, giving the loop realistic capacity numbers for planning replication jobs.
- Testing: measure with parallel flows and large transfers (iperf-style), not single-stream curl, to see the practical ceiling; the single-stream number misleads for most services.
- Overhead accounting: subtract protocol and retransmission overhead when sizing; a link at 95% utilization is already oversubscribed in practice. Base capacity decisions on achieved-throughput dashboards per path, not interface counters.

## Related
- [[wiki/infrastructure/throughput-of-storage|Storage Throughput]]
- [[wiki/infrastructure/bandwidth-allocation|Bandwidth Allocation]]
- [[wiki/cloud-infra/cost-of-bandwidth|Cost of Bandwidth]]
