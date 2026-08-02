---
type: "concept"
title: "Configuration Management"
description: "Keeping system state declarative and convergent"
tags: ["config-management", "ansible", "state", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.ansible.com/ansible/latest/index.html",
  "https://www.puppet.com/docs/puppet/latest/puppet_overview.html",
]
---

# Configuration Management

## Summary
Configuration management keeps servers in a declared state, converging drift automatically or reporting it. Tools range from agent-based convergence to push-based orchestration. It is the operational layer below infrastructure as code and the backbone of fleet consistency.

## Details
- Desired-state models compare current system state to declarations and apply only the difference.
- Ansible documents its agentless model and module system.
- Puppet's declarative language and agent architecture are documented by the project.
- Idempotency is the key guarantee: running twice changes nothing twice.
- Secrets and templates are injected during convergence, not baked in.
- In mykb, configuration management connects to IaC, secrets, and package management.
- Convergence reports and drift metrics show whether the fleet actually matches declarations.
- Roles and inventories group hosts so the same declarations apply to similar machines.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/infrastructure/configuration-management|Configuration Management]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
