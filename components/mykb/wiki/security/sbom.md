---
type: "concept"
title: "SBOM"
description: "Machine-readable inventory of software components and dependencies enabling vulnerability tracking"
tags: ["sbom", "supply-chain", "security", "dependencies", "cisa"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.cisa.gov/sbom"]
---

# SBOM

## Summary
A Software Bill of Materials (SBOM) is a formal, machine-readable inventory of every component — libraries, packages, and their versions — in a software artifact. It lets organizations know what is inside their software so they can match vulnerabilities (CVEs) to real deployments. CISA promotes SBOMs as foundational to supply-chain risk management, typically in SPDX or CycloneDX format.

## Details
- Formats: SPDX (ISO standard) and CycloneDX (OWASP) are the dominant schemas; both capture components, versions, licenses, and dependency graphs.
- Generation: package managers (npm, pip, Maven) and build tools emit SBOMs at build time; container images get them from scanners (Syft, Trivy).
- Uses: vulnerability matching, license compliance, provenance verification, and incident response ("which of our images contain Log4j?").
- Minimum elements per CISA: supplier, component name, version, unique identifiers (CPE/PURL), dependency relationships, and author/timestamp.
- Distribution: attach SBOMs to releases and container registries; sign them so consumers can verify authenticity.
- Worked example: a mykb repo scan generating a CycloneDX SBOM per commit lets a CI job alert when a dependency CVE appears in the live dashboard build.
- Relationship: SBOMs are the input layer for [[wiki/security/supply-chain-security|supply-chain security]] tooling like SLSA verification.

## Related
- [[wiki/security/supply-chain-security|Supply Chain Security]] — SBOM is the inventory half
- [[wiki/devops-infra/github-actions|GitHub Actions]] — emit and scan SBOMs in CI
- [[wiki/security/container-hardening|Container Hardening]] — image inventories feed vulnerability scans
- [[wiki/tooling/alembic|Alembic]] — dependency tracking for database migrations
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — dependency baseline of the bundle
- [[wiki/ops/gap-report|Gap Analysis Report]] — noted supply-chain gaps
- [[wiki/devops-infra/kubernetes|Kubernetes]] — image scanning and admission policies in clusters
