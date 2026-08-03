---
type: "entity"
title: "REST"
description: "API — service communication interface, Bash — shell scripting language, CLI — command-line tooling"
tags: ["entity", "acronym", "api", "bash", "bootstrap", "cli"]
timestamp: "2026-07-19T22:41:41Z"
status: "growing"
resource: ""
---
## Rest
REST (Representational State Transfer) is an architectural style for designing networked applications. Uses HTTP methods (GET, POST, PUT, DELETE) for CRUD operations.
Acronym referenced in session 019f1a6b
**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Tooling]] › [[wiki/web-platforms/00-index|Shell Cli]]
## Overview
REST is an architectural style for networked applications that treats the system as a set of addressable resources manipulated over HTTP. Resources are identified by URLs, and the standard methods — GET, POST, PUT, PATCH, and DELETE — map onto read and write operations. The style emphasizes stateless requests, self-describing messages, and a uniform interface, which keeps clients simple and lets servers evolve representations independently.
## Details
- CRUD mapping: GET reads, POST creates, PUT/PATCH update, DELETE removes; collections and members give URLs a predictable shape.
- Status codes: responses signal outcome — 200 OK, 201 Created, 204 No Content, 400 bad request, 401 unauthorized, 403 forbidden, 404 missing, and 5xx server errors.
- Statelessness: each request carries its own context (headers, auth, body), enabling caching, scaling, and retries without server-side session state.
- Headers and caching: `Content-Type`, `ETag`, and `Cache-Control` control representation and freshness.
- CLI usage: tools like `curl` exercise REST endpoints directly from the shell, which is why the entity sits under shell-cli — scripts compose requests, parse JSON responses, and drive APIs.
- Contrast: REST differs from RPC-style and from single-endpoint query APIs like [[wiki/api-protocols/entities/graphql|GraphQL]]; choosing between them is a contract-design decision.
In practice, REST APIs dominate public and internal service contracts, and shell automation is the fastest way to explore them: a few `curl` commands reveal headers, status codes, and payload shapes before any client code is written. Good REST design — consistent naming, correct status codes, and explicit error bodies — makes both browsers and scripts predictable consumers.
## Related Entities
- [[wiki/tooling/categories/shell-cli/busuj|Busuj]]
- [[wiki/tooling/categories/shell-cli/dims-2|Dims 2]]
- [[wiki/tooling/categories/shell-cli/intent-distribution-engine-2|Intent Distribution Engine 2]]
