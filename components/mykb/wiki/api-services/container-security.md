---
type: "concept"
title: "Container Security"
description: "Hardening container images and runtimes against compromise"
tags: ["containers", "docker", "images", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.docker.com/engine/security/", "https://owasp.org/www-project-docker-top-10/"]
---

# Container Security

## Summary


## Details
- Container security spans the image supply chain, the runtime, and the host: base images, dependencies, privileges, and isolation all contribute.
- Images should be minimal, pinned, and scanned for vulnerabilities before deployment; signing and provenance records verify where they came from.
- At runtime, containers should run as non-root with dropped capabilities, read-only filesystems where possible, and resource limits.
- The container is not a security boundary by itself — the host kernel and container runtime hardening are part of the same decision.
- **Worked example / comparison** — Worked example — a wiki export container builds from a pinned slim base, runs as an unprivileged user with no network egress, and is scanned in CI before publish.
- For mykb, container security is documented as the image-plus-runtime story beneath the kubernetes-security article.

## Related
- [[wiki/api-services/kubernetes-security|Kubernetes Security]]
- [[wiki/security/container-hardening|Container Hardening]]
- [[wiki/api-services/sca|Software Composition Analysis]]
- [[wiki/security-auth/least-privilege|Least Privilege]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
