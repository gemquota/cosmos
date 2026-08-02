---
type: "concept"
title: "Backend for Frontend"
description: "Per-client BFF gateway pattern"
tags: ["bff", "backend-for-frontend", "api-gateway", "architecture", "clients"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://samnewman.io/patterns/architectural/bff/", "https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends"]
---

# Backend for Frontend

## Summary
The Backend for Frontend (BFF) pattern gives each client family its own server-side API layer: one BFF for mobile, one for web, one for partners. Each BFF shapes, aggregates, and secures backend services for its client's specific needs — no shared gateway tries to serve every screen size.

## Details
- Why separate BFFs: mobile needs small payloads and offline sync; web wants deep links and full data; a single API forces compromises that hurt both.
- BFF responsibilities: aggregation (one round trip for a screen), shaping (fields the UI needs), and security (tokens never reach the browser).
- It is a gateway variant: routing, authn, and rate limiting still apply, but scoped per client family instead of globally.
- Code sharing: BFFs can be thin (proxy + transform) or thick (own domain logic); thick BFFs risk becoming god services — keep them presentation-focused.
- Versioning: the BFF couples UI to API, so it absorbs backend breaking changes and lets clients upgrade independently.
- Ownership: the client team owns the BFF — a big advantage for autonomy, a risk if every team builds one differently.
- Contrast: a single generic gateway (API Gateway pattern) is for cross-cutting policy; BFF is for client-specific experience.

## Related
- [[wiki/api-protocols/api-gateway|API Gateway]] — the general gateway pattern BFF specializes
- [[wiki/api-protocols/graphql|GraphQL]] — a client-driven BFF alternative
- [[wiki/api-protocols/rpc-styles|RPC Styles]] — per-client API styles behind the BFF
- [[wiki/api-protocols/api-design-first|Design-First APIs]] — BFF contracts designed from client needs
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — BFFs hold tokens that browsers must not
