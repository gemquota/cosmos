---
type: "concept"
title: "Container Registries"
description: "Systems that store, sign, and distribute container images to clusters and CI pipelines"
tags: ["registries", "oci", "containers", "supply-chain", "distribution"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.docker.com/registry/introduction/"]
---

# Container Registries

## Summary
A container registry is the distribution backbone for container images: it stores image layers and manifests and serves pushes and pulls over HTTPS. Registries make images addressable by tag and digest, enable caching and mirroring, and are a natural place to enforce signing and vulnerability policy. Public registries such as Docker Hub and GitHub Container Registry coexist with private and self-hosted options.

## Details
- The OCI distribution specification defines the registry API: clients push layers and manifests, then pull by tag or by immutable content digest.
- Tag vs digest: tags are mutable and human-friendly (app:v1.2.3), digests (sha256:...) are immutable and cryptographically verifiable — production deployments should pin digests.
- Pull-through caches sit between a cluster and an upstream registry, reducing egress and rate-limit pressure while adding a local audit point.
- Access control: registries authenticate clients (token or mTLS), support scoped permissions, and integrate with identity systems like the wiki's RBAC model.
- Signing with cosign or Notary attaches provenance so consumers can verify who built an image; SBOMs can be attached and scanned at push time.
- Worked example: a mykb deployment pipeline would push an image to a private registry with a digest-pinned deploy manifest; the cluster's kubelet would pull via a pull-through cache in the same VPC.
- Self-hosting (Docker Registry, Harbor, Quay) gives data residency but adds storage, auth, and uptime responsibility.

- Digest discipline: production deployments should pin digests rather than tags, because a tag can move under the deployment; the standing rule is that tags are for humans and digests are for machines.
- Cleanup policy: registries accumulate orphaned layers, so retention rules should prune unreferenced images on a schedule rather than letting storage grow unbounded.
## Related
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]] — broader home for images, packages, and binaries
- [[wiki/infrastructure/container-scanning|Container Scanning]] — policy checks applied at push time
- [[wiki/devops-infra/helm|Helm]] — charts that reference registry images
- [[wiki/security/sbom|SBOM]] — software bill of materials attached to images
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — provenance and signing for artifacts
- [[wiki/devops-infra/docker-compose|Docker Compose]] — local image usage before registry push
