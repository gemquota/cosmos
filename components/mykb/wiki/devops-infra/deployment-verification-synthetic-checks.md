---
type: "concept"
title: "Deployment Verification & Synthetic Checks"
description: "Post-deploy checks that prove the service actually works"
tags: ["synthetic", "verification", "deployment", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Deployment Verification & Synthetic Checks

## Summary
Synthetic checks verify deployments by probing the system as a user would, from outside: HTTP status, JSON shape, latency, and critical flows. Because they are scripted and deterministic, they can run the moment a deploy completes — before real users arrive — and continuously afterward to catch regressions.

## Details
- Mechanism: a probe executes a scripted request or flow against the deployed environment and asserts on response; probes run from outside the cluster (public URL, API endpoint, or browser automation) so they test the full path: DNS, ingress, app, database; results feed the deploy pipeline and dashboards; frequency scales from one-shot post-deploy to continuous every-minute monitoring.
- Concrete example: after a deploy, a probe asserts `GET /health` returns 200 with `{"status":"ok"}`, a login flow succeeds, and a checkout completes with a test card; the same probe runs every minute in production; latency and error-rate assertions trip alerts; Playwright or curl-based scripts parameterized per environment.
- Failure modes: synthetic tests diverging from real user behavior (they pass while users fail) — keep them end-to-end and realistic; probes hammering the system (thundering herd at deploy time) or tripping their own alerts; tests depending on mutable state (test accounts locked, seeded data deleted) causing false failures; probe endpoints that bypass the real stack, verifying nothing.
- Tradeoffs: synthetics are deterministic and catch deploy-time breakage early, but they cannot cover the long tail of real-user paths — combine with real-user monitoring and error budgets; they cost infrastructure and maintenance, so keep a small, high-value suite rather than exhaustive coverage.
- Operational notes: run post-deploy synthetics synchronously in the release pipeline, keep credentials for probes in a vault, and make probe failures page the right team.
- RSIS3 relevance: after RSIS3 regenerates its dashboard or upgrades the wiki daemon, a synthetic check of the published pages verifies the artifact pipeline end to end.

## Related
- [[wiki/devops-infra/deploy-safety-checks|Deploy Safety Checks]] — related coverage in the same cluster
- [[wiki/devops-infra/preflight-checks-and-guards|Preflight Checks & Guards]] — related coverage in the same cluster
- [[wiki/infrastructure/data-deployment-strategies|Data Deployment Strategies]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
