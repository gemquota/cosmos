---
type: "concept"
title: "Container Hardening"
description: "Reducing container attack surface with minimal images, least privilege, and runtime security controls"
tags: ["containers", "docker", "security", "devops", "hardening"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.cisecurity.org/benchmark/docker"]
---

# Container Hardening

## Summary
Container hardening minimizes the attack surface of container images and runtimes: small base images, non-root users, read-only filesystems, pinned dependencies, and restricted capabilities. CIS Docker Benchmarks codify the checks. Since containers share the host kernel, defense-in-depth matters more than image size alone.

## Details
- Base images: prefer distroless or Alpine variants; scan images with Trivy/Grype before registry push.
- Least privilege: run as non-root (`USER 10001`), drop capabilities (`--cap-drop ALL`), and mount filesystems read-only where possible.
- Pin everything: image digests (`image@sha256:...`) and lockfiles prevent drift and surprise base-image updates.
- Runtime: seccomp/AppArmor profiles, no privileged mode, resource limits (CPU/memory), and `--read-only` root filesystems.
- Supply chain: sign images (cosign), verify signatures at deploy, and keep SBOMs attached for vulnerability matching.
- Secrets: never bake credentials into images; inject at runtime from vaults or mounted secrets.
- Worked example: a hardened mykb daemon container runs as UID 10001, reads only the wiki volume, and drops all capabilities — reducing a compromise to filesystem access only.

## Related
- [[wiki/security/sbom|SBOM]] — component inventory for image scanning
- [[wiki/security/supply-chain-security|Supply Chain Security]] — signed, pinned artifacts
- [[wiki/security/secrets-management|Secrets Management]] — runtime injection, not baked-in
- [[wiki/devops-infra/docker-compose|Docker Compose]] — local hardening applies there too
- [[wiki/devops-infra/kubernetes|Kubernetes]] — admission policies enforce image policy
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — containerized daemon notes
- [[wiki/ops/gap-report|Gap Analysis Report]] — hardening gaps tracked
