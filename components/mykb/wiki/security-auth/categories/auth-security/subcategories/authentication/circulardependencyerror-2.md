---
type: "entity"
title: "CircularDependencyError"
description: "Error"
tags: ["api", "ast", "auth", "authentication", "bash", "bug", "bun", "cli", "entity"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
status: "growing"
---

## Circulardependencyerror 2

Error — exception and error conditions in software. Sessions show error handling patterns including try/catch blocks, error types, and recovery strategies.

**Related topics:** api, auth, authentication, bash, bug, bun, cli

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Security Auth]] › [[wiki/web-platforms/00-index|Auth Security]] › Circulardependencyerror 2

## The Exception

`CircularDependencyError` is raised when a dependency graph contains a cycle that cannot be resolved at configuration time. The name is most familiar from SQLAlchemy's ORM, which raises it when two mapped classes reference each other through relationships and no resolution strategy breaks the cycle during table creation or mapper configuration. Dependency-injection containers in other ecosystems raise an analogous error when component A requires component B while component B requires component A.

Common manifestations:

- ORM models with bidirectional relationships where both sides define foreign keys with no clear creation order.
- Module-level circular imports in Python or JavaScript — `a` imports `b` while `b` imports `a` — which surface as import-time errors or undefined bindings.
- DI graphs where constructor injection cycles through several components.
- Build and schema tools whose topological sort finds no valid ordering.

The fixes mirror each other: break the cycle by deferring one edge — lazy imports, setter injection, deferred foreign-key resolution, or splitting the module so the shared dependency moves to a third component. In sessions tagged with bug, bun, and CLI, the error most often appeared while wiring up a service graph or running a build that resolved modules in the wrong order.

## Prevention

Cycles are easiest to prevent at design time: draw the dependency graph before coding, keep layers acyclic, and let a linter or import checker flag back-edges early. A cycle that reaches configuration time is a design smell, and the exception is the reminder to restructure rather than to patch the symptom.

## Related Notes

- [[wiki/tooling/sqlalchemy|SQLAlchemy]] — the ORM that names the exception
- [[wiki/dev-tools/entities/python-2|Python]] — module-import cycles
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the error-handling family

## Related Entities

- [[wiki/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/automatic-10|Automatic 10]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]

