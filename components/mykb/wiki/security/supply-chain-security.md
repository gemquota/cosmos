---
type: "concept"
title: "Software Supply Chain Security"
description: "Protecting the end-to-end pipeline that produces and ships software, from source to artifact"
tags: ["supply-chain", "security", "slsa", "ci-cd", "provenance"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://slsa.dev/"]
---

# Software Supply Chain Security

## Summary
Software supply chain security protects everything between a developer's commit and a deployed artifact: dependencies, build systems, registries, and release channels. Attacks inject malicious code into popular packages or compromise build infrastructure to ship tampered binaries. Frameworks like SLSA (Supply-chain Levels for Software Artifacts) define graduated controls — from provenance attestations to hermetic builds — that make tampering detectable.

## Details
- Threat model: typosquatted packages, account takeovers of maintainers, compromised CI runners, and registry poisoning.
- SLSA levels: L1 (provenance exists) through L4 (two-person review, hermetic builds, signed provenance) give teams a maturity ladder.
- Key controls: lockfiles with pinned hashes, dependency scanning, signed commits (GPG/SSH), SBOM generation, and artifact signing with attestation.
- Build hygiene: hermetic, reproducible builds; no secrets in build logs; isolated runners for untrusted pull requests.
- Verification: consumers check signatures and attestations before deployment — registry proxies and admission controllers enforce policy.
- Worked example: the cosmos bundle could pin Python and npm lockfiles, sign release artifacts, and attach a CycloneDX SBOM, moving its GitHub Actions pipeline toward SLSA L2.
- Relationship: [[wiki/security/sbom|SBOM]] inventories components; SLSA verifies the chain that produced them.

## Related
- [[wiki/security/sbom|SBOM]] — the component inventory layer
- [[wiki/devops-infra/github-actions|GitHub Actions]] — build pipeline subject to compromise
- [[wiki/security/container-hardening|Container Hardening]] — minimal, pinned images
- [[wiki/security/secrets-management|Secrets Management]] — leaked tokens enable attacks
- [[wiki/security/zero-trust|Zero Trust Architecture]] — extends trust boundaries to artifacts
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — toolchain dependencies of the wiki system
- [[wiki/devops-infra/helm|Helm]] — chart provenance and signature verification
- [[wiki/devops-infra/kubernetes|Kubernetes]] — admission control for signed images
- [[wiki/ops/gap-report|Gap Analysis Report]] — supply-chain gaps tracked
