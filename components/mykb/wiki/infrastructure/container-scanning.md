---
type: "concept"
title: "Container Scanning"
description: "Checking images for known vulnerabilities, secrets, and policy violations before they ship"
tags: ["container-security", "scanning", "vulnerabilities", "supply-chain"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Container Scanning

## Summary
Container scanning inspects images for CVEs, embedded secrets, and policy violations, ideally at build and push time so bad images never reach production. It is the image-side half of container supply-chain security: the runtime hardens what runs, but scanning decides what is allowed to run in the first place.

## Details
- Scanners match image layers and packages against vulnerability databases (Trivy, Grype, Clair). The mechanism: each image is unpacked into its layers, each layer's installed packages (apt, apk, pip, npm, go modules, Java jars) are enumerated, and each package version is looked up against vulnerability feeds (OSV, NVD, vendor advisories). The scan output is a per-layer inventory of findings with severity (critical/high/medium/low), the affected package, and the fixing version. Because the scan operates on layers, it can attribute a vulnerability to the layer that introduced it — which matters for fixing (rebuild just that layer's context, or update the base image).
- Gate on severity and fixability: blocking on every CVE stalls delivery; failing on criticals is the norm. The policy question is what makes an image fail: blocking on any CVE, even low-severity ones in obscure packages, turns every deploy into a triage meeting; blocking on nothing makes scanning decoration. The standard middle is severity-based gating (critical and high fail the build) plus fixability awareness (a critical with no fix should block or at least require sign-off; a high with a trivial fix should fail until the fix is applied) and context (a vulnerability in a network-exposed service matters more than one in a CLI tool that never runs). The policy must be written down and versioned, because ad-hoc gating is inconsistently applied gating.
- Scan base images and dependencies, not just the final layer. Most findings come from the base image and the dependency tree, not the application code — so the scan must cover the full image history and the lockfile-derived dependency sets. The practical workflow: scan the base image once per update (not per build), scan dependencies at build time (from lockfiles, where available), and scan the final image before push. SBOM generation alongside scanning makes the inventory auditable and lets scanners focus on what changed.
- Open question: how scan results should gate promotion in the pipeline — severity-only, or also exploitability, reachability, and runtime context, which would reduce noise dramatically but require runtime-aware analysis.
- For mykb: container scanning is the sibling of dependency auditing and supply-chain attestation — the same "know what you ship" discipline applied to images.

## Related
- [[wiki/infrastructure/docker-image-optimization|Docker Image Optimization]] — smaller images scan cleaner
- [[wiki/infrastructure/container-registries|Container Registries]] — scanning at push time
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]] — scanning the wider artifact stream
- [[wiki/security/container-hardening|Container Hardening]] — runtime side of image hygiene
