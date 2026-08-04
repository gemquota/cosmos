---
type: "entity"
title: "E2E Test"
description: "E2E test: full-journey verification through the real system stack"
tags: ["test", "entity", "e2e", "verification"]
timestamp: "2026-07-21T12:06:50Z"
---

# E2E Test

## Summary

An end-to-end (E2E) test exercises a complete user journey through the real system, from interface to backend to data store. Unlike unit tests, it validates the integration of all parts. E2E tests matter because they catch the cross-component failures that unit tests systematically miss. For agentic systems, the same full-stack discipline applies to protocol runs and their artifacts.

## Details

- **Definition** — An E2E test drives the system the way a user does, asserting on observable outcomes across the full stack.
- **Journey design** — Tests are built around real user goals, such as signing in and retrieving a record, rather than isolated functions.
- **Integration value** — E2E tests verify contracts between UI, API, and persistence layers, where integration bugs actually live.
- **Environment fidelity** — Tests are only as good as their environment; staging data and service variants must match production closely.
- **Stability** — Flakiness from timing, network, and shared state is the main cost; retries, wait strategies, and isolated data help.
- **Test pyramid** — A few E2E tests atop many unit and integration tests balances coverage against runtime cost.
- **Failure modes** — Brittle selectors, environment drift, and slow suites discourage maintenance and breed false failures.
- **Practical relevance** — For agentic systems, E2E verification extends to the agent loop: run the protocol, assert on outcomes and artifacts.
- **Test data** — Dedicated fixtures with known outcomes make assertions deterministic and failures meaningful.
- **Parallel safety** — Isolating test data per run prevents one test from contaminating another's assertions.
- **Failure diagnosis** — Screenshots, logs, and request traces captured at failure time turn red runs into fixable bugs.

## Related

- [[wiki/entities/e2e-test-001|E2E Verification]] — companion verification entity
- [[wiki/entities/pulse-engine|Pulse Engine]] — system under test in RSIS3
- [[wiki/entities/rrp-state-machine|RRP State Machine]] — protocol being verified
- [[wiki/entities/llm-proxy-agent|LLM Proxy Agent]] — component under test
- [[wiki/entities/memory-client|Memory Client]] — data layer under test
- [[wiki/entities/identity-snapshot-0001|Identity Snapshot 0001]] — fixture entity
