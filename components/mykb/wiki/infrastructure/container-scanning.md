---
type: "concept"
title: "Container Scanning"
description: "Checking images for known vulnerabilities, secrets, and policy violations before they ship"
tags: ["container-security", "scanning", "vulnerabilities", "supply-chain"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Container Scanning

## Summary
Container scanning inspects images for CVEs, embedded secrets, and policy violations, ideally at build and push time so bad images never reach production.

## Details
- Scanners match image layers and packages against vulnerability databases (Trivy, Grype, Clair).
- Gate on severity and fixability: blocking on every CVE stalls delivery; failing on criticals is the norm.
- Scan base images and dependencies, not just the final layer.
- Open question: how scan results should gate promotion in the pipeline.

## Related
- [[wiki/infrastructure/docker-image-optimization|Docker Image Optimization]] — smaller images scan cleaner
- [[wiki/infrastructure/container-registries|Container Registries]] — scanning at push time
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]] — scanning the wider artifact stream
- [[wiki/security/container-hardening|Container Hardening]] — runtime side of image hygiene
