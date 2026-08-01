---
type: "concept"
title: "Container Security"
description: "Hardening container images and runtimes against compromise"
tags: ["containers", "docker", "images", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html"]
---

# Container Security

- Container security covers image hygiene (minimal base, no secrets, vulnerability scanning), runtime hardening, and host isolation.
- OWASP's Docker Security Cheat Sheet: run non-root, read-only rootfs, drop capabilities, and pin base images.
- Supply-chain angle: images must be signed and scanned because they aggregate third-party software.
- For mykb: agent runtimes should run in least-privilege containers with no write access to the host.

## Related

- [[wiki/api-services/kubernetes-security|Kubernetes Security]] — the orchestrator layer
- [[wiki/security/container-hardening|Container Hardening]] — existing article on hardening
- [[wiki/api-services/sca|Software Composition Analysis]] — scanning image dependencies
- [[wiki/security-auth/least-privilege|Least Privilege]] — minimal container privileges
