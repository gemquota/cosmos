---
type: "concept"
title: "Preview Environments"
description: "Full-stack environments attached to pull requests"
tags: ["preview", "environments", "pull-requests", "dev"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Preview Environments

## Summary
Preview environments are short-lived deployments of a branch or PR, reachable at a unique URL, used for review and testing before merge. They bring production-like verification to the pull-request stage — reviewers click through real UI, E2E tests run against real backends — instead of relying on local runs and faith.

## Details
- Mechanism: a trigger (PR opened/updated) provisions the environment from the branch's images and config; dynamic routing maps a URL to it; databases are seeded from sanitized snapshots or migrations; the environment is destroyed on merge or after inactivity; the pipeline reports environment status and URL in the PR.
- Concrete example: a preview platform creates `pr-42.app.example.com` with its own API and database; the PR description links it; automated E2E tests run against it in parallel with human review; after merge, a cleanup job deletes the namespace and resources.
- Failure modes: drift from production — previews with different env vars, data, or feature flags produce false confidence; resource exhaustion when every PR runs a full stack (share services, thin clones, spot instances); stateful previews that leak or accumulate cost; seed data containing PII requiring sanitization; environments that are broken at creation and ignored, so reviewers test nothing.
- Tradeoffs: previews shorten feedback loops and remove staging contention but multiply infrastructure cost and pipeline complexity; the alternative — a shared staging environment — serializes testing and drifts; the pragmatic pattern is previews for risky or UI-heavy changes and shared staging for the rest.
- Operational notes: enforce TTL cleanup, monitor environment counts and cost, and make environment status visible in the PR itself.
- RSIS3 relevance: the cosmos dashboard previews per change fit RSIS3's experimental philosophy — validate in an isolated, disposable copy before promoting to the live wiki.

## Related
- [[wiki/shell-environment/shell-environments-and-rc-files|Shell Environments & RC Files]] — related coverage in the same cluster
- [[wiki/devops-infra/ephemeral-environments|Ephemeral Environments]] — related coverage in the same cluster
- [[wiki/devops-infra/development-environments-as-code|Development Environments as Code]] — related coverage in the same cluster
- [[wiki/infrastructure/data-environments-dev-staging-prod|Data Environments Dev Staging Prod]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
