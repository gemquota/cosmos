---
type: "concept"
title: "Smoke Testing"
description: "Quick shallow checks that core functionality survives a build or deploy"
tags: ["smoke-testing", "testing", "deployment", "release"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.github.com/en/actions", "https://www.ibm.com/topics/smoke-testing"]
---

# Smoke Testing

## Summary
Smoke tests are shallow, fast checks that the core path of a build or deployment still works, such as the app booting, the main page loading, and the health endpoint responding. They are the first gate after deploy and catch environment breakage before deeper testing begins.

## Details
- Deploy pipeline: run smoke tests immediately after release against the target environment.
- Typical checks: process starts, configuration loads, database connectivity, and a 200 on health or homepage.
- Keep the suite minutes long; every failure should be diagnosable in seconds.
- Stronger than health checks: smoke tests assert behavior, not just liveness.
- Tooling: Playwright for browser smoke, HTTP assertions for API smoke, custom deploy scripts.
- On failure, halt the pipeline and roll back or auto-revert the release.
- Reuse the same smoke set across staging and production for parity.

## Related
- [[wiki/testing/recovery-testing|Recovery Testing]] — deeper failure handling beyond the smoke gate
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — smoke tests run as a deploy gate
- [[wiki/api-protocols/health-checks|Health Checks]] — liveness signals smoke tests extend
- [[wiki/devops-infra/rollback-plans|Rollback Plans]] — what happens when smoke fails
- [[wiki/devops-infra/release-trains|Release Trains]] — smoke tests gate each release
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — fuller journeys after smoke passes
