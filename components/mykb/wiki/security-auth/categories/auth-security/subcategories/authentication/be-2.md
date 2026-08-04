---
type: "entity"
title: "BE"
description: "Babel"
tags: ["acronym", "api", "ast", "auth", "authentication", "entity"]
timestamp: "2026-07-19T22:41:40Z"
status: "growing"
resource: ""
---

## Be 2

Babel — a JavaScript transpiler that converts ES6+ code into backwards-compatible versions.

**Related topics:** api, auth, authentication

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Security Auth]] › [[wiki/web-platforms/00-index|Auth Security]] › Be 2

## Overview

Babel is a JavaScript toolchain that transforms modern syntax into backwards-compatible output, letting developers target current language features while shipping code that older runtimes can parse. It parses source into an AST, runs plugins and presets, and regenerates JavaScript. In this knowledge base, the two-letter title BE is a shorthand for Babel, the same entity as [[wiki/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]].

## Details

- Pipeline: source → parse → transform → generate; each step is observable and each transform is a discrete plugin.
- Presets: `@babel/preset-env` transpiles only the syntax unsupported by configured targets, keeping output lean.
- Syntax vs runtime: Babel transforms syntax; missing built-ins still require polyfills or runtime helpers.
- Integration: bundlers run Babel during builds, so config lives in `babel.config.js` or `.babelrc`.
- Debugging: source maps correlate output back to authored code, and failing transforms often come from plugin order or incompatible presets.

In API and authentication code, the transformed bundle ships the client logic — login, token refresh, request signing — so build correctness is security-relevant: a broken transform could drop error handling or miscompile a check. Knowing the pipeline helps trace issues that reproduce only in production browsers. When the acronym appears in notes, the surrounding build configuration disambiguates it from other uses of BE, such as backend engineering.

## Related Entities
## Build Hygiene

Keep the Babel config small and explicit: one preset, a pinned target list, and only the plugins the codebase actually uses. Upgrade plugin versions deliberately and re-run the full client test suite, because a config change can silently alter output for every page. Add a smoke test that exercises the transformed bundle in the oldest supported runtime so regressions surface in CI rather than in user browsers.


- [[wiki/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/automatic|Automatic 10]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]
