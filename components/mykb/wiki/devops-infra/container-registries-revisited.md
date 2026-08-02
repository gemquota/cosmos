---
type: "concept"
title: "Container Registries"
description: "Storing and distributing container images at scale"
tags: ["registry", "containers", "images", "distribution"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://distribution.github.io/distribution/",
  "https://docs.docker.com/registry/",
]
---

# Container Registries

## Summary
Container registries store and distribute images, acting as the artifact hub between CI and clusters. They add access control, signing, and caching on top of the OCI distribution protocol. Registry operations are central to software supply chains.

## Details
- The OCI distribution spec defines the push/pull API used by all major registries, including authentication and layer blob handling.
- Docker Distribution is the reference open-source registry implementation.
- Access control, pull-through caching, and vulnerability scanning are typical managed-registry features that harden the supply chain.
- Mirroring registries into private networks reduces egress cost and supply-chain exposure.
- Retention and GC policies keep registries from filling with stale images and unreferenced layers over time.
- In mykb, registries connect to image signing, SBOM, mirroring, and CI/CD pipelines across the supply-chain cluster.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/container-network-interfaces|Container Network Interfaces]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/infrastructure/container-registries|Container Registries]]
- [[wiki/infrastructure/container-scanning|Container Scanning]]
