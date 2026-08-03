---
type: "concept"
title: "NoSQL Injection"
description: "Injecting operators and query syntax into MongoDB-style queries"
tags: ["security", "injection", "nosql", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# NoSQL Injection

## Summary
NoSQL injection abuses the query language of document databases (MongoDB, Elasticsearch, DynamoDB expressions) by smuggling operators into inputs that are interpolated into queries. The classic payload turns a login check into an always-true query.

## Details
Unlike SQL, document databases don't concatenate strings in the same way, but the injection is still real: if user input is parsed as query syntax, an attacker can add operators. The classic MongoDB login bypass sends {"username": {"$ne": null}, "password": {"$ne": null}} — the query matches any user whose fields exist, bypassing authentication entirely. Operator injection ($where, $gt, $regex, $expr) can also extract data, cause denial of service (expensive regex), or escalate to code execution when $where runs JavaScript.

The mechanism: the vulnerability occurs when the application builds queries from unvalidated JSON (req.body passed straight to find()) or string-interpolates user values into query DSLs. MongoDB's $where and $function execute server-side JavaScript; Elasticsearch's script queries do the same. Even without code execution, $regex injection allows blind data extraction by testing patterns, and $gt/$lt operators break authorization checks ("find invoices where amount < user input").

Concrete example: a wiki API looks up a note with Note.find({_id: req.params.id}). The id is user input; an attacker sends {"$gt": ""} as the id, which matches the first note in the collection — an IDOR-by-injection that bypasses any id-based filtering. A login route with User.findOne({email: input.email, password: input.password}) is bypassed by sending {"email": {"$ne": null}, "password": {"$ne": null}}.

Failure modes: treating the request body as a query document; string-building query DSLs without escaping operators; enabling $where/$function or script fields on untrusted data; and type coercion where a string id becomes an object. Validation libraries that check the shape but not the values (operators are values too) miss the attack.

Operational tradeoffs: the durable fix is to treat query input as data: build queries from allowlisted fields with typed values, reject documents containing operator keys ($-prefixed) at the boundary, and disable server-side scripting where unused. The tradeoff is expressiveness — rich client-driven filtering requires either a safe query DSL or server-side whitelisting of operators. Tests should include operator-laden payloads for every parameterized query.

RSIS3/mykb relevance: the wiki's search and graph queries should reject $-prefixed operator injection; documenting the boundary rule gives RSIS3's security checks a concrete input test.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/second-order-injection|Second-Order Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/blind-injection|Blind Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/header-injection|Header Injection]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
