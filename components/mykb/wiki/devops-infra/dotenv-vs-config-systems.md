---
type: "concept"
title: "dotenv vs Config Systems"
description: "Flat .env files versus structured config services"
tags: ["dotenv", "config", "environment", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# dotenv vs Config Systems

## Summary
dotenv files and full configuration systems solve adjacent problems: .env keeps twelve-factor config in a flat file for local development, while config systems (Vault, Consul, AWS AppConfig, Kubernetes ConfigMaps/Secrets) manage config across environments with rotation, versioning, and audit. The choice is between simplicity for local dev and governance for production.

## Details
- dotenv mechanics: a `.env` file holds `KEY=value` pairs loaded into the process environment by the runtime or a loader (python-dotenv, dotenv-cli); it is local-only, committed-never, and trivially understandable; values can reference other values and comments document intent.
- Config-system mechanics: centralized stores serve config over an API or filesystem mount with versions, change history, access control, and dynamic reload; secrets are separated from non-secret config; rotation and rollback are first-class operations.
- Concrete example: developers run with `.env` overrides; CI injects values from the secret store; production reads from Vault or a mounted Secret that the app watches for changes; a config diff is reviewed in the store's UI or via git-backed values before promotion.
- Failure modes: committing `.env` files leaks secrets (gitignore and secret scanning are mandatory); environment variables that silently shadow each other (shell env beats .env, or vice versa) causing "works locally" bugs; config systems that become a second source of truth that drifts from the repo; dynamic reload surprises where a config change propagates to some instances but not others.
- Tradeoffs: dotenv is zero-infrastructure but has no audit, rotation, or versioning; config systems add infrastructure and operational complexity in exchange for governance; the common split is .env for local ergonomics plus a real config system for everything shared.
- Operational notes: keep `.env.example` as the documented contract, load order explicit, and treat secrets strictly via the store.
- RSIS3 relevance: RSIS3's local runs can use dotenv for developer ergonomics while production configuration (daemon tokens, dashboard endpoints) belongs in the config system layer.

## Related
- [[wiki/os-shell/systemd-and-init-systems|systemd & Init Systems]]
- [[wiki/infrastructure/intrusion-detection-systems|Intrusion Detection Systems]]
- [[wiki/devops-infra/feature-flag-systems-revisited|Feature Flag Systems]]
