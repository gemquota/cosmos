---
type: "concept"
title: "Flow Control"
description: "Receiver-window based pacing that prevents sender overflow of buffers"
tags: ["flow-control", "tcp", "windows", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Flow Control

## Summary

Flow control is the mechanism that stops a fast sender from overwhelming a slow receiver: TCP's receive-window throttling, QUIC's stream-level control, and link-level pause frames. It is distinct from congestion control (which protects the network, not the receiver).

## Details
- Mechanism: TCP flow control is receiver-driven: the receiver advertises a window (the free buffer space), the sender cannot send more than the window without an update; a zero window stalls the connection until a window-update (window probe) arrives. QUIC does this per stream and per connection, so one stalled consumer does not block others; hardware flow control (pause frames) handles link-level backpressure.
- Concrete example: a slow database client with a tiny receive buffer throttles a bulk sender through window updates — the sender's throughput collapses despite a fat link; HTTP/2's per-connection flow control (but per-stream too) prevents one slow stream from hogging buffers; tuning receive buffers upward fixes throughput on high-BDP paths where the receiver window, not the network, is the limit.
- Failure modes: confusing flow control with congestion — tuning one does not fix the other; zero-window deadlocks when window updates are lost (probes exist but can stall); buffer bloat from huge windows defeating latency; and receiver-side limits (NIC, socket buffers) that silently cap throughput.
- Operational tradeoffs: correctly sized buffers are the whole game: too small throttles, too large bloats latency; modern kernels autotune, but proxies and middleboxes still impose their own windows. Measure per-connection window usage when throughput is suspiciously capped.
- RSIS3/mykb relevance: the wiki's transfer diagnostics record window and buffer stats, so the loop's replication tuning separates receiver limits from network limits.
- Buffer sizing: set socket buffers to the bandwidth-delay product for high-throughput paths; an undersized receive buffer throttles throughput invisibly. The window is per direction, so both peers' buffers matter on asymmetric paths.

## Related
- [[wiki/os-shell/job-control-and-background-tasks|Job Control & Background Tasks]]
- [[wiki/cloud-infra/congestion-control-algorithms|Congestion Control Algorithms]]
- [[wiki/cloud-infra/network-access-control-lists|Network Access Control Lists]]
