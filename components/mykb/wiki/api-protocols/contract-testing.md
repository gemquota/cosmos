---
type: "concept"
title: "Contract Testing"
description: "Consumer-driven contract verification"
tags: ["contract-testing", "testing", "consumer-driven", "api-testing", "microservices"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.pact.io/", "https://martinfowler.com/articles/consumerDrivenContracts.html"]
---

# Contract Testing

## Summary
Contract testing verifies that an API provider and its consumers agree on the wire contract — request shapes, response shapes, and status semantics — without running the whole system. Consumer-driven contracts (Pact) capture each consumer's expectations and play them back against the provider, catching breaking changes before deploy.

## Details
- The idea: a contract is a pact of expectations — the consumer records what it calls and expects; the provider runs those expectations as tests.
- Consumer side: a Pact test drives the consumer's real client against a mock provider and publishes the resulting contract.
- Provider side: the provider replays all consumer contracts (via a broker) against its real implementation, proving compatibility.
- Versioning: contracts are versioned and tagged (main, prod); providers must pass contracts for all consumers in production before releasing.
- Granularity: contract tests sit between unit tests and E2E — they test agreement, not behavior, so they are fast and deterministic.
- Beyond REST: Pact supports HTTP, gRPC, and message/event contracts (queues), matching modern polyglot stacks.
- Pitfalls: contracts drift when consumers do not update them, and a monolithic provider with many consumers needs CI to run the whole suite.

## Related
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]] — contracts encode compatibility rules
- [[wiki/api-protocols/api-design-first|Design-First APIs]] — spec-first feeds contract generation
- [[wiki/testing/golden-tests|Golden Tests]] — snapshot-style verification at the message level
- [[wiki/api-protocols/openapi|OpenAPI]] — the shared contract source for REST
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — errors are part of the contract
