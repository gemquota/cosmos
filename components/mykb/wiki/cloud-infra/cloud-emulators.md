---
type: "concept"
title: "Cloud Emulators"
description: "Local software that mimics cloud services (S3, Lambda, Pub/Sub) for development and testing"
tags: ["emulators", "testing", "local-development", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Cloud Emulators

## Summary
Cloud emulators replicate cloud service APIs locally — S3, Lambda, queues, databases — so developers and CI can test without cloud accounts or cost.

## Details
- Examples: LocalStack for AWS APIs, MinIO for S3, and emulator containers for GCP services.
- Emulators shine in CI: deterministic, fast, and free; real-cloud smoke tests still run on deploy.
- Fidelity gaps (latency, limits, auth) mean emulator-passing code can still fail in the cloud.

## Related
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — serverless functions tested locally
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]] — IaC validated against emulated clouds
- [[wiki/devops-infra/tfstate-management|Terraform State Management]] — local state for emulated providers
- [[wiki/devops-infra/docker-compose|Docker Compose]] — running emulator stacks locally
