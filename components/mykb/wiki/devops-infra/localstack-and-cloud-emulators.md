---
type: "concept"
title: "LocalStack & Cloud Emulators"
description: "Emulating cloud services locally for development and tests"
tags: ["localstack", "emulator", "cloud", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# LocalStack & Cloud Emulators

## Summary
LocalStack and cloud emulators run mock implementations of cloud services (S3, DynamoDB, SQS, Lambda, and hundreds more) on a developer machine or in CI, letting code that calls cloud APIs run and be tested without a cloud account. They trade fidelity for speed, cost, and determinism.

## Details
- Mechanism: LocalStack exposes a single endpoint that emulates AWS APIs over HTTP; SDKs point at it via endpoint override or environment variables; services emulate behavior (buckets, tables, queues) in a local container, including some advanced features (Lambda execution, SQS visibility timeouts); the emulator state persists across runs via a volume or resets per test.
- Concrete example: CI runs integration tests against LocalStack for a service that uploads to S3 and reads from DynamoDB — no AWS account, no network, no cost; a developer runs the same stack locally with `docker compose`; tests assert on object contents and table rows exactly as against the real API.
- Failure modes: fidelity gaps — emulated semantics differ from AWS (eventual consistency timing, IAM enforcement, throttling), so code that passes locally can fail in the cloud; emulator-only bugs where a missing emulated feature forces workarounds that become permanent; state leaks between tests when the emulator is not reset; version mismatch between the emulator and the SDK/API version the code targets.
- Tradeoffs: emulators give fast, cheap, hermetic tests but cannot replace the real service for contract and behavior validation — schedule periodic live-cloud test runs; the alternative is a sandbox cloud account, which is realistic but slow, costly, and non-deterministic.
- Operational notes: pin the emulator version, reset state between tests, and mark emulator-only assumptions in code.
- RSIS3 relevance: cosmos can use emulators to test the wiki daemon's cloud integrations (object storage backup, static hosting) in CI, reserving real-cloud runs for acceptance.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]] — related coverage in the same cluster
- [[wiki/cloud-infra/multi-cloud-hybrid-cloud|Multi-Cloud & Hybrid Cloud]] — related coverage in the same cluster
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]] — related coverage in the same cluster
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
