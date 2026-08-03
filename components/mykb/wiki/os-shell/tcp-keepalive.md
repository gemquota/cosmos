---
type: "concept"
title: "TCP Keepalive"
description: "Detecting dead peers with idle-probe-kill timing"
tags: ["tcp", "keepalive", "sockets", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# TCP Keepalive

## Summary
TCP keepalive is the mechanism that detects dead or unreachable peers: after a socket has been idle for a while, the kernel sends empty probes and, if the peer does not respond, eventually declares the connection dead and fails it with an error. It turns silent hangs — a crashed server, a vanished client, a broken link — into a bounded, detectable failure instead of an infinite wait.

## Details
- Mechanism: keepalive is off by default for most sockets; when enabled, the kernel sends a probe after `tcp_keepalive_time` (default 7200s = 2 hours) of idle, then `tcp_keepalive_intvl` (default 75s) apart, and gives up after `tcp_keepalive_probes` (default 9). Per-socket tuning overrides these globals: `SO_KEEPALIVE` turns it on, `TCP_KEEPIDLE`, `TCP_KEEPINTVL`, and `TCP_KEEPCNT` set the three timers; `TCP_USER_TIMEOUT` bounds how long the connection can be unresponsive before the kernel aborts it (which also affects retransmission). The probe is an empty ACK-like segment: if the peer is alive, it answers; if the network dropped the connection, the kernel gets no reply and kills the socket with ETIMEDOUT (or ECONNRESET if the peer RSTs).
- Concrete examples: a long-lived API connection (a WebSocket or a dashboard poll socket) that sits idle for hours — with keepalive, a crashed peer is detected in minutes instead of never; a load balancer that enables keepalive with `TCP_KEEPIDLE=60` so dead backends leave the pool quickly; a mobile app connection that must detect a phone that fell off the network; `ss -o state established` shows the keepalive timers on sockets.
- Failure modes: the classic failure is relying on the two-hour default, which is useless for real-world dead-peer detection — an idle connection to a dead host lingers for 2h+ before failing. The opposite failure is keepalive so aggressive that idle-but-healthy connections are killed by transient probe loss (probes share the retransmission machinery, so a bad network path can abort connections that would have recovered). Middleboxes also interfere: some NATs and firewalls drop idle connections silently, which is exactly the problem keepalive solves but also the reason interval choices matter — probes must outpace the middlebox's idle timeout.
- Operational tradeoffs: keepalive trades a tiny amount of traffic (one small probe per interval per idle connection) for bounded failure detection; the knobs are the idle time (tune to your real idle pattern), interval, and count (tune to your network's loss tolerance). The practice rules: enable it on long-lived connections, set `TCP_KEEPIDLE` well below both your app timeout and the middlebox's NAT timeout, bound the total with `TCP_USER_TIMEOUT`, and treat keepalive as the transport-level complement to application heartbeats — not a replacement. RSIS3/mykb relevance: the daemon's agent and dashboard connections are long-lived; tuned keepalive plus application-level heartbeats ensures a dead agent is evicted and its loops reassigned — mirroring the loop registry's liveness discipline.

## Related
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/cloud-infra/udp-vs-tcp|UDP vs TCP]]
- [[wiki/cloud-infra/tcp-retransmission|TCP Retransmission]]
