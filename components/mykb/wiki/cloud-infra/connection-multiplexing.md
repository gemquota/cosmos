---
type: "concept"
title: "Connection Multiplexing"
description: "Sharing one transport connection across many concurrent streams"
tags: ["multiplexing", "http2", "streams", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Connection Multiplexing

## Summary

Connection multiplexing carries many logical streams over one physical connection — HTTP/2's frames, HTTP/3's QUIC streams, TCP connection reuse, and databases' session pools. It removes per-request handshakes and head-of-line blocking at the transport layer.

## Details
- Mechanism: HTTP/2 multiplexes requests over one TCP connection using frames, ending the browser's 6-connection-per-origin limit, but TCP-level head-of-line blocking remains (one lost packet stalls all streams); HTTP/3/QUIC multiplexes over UDP with independent streams, isolating loss per stream; connection pooling (keep-alive, PgBouncer, HikariCP) reuses established connections for many short operations.
- Concrete example: a browser fetching 100 resources over HTTP/2 on one connection saves 99 handshakes; a chat app over QUIC keeps typing and file upload flowing when the other stream loses packets; an API gateway pooling upstream connections cuts per-request TLS and TCP setup from ~30ms to ~0ms.
- Failure modes: HTTP/1.1-parallelism assumptions breaking behind multiplexing proxies; head-of-line blocking on lossy links for HTTP/2 (mitigate by switching to HTTP/3); connection pools that grow unbounded or leak under churn; and protocol sniffing/rate limits that treat one multiplexed connection as one client.
- Operational tradeoffs: multiplexing trades connection count and handshake cost for flow-complexity and single-connection risk (one bad stream can still share a bottleneck); the standard pattern is HTTP/3 for edge, pooled connections for services, and careful pool sizing for databases.
- RSIS3/mykb relevance: the wiki dashboard's API calls multiplex over HTTP/2 with pooled upstreams; this note records the pool sizing so the loop does not reintroduce per-request handshakes.
- Protocol interplay: multiplexing changes how load balancers and proxies see connections; ensure keep-alive timeouts and connection limits are tuned for few, long-lived connections rather than many short ones.
- Pool sizing: size connection pools from concurrency, not traffic volume; too few connections serialize requests and too many exhaust server file descriptors.

## Related
- [[wiki/cloud-infra/http-2-multiplexing|HTTP/2 Multiplexing]]
- [[wiki/devops-infra/connection-pools|Connection Pools]]
- [[wiki/devops-infra/connection-pooling|Connection Pooling]]
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
