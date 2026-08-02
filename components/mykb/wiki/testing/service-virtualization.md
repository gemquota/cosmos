---
type: "concept"
title: "Service Virtualization"
description: "Simulating unavailable third-party services at the network level"
tags: ["service-virtualization", "testing", "mocking", "third-party"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://wiremock.org/", "https://www.mbtest.org/"]
---

# Service Virtualization

## Summary
Service virtualization simulates unavailable, expensive, or unstable third-party services at the network level, returning recorded or scripted responses. It lets teams test against realistic dependencies without the real endpoint being reachable.

## Details
- Tools: WireMock, Mountebank, Hoverfly, and cloud API mocks.
- Record real traffic by proxying to build realistic stubs, then script edge cases on top.
- Differs from in-process doubles: virtualization sits at the HTTP boundary, so code paths stay real.
- Use for payment gateways, auth providers, mainframe APIs, and external SaaS.
- Stateful scenarios model sequences, delays, and failures to mimic real behavior.
- Risk: drift from the live API; refresh recordings and keep contract tests against the real provider.
- Combine with consumer-driven contracts so virtualized services stay honest.

## Related
- [[wiki/testing/fakes|Fakes]] — in-process alternatives to network virtualization
- [[wiki/testing/contract-testing|Contract Testing]] — keeps virtualized services honest
- [[wiki/testing/consumer-driven-contracts|Consumer-Driven Contracts]] — consumer expectations for stubbed providers
- [[wiki/testing/test-environments|Test Environments]] — where virtualized services run
- [[wiki/testing/api-testing|API Testing]] — behavioral checks against virtualized endpoints
- [[wiki/testing/containerized-test-environments|Containerized Test Environments]] — running virtualized services in CI
