---
type: "concept"
title: "Secret Stores: Vault & Consul"
description: "Centralized secret storage with leases and access policies"
tags: ["vault", "consul", "secrets", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Secret Stores: Vault & Consul

## Summary
Secret stores centralize secrets — API keys, tokens, passwords, certificates — behind an audited, access-controlled service, instead of scattering them in configs, env vars, and repos. HashiCorp Vault is the reference tool, with dynamic secrets, encryption-as-a-service, and rotation; Consul adds service discovery and KV storage alongside.

## Details
- Vault mechanics: secrets live in paths with policies controlling who may read or write; authentication integrates with identity providers (OIDC, Kubernetes, LDAP); dynamic secrets (database credentials, cloud keys) are issued on demand with short TTLs and auto-rotation; encryption-as-a-service lets applications encrypt data without storing keys; audit logs record every access.
- Consul mechanics: a distributed KV store and service registry with health checking; Consul's KV can hold config but is not a secrets engine — teams often pair Vault (secrets) with Consul (service discovery and config) rather than treating them as equivalents.
- Concrete example: an app authenticates to Vault via its Kubernetes service account, requests a database credential valid for 5 minutes, and the credential is revoked when it expires; a cron job rotates a signing key by writing a new version to Vault; audit logs show who read which secret when.
- Failure modes: Vault becoming a single point of failure — if it is down, apps cannot get secrets, so run it HA with auto-unseal and cache leases; secrets leaked into logs or env vars despite the store; policies too broad, granting read to everything; unseal-key handling errors locking the cluster out; applications caching secrets past their TTL, invalidating rotation.
- Tradeoffs: a secret store trades operational complexity for security and auditability; the alternative — env-var and config-file secrets — is simpler and fails only at compromise time; the mature pattern is short-lived, least-privilege, auto-rotating secrets for anything sensitive, with the store itself run HA and rehearsed in drills.
- Operational notes: run Vault HA with auto-unseal, keep policies in code, audit access, and test the failure path.
- RSIS3 relevance: cosmos's tokens (deployment, daemon credentials) belong in a store with short TTLs — RSIS3's operational notes should record where they live and how they rotate.

## Related
- [[wiki/cloud-infra/parameter-stores-aws-ssm-azure-keyvault-gcp-secretmanager|Cloud Parameter Stores]]
- [[wiki/infrastructure/secret-rotation|Secret Rotation]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
