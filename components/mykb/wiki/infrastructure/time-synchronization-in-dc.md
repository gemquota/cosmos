---
type: "concept"
title: "Time Synchronization in the Datacenter"
description: "Stratum servers, PTP, and disciplined clocks at scale"
tags: ["time", "sync", "datacenter", "ptp"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Time Synchronization in the Datacenter

## Summary
Time synchronization in the datacenter keeps every host, switch, and storage array on the same clock using a hierarchy of time sources: GPS- or atomic-referenced stratum servers feed NTP, and precision-sensitive workloads add PTP for sub-microsecond alignment. Skew between machines breaks distributed systems in ways that are nearly impossible to debug without understanding the clock topology.

## Details
- Hierarchy: stratum 0 devices (GPS, atomic clocks) discipline stratum 1 servers inside the datacenter; hosts then sync from those local servers over NTP, avoiding the public internet and its jitter. Local stratum servers make sync faster, more stable, and independent of external outages.
- PTP: for finance, media, and distributed databases that need sub-microsecond alignment, PTP (IEEE 1588) with hardware timestamping synchronizes across the fabric; boundary clocks in switches refresh the time at each hop, since software timestamping alone cannot reach the same precision.
- Concrete failure modes: a clock that jumps forward or backward can break TLS validity windows, message ordering assumptions, TTL/lease expiration, and incremental backups; NTP refusals or wrong `server` lines leave hosts drifting; and a misconfigured authoritative source (for example syncing to an unauthenticated public pool) can pull the whole fleet off time.
- Practical examples: Kubernetes and cloud VMs rely on synchronized time for token expiry and retry logic; databases use timestamps for MVCC visibility; and logs from two hosts with a 30-second skew make root-cause correlation impossible.
- Tradeoffs: NTP over the internet is simple but jittery; local stratum servers cost hardware and maintenance; PTP gives the best precision but demands hardware support and careful network design, and every link with asymmetric delay injects error.
- Operational practice: run local NTP (chrony/ntpd) with multiple sources, monitor offset and jitter per host, use hardware timestamping where available, and test what happens to your services when the clock steps forward — chaos engineering should include time faults.
- RSIS3/mykb relevance: telemetry and checkpoint ordering depend on trustworthy clocks; this node supplies the hierarchy and failure modes loops need when interpreting timestamped state.

## Related
- [[wiki/infrastructure/network-time-protocol|Network Time Protocol]]
- [[wiki/infrastructure/precision-time-protocol|Precision Time Protocol]]
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]]
- [[wiki/infrastructure/redundancy-and-failover-dc|Datacenter Redundancy & Failover]]
