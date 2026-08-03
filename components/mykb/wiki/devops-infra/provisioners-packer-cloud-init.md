---
type: "concept"
title: "Provisioners: Packer & cloud-init"
description: "Building images with Packer and first-boot config with cloud-init"
tags: ["packer", "cloud-init", "provisioning", "images"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Provisioners: Packer & cloud-init

## Summary
Provisioning systems — Packer for baking images, cloud-init for first-boot config, Terraform/Ansible for infrastructure state — form the pipeline that turns a bare OS into a working, policy-compliant instance. Each tool has a role: Packer bakes the reusable image, cloud-init personalizes each boot, and config management reconciles ongoing state.

## Details
- Packer: builds golden images reproducibly — a template defines builders (AWS, QEMU, Docker), provisioners (shell, Ansible), and post-processors (compress, publish); the result is a versioned, reusable image; bake time is the right place for packages, hardening, and agents.
- cloud-init: runs at first boot from instance metadata — sets users, SSH keys, hostname, mounts disks, installs packages, runs commands; it personalizes generic images per instance without changing the image.
- Config management (Ansible, Terraform): Terraform owns infrastructure state (instances, networks), Ansible owns mutable configuration and orchestration; both are declarative and drift-reconciling to varying degrees.
- Concrete example: Packer bakes ubuntu-24.04-hardened; Terraform provisions instances from it with user-data; cloud-init sets the host identity and registers the node; Ansible (or a boot-time agent) installs the app and enrolls monitoring.
- Failure modes: responsibility overlaps — packages installed both at bake and boot drift; user-data that fails silently leaving an unmanaged instance; Packer builds that are not reproducible (unpinned packages, network dependence); image-versus-config mismatches where the app expects a library the image lacks; secrets leaking through templates or user-data.
- Tradeoffs: baking more (thick images) makes boot fast and consistent but slow to change; baking less (thin images plus boot config) is flexible but slower and more variable; the standard split is a small hardened base baked, with instance-specific state handled at boot and by config management.
- Operational notes: version templates, scan images in CI, test first boot, and keep provisioning code reviewed like app code.
- RSIS3 relevance: cosmos's own provisioning should follow the same layering — known base image, deterministic first boot, declarative state — so any node reproduces the wiki environment exactly.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]] — related coverage in the same cluster
- [[wiki/cloud-infra/multi-cloud-hybrid-cloud|Multi-Cloud & Hybrid Cloud]] — related coverage in the same cluster
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]] — related coverage in the same cluster
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
