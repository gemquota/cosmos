---
type: "concept"
title: "Parameter Pollution"
description: "Duplicate or ambiguous parameters that confuse validation and business logic"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Parameter Pollution

## Summary
Parameter pollution exploits ambiguity in how duplicate or malformed parameters are parsed across layers. When a gateway, WAF, framework, and application each resolve ?a=1&a=2 differently, validation can be bypassed and logic can act on the wrong value.

## Details
HTTP allows repeated parameters (?role=user&role=admin) and ambiguous encodings (semicolons, encoded separators, array-style names). Different stacks resolve duplicates differently: first-wins, last-wins, join-with-comma, or collect-all. The attack feeds on that divergence: the layer that validates reads one value, the layer that acts reads another.

The mechanism: a WAF blocks ?role=admin; the backend reads the last value. The attacker sends ?role=user&role=admin. The WAF sees role=user (first), the backend sees role=admin (last) — the check is bypassed. The same ambiguity affects signature verification (only the first occurrence is signed), cache keys (only part of the input keys the cache), and server-side request forgery where parameter merging combines values from two sources.

Concrete example: an admin endpoint checks ?tenant=acme in the gateway but the application iterates all tenant values. An attacker sends tenant=acme&tenant=other; the gateway allows acme, the app processes other — cross-tenant access. A variant uses encoded values (?role=%75ser&role=admin) to defeat literal string matching while the parser decodes both to the same field.

Failure modes: assuming one parser's semantics hold through the whole chain; frameworks that silently merge duplicates (PHP-style a[]= or comma-joining); normalization gaps (encoded vs decoded, case differences, plus-as-space); and gateways that pass duplicate headers or parameters through unchanged. Even well-defined stacks can disagree on ordering or on whether the first or last occurrence wins.

Operational tradeoffs: the durable fix is deterministic parsing: reject requests with duplicate parameters (documented, enforced at the edge), or define and enforce first-wins/last-wins everywhere. The contract should be tested across the full chain — gateway, WAF, framework, app — with duplicates, encoded duplicates, and mixed encodings. Where multi-value input is legitimate (filters), use one parameter with a defined list separator instead of repetition.

RSIS3/mykb relevance: wiki API request validation should reject duplicates by contract; documenting the rule lets RSIS3's request-shaping tests verify that gateway and origin agree.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/http-parameter-pollution|HTTP Parameter Pollution]]
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]]
- [[wiki/api-protocols/http-headers|HTTP Headers]]
- [[wiki/api-protocols/api-gateway|API Gateway]]
