---
type: "concept"
title: "Stubbing"
description: "Returning canned responses from collaborators without verification"
tags: ["stubbing", "testing", "test-doubles", "determinism"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://sinonjs.org/how-to/stub/", "https://docs.pytest.org/en/stable/how-to/monkeypatch.html"]
---

# Stubbing

## Summary
Stubbing configures a collaborator to return canned responses without recording or verifying calls. It controls the environment, time, network, and random values, so the code under test behaves deterministically and error paths can be forced.

## Details
- Frameworks: Sinon stubs, Mockito when-thenReturn, and unittest.mock patch.
- Stubs excel at simulating error responses, timeouts, and rare states that are hard to produce live.
- No verification: a stub does not fail the test if unused; assertions target the system's output.
- Stub at the right seam: the port the code depends on, not the adapter's internals.
- Distinguish stub from mock: stubs answer, mocks verify; reach for the weaker tool first.
- Dynamic stubs can raise exceptions or return sequences to model stateful behavior.
- Keep stubbed values realistic so tests do not pass on impossible data.

## Related
- [[wiki/testing/test-doubles|Test Doubles]] — the family stubbing belongs to
- [[wiki/testing/mocking|Mocking]] — adds verification to scripted behavior
- [[wiki/testing/fakes|Fakes]] — realistic behavior without canned answers
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — tooling for configuring stubs
- [[wiki/testing/fault-injection|Fault Injection]] — forcing dependency failures on demand
- [[wiki/testing/negative-testing|Negative Testing]] — error paths stubs help exercise
