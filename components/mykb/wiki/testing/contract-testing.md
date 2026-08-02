---
type: "concept"
title: "Contract Testing"
description: "Verifying provider and consumer agreements between services"
tags: ["contract-testing", "testing", "microservices", "pact"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.pact.io/", "https://spring.io/projects/spring-cloud-contract"]
---

# Contract Testing

## Summary
Contract testing verifies that a service provider and its consumers agree on message shapes, requests, responses, and events, by running each side against recorded contracts. It catches breaking API changes before deployment without standing up the full stack.

## Details
- Main tools: Pact for consumer-driven flows and Spring Cloud Contract for provider-authored contracts.
- Providers publish contracts; consumers verify their expectations against them.
- Faster and more deterministic than E2E: each service verifies independently.
- Versioned contracts plus provider verification in CI prevent surprise breakage.
- Contracts cover request and response schemas, headers, status codes, and example values.
- Works for REST, GraphQL, message queues, and gRPC integrations.
- Schema validation is a static check; contracts add behavioral examples on top.

## Related
- [[wiki/testing/consumer-driven-contracts|Consumer-Driven Contracts]] — contracts authored by consumers
- [[wiki/testing/schema-contract-validation|Schema Contract Validation]] — structural guarantees under contracts
- [[wiki/testing/api-testing|API Testing]] — behavioral checks alongside contracts
- [[wiki/api-protocols/openapi|OpenAPI]] — describing the contract surface
- [[wiki/api-protocols/rest-apis|REST APIs]] — the interaction style most contracts cover
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — why contract testing matters at scale
