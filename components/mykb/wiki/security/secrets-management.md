---
type: "concept"
title: "Secrets Management"
description: "Storing, rotating, and auditing API keys, tokens, and passwords with centralized vaults"
tags: ["secrets", "vault", "security", "devops", "iam"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://developer.hashicorp.com/vault/docs"]
---

# Secrets Management

## Summary
Secrets management is the practice of storing API keys, database passwords, tokens, and certificates in a central, encrypted store with access control, rotation, and audit trails — never in source code or config files. Tools like HashiCorp Vault add dynamic secrets and leases, so credentials are short-lived and auto-rotating. It is a prerequisite for secure automation and supply-chain hygiene.

## Details
- Golden rule: no secrets in git, dotfiles, or build logs; reference vault paths or environment-injected secrets instead.
- Central store: encrypted at rest and in transit, with RBAC policies per application and human role.
- Dynamic secrets: Vault can mint short-lived database credentials or cloud keys per request, eliminating long-lived static keys.
- Rotation: schedule rotation for static secrets, detect exposure, and revoke leaked credentials in minutes via audit trails.
- Agent integration: CI/CD (GitHub Actions), containers, and edge functions read secrets at runtime; never bake them into images.
- Worked example: RSIS3's Telegram and LLM API keys could move from a local JSON file into Vault, with per-loop leases and an audit log of every access.
- Relationship: feeds [[wiki/security/zero-trust|Zero Trust]] identity and protects [[wiki/api-protocols/webhooks|webhook]] signing material.

## Related
- [[wiki/security/supply-chain-security|Supply Chain Security]] — leaked tokens are a top breach vector
- [[wiki/devops-infra/github-actions|GitHub Actions]] — CI secret injection patterns
- [[wiki/devops-infra/terraform|Terraform]] — provisioning vault policies as code
- [[wiki/security/zero-trust|Zero Trust Architecture]] — secrets as short-lived identity
- [[wiki/api-protocols/webhooks|Webhooks]] — signature secrets must be vaulted
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — credential handling across components
- [[wiki/devops-infra/kubernetes|Kubernetes]] — Secrets objects and sidecar injection
- [[wiki/devops-infra/istio|Istio]] — workload identity and SPIFFE-style trust
- [[wiki/ops/gap-report|Gap Analysis Report]] — credential-handling gaps noted
