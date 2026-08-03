---
type: "concept"
title: "Trivy & Image Scanning"
description: "Finding vulnerabilities in images and filesystems"
tags: ["trivy", "scanning", "vulnerabilities", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Trivy & Image Scanning

## Summary
Trivy scans container images, filesystems, and repositories for vulnerabilities and misconfigurations, integrating into CI and admission so known-bad artifacts are caught before deploy. Image scanning closes the loop that SBOMs open: the SBOM says what is in the artifact, the scan says which of it is known-vulnerable.

## Details
- Mechanism: Trivy parses lockfiles and image layers to enumerate packages, matches versions against vulnerability databases (OS and language ecosystems), and reports severity with fix versions; it also scans IaC and Kubernetes manifests for misconfigurations; scans run in CI (image scan gate), on a schedule (registry scanning), and at admission (Trivy Operator).
- Concrete example: CI builds an image, runs `trivy image --severity CRITICAL,HIGH --exit-code 1`, and fails the build on unfixed criticals; a nightly job rescans the registry and files tickets for newly disclosed CVEs; Trivy Operator blocks pods using images with critical vulnerabilities.
- Failure modes: scan gates that block on unfixable or false-positive findings, so teams disable them — tune severity and fixable-only policies; databases that lag, missing fresh CVEs; scanning only at build time, missing base-image updates that occur later; exit-code thresholds that are too lax, catching nothing; scans with no SBOM context, missing transitive dependencies.
- Tradeoffs: scanning adds CI time and a triage burden (every finding needs a decision), but it converts supply-chain risk from unknown to tracked; the alternative — not scanning — is faster until a known CVE ships; the mature pattern is gate on fixable criticals, alert on the rest, and rescans on a schedule.
- Operational notes: keep vulnerability databases updated, tune policies per environment (prod stricter), and track time-to-fix as a metric.
- RSIS3 relevance: cosmos's daemon and dashboard images should pass the same scan gate — RSIS3's operational notes can treat CVE debt as one of its telemetry signals.

## Related
- [[wiki/devops-infra/image-signing-and-notary|Image Signing & Notary]] — related coverage in the same cluster
- [[wiki/devops-infra/golden-images-and-image-baking|Golden Images & Image Baking]] — related coverage in the same cluster
- [[wiki/infrastructure/container-scanning|Container Scanning]] — related coverage in the same cluster
- [[wiki/infrastructure/docker-image-optimization|Docker Image Optimization]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
