---
type: "concept"
title: "Smoke Tests After Deploy"
description: "Fast end-to-end sanity checks run on each release"
tags: ["smoke-test", "deployment", "testing", "ci"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Smoke Tests After Deploy

## Summary
Smoke tests after deploy are quick, shallow checks that the new version actually works in the environment it was deployed to: the service starts, key endpoints respond, the database is reachable, and critical flows complete. They catch deployment-time failures — wrong config, missing secrets, failed migrations — before real traffic arrives.

## Details
- Mechanism: after the rollout, a suite of lightweight checks runs against the deployed version: health endpoints, a couple of real requests, a minimal write/read to the database, and a representative user flow; failures stop promotion or trigger rollback; results feed the deployment pipeline and dashboards.
- Concrete example: a deploy pipeline calls the readiness endpoint, asserts a 200 on a public route, creates and fetches a record, and verifies the version header matches the deployed tag; a failure auto-reverts to the previous version and pages the team; the same smoke suite runs on each environment after every promotion.
- Failure modes: smoke tests that bypass the real stack (checking a static file instead of the served app); tests that mutate production data without cleanup; test accounts or seed data expiring and causing false failures; smoke suites that are really full regression tests, taking too long and being skipped; tests that pass in the pipeline but not against the live environment (network, DNS, CDN caching).
- Tradeoffs: smoke tests are cheap, fast insurance against deployment-day surprises, but they only sample the surface — the alternative, deeper verification, costs time and risks flakiness; the mature pattern is a small, reliable smoke suite as a hard gate plus synthetic monitoring for ongoing coverage.
- Operational notes: keep the smoke suite small and stable, run it synchronously in the release pipeline, and review every false failure.
- RSIS3 relevance: after cosmos regenerates its dashboard or upgrades the daemon, a smoke check of the published pages and store endpoints verifies the artifact pipeline end to end.

## Related
- [[wiki/devops-infra/deploy-safety-checks|Deploy Safety Checks]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
