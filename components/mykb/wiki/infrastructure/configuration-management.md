---
type: "concept"
title: "Configuration Management"
description: "Keeping software configuration on servers consistent and convergent through automation tools"
tags: ["configuration", "ansible", "automation", "devops", "servers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.ansible.com/ansible/latest/index.html"]
---

# Configuration Management

## Summary
Configuration management automates the setup and upkeep of software on servers: packages, services, users, and files are declared as desired state, and tools converge the machine toward it. It turns fragile manual server tweaks into repeatable, reviewable playbooks. The practice sits downstream of infrastructure provisioning and upstream of application deployment.

## Details
- Push vs pull: Ansible connects to nodes on demand (push), while Chef, Puppet, and Salt run agents on a schedule (pull) — push is simpler to start, pull scales better.
- Desired-state convergence: playbooks declare packages and services; the tool compares actual state and fixes differences, which makes reruns safe and idempotent.
- Composition: roles and inventories separate reusable logic from node groups, and variables keep environment-specific values out of playbooks.
- Integration: configuration management runs after provisioning (Terraform creates the server, Ansible configures it) and can bootstrap ephemeral, immutable images.
- Secrets: variables must not embed credentials; they come from a vault or the secret store at runtime — see secret rotation for the lifecycle.
- Worked example: an Ansible playbook that installs nginx, writes a site config from a template, opens the firewall port, and verifies the service is listening.
- Drift is the enemy: out-of-band edits get overwritten on the next run, which is why ad-hoc SSH changes should be forbidden in managed fleets.

## Related
- [[wiki/infrastructure/configuration-drift|Configuration Drift]] — the failure mode convergence prevents
- [[wiki/infrastructure/secret-rotation|Secret Rotation]] — managing credentials in managed fleets
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]] — provisioning layer above config management
- [[wiki/devops-infra/terraform|Terraform]] — provisions the servers playbooks configure
- [[wiki/security/secrets-management|Secrets Management]] — where playbook credentials should live
- [[wiki/devops-infra/github-actions|GitHub Actions]] — triggering config runs from CI
