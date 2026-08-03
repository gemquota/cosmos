---
type: "concept"
title: "SBOMs & Syft"
description: "Machine-readable bills of materials for container images"
tags: ["sbom", "syft", "supply-chain", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SBOMs & Syft

## Summary
A Software Bill of Materials (SBOM) lists every component in an artifact — packages, versions, licenses, hashes, and dependency relationships — making the supply chain visible. Syft generates SBOMs from images and filesystems; Grype scans them for vulnerabilities; together they give CI a continuous answer to what is in the artifact and what is known-bad.

## Details
- Mechanism: Syft inspects a container image or directory and produces an SBOM (CycloneDX or SPDX); Grype matches the component list against vulnerability databases; the SBOM is attached to the artifact (attested with signatures) and stored with it; consumers and scanners can audit any artifact's contents without re-inspecting it.
- Concrete example: CI runs `syft scan image:latest` producing `sbom.cdx.json`, then `grype` reports CVEs with severity; the pipeline fails on critical vulnerabilities; the SBOM is published alongside the image and signed with Cosign; a post-release audit answers which images contain a newly disclosed CVE by querying SBOMs.
- Failure modes: SBOMs generated once and never updated — they describe the artifact at build time, so a base-image update invalidates them; scanning that is not enforced (SBOM exists, nothing acts on it); vulnerability databases lagging, so fresh CVEs are missed; SBOM formats and fields that vary, breaking downstream tooling; false positives from version-only matching without fix-version context.
- Tradeoffs: SBOMs add build time, storage, and toolchain complexity but provide the provenance and audit trail that incident response needs; the alternative — asking what is in an image after a compromise — is too late; the maturity path is generate, sign, store, scan, and alert, in that order.
- Operational notes: attach SBOMs to every release artifact, enforce scanning gates, and keep SBOMs retrievable for at least the artifact's retention window.
- RSIS3 relevance: cosmos's artifacts (dashboard bundles, daemon images) should carry SBOMs so RSIS3 can assess the exposure of its own stack when a CVE lands; scanning must run on every promotion, not just at release.

## Related
