---
type: "concept"
title: "Project Scaffolding"
description: "Creating the initial structure of a project from a template so every start follows the same golden path"
tags: ["tooling", "templates", "onboarding", "dx"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Project Scaffolding

## Summary
Scaffolding generates the skeleton of a new project — config, folders, CI, tests — from a maintained template. It encodes the team's conventions so that every project starts consistent.

## Details
- Tools range from framework CLIs (create-next-app) to Cookiecutter, Copier, and Yeoman.
- Templates need versioning and review; a stale template propagates bad defaults.
- RSIS3 relevance: new wiki areas and article types deserve their own scaffolds.

## Related
- [[wiki/software-engineering/developer-experience|Developer Experience]] — scaffolding is the first DX touchpoint
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — workspaces make per-package scaffolding uniform
- [[wiki/dev-tools/devcontainers|Devcontainers]] — scaffolded environments include dev setups
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]] — scaffolding plus docs completes onboarding
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — scaffolds ship with pipeline config
