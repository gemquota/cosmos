---
type: "concept"
title: "Strangler Fig Pattern"
description: "Incrementally replacing a legacy system piece by piece until the new system fully takes over"
tags: ["strangler-fig", "migration", "refactoring", "legacy"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Strangler Fig Pattern

## Summary
The strangler fig pattern replaces a monolithic legacy system gradually: new functionality is routed to a new implementation while old behavior slowly retires.

## Details
- Routing is the enabler: a facade (API gateway or proxy) sends new paths/requests to the new system and old ones to the legacy system.
- Each increment ships value and reduces risk; the system is always working.
- Data migration is the hard part — split databases and sync while both sides run.

## Related
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]] — the incremental member of the family
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — replacement targets a new stack
- [[wiki/cloud-infra/re-platforming|Re-platforming]] — a middle path to replacement
