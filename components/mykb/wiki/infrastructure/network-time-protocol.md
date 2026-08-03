---
type: "concept"
title: "Network Time Protocol"
description: "Hierarchical time sync to UTC within milliseconds over UDP"
tags: ["ntp", "time", "sync", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Network Time Protocol

## Summary
Network Time Protocol (NTP) synchronizes computer clocks to UTC within milliseconds over UDP, using a hierarchy of time sources. It is the internet's clock: every server that needs consistent timestamps — for logs, authentication (Kerberos is NTP-sensitive), TLS certificate validation, distributed coordination, and cache invalidation — depends on NTP keeping its clock within a few milliseconds of the rest of the world.

## Details
- The protocol mechanics: an NTP client sends a request with its transmit timestamp; the server replies with its receive and transmit timestamps; the client computes the offset (how far its clock is from the server) and the round-trip delay from the four timestamps, then adjusts its clock — slewing for small offsets (gradually changing the clock rate to avoid time jumps) and stepping for large ones. The four-timestamp exchange is the clever part: it separates the offset from the network delay, and the delay itself becomes the measurement of the sync quality. The accuracy depends on the delay being symmetric (the request and reply take the same path) — asymmetric routing and congested links degrade accuracy.
- The hierarchy: stratum 0 sources (atomic clocks, GPS receivers) generate true time; stratum 1 servers sync directly from stratum 0; stratum 2 from stratum 1; and so on down to the clients. Each stratum hop adds a small amount of jitter, so the design goal is a shallow, redundant hierarchy: a datacenter runs internal stratum 2/3 servers synced to multiple stratum 1 upstreams, and all clients sync to the internal servers — giving fleet-consistent time (what most systems actually need) and resilience against upstream failure. The client-side algorithm (the NTP intersection algorithm) filters the sample set, rejects outliers (a broken upstream, a delayed packet), and selects the best cluster of sources.
- The operational rules: run a local NTP tier (never point thousands of servers at public pools — the pool gets hammered and the fleet's sync quality varies); use multiple upstreams and monitor the offsets; use chrony on modern Linux (it handles asymmetric delay and intermittent connectivity far better than ntpd); and configure step thresholds so a large clock jump (a rebooted machine with a dead RTC battery, a suspended VM) gets corrected safely rather than causing a timestamp discontinuity mid-transaction.
- Failure modes: NTP blocked by firewalls (clocks drift silently — days of drift are invisible until a Kerberos ticket or a TLS certificate fails), a poisoned upstream (the fleet syncs to a wrong clock — the "time" the fleet shares is wrong everywhere), and the leap-second/step class of bugs (a stepped clock breaks monotonic-time assumptions, which is why applications must use monotonic clocks for durations).
- For mykb: NTP is the millisecond-scale member of the time-sync cluster — the sibling Precision Time Protocol (PTP) does microseconds-to-nanoseconds in the datacenter, and clock drift is the underlying problem both solve.

## Related
- [[wiki/cloud-infra/wireguard-protocol|WireGuard Protocol]] — related coverage in the same cluster
- [[wiki/devops-infra/network-observability|Network Observability]] — related coverage in the same cluster
- [[wiki/infrastructure/precision-time-protocol|Precision Time Protocol]] — related coverage in the same cluster
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
