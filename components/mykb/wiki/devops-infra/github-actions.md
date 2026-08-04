---
type: "entity"
title: "GitHub Actions"
description: "Event-driven CI/CD platform running workflows on GitHub repositories for build, test, and deploy"
tags: ["github-actions", "ci-cd", "devops", "automation", "workflows"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://docs.github.com/en/actions"]
---

# GitHub Actions

## Summary
GitHub Actions is a CI/CD platform that runs workflows triggered by repository events — pushes, pull requests, schedules, or webhooks. Workflows are YAML files composed of jobs, steps, and reusable actions, executed on GitHub-hosted or self-hosted runners. It is the integration backbone for the cosmos repos and most open-source projects.

## Details
- Anatomy: `.github/workflows/*.yml` files with `on:` triggers, `jobs:` (parallel units), and `steps:` (commands or marketplace actions).
- Marketplace: community actions (checkout, setup-python, upload-artifact) are pinned by SHA for supply-chain hygiene.
- Environments and secrets: environments gate deploys with approvals; `secrets.*` injects vaulted values without exposing them in logs.
- Caching and artifacts: dependency caches speed runs; artifacts persist build outputs for release or SBOM attachment.
- Matrix builds: test across OS/version matrices (e.g. Python 3.11-3.13) in one workflow.
- Security: `pull_request_target` needs careful token scoping; untrusted PRs must run with read-only permissions (`permissions: contents: read`).
- Worked example: a cosmos workflow runs `okf validate` on the wiki, executes RSIS3's test suite, and deploys the dashboard to GitHub Pages on main — the existing `ci-cd-patterns` entity documents this pattern.

## Related
- [[wiki/security/supply-chain-security|Supply Chain Security]] — pin actions by SHA, scan dependencies
- [[wiki/security/secrets-management|Secrets Management]] — CI secret injection
- [[wiki/devops-infra/terraform|Terraform]] — plan/apply gated in workflows
- [[wiki/security/sbom|SBOM]] — generate and attach per build
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — existing pattern notes
- [[wiki/ops/gap-report|Gap Analysis Report]] — pipeline gaps tracked
- [[wiki/devops-infra/helm|Helm]] — CI deploys and upgrades charts
- [[wiki/devops-infra/kustomize|Kustomize]] — CI applies environment overlays
