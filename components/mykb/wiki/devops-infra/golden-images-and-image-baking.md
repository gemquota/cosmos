---
type: "concept"
title: "Golden Images & Image Baking"
description: "Pre-baked machine images with known-good configuration"
tags: ["golden-image", "baking", "packer", "images"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Golden Images & Image Baking

## Summary
Golden images are pre-baked, hardened base images — OS, security patches, agents, and defaults — that instances are created from; image baking is the pipeline (Packer, image builders, CI) that builds and publishes them. Baking moves provisioning work to build time, so boot is fast, deterministic, and consistent with the security baseline.

## Details
- Mechanism: a build pipeline starts from a base OS image, applies a scripted provisioner (Packer: install packages, apply CIS hardening, install agents, enable services, set timezone and SSH config), runs validation and scans, then publishes a versioned, signed image to a registry; instance creation references the exact image version.
- Concrete example: a quarterly bake produces `ubuntu-24.04-cis-2026.08` from a versioned Packer template; a security patch forces a new bake rather than in-place updates; CI runs `packer validate` and vulnerability scans before publishing; autoscaling uses the latest golden image so new instances are already patched.
- Failure modes: stale golden images — instances born old because the bake is infrequent or the autoscaler references an old version; in-place patching drift undermining the bake (patch at instance level too, or rebuild); image bloat from baked-in but unused packages; a bad bake propagating a broken config to every new instance (test images before promoting to prod); bake secrets embedded in the image.
- Tradeoffs: baking makes boot fast and consistent but slows change — every package update needs a bake cycle; the alternative, first-boot configuration, is more flexible but slower and less consistent; the common split is a small golden image for the OS baseline plus first-boot config for instance-specific state.
- Operational notes: version and sign images, scan them in CI, test a boot before promotion, and track which image versions run where.
- RSIS3 relevance: cosmos services benefit from the same discipline — a known, reproducible base for the daemon and dashboard serving ensures new instances behave like tested ones.

## Related
- [[wiki/devops-infra/container-images-oci|Container Images (OCI)]] — related coverage in the same cluster
- [[wiki/devops-infra/image-signing-and-notary|Image Signing & Notary]] — related coverage in the same cluster
- [[wiki/devops-infra/trivy-and-image-scanning|Trivy & Image Scanning]] — related coverage in the same cluster
- [[wiki/devops-infra/golden-signals|Golden Signals]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
