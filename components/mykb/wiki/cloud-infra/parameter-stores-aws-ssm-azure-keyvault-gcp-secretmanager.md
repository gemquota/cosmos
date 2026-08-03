---
type: "concept"
title: "Cloud Parameter Stores"
description: "SSM, Key Vault, and Secret Manager as central config stores"
tags: ["ssm", "keyvault", "secret-manager", "config"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cloud Parameter Stores

## Summary

Parameter stores — AWS SSM Parameter Store, Azure Key Vault, GCP Secret Manager — centralize configuration and secrets with encryption, access control, and versioning. They replace config files and env-var sprawl, but each has quirks: SSM's secret size and pricing, Key Vault's throttling, Secret Manager's cost per access.

## Details
- Mechanism: all three store key-value data (plaintext config, encrypted secrets), enforce IAM/RBAC access, and version values; AWS has Parameter Store (free, 4KB/8KB tiers, no native rotation) vs Secrets Manager (paid, 64KB, built-in rotation); Key Vault adds keys/certificates and throttling limits; Secret Manager integrates with KMS and has automatic rotation via functions/lambdas.
- Concrete example: a service reads its DB credentials at startup from Secret Manager with IAM-scoped access; a deployment pulls image tags from SSM parameters; a key-rotation schedule updates Key Vault with versioned secrets that apps resolve by label, avoiding config redeploys.
- Failure modes: secrets in plaintext parameter-store tiers (priced cheap, dangerous); access policies too broad (any lambda can read any secret); rotation without dependent-service coordination (apps caching old values break); throttling (Key Vault's default limits) under high-frequency reads; and secret sprawl when teams bypass the store for "speed".
- Operational tradeoffs: central stores trade a small dependency for auditability and rotation; the pattern is least-privilege per service, versioned secrets, and rotation tested in staging. Cache values with short TTLs to absorb throttling, and treat the store itself as crown-jewel infrastructure with locked-down control-plane access.
- RSIS3/mykb relevance: the wiki's deployments read configuration and secrets from a parameter store with per-service IAM; this note records the naming and rotation conventions the loop's tooling reuses.
- Secret rotation: automate rotation with a schedule and dependent-service coordination; a rotated secret no consumer knows about is an outage with good intentions. Version secrets by label so consumers resolve the current value without redeploys.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/aws-vpc-design|AWS VPC Design]]
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]]
- [[wiki/infrastructure/azure-synapse|Azure Synapse]]
