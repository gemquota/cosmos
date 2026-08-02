---
type: "concept"
title: "Cloud Emulators"
description: "Local software that mimics cloud services (S3, Lambda, Pub/Sub) for development and testing"
tags: ["emulators", "testing", "local-development", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://firebase.google.com/docs/emulator-suite", "https://cloud.google.com/functions/docs/local-development", "https://aws.amazon.com/serverless/sam/"]
---

# Cloud Emulators

## Summary
Cloud emulators replicate cloud service APIs locally — S3, Lambda, queues, databases — so developers and CI can test without cloud accounts or cost.

## Details
- Examples: LocalStack for AWS APIs, MinIO for S3, and emulator containers for GCP services.
- Emulators shine in CI: deterministic, fast, and free; real-cloud smoke tests still run on deploy.
- Fidelity gaps (latency, limits, auth) mean emulator-passing code can still fail in the cloud.
- Cloud emulators run local, in-process versions of cloud services so development can proceed without real cloud accounts, credentials, or network calls.
- They support fast iteration, offline development, and deterministic tests, but they are approximations — behavior gaps exist versus the real service.
- CI pipelines use emulators for integration tests, with a final verification against the real service before release.
- The tradeoff is fidelity: emulators may not enforce quotas, IAM, or eventual consistency exactly like production.
- **Worked example / comparison** — Worked example — a wiki backend test suite runs against the local emulator for storage and queues in CI, then a nightly job validates against the real cloud services.
- For mykb, cloud emulators are documented as the development-speed tool that keeps the wiki's cloud-backed tests hermetic.

## Related
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]]
- [[wiki/devops-infra/tfstate-management|Terraform State Management]]
- [[wiki/devops-infra/docker-compose|Docker Compose]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
