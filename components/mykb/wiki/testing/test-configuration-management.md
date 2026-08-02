---
type: "concept"
title: "Test Configuration Management"
description: "Managing env vars, profiles, and settings across test runs"
tags: ["test-configuration", "testing", "environment", "reproducibility"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.pytest.org/en/stable/reference/customize.html", "https://12factor.net/config"]
---

# Test Configuration Management

## Summary
Test configuration management controls environment variables, profiles, and settings across test runs, defining what each environment enables and keeping runs reproducible. Configuration drift silently changes what a test means.

## Details
- Sources: environment variables, config files, feature flags, and dev, staging, or production profiles.
- Twelve-factor config keeps environment variables explicit and versioned.
- Record which configuration a run used; store it in test artifacts for debugging.
- Pin feature-flag states per run; tests must not inherit unknown flags.
- Inject secrets through secret managers and CI, never by committing them.
- Document configuration contracts; fail fast on unknown or unset variables.
- Reproducibility: the same config and code must produce the same behavior.

## Related
- [[wiki/testing/test-environments|Test Environments]] — where configuration applies
- [[wiki/testing/test-data-management|Test Data Management]] — data configuration alongside settings
- [[wiki/devops-infra/feature-flags|Feature Flags]] — flag states pinned per run
- [[wiki/testing/ephemeral-environments|Ephemeral Environments]] — per-branch configuration
- [[wiki/testing/test-isolation|Test Isolation]] — config state must not leak
- [[wiki/software-engineering/architecture-decision-records|Architecture Decision Records]] — documenting config decisions
