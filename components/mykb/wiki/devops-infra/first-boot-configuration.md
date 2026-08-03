---
type: "concept"
title: "First-Boot Configuration"
description: "Applying network, storage, and agent config at first launch"
tags: ["first-boot", "provisioning", "config", "bootstrap"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# First-Boot Configuration

## Summary
First-boot configuration provisions a fresh machine or container from zero to a usable, policy-compliant state: base image, users, packages, services, secrets, and registration with the management plane. Cloud-init, Ignition, and provisioning tools (Ansible, Packer, Terraform) are the mechanisms; the goal is deterministic, unattended bring-up.

## Details
- Mechanism: the instance boots with user-data; cloud-init runs modules (set hostname, users, SSH keys, write files, run commands, install packages) and reports status; Ignition applies a JSON config at first boot before the userspace services start, which is essential for immutable Fedora CoreOS-style images; afterwards a config manager reconciles ongoing state.
- Concrete example: a Terraform-created VM passes a cloud-init user-data script that configures SSH, mounts the data disk, installs the agent, and registers with Consul or the CMDB; a reboot keeps the state, while a replacement VM reaches the same state automatically.
- Failure modes: user-data that fails partway leaves a half-configured machine that "succeeds" in the console — cloud-init status and logs must be checked; secrets in user-data persist on the instance and in logs; first-boot scripts that assume network or package availability at boot race dependencies; re-running idempotency — scripts that fail on second boot after a partial first run.
- Tradeoffs: first-boot provisioning gives fast, reproducible bring-up but the config drifts once machines age — pair it with continuous reconciliation; baking everything into images (golden images) is more deterministic but slower to change; the split is first-boot for instance identity and secrets plus a config manager for everything else.
- Operational notes: version user-data with the repo, test first boot in CI, and monitor first-boot success rates.
- RSIS3 relevance: wherever cosmos runs its services, first-boot config should be reviewable code so a replacement node for the wiki daemon reaches the same state without manual steps.

## Related
- [[wiki/devops-infra/configuration-management-revisited|Configuration Management]] — related coverage in the same cluster
- [[wiki/os-shell/boot-process-and-firmware|Boot Process & Firmware]] — related coverage in the same cluster
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]] — related coverage in the same cluster
- [[wiki/devops-infra/configuration-as-data|Configuration as Data]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
