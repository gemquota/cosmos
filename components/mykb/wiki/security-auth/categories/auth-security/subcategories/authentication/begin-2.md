---
type: "entity"
title: "BEGIN"
description: "Acronym referenced in session fe448bc7"
tags: ["acronym", "ajax", "android", "api", "ast", "auth", "authentication", "bug", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
status: "growing"
---


## Begin 2

BEGIN appears in 5 session(s) categorized as API, Debugging, Mobile, Security. Related topics: acronym, ajax, android, api, auth, authentication.

**Domain:** Web Platforms › [[wiki/web-platforms/supercategories/security-auth/index|Security Auth]] › [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/index|Auth Security]] › Begin 2

## SQL Transaction Keyword

In SQL, `BEGIN` starts a transaction: a sequence of statements that commit atomically or roll back as a unit. The canonical pattern is:

- `BEGIN;` — open the transaction.
- Run the statements that must succeed together.
- `COMMIT;` — make the changes durable, or `ROLLBACK;` — discard them.

PostgreSQL uses `BEGIN`/`COMMIT`/`ROLLBACK`; MySQL defaults to autocommit per statement and uses `START TRANSACTION`; some engines support `SAVEPOINT` to create nested rollback points inside an open transaction. Transactions guarantee atomicity, consistency, isolation, and durability (ACID) for the work they wrap.

Because the page is tagged as an acronym, `BEGIN` also appears in non-SQL senses: block delimiters in languages like Pascal and Ruby, shell constructs, and protocol keywords. The knowledge base keeps all readings open and uses the session tags — AJAX, Android, API, authentication — as evidence: an API or authentication session is far more likely to reference transaction boundaries than a language keyword.

## Debugging Sessions

The bug tag points to how BEGIN appears in debugging sessions: a transaction left open because `COMMIT` never ran, a rollback that discarded intended work, or an autocommit mismatch between the application and the database. Reading transaction boundaries — what each statement is grouped with — is often the fastest way to explain lost or duplicated writes. The SQL reading is therefore recorded as primary, while alternative expansions stay indexed under the same tags for future disambiguation.

## Related Notes

- [[wiki/devops-infra/transactions|Transactions]] — the semantics BEGIN enables
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — behavior inside the transaction
- [[wiki/devops-infra/postgresql|PostgreSQL]] — a common BEGIN/COMMIT dialect

## Related Entities

- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/automatic-10|Automatic 10]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]


