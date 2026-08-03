---
type: "concept"
title: "Environment Variable Management"
description: "Organizing env vars across local, CI, and production"
tags: ["env", "environment", "config", "twelve-factor"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Environment Variable Management

## Summary
Environment variable management covers where variables come from, how they are named, scoped, injected, and rotated across local, CI, and production. Poor env-var discipline produces configuration sprawl, secret leaks, and environment-specific bugs; good discipline treats env vars as a typed, documented, validated interface to the process.

## Details
- Naming and scoping: one prefix per app (e.g. `APP_DB_URL`), documented in `.env.example` or a config schema; separate per environment, per deployment, and per service so values cannot bleed across boundaries; CI variables, Kubernetes Secrets, and cloud secrets managers each have their own lifecycle.
- Validation: fail fast at startup — parse, type-check, and require every variable the app reads (pydantic settings, zod env, envsubst in entrypoints); a startup error beats a runtime null-pointer three hours later.
- Concrete example: a service that reads `DATABASE_URL` from the environment, validates it, and refuses to start without it; CI sets ephemeral values per pipeline run; production injects from Vault with rotation support; `printenv`-style debugging is replaced by a `--print-config` startup flag.
- Failure modes: secrets in env vars leaking via process listings, CI logs, or crash dumps (env is visible to any same-user process); shadowing — the same variable defined in shell, .env, and compose with different values; unset-variable crashes in one environment only; over-rotation breaking long-running processes that cached values at startup.
- Tradeoffs: env vars are simple and language-agnostic but untyped and hard to audit; file-based config and stores add tooling but enable validation and rotation; the operational sweet spot is env for bootstrap and small values plus a store for secrets and large config.
- Operational notes: keep a schema of all variables, audit them periodically, and rotate secrets on a schedule with a documented grace window.
- RSIS3 relevance: the wiki daemon and dashboard read env vars for ports and tokens — a documented, validated env contract keeps loop runs reproducible across machines.

## Related
- [[wiki/os-shell/logical-volume-management|Logical Volume Management]] — related coverage in the same cluster
- [[wiki/devops-infra/helm-and-chart-management|Helm & Chart Management]] — related coverage in the same cluster
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]] — related coverage in the same cluster
- [[wiki/infrastructure/security-information-and-event-management|SIEM]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
