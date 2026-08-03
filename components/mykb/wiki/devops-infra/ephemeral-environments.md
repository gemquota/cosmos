---
type: "concept"
title: "Ephemeral Environments"
description: "Short-lived preview environments created per branch or PR"
tags: ["ephemeral", "environments", "preview", "dev"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Ephemeral Environments

## Summary
Ephemeral environments are short-lived, on-demand copies of the stack created per PR or branch and destroyed automatically. They give every change a realistic staging surface — same images, same services, same data shape — without the cost and drift of long-lived shared staging environments.

## Details
- Mechanism: a trigger (PR opened, commit pushed) provisions the environment from the branch's images and config; a scheduler or CI job tears it down on merge or inactivity; dynamic DNS and routing map each PR to its environment; databases are seeded from sanitized production snapshots or migrations.
- Concrete example: a preview platform (Vercel previews, Gitpod, Kubernetes namespace-per-PR) creates `pr-123.app.example.com` with its own backend; the PR description links the live preview; reviewers and automated E2E tests run against it; after merge, the namespace and its resources are deleted.
- Failure modes: environment drift — previews that differ from production (different data, different env vars) and give false confidence; resource exhaustion when many PRs each run a full stack (use shared services, thin clones, or spot scheduling); stateful environments that cannot be torn down cleanly, leaking cost; database seeds that are stale or contain PII, requiring sanitization.
- Tradeoffs: ephemeral environments multiply infrastructure spend and pipeline complexity but collapse the feedback loop and remove staging contention; the alternative — one shared staging env — serializes testing and accumulates drift; the middle ground provisions ephemeral environments only for risky or high-traffic changes.
- Operational notes: set TTL-based cleanup, monitor environment count and cost, and make environment URLs and status visible in the PR.
- Cost shape: namespace-per-PR with shared Redis and object storage keeps each preview cheap, but set namespace quotas so a PR burst cannot exhaust cluster capacity.
- RSIS3 relevance: the cosmos dashboard's preview environment per change mirrors RSIS3's experimental principle — try changes in an isolated, disposable copy before promoting to the live wiki.

## Related
- [[wiki/shell-environment/shell-environments-and-rc-files|Shell Environments & RC Files]]
- [[wiki/devops-infra/development-environments-as-code|Development Environments as Code]]
- [[wiki/infrastructure/data-environments-dev-staging-prod|Data Environments Dev Staging Prod]]
