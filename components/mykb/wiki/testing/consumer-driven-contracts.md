---
type: "concept"
title: "Consumer-Driven Contracts"
description: "Contracts authored by consumers that drive provider behavior"
tags: ["contract-testing", "testing", "pact", "microservices"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.pact.io/getting_started/terminology", "https://docs.pact.io/"]
---

# Consumer-Driven Contracts

## Summary
Consumer-driven contracts are authored by the consuming service and define exactly what it expects from a provider. Providers verify every consumer contract in CI, so changes that would break consumers fail the build before release.

## Details
- Pact flow: consumers write expectations as interactions, publish the pact file, and the provider replays and verifies.
- Consumer tests double as the integration contract; no shared test code is required.
- The Pact Broker stores pacts, tracks verification status, and can gate deployments.
- Matchers keep contracts tolerant by allowing dynamic values such as IDs and dates.
- Applies to REST, message queues, GraphQL, and gRPC consumers.
- Teams deploy consumer and provider independently instead of coordinating E2E environments.
- Provider teams own verification runs and communicate breaking changes through the broker.

## Related
- [[wiki/testing/contract-testing|Contract Testing]] — the broader practice this is a flavor of
- [[wiki/testing/service-virtualization|Service Virtualization]] — simulated providers for consumer tests
- [[wiki/testing/api-testing|API Testing]] — behavioral verification of endpoints
- [[wiki/api-protocols/openapi|OpenAPI]] — structural description of provider APIs
- [[wiki/testing/schema-contract-validation|Schema Contract Validation]] — payload shape enforcement
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — independent deployment enabled by contracts
