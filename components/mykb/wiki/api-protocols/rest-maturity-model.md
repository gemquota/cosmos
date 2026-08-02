---
type: "concept"
title: "REST Maturity Model"
description: "Richardson Maturity Model levels 0-3"
tags: ["rest", "maturity-model", "hateoas", "api-design", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/articles/richardsonMaturityModel.html", "https://restfulapi.net/richardson-maturity-model/"]
---

# REST Maturity Model

## Summary
The Richardson Maturity Model grades an API on how fully it adopts REST constraints, in four levels: 0 uses HTTP as a tunnel for RPC, 1 introduces resources, 2 adds HTTP verbs and status codes, and 3 adds hypermedia. Each level removes coupling and makes the API more self-describing.

## Details
- Level 0 (POX): a single POST endpoint that switches on a body field — the classic SOAP or RPC style over HTTP; everything is action-oriented.
- Level 1 (resources): distinct URIs for entities, but still mostly POSTs; the address space becomes meaningful and linkable.
- Level 2 (verbs and status): GET/PUT/PATCH/DELETE with the correct semantics, status codes that describe outcomes, and headers like Location; this is the pragmatic target for most production APIs.
- Level 3 (hypermedia): responses embed links describing what the client can do next, so the API itself drives client navigation.
- The model is a maturity scale, not a mandate: many excellent APIs stop at level 2 because HATEOAS adds complexity with limited client payoff.
- Assessment should be about coupling reduction — level 2 removes action-coupling, level 3 removes path-coupling — not about scoring aesthetics.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — the model grades how fully an API is RESTful
- [[wiki/api-protocols/hateoas|HATEOAS]] — level 3 is defined by hypermedia
- [[wiki/api-protocols/rest-resource-design|REST Resource Design]] — resource modeling is the level-1 step
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — level 2 centers on correct status semantics
- [[wiki/api-protocols/rpc-styles|RPC Styles]] — level 0 is RPC over HTTP
