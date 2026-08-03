---
type: "concept"
title: "Development Environments as Code"
description: "Declaring dev environments with devcontainers and scripts"
tags: ["dev-environments", "devcontainer", "as-code", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Development Environments as Code

## Summary
Development environments as code means every environment — local, preview, staging — is defined in the repository as declarative configuration (Docker Compose, devcontainers, Terraform modules, environment manifests) rather than assembled by hand. The environment becomes reviewable, reproducible, and promotable like the application code it hosts.

## Details
- Mechanism: a single source of truth describes the stack (services, dependencies, ports, secrets references); local tooling (compose, devcontainer, tilt) instantiates it; CI and preview platforms instantiate the same definition; drift between environments becomes a diff rather than a mystery.
- Concrete example: `docker-compose.yml` defining app, database, and cache for local development; the same services defined in the staging Terraform module; a preview environment created per PR from the same image and config; a schema migration scripted into every environment creation so parity holds.
- Failure modes: environment definitions that diverge from production (a local-only mock that hides integration bugs); secret handling that leaks or blocks environment bring-up; resource blowups when every PR preview runs a full stack; drift when environments are mutated by hand instead of recreated; version skew between the environment config and the app expecting it.
- Tradeoffs: environments-as-code shifts work into maintaining declarative definitions but makes onboarding and parity dramatically better; the cost is complexity — multi-service definitions, service discovery, and stateful dependencies need careful design; ephemeral, recreatable environments trade away long-lived state by design.
- Operational notes: test environment definitions in CI, recreate environments from scratch regularly to prove reproducibility, and gate environment changes through review like code changes.
- RSIS3 relevance: the cosmos repo's components (RSIS3, MyKB, SPACE) benefit from one declarative environment definition so every loop experiment runs against the same stack, making results comparable.

## Related
- [[wiki/devops-infra/infrastructure-as-code-revisited|Infrastructure as Code]] — related coverage in the same cluster
- [[wiki/shell-environment/shell-environments-and-rc-files|Shell Environments & RC Files]] — related coverage in the same cluster
- [[wiki/devops-infra/gatekeeper-and-policy-as-code|Gatekeeper & Policy as Code]] — related coverage in the same cluster
- [[wiki/devops-infra/configuration-as-data|Configuration as Data]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
