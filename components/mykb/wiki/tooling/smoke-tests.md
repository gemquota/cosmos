---
type: "concept"
title: "Smoke Tests"
description: "Quick sanity checks that a deploy is alive and basically working"
tags: ["smoke-tests", "deployment", "testing", "verification"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Smoke Tests

## Summary
Smoke tests are fast, shallow checks that run right after a deploy — the service starts, the health endpoint responds, a key flow works. They catch broken deploys in seconds, before deep test suites run.

## Details
- Run against the deployed environment, not just CI; they verify packaging and config too.
- A few minutes of smoke beats ten minutes of deep suite: order matters.
- Include a write path (or a read-only variant) so DB connectivity is actually proven.
- mykb relevance: post-sync smoke checks confirm the wiki index rebuilt and links resolve.

## Related
- [[wiki/testing/smoke-testing|Smoke Testing]]
- [[wiki/devops-infra/health-endpoint-contracts|Health Endpoint Contracts]]
- [[wiki/devops-infra/deployment-verification-synthetic-checks|Deployment Verification]]
- [[wiki/dev-tools/continuous-deployment|Continuous Deployment]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
