---
type: "entity"
title: "ACP"
description: "ACP: access control points and policy enforcement at system boundaries"
tags: ["acronym", "ajax", "alpine", "android", "angular", "api", "ast", "auth", "bash", "entity", "access-control"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# ACP

## Summary

ACP is the angular-cluster entity for access control points: the boundaries where requests are checked against policy before proceeding. Centralizing checks at control points prevents authorization gaps. It matters because access control is only as strong as its enforcement points. Control points are also audit points: every decision at the boundary is loggable.

## Details

- **Definition** — An access control point is a chokepoint in a request's path where identity and permission are verified.
- **Placement** — Gateways, middleware, and route guards are the classic control points; each must enforce the same policy.
- **Identity first** — Authentication establishes who is calling before authorization decides what they may do.
- **Capability checks** — Fine-grained checks verify specific permissions per action rather than coarse role checks alone.
- **Defense in depth** — Multiple control points compensate for a single layer being bypassed. Checks should also verify the identity of the caller, not just the presence of a token, to avoid replay and delegation abuse.
- **Failure modes** — Checks only in the UI, duplicated logic that drifts, and deny-by-default violations create gaps.
- **Worked example** — An API gateway authenticates, a route guard filters pages, and a service checks object-level permissions.
- **Practical relevance** — For agentic systems, control points become approval gates where consequential actions pause for permission.
- **Deny by default** — Anything not explicitly permitted is refused, which keeps new features safe by construction.
- **Policy centralization** — One policy module consumed by all points prevents the drift of duplicated checks.
- **Failure logging** — Denied access is logged with identity, action, and reason, creating an audit trail.
- **Testing** — Authorization tests that assert both allowed and denied outcomes at each control point prevent regression drift.

## Related

- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — permission gates for agents
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/alert|ALERT]] — auth failure notifications
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/build|BUILD]] — cluster sibling page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/environmental-check|Environmental Check]] — checking auth environment
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/automationmanager|AutomationManager]] — automating policy checks
