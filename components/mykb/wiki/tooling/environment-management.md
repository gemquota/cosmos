---
type: "concept"
title: "Environment Management"
description: "Running and controlling dev, staging, and production environments"
tags: ["environments", "deployment", "staging", "management"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Deployment_environment", "https://en.wikipedia.org/wiki/Software_environment"]
---

# Environment Management

## Summary
Environment management covers the lifecycle of the places software runs — dev, test, staging, production — their configuration, data, and promotion rules. The discipline is parity: environments that drift from production produce surprises at deploy time.

## Details
- Parity is the goal: same code, same config shape, and representative data so staging results transfer to production.
- Environment promotion moves artifacts, not builds: the same immutable artifact flows through each environment.
- Ephemeral environments (preview deploys per PR) give fast feedback without long-lived staging clutter.
- Configuration belongs in code and secrets in vaults; environment-specific values are the only drift allowed.
- Access control and data hygiene differ per environment: production is the one that matters.
- For the mykb bundle, environments are the staging wiki mirror and the production bundle — promoted by the same pipeline.
- Worked example — a PR opens an ephemeral wiki preview with a sample corpus; merge promotes the same bundle to staging, then production after the link-check gate.

Worked example — a PR opens an ephemeral wiki preview with a sample corpus; merge promotes the same bundle to staging, then production after the link-check gate.

## Related
- [[wiki/dev-tools/release-management|Release Management]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/devops-infra/ephemeral-environments|Ephemeral Environments]]
- [[wiki/tooling/platform-engineering|Platform Engineering]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/tooling/feature-flag-sdks|Feature Flag SDKs]]
- [[wiki/tooling/smoke-tests|Smoke Tests]]
- [[wiki/devops-infra/environment-promotion-models|Environment Promotion Models]]
