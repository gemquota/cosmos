---
type: "concept"
title: "Precision Time Protocol"
description: "Sub-microsecond clock sync for datacenter and industrial networks"
tags: ["ptp", "time", "sync", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Precision Time Protocol

## Summary
Precision Time Protocol (PTP, IEEE 1588) synchronizes clocks to sub-microsecond accuracy over Ethernet — orders of magnitude beyond NTP's milliseconds. It achieves this by doing the timestamping in hardware (the NIC stamps packets as they cross the wire, eliminating the software latency that limits NTP) and by measuring the network path precisely, with transparent clocks and boundary clocks correcting for switch delay. It is the clock layer for industrial control, high-frequency trading, and increasingly the datacenter (the "Time-Sensitive Networking" story).

## Details
- Why NTP is not enough: NTP's accuracy is bounded by software timestamping — the timestamps are taken in the kernel stack, where interrupt latency, scheduling, and queueing add hundreds of microseconds of unpredictable delay, and the delay asymmetry between request and reply limits correction. PTP moves the timestamping into the NIC hardware: the packet's departure and arrival times are stamped at the physical layer, so the measurements are accurate to nanoseconds and the protocol can converge to sub-microsecond sync.
- The protocol architecture: a grandmaster clock (the time source, typically GPS- or atomic-referenced) is elected via the Best Master Clock Algorithm (BMCA); ordinary clocks sync to it, and the network's switches participate as boundary clocks (each port acts as a PTP node, correcting for the switch's own delay) or transparent clocks (measuring and compensating the time each PTP message spends inside the switch). The measurement exchange (sync/follow_up/delay_req/delay_resp) computes offset and delay with hardware timestamps, and the slave disciplines its local oscillator (servo) to track the master. The result: nanosecond-level precision on the wire, sub-microsecond end to end.
- PTP in the datacenter: the same mechanism that serves industrial control serves distributed systems that need precisely ordered events — trading (timestamping trades identically across machines), financial compliance (regulators require synchronized clocks for audit), and research/measurement. The datacenter profile (IEEE 1588 telecom profiles, or the newer "PTP for datacenters" work) defines how switches and hosts participate; the operational requirement is that every switch in the path must be PTP-aware (a non-PTP switch breaks the boundary/transparent-clock chain and accuracy collapses back to NTP levels).
- The failure modes: grandmaster loss (the BMCA must elect a new master — the failure window is the re-election), asymmetric paths (a link that delays one direction differently than the other introduces uncorrectable offset), and the silent accuracy decay: PTP configured but not verified, with the clocks drifting apart unnoticed — the discipline is monitoring the offset and testing holdover (how well clocks keep time when the master disappears).
- For mykb: PTP is the microsecond layer of the time-sync cluster — NTP (milliseconds), PTP (sub-microsecond), and time-sync-in-DC (the datacenter practice) form the spectrum.

## Related
- [[wiki/cloud-infra/wireguard-protocol|WireGuard Protocol]]
- [[wiki/infrastructure/network-time-protocol|Network Time Protocol]]
- [[wiki/infrastructure/time-synchronization-in-dc|Time Synchronization in the Datacenter]]
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
