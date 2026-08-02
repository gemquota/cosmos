---
type: "concept"
title: "Ephemeral Environments"
description: "On-demand per-branch environments for integration and preview testing"
tags: ["ephemeral-environments", "testing", "preview", "ci"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://vercel.com/docs/deployments/preview-environments", "https://www.netlify.com/products/deploy/"]
---

# Ephemeral Environments

## Summary
Ephemeral environments spin up on demand per branch or pull request, full app stacks with preview URLs, and tear down when merged. They give realistic integration feedback before code lands.

## Details
- Providers: Vercel previews, Netlify deploys, GitHub Codespaces, Kubernetes namespaces, and docker-compose stacks.
- Each PR gets isolated services and a seeded database; teardown is automatic.
- Great for manual review, E2E runs, and stakeholder demos.
- Cost and quota management: auto-expire idle environments and cap concurrent stacks.
- Integrate with CI: deploy preview, run E2E, and report links in PR comments.
- Secrets and permissions must be scoped per environment.
- Parity with staging and production keeps previews trustworthy.

## Related
- [[wiki/testing/test-environments|Test Environments]] — the lifecycle ephemeral stacks fit
- [[wiki/testing/containerized-test-environments|Containerized Test Environments]] — container-based ephemeral stacks
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — preview validation in CI
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — journeys against preview URLs
- [[wiki/devops-infra/github-actions|GitHub Actions]] — triggering preview deployments
- [[wiki/devops-infra/terraform|Terraform]] — provisioning ephemeral infrastructure
