---
type: "concept"
title: "gRPC Load Balancing"
description: "Client-side and xDS load-balancing policies"
tags: ["grpc", "load-balancing", "xds", "rpc", "infrastructure"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grpc.io/blog/grpc-load-balancing/", "https://grpc.io/docs/guides/load-balancing/"]
---

# gRPC Load Balancing

## Summary
gRPC load balancing differs from HTTP load balancing because connections are long-lived and multiplexed: a connection-level balancer would pin one client to one backend for every call. gRPC uses client-side load balancing — the client picks a backend per RPC — with subchannel pools and the xDS control plane for dynamic policies.

## Details
- Why client-side: HTTP/2 multiplexes many RPCs over one connection, so balancing connections (L4) does not balance calls; the client must spread calls across subchannels.
- pick_first: try subchannels in order until one connects — the default, with no per-call balancing.
- round_robin: cycle RPCs across ready subchannels, improving utilization on long-lived channels.
- Weighted targets and least-request policies exist in extended resolvers (for example gRPC-LB and Envoy's least_request) for skew-aware balancing.
- xDS: the control plane (Envoy ADS, Istio, or a custom server) publishes cluster endpoints, health, and policies to gRPC clients via the xDS protocol, enabling dynamic updates.
- Health awareness: subchannels track readiness; gRPC health checking (grpc.health.v1) marks backends ready/not-ready, and the balancer stops routing to failed ones.
- Sticky vs stateful: stateful calls (streams, transactions) need affinity hints, which plain balancing cannot provide without session affinity layers.

## Related
- [[wiki/api-protocols/load-balancing|Load Balancing]] — the general distribution problem gRPC solves differently
- [[wiki/api-protocols/grpc-streaming|gRPC Streaming]] — long streams interact with balancing policies
- [[wiki/api-protocols/health-checks|Health Checks]] — readiness feeds balancer decisions
- [[wiki/api-protocols/service-mesh|Service Mesh]] — xDS control planes come from mesh infrastructure
- [[wiki/devops-infra/envoy|Envoy]] — a common xDS server for gRPC clients
