---
type: "concept"
title: "Fault Injection"
description: "Inducing errors in dependencies to verify graceful handling"
tags: ["fault-injection", "testing", "resilience", "error-paths"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://istio.io/latest/docs/tasks/traffic-management/fault-injection/", "https://toxiproxy.readthedocs.io/"]
---

# Fault Injection

## Summary
Fault injection induces errors in dependencies, network failures, timeouts, corrupted payloads, and crashing services, to verify the system handles them gracefully. It is the systematic way to test error paths that rarely occur naturally.

## Details
- Layers: network via toxiproxy or tc netem, service via chaos tools, and code via injectable error factories.
- Test targets: retry logic, circuit breakers, fallbacks, queues, and user-facing error responses.
- Combine with negative tests: injected faults assert the error response contract.
- Timeouts and partial failures are the hardest to reproduce; inject them deliberately.
- Integration testing with fault injection proves resilience features actually work.
- Adopt fault injection in CI for critical paths and chaos for production-scale effects.
- Log and report injected faults so test results stay interpretable.

## Related
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — production-scale failure injection
- [[wiki/testing/negative-testing|Negative Testing]] — invalid inputs and error handling
- [[wiki/testing/recovery-testing|Recovery Testing]] — recovery after injected faults
- [[wiki/api-protocols/retry-backoff|Retry Backoff]] — behavior faults exercise
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — the pattern faults should trip
- [[wiki/testing/service-virtualization|Service Virtualization]] — scripting faulty dependencies
