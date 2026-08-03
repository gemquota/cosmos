---
type: "concept"
title: "Clock Drift & NTP"
description: "How clocks drift and NTP keeps systems in sync"
tags: ["clock", "drift", "ntp", "time"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Clock Drift & NTP

## Summary
Clock drift is the gradual divergence of a machine's clock from true time, caused by the physical oscillator (typically a quartz crystal) running slightly fast or slow; NTP (Network Time Protocol) is the protocol that keeps distributed clocks in sync. The topic matters because distributed systems assume synchronized time — for log correlation, cache expiration, authentication, and coordination — and a drifting clock silently breaks all of them.

## Details
- Drift has two components: skew (the rate at which the clock diverges — a quartz oscillator can run off by tens of parts per million, meaning seconds per day) and offset (the current difference from true time). Environmental factors — temperature, age, and power supply — change the skew over time, so drift cannot be calibrated once and forgotten; it must be continuously measured and corrected. The classic failure is a server whose clock drifts minutes per day without any error being raised, because the OS happily reports the wrong time.
- NTP works by measuring the round-trip to a reference clock: the client sends a timestamped request, the server replies with its timestamps, and the client computes both the offset (how far its clock is from the server) and the network delay (to bound measurement error). The client then adjusts its clock — small adjustments by slewing (slowing or speeding the clock gradually, avoiding jumps) and large corrections by stepping. Stratum levels organize the hierarchy: stratum 0 is the reference (atomic clocks, GPS), stratum 1 servers sync from it, and so on; a machine should sync to multiple upstreams and reject outliers, so a single broken upstream cannot drag it off.
- Deployment practice: a fleet should run its own NTP servers (stratum 2) synced to multiple stratum 1 sources, with all clients pointing at the internal servers — this gives consistent time within the fleet (what most systems actually need) and resilience against upstream failures. `chrony` (the modern Linux daemon) is preferred over `ntpd` because it handles asymmetric network delay and intermittent connectivity better.
- Failure modes: NTP blocked by firewalls (clocks drift silently), a misconfigured upstream (the fleet syncs to a broken clock — the "time poisoning" failure), and the leap/second handling bug class, where a sudden step backward breaks systems that assume monotonic time (which is why log timestamps should use monotonic clocks for durations and wall clocks for display).
- For mykb: the node connects to the time-synchronization cluster — NTP, PTP, and time-sync-in-datacenter — and clock drift is the shared underlying enemy of all of them.

## Related
- [[wiki/devops-infra/infrastructure-drift-detection|Infrastructure Drift Detection]]
- [[wiki/infrastructure/configuration-drift|Configuration Drift]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
