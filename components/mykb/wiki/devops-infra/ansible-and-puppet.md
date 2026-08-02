---
type: "concept"
title: "Ansible & Puppet"
description: "Agentless and agent-based configuration tools"
tags: ["ansible", "puppet", "config-management", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.ansible.com/ansible/latest/getting_started/index.html",
  "https://www.puppet.com/docs/puppet/latest/architecture.html",
]
---

# Ansible & Puppet

## Summary
Ansible and Puppet represent the two dominant configuration management models: push-based, agentless orchestration versus pull-based, agent-managed convergence. Choosing between them shapes how fleets are managed and secured. Most organizations standardize on one model and layer tools around it.

## Details
- Ansible runs over SSH in push mode, with playbooks of modules and inventory-based targeting.
- Puppet runs an agent on each node that pulls and applies a catalog compiled from manifests.
- Ansible's getting-started docs show ad-hoc commands and playbooks.
- Ansible's getting-started documentation shows ad-hoc commands, playbooks, and inventory patterns.
- Scale and network topology favor pull models; simplicity favors push.
- In mykb, both connect to configuration management, IaC, and package updates.
- Ansible's inventory and ad-hoc commands make quick fleet operations simple and auditable.
- Puppet's reporting gives per-node compliance visibility into the desired state.
- Hybrid shops often use Ansible for orchestration and Puppet or another agent for long-term state.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/acid|ACID]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
