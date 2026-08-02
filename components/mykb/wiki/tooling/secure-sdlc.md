---
type: "concept"
title: "Secure SDLC"
description: "Building security into every phase of the software development lifecycle"
tags: ["secure-sdlc", "security", "lifecycle", "process"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://csrc.nist.gov/Projects/ssdf", "https://en.wikipedia.org/wiki/DevSecOps"]
---

# Secure SDLC

## Summary
A secure SDLC embeds security activities in every phase of development — training, design review, threat modeling, secure coding, testing, and response — instead of auditing at the end. NIST's SSDF formalizes the practice for software producers and acquirers.

## Details
- Security is a phase-by-phase thread: requirements (abuse cases), design (threat model), coding (standards, scanning), testing (SAST/DAST), release (SBOM, signing), and operations (incident response).
- Shift-left economics: a flaw caught in design costs pennies compared to one fixed in production.
- Automation is the enabler: scanners and pipelines enforce policy without depending on memory.
- The SDLC also secures the supply chain: provenance, signed artifacts, and dependency verification.
- Security debt is technical debt: inventory and schedule it like any other debt.
- For the mykb bundle, the SDLC covers the tooling and the corpus — sources verified, links checked, content signed.

Worked example — the wiki's SDLC: threat model at design, SAST in CI, dependency scans on every merge, SBOM with each release, and a documented incident path for compromised sources.

## Related
- [[wiki/compositions/threat-modeling|Threat Modeling]]
- [[wiki/compositions/shift-left-security|Shift-Left Security]]
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
- [[wiki/compositions/security-engineering|Security Engineering]]
- [[wiki/communities/incident-management|Incident Management]]
- [[wiki/communities/vulnerability-scanning-ci|Vulnerability Scanning in CI]]
- [[wiki/communities/image-scanning|Image Scanning]]
- [[wiki/security/supply-chain-security|Software Supply Chain Security]]
- [[wiki/testing/security-testing|Security Testing]]
