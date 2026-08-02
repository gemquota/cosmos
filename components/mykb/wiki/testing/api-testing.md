---
type: "concept"
title: "API Testing"
description: "Testing REST and GraphQL endpoints for behavior, errors, and contracts"
tags: ["api-testing", "testing", "rest", "graphql"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learning.postman.com/docs/developing-apis/", "https://www.postman.com/use-cases/api-testing-automation/"]
---

# API Testing

## Summary
API testing verifies REST and GraphQL endpoints for behavior, validation, errors, and contracts, covering status codes, payloads, authentication, pagination, and rate limits. It is fast, precise, and the backbone of backend quality.

## Details
- Tools: Postman, curl, Karate, pytest with requests, Supertest, and Schemathesis.
- Assert status codes, response schemas, headers, error shapes, idempotency, and ordering.
- Test matrix: happy paths, validation errors, auth failures, edge payloads, and large inputs.
- Contract and schema tests formalize shape; API tests exercise behavior.
- GraphQL: test queries, mutations, fragments, and error paths.
- Automate in CI as integration tests; keep collections version-controlled.
- Include security cases: authentication, authorization, rate limits, and injection.

## Related
- [[wiki/testing/contract-testing|Contract Testing]] — agreements API tests validate
- [[wiki/testing/schema-contract-validation|Schema Contract Validation]] — payload shape checks
- [[wiki/testing/authentication-testing|Authentication Testing]] — auth flows in API suites
- [[wiki/api-protocols/rest-apis|REST APIs]] — the interaction style under test
- [[wiki/api-protocols/graphql|GraphQL]] — query language API tests cover
- [[wiki/api-protocols/openapi|OpenAPI]] — describing the API surface
