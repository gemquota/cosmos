---
type: "concept"
title: "Integration Testing"
description: "Verifying interactions between modules and their real collaborators"
tags: ["integration-testing", "testing", "collaborators", "testcontainers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://java.testcontainers.org/", "https://docs.docker.com/get-started/"]
---

# Integration Testing

## Summary
Integration tests verify that modules work together against real collaborators, such as databases, message brokers, and HTTP services, inside a contained environment. They catch contract and configuration mismatches that mocks cannot, because doubles only approximate real behavior.

## Details
- Scope: at minimum two real components, for example service plus database, queue, or API client plus server.
- Infrastructure: Testcontainers and docker-compose spin up disposable Postgres, Kafka, or Redis instances per run.
- Slower than unit tests, so keep the suite lean and parallelize across services.
- Common catches: SQL dialect differences, serialization mismatches, transaction boundaries, and timezone bugs.
- HTTP integrations: run against real network boundaries; record-and-replay proxies are a middle ground.
- Assert observable side effects, such as a row written or a message enqueued, in addition to return values.
- Run in CI against a dedicated environment seeded with known data, cleaned up per test.

## Related
- [[wiki/testing/unit-testing|Unit Testing]] — the fast layer above which integration tests sit
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — full-stack journeys beyond integration scope
- [[wiki/testing/contract-testing|Contract Testing]] — locks service-to-service agreements
- [[wiki/testing/containerized-test-environments|Containerized Test Environments]] — how real collaborators are provisioned
- [[wiki/testing/database-seeding|Database Seeding]] — known initial state for integration runs
- [[wiki/testing/test-environments|Test Environments]] — where integration suites execute
