---
type: "entity"
title: "ESM"
description: "Acronym referenced in session 019f4e5d"
tags: ["acronym", "ajax", "android", "api", "ast", "auth", "entity"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
status: "growing"
---

## Esm 2

ECMAScript Modules (ESM) — a standard module system for JavaScript using import/export syntax. Referenced in the companion-particle-life project.

**Related topics:** ajax, android, api, auth

**Domain:** Web Platforms › [[wiki/web-platforms/index|Frontend]] › [[wiki/web-platforms/index|Frontend Frameworks]] › Esm 2

## Overview

ESM (ECMAScript Modules) is the standardized module system for JavaScript, built on import and export statements that are statically analyzable. Unlike earlier script-loading conventions, ESM gives each module its own scope, explicit dependencies, and deterministic loading, which makes large applications easier to reason about. The page records that ESM was referenced in the companion-particle-life project, and it sits in the Ajax-Spa branch where modern frontends are assembled from modules.

## Syntax and Semantics

Modules declare exports with the export keyword and consume them with import. Named exports and default exports cover different sharing styles, and dynamic import() loads modules on demand, which is the basis for code splitting. Static analysis of the import graph lets bundlers tree-shake unused exports and resolve cycles deterministically, a sharp contrast with CommonJS where the graph is discovered at runtime.

## Ecosystem

All modern browsers support ESM natively via script type=module, and Node.js supports it with the .mjs extension or an appropriate package type. Bundlers such as Vite, Rollup, and webpack consume ESM as the source format and emit optimized bundles. Interop with CommonJS remains a practical concern in mixed codebases, handled by tools that translate between the two module systems at build time.

## Project Context

In the companion-particle-life project, ESM provides the module structure that keeps simulation, rendering, and UI code separate while letting them share state and utilities. For single-page applications, module boundaries double as dependency documentation: the import graph shows at a glance which parts of the system depend on which others, easing maintenance and testing.

## Related Entities

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace-10|Ace 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains-10|Jetbrains 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv-10|Csv 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
