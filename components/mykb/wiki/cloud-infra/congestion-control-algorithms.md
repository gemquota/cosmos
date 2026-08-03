---
type: "concept"
title: "Congestion Control Algorithms"
description: "CUBIC, Reno, BBR and how senders adapt rate to network conditions"
tags: ["congestion", "tcp", "bbr", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Congestion Control Algorithms

## Summary

Congestion control is TCP's (and QUIC's) mechanism for finding and respecting the network's available capacity: send more until loss, then back off. Algorithm choice (CUBIC, BBR, Reno, compound) changes throughput and latency profiles, especially over high-BDP and lossy paths.

## Details
- Mechanism: senders probe bandwidth by increasing window (additive increase) and react to loss (multiplicative decrease); CUBIC grows the window with a cubic function for fast recovery; BBR models bottleneck bandwidth and RTT instead of reacting to loss, maintaining throughput over lossy links; Reno/Vegas are the older AIMD baselines. QUIC runs its own congestion control in user space with similar algorithms.
- Concrete example: a 1 Gbps, 100ms RTT link with 1% loss: CUBIC collapses toward a few Mbps while BBR sustains near line rate; file-transfer services and CDNs tune algorithms or use parallel flows for exactly this reason; cloud inter-region replication typically measures a big win switching from default CUBIC to BBR.
- Failure modes: algorithms tuned for one regime misbehaving in another (BBR's initial probing can burst; CUBIC's fairness with competing Reno flows); kernel defaults lagging modern defaults (enable ECN, BBR where available); and blaming the network when the algorithm, buffer, or window scale is the actual limiter.
- Operational tradeoffs: for bulk transfers over lossy long-haul paths, BBR-class control wins; for interactive latency, congestion control matters less than queueing/buffering — use ECN, pacing, and correct window sizing first. Test per path, since cloud topologies and middleboxes differ, and record buffer sizes since BBR assumes a bounded, non-drop-tail path.
- RSIS3/mykb relevance: the wiki's sync jobs between regions would record algorithm-vs-throughput comparisons, so the loop's replication planner enables BBR-class control on paths where it measurably wins.
- Kernel policy: enable modern defaults (BBR where supported, ECN, large windows) at the OS level; application-level tuning cannot rescue a kernel stuck on legacy defaults. For QUIC, the application picks the algorithm, so set the same defaults in the HTTP/3 stack.

## Related
- [[wiki/os-shell/algorithms|Algorithms]]
- [[wiki/cloud-infra/flow-control|Flow Control]]
- [[wiki/cloud-infra/network-access-control-lists|Network Access Control Lists]]
