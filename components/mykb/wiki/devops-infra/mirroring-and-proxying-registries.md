---
type: "concept"
title: "Mirroring & Proxying Registries"
description: "Caching and controlling access to container registries"
tags: ["mirror", "registry", "proxy", "containers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Mirroring & Proxying Registries

## Summary
Registry mirroring and proxying put a local cache in front of container registries: pulls of popular images are served from the mirror instead of the upstream, reducing egress cost, latency, and upstream rate limits — and keeping pulls working during upstream outages or registry throttling.

## Details
- Mechanism: a registry configured as a pull-through cache (Harbor, Nexus, distribution mirror) proxies requests to the upstream, caches layers, and serves subsequent pulls locally; clients point their registry config at the mirror (mirror: in /etc/containers/registries.conf, containerd config, or a registry fallback); tags and digests are validated against the upstream to prevent tampering.
- Concrete example: a fleet of build machines and clusters all pull through a local Harbor that caches `docker.io` layers; first pull is slow, subsequent ones are local; during a Docker Hub rate-limit event, the cache absorbs the load; promotion pipelines push internal images to the same registry.
- Failure modes: stale cached layers when upstream re-tags (cache-busting issues, resolved by digest-based pulls); mirror outages blocking all pulls — the mirror becomes a single point of failure unless clients can fall back; cache poisoning if the mirror does not validate signatures; unbounded disk growth from layer caching (configure retention and GC); authentication propagation — mirroring private upstreams needs the mirror to hold credentials.
- Tradeoffs: mirrors cut cost and latency and provide an availability buffer, but add infrastructure and a trust boundary; the alternative — pulling direct — is simpler but pays egress and throttling; the standard pattern is mirror for public upstreams plus a private registry for internal images.
- Operational notes: monitor cache hit ratio, disk usage, and upstream health; sign internal images; test the fallback path.
- RSIS3 relevance: cosmos's CI pulls many images — a local mirror makes builds reproducible and fast and keeps them running when upstream rate limits bite.

## Related
- [[wiki/devops-infra/container-registries-revisited|Container Registries]]
- [[wiki/devops-infra/websocket-proxying|WebSocket Proxying]]
- [[wiki/devops-infra/mirroring-and-shadow-traffic|Mirroring & Shadow Traffic]]
- [[wiki/infrastructure/container-registries|Container Registries]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
