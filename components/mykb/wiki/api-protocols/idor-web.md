---
type: "concept"
title: "IDOR on the Web"
description: "Insecure Direct Object References exposing objects by predictable id"
tags: ["security", "authorization", "attacks", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# IDOR on the Web

## Summary
Insecure Direct Object Reference (IDOR) is an authorization flaw: the API trusts that a client asking for /users/1234 is allowed to see user 1234, so anyone can enumerate ids and read or mutate objects they don't own.

## Details
An IDOR exists when a resource is addressed directly by a predictable identifier (numeric id, UUID, slug) and the endpoint performs no ownership or permission check. GET /invoice/42 returns invoice 42 to whoever asks; PUT /users/7/profile updates whoever is at id 7. The vulnerability is missing authorization, not missing encryption — UUIDs slow enumeration but are not a fix.

The mechanism: the handler fetches by id and returns the object. Authorization checks must compare the requesting principal against the object's owner or required role; when the check is absent, every id is accessible. Attackers automate enumeration: sequential ids are trivially walked; even UUIDs leak through logs, referrers, and shared links, so unguessable ids are defense in depth, not a control.

Concrete example: a wiki API exposes GET /api/notes/{id}. The handler loads the note by id without checking that the current user owns it. A user signs up, changes the numeric id in the URL, and reads every other user's private notes — a data breach by enumeration. The fix: the query includes the owner predicate (WHERE id=? AND owner_id=?) or an explicit authorization check after load.

Failure modes: checking authorization only on some endpoints (list yes, detail no); trusting client-supplied ownership fields (mass assignment); logging full object ids in URLs, which leak via referrers; and authorization checks that use the object's own fields (if obj.owner == user) when those fields are client-controllable. Object-level permissions on shared resources (team documents) need role-aware checks, not just owner equality.

Operational tradeoffs: centralizing authorization (policy layer or per-object capability checks) prevents per-endpoint drift; capability-style URLs (opaque tokens per share) trade URL guessability for access control but complicate revocation. The practical baseline: every object access goes through a query or middleware that binds the resource to the principal, ids are not treated as secrets, and tests enumerate other users' ids to prove the checks hold.

RSIS3/mykb relevance: the wiki API's note, graph, and pulse endpoints are object-addressed; documenting the owner-bound query rule gives RSIS3's security reviews a pattern to assert on every resource route.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/mass-assignment|Mass Assignment]] — related coverage in the same cluster
- [[wiki/api-protocols/insecure-deserialization|Insecure Deserialization]] — related coverage in the same cluster
- [[wiki/api-protocols/file-upload-security|File Upload Security]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
