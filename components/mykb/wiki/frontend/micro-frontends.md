---
type: "concept"
title: "Micro-Frontends"
description: "Splitting frontends across teams and integration modes"
tags: [micro-frontends", "architecture", "module-federation", "teams", "scalability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://micro-frontends.org/", "https://webpack.js.org/concepts/module-federation/"]
---

# Micro-Frontends

## Summary
Micro-frontends split one web application into independently owned, deployed pieces so separate teams ship separately. Integration happens at runtime — iframes, Web Components, or module federation — rather than one shared build. The model brings microservice-style autonomy to the frontend at the cost of coordination and consistency.

## Details
- Integration modes: iframes isolate fully; Web Components wrap frameworks; module federation shares modules at runtime.
- Ownership: each team owns a vertical slice — UI, API, and data for a domain — with a contract for interop.
- Deployment: teams deploy independently, avoiding the coordination serialization of monolith frontend releases.
- Shared concerns: design tokens, routing, auth, and error handling need a shared platform layer and governance.
- Costs: duplicate dependencies, cross-team UX drift, and harder end-to-end debugging.
- Fit: large organizations with many teams and clear domains; small apps pay overhead without benefit.

## Related
- [[wiki/frontend/web-components|Web Components]] — a runtime integration technology
- [[wiki/frontend/module-bundlers|Module Bundlers]] — federation support in bundlers
- [[wiki/frontend/webpack-concepts|Webpack Concepts]] — Module Federation implementation
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — the backend pattern mirrored
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — the coordination alternative
- [[wiki/frontend/component-composition|Component Composition]] — composing federated parts
