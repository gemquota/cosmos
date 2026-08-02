---
type: "concept"
title: "Container Images (OCI)"
description: "Layered, immutable image format defined by the OCI spec"
tags: ["oci", "images", "containers", "layers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://opencontainers.org/",
  "https://github.com/opencontainers/image-spec",
]
---

# Container Images (OCI)

## Summary
OCI container images are immutable, layered bundles of filesystem changes plus configuration. The image spec defines the format, making images portable across runtimes and registries. Image design drives build caching and supply-chain security.

## Details
- An image is a manifest referencing layers, each layer a filesystem diff applied in order to form the rootfs.
- The OCI image spec standardizes the format so Docker, containerd, Podman, and registries interoperate across vendors.
- Layers are content-addressed, which enables sharing and caching across images.
- Configuration in the image sets entrypoint, environment, exposed ports, and user.
- Rebuilding only changed layers speeds CI, but mutable tags and fat images create real supply-chain risk in production.
- In mykb, images connect to registries, signing, SBOM, build caching, and container runtime articles.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/container-network-interfaces|Container Network Interfaces]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/infrastructure/container-registries|Container Registries]]
- [[wiki/infrastructure/container-scanning|Container Scanning]]
