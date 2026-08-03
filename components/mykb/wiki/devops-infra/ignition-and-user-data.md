---
type: "concept"
title: "Ignition & User Data"
description: "First-boot configuration for Fedora CoreOS and cloud VMs"
tags: ["ignition", "user-data", "provisioning", "coreos"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Ignition & User Data

## Summary
Ignition and cloud-init are the two first-boot provisioning systems for Linux instances: cloud-init is the ubiquitous, distro-agnostic tool that runs user-data scripts and modules; Ignition is the Fedora CoreOS-style system that applies a JSON config to the raw disk at first boot, before services start. Both make boot-time configuration declarative and reproducible.

## Details
- cloud-init mechanics: instance metadata (user-data, instance-id) is consumed by modules in phases (network, config, final); it writes files, users, SSH keys, packages, and runs arbitrary commands; it is idempotent via instance-id tracking and reports status to the console or a datasource.
- Ignition mechanics: a JSON config (Butane transpiles human-friendly YAML to JSON) is written to the disk image; on first boot Ignition parses it and provisions storage, filesystems, files, systemd units, and users before the OS services start — making it suited to immutable images where runtime mutation is discouraged.
- Concrete example: a Terraform-created VM passes cloud-init user-data that sets the admin user, installs the agent, and registers the host; a CoreOS node is built with an Ignition config that formats disks, writes the workload, and starts the container runtime on boot.
- Failure modes: user-data that fails partway leaves a broken instance that "boots" — check cloud-init status; scripts that are not idempotent break on second run; secrets embedded in user-data persist in metadata and logs; Ignition configs that reference files or units that do not exist fail boot with obscure errors; base-image changes invalidating assumptions (distro version, network config).
- Tradeoffs: cloud-init is flexible and widely supported but imperative at its edges (shell); Ignition is declarative and deterministic but tied to the CoreOS ecosystem; choose by image philosophy — mutable images pair with cloud-init, immutable with Ignition.
- Operational notes: version user-data and Ignition configs in the repo, test first boot in CI, and monitor boot success signals.
- RSIS3 relevance: wherever cosmos nodes boot, deterministic first-boot config means a replacement wiki daemon host reaches the same state without manual recovery steps.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]] — related coverage in the same cluster
- [[wiki/infrastructure/data-plane-versus-control-plane|Data Plane vs Control Plane]] — related coverage in the same cluster
- [[wiki/cloud-infra/data-archiving|Data Archiving]] — related coverage in the same cluster
- [[wiki/infrastructure/data-deduplication-in-storage|Data Deduplication in Storage]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
