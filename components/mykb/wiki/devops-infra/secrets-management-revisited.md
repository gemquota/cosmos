---
type: "concept"
title: "Secrets Management"
description: "Storing, rotating, and distributing credentials safely"
tags: ["secrets", "vault", "security", "rotation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://developer.hashicorp.com/vault/docs",
  "https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html",
]
---

# Secrets Management

## Summary
Secrets management covers the storage, rotation, and distribution of credentials, keys, and tokens. Centralizing secrets in vaults reduces sprawl, audit blind spots, and leak blast radius. It is a core security control for every service and a recurring theme in the mykb security cluster.

## Details
- A secret store encrypts values at rest and grants access by policy and lease.
- HashiCorp Vault documents its secrets engines, auth methods, and dynamic secrets.
- Cloud services (Secrets Manager, Key Vault) integrate rotation with application roles.
- Secrets in Git, config files, or environment dumps are the top leak vector.
- Dynamic and short-lived credentials shrink the blast radius of a leak.
- In mykb, secrets connect to Vault, parameter stores, and Kubernetes secrets rotation.
- Audit logs of secret access are essential for incident investigation and compliance.
- Secrets should be injected at runtime, not baked into images or committed to repositories.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
- [[wiki/cloud-infra/quota-management|Quota Management]]
