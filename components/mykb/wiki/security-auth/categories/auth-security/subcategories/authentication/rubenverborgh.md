---
type: "entity"
title: "RubenVerborgh"
resource: ""
---
description: "Web researcher associated with the Solid project, linked data, and decentralized data ownership"
tags: ["entity", "angular", "api", "ast", "auth", "authentication", "decentralized-web", "linked-data"]
timestamp: "2026-07-19T22:41:41Z"

# RubenVerborgh

## Summary
Ruben Verborgh is a Belgian computer scientist and web researcher whose work centers on linked data, RESTful web architecture, and the decentralized web. He is closely associated with the Solid project, which gives people personal data stores, called pods, that applications request access to. His ideas matter because they reframe identity and data control as user-owned rather than platform-owned, and they offer a concrete architectural answer to platform lock-in.

## Details
- **Linked data** — the approach of publishing structured, interlinked data with stable identifiers so that information from many sources can be combined into a single knowledge graph.
- **REST emphasis** — Verborgh argues for designing web APIs as addressable resources with uniform interfaces and hypermedia, rather than bespoke remote procedure calls tied to one client.
- **Solid pods** — personal online data stores hold a user's data; applications must request access, which reverses the usual model of platforms hoarding data and makes portability possible.
- **Identity model** — WebID and Solid's use of OpenID Connect tie authentication to the user's identity while keeping authorization scoped per data store and per application.
- **Why it matters** — separating data from applications means users can switch tools without losing their history, and researchers can reuse data across services with consent.
- **Open standards** — the ecosystem builds on existing web standards such as HTTP, linked data, and OpenID Connect instead of proprietary formats, which lowers switching costs.
- **Common failure modes** — decentralized systems struggle with discoverability, inconsistent authorization policies, and the coordination cost of maintaining multiple interlocking standards.
- **Practical relevance** — the decentralized data-store model is a reference point for privacy-preserving identity, consent-based data sharing, and interoperable personal knowledge.

## Related
- [[wiki/identity/openid-connect|OpenID Connect]] — identity layer used in Solid
- [[wiki/identity/identity-providers|Identity Providers]] — who vouches for an identity
- [[wiki/api-protocols/oauth2|OAuth 2]] — delegated authorization flows
- [[wiki/security/secrets-management|Secrets Management]] — protecting stored credentials
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — portable knowledge data
- [[wiki/security/zero-trust|Zero Trust]] — per-request data access control
