---
type: "concept"
title: "Base Image Management"
description: "Curating, updating, and pinning the base images everything builds on"
tags: ["base-images", "containers", "supply-chain", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Base Image Management

## Summary
Base image management treats base images as dependencies: pinned by digest, tracked for updates, minimized in size, and rebuilt on a cadence. A stale base image silently ships every CVE fixed upstream — a classic supply-chain gap.

## Details
- Pin by digest (sha256:) not tag; automation (Renovate/Dependabot) tracks upstream updates.
- Use minimal, distroless-style bases to shrink attack surface and scan results.
- Rebuild cadence matters: weekly rebuilds roll in security fixes even without code changes.
- mykb relevance: the wiki rebuilds images weekly from pinned digests with scans.

## Related
- [[wiki/tooling/containerization-practice|Containerization Practice]]
- [[wiki/communities/dependency-updates|Dependency Updates]]
- [[wiki/communities/image-scanning|Image Scanning]]
- [[wiki/compositions/shift-left-security|Shift-Left Security]]
- [[wiki/communities/registry-practice|Registry Practice]]
