---
type: "entity"
title: "ReferenceError"
description: "A JavaScript error raised when code refers to a binding that does not exist"
tags: ["entity", "javascript", "errors", "scope", "runtime"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# ReferenceError

## Summary

ReferenceError is a JavaScript error raised when code evaluates an identifier that is not defined in any accessible scope. It is among the most common early JavaScript failures, usually revealing typos, missing declarations, or scope mistakes. Understanding the scope chain and temporal dead zone explains most ReferenceError occurrences.

## Details

- **Definition** — Evaluating an undefined identifier throws ReferenceError; the message names the offending binding, though minified code can obscure it.
- **Scope chain** — Lookup walks local, enclosing, and global scopes; a miss at every level raises the error, so shadowing and hoisting behavior matter.
- **Declarations** — var, let, const, and function declarations differ in hoisting; let and const also create a temporal dead zone before initialization.
- **Common causes** — Typos, forgetting to declare, referencing a variable before its declaration executes, and accessing destroyed closure bindings are typical causes.
- **Worked example** — A handler uses results where the variable was named result; the typo throws ReferenceError and the request fails with a 500.
- **Debugging** — Stack traces point at the expression, and scope inspection in devtools shows which bindings actually exist at that point.
- **Common failure modes** — Catching ReferenceError and continuing hides the bug; better to fix the declaration or add a guard at the data boundary.
- **Practical relevance** — Linters and type checkers catch most ReferenceErrors statically, which is why they are rarer in mature codebases.
- **Telemetry note** — Recorded among API and cloud tags, consistent with a frontend or edge-runtime error surfaced in logs.
- **Modules** — ES module scope and strict mode change what is visible; referencing a module-scope binding from outside, or a type-only import at runtime, raises the error.
- **Strict mode** — Assigning to an undeclared variable in strict mode throws ReferenceError, converting silent global creation into a loud failure.
- **Worked example** — A script uses a variable imported as a type in a runtime expression; the bundler strips the import, and the first use throws ReferenceError in production only.
- **Prevention** — Declaring variables with const and let, enabling linters, and keeping data at module boundaries prevent the whole class of errors.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the exception family
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/errorcode|ErrorCode]] — coding the failure
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/keyerror|KeyError]] — missing key analogue in Python
- [[wiki/dev-tools/debuggers|Debuggers]] — inspecting scopes
- [[wiki/dev-tools/debug-logging|Debug Logging]] — logging the failure context
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — where the error occurs
