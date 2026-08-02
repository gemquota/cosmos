---
type: "concept"
title: "Test Environments"
description: "Managing dev, staging, and prod-like environments for reliable testing"
tags: ["test-environments", "testing", "staging", "parity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/test-environment", "https://docs.github.com/en/actions/deployment/targeting-different-environments"]
---

# Test Environments

## Summary
Test environments, dev, staging, and prod-like, give tests realistic infrastructure: services, databases, and configuration. Environment mismatch is a top cause of the works-in-CI-fails-in-prod problem.

## Details
- Environment types: local, CI, shared staging, preview or ephemeral, and production-like.
- Parity: versions, configuration, feature flags, data scale, and network topology.
- Staging should mirror production: same services, env vars, and deployment process.
- Manage configuration with env vars and profiles; never hardcode secrets.
- Ephemeral environments per branch reduce contention and drift.
- Production testing, canaries and smoke, complements staging for final validation.
- Track environment drift and rotate credentials regularly.

## Related
- [[wiki/testing/ephemeral-environments|Ephemeral Environments]] — on-demand per-branch stacks
- [[wiki/testing/containerized-test-environments|Containerized Test Environments]] — reproducible infrastructure
- [[wiki/testing/test-configuration-management|Test Configuration Management]] — env config across environments
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — environments gates deploy to
- [[wiki/testing/test-data-management|Test Data Management]] — data parity across environments
- [[wiki/devops-infra/feature-flags|Feature Flags]] — flag states per environment
