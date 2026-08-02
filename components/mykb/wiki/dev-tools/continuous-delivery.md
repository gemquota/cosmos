---
type: "concept"
title: "Continuous Delivery"
description: "Keeping every change releasable through automated, production-like pipelines"
tags: ["cd", "delivery", "pipeline", "releasability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Continuous_delivery", "https://dora.dev/"]
---

# Continuous Delivery

## Summary
Continuous delivery keeps software permanently releasable: every change that passes automated verification could ship to production at the push of a button. It decouples deployment from release, so shipping is a business decision rather than a technical ordeal.

## Details
- The pipeline runs automated build, test, and staging deployments; the final production push may be manual or automatic.
- Deployability is a design goal: feature flags, backward-compatible schemas, and rollback paths keep changes safe to release.
- DORA links continuous delivery to higher deployment frequency and lower change failure rates.
- CD requires trust in automation — if the pipeline is flaky, humans bypass it and the guarantee collapses.
- Environment parity (staging mirrors production) is what makes pipeline green meaning releasable.
- For the mykb bundle, CD means every merge produces a verified, tagged bundle that can be published on demand.

Worked example — a wiki pipeline builds the bundle, runs link verification, deploys to a staging mirror, and reports a green status. Publishing is a single approval that promotes the staged bundle to the live wiki.

## Related
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/dev-tools/continuous-deployment|Continuous Deployment]]
- [[wiki/dev-tools/release-management|Release Management]]
- [[wiki/dev-tools/canary-releases|Canary Releases]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/tooling/environment-management|Environment Management]]
- [[wiki/tooling/progressive-delivery|Progressive Delivery]]
- [[wiki/tooling/smoke-tests|Smoke Tests]]
- [[wiki/devops-infra/continuous-delivery-pipelines|Continuous Delivery Pipelines]]
- [[wiki/devops-infra/environment-promotion-models|Environment Promotion Models]]
