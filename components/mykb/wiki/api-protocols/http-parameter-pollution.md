---
type: "concept"
title: "HTTP Parameter Pollution"
description: "Sending duplicate parameters to confuse validation and backend logic"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# HTTP Parameter Pollution

## Summary
HTTP parameter pollution (HPP) sends the same parameter multiple times (?role=user&role=admin) to exploit the difference between how the frontend validates parameters and how the backend consumes them. The divergence between layers is the vulnerability.

## Details
HTTP allows repeated query parameters and form fields. Different layers resolve duplicates differently: many frameworks take the first value, others take the last, some join them with commas, and application code may iterate all of them. When a WAF, proxy, or frontend validates the first value while the backend uses the last (or vice versa), an attacker can smuggle a value past validation.

The mechanism: the attack needs a layer mismatch. Classic example: a proxy blocks ?role=admin but allows ?role=user; the backend, taking the last value, reads role=admin. Or a framework's request parser joins duplicate keys into a comma list that later SQL or template code mishandles. HPP also enables bypassing signature checks that only cover the first occurrence, and it can turn a single-valued endpoint into a multi-value one for injection.

Concrete example: an admin API checks ?user_id=123 against an allowlist in the gateway, but the application iterates all user_id values and processes each. An attacker sends user_id=123&user_id=456, passes the gateway check on the first value, and the backend acts on 456 — a horizontal privilege escalation if 456 belongs to another tenant. The same divergence can break CSRF token checks that read the first value while the handler uses the last.

Failure modes: relying on a single layer's parsing rules without testing the full chain; frameworks that silently join duplicates (PHP, ASP.NET historically) creating comma-injected values; and gateways that normalize one way while origin servers normalize another. Even well-behaved stacks can disagree on ordering, encoding, or semicolon handling.

Operational tradeoffs: the durable fix is deterministic parsing: reject requests with duplicate parameter names outright (or define and document first-wins/last-wins), and ensure gateway and origin use the same parser semantics. Tests should exercise duplicates, encoded duplicates (%72%6fle), and mixed case across the whole chain. Where duplicates must be allowed (multi-select filters), the contract should use a single parameter with comma separation instead of repetition.

RSIS3/mykb relevance: wiki APIs that accept query parameters should reject duplicates by contract; documenting that rule lets RSIS3's request-shaping tests verify gateway and origin agreement.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/parameter-pollution|Parameter Pollution]]
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]]
- [[wiki/api-protocols/http-headers|HTTP Headers]]
- [[wiki/api-protocols/api-gateway|API Gateway]]
