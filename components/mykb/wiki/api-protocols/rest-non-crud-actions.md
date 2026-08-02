---
type: "concept"
title: "REST Non-CRUD Actions"
description: "Modeling custom operations outside CRUD"
tags: ["rest", "actions", "api-design", "rpc", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#organize-the-api-around-resources", "https://restfulapi.net/rest-api-design-tutorial-with-example/"]
---

# REST Non-CRUD Actions

## Summary
Not every operation is a create-read-update-delete on a noun: approvals, retries, refunds, and notifications change state in ways a bare POST does not express. REST handles these with sub-resources that turn actions into state machines, or with explicit action endpoints when a sub-resource is overkill.

## Details
- Prefer modeling the action as a resource: POST /orders/42/refunds creates a Refund; POST /invoices/9/payments records a Payment; the outcome is queryable history, not a one-shot side effect.
- State transitions fit the same shape: POST /tickets/5/approve and POST /tickets/5/reject model a workflow where each transition is auditable.
- When a transition has no natural sub-resource, an action suffix is acceptable and widely used: POST /users/42/activate or POST /runs/7/cancel, documented explicitly.
- Return 201 with a Location when the action creates something, or 200/202 with a representation when it mutates state; long-running actions return 202 Accepted plus a status endpoint.
- Verbs in URIs should be rare and always POST — never GET, since GETs must be safe and cacheable.
- RPC-style operations (calculate, validate, export) that do not own state can live under a dedicated controller resource: POST /calculations.

## Related
- [[wiki/api-protocols/rest-resource-design|REST Resource Design]] — actions as sub-resources fit the noun model
- [[wiki/api-protocols/rest-maturity-model|REST Maturity Model]] — action endpoints sit between RPC and resource modeling
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — 202 Accepted suits long-running actions
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — actions as events preserve history
- [[wiki/api-protocols/rpc-styles|RPC Styles]] — the spectrum from pure RPC to pure resources
