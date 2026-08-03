---
type: "concept"
title: "Mass Assignment"
description: "Binding client-supplied fields directly onto models, enabling privilege escalation"
tags: ["security", "api", "attacks", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Mass Assignment

## Summary
Mass assignment happens when a framework binds all request fields directly onto an object, and a client sneaks in a field that was never meant to be settable — role=admin, is_verified=true, owner_id=attacker. The fix is explicit allowlists or per-field setter APIs.

## Details
Frameworks that auto-bind request parameters to model attributes (Rails strong parameters being the hardened version, Laravel fillable, Django model forms, Java bean binding) make the attack easy: a POST to /api/users with {"name": "x", "role": "admin"} updates role because the binder maps every provided key onto a setter. The classic 2012 GitHub vulnerability let users add a public_key to any account — an account-takeover mass assignment.

The mechanism: the binder reflects over the target object's attributes and calls setters for each supplied key. Any attribute without a guard — role, admin, plan, balance — becomes client-writable. The defense is the inverse: only explicitly listed fields may be bound (permit list), with everything else ignored or rejected. Validation after binding is not enough if the dangerous field is valid for some contexts, which is why the binding boundary, not the model validation, must enforce it.

Concrete example: a wiki API's PUT /api/users/{id} binds the body to the user model. A user edits their own profile and adds "role": "admin". If the binder permits role, they are now an admin. With strong-parameters-style permissioning (permit name, email only), the extra field is stripped before the model is touched — the escalation simply cannot happen through that endpoint.

Failure modes: allowlists that accidentally include privileged fields; binder code that permits "all fields except..." (denylists are fragile — new attributes are exposed by default); nested mass assignment (updating an association's fields through parent params); and JSON-only protections that don't cover form-encoded input on the same endpoint. Separate admin endpoints must use separate binding contracts, not shared models.

Operational tradeoffs: explicit permit lists add boilerplate per endpoint but make the write contract auditable — the OpenAPI spec can mirror the permitted fields. The alternative (explicit setter APIs or command objects) is cleaner for complex writes but heavier to build. The baseline: never auto-bind request bodies to models; always filter through an endpoint-specific allowlist, and treat any field not in the spec as rejected input.

RSIS3/mykb relevance: any RSIS3-generated CRUD endpoint must define its writable fields explicitly; documenting the permit-list rule lets check-practices verify bindings across services.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/insecure-deserialization|Insecure Deserialization]] — related coverage in the same cluster
- [[wiki/api-protocols/file-upload-security|File Upload Security]] — related coverage in the same cluster
- [[wiki/api-protocols/zip-slip|Zip Slip]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
