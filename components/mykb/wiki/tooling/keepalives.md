---
type: "concept"
title: "Keepalives"
description: "Mechanisms that detect dead peers and hold connections open"
tags: ["keepalives", "networking", "tcp", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Keepalives

## Summary
Keepalives are periodic probes that confirm a connection is still alive — TCP keepalive in the kernel, HTTP/2 pings, or app-level heartbeats. They detect half-open connections and dead peers that silence would otherwise hide.

## Details
- TCP keepalive detects dead peers but is slow by default; HTTP/2 pings and app heartbeats are faster.
- Heartbeats double as liveness for leader election and replica health.
- Keepalive traffic costs bandwidth; tune intervals to your failure tolerance.
- mykb relevance: the wiki sync daemon heartbeats so a hung worker is detected and replaced.

## Related
- [[wiki/devops-infra/healthcheck-and-sidecar-containers|Healthcheck and Sidecar Containers]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]]
- [[wiki/devops-infra/healthcheck-and-sidecar-containers|Keepalives]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
