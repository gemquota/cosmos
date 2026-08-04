---
type: "entity"
title: "Dead Imports"
description: "Dead Imports: detecting and removing unused imports and unreachable code"
tags: ["entity", "api", "ast", "aws", "bash", "bootstrap", "code-quality"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# Dead Imports

## Summary

Dead Imports is the bootstrap-cluster entity for unused imports and unreachable code: modules that are imported but never used. Dead imports bloat bundles and mislead readers about dependencies. Removing them matters because lean, honest dependency graphs are faster and safer. Import hygiene is a small, continuous cost that prevents compounding dependency debt.

## Details

- **Definition** — A dead import is a module pulled into a file but never referenced, surviving as a tax on size and clarity.
- **Detection** — Linters and bundler warnings flag unused imports; whole-program analysis finds dead modules.
- **Bundle impact** — Each dead import costs parse time and bytes, and can pull entire dependency subtrees into the bundle.
- **Reader cost** — Unused imports imply false dependencies, sending readers down paths that do not matter.
- **Tree shaking limits** — Bundlers can drop unused exports only if modules are side-effect-free; dead imports defeat the optimization.
- **Worked example** — A refactor removes an API client but leaves its import; the next build report shows the dead module disappearing after cleanup.
- **Failure modes** — Aggressive removal that drops side-effectful imports, and churn from auto-import tooling, cause regressions.
- **Practical relevance** — Keeping imports clean is part of circular-import and dependency hygiene.
- **Automated removal** — Lint autofixes and IDE actions remove dead imports mechanically, making cleanup routine.
- **Bundle reports** — Build output that lists module sizes exposes the cost of accidental imports.
- **Side-effect awareness** — Modules with side effects must be imported deliberately; removal tools need an explicit allowlist.
- **Review habit** — Noticing and removing dead imports during review keeps the codebase clean without dedicated cleanup sprints.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/circular-import-risk|Circular Import Risk]] — related dependency hazard
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/filesystemloader|FileSystemLoader]] — loading only what is needed
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/nodedefinitions|NodeDefinitions]] — referenced definitions only
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/edgeid|EdgeId]] — referenced identities
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/dimensions|Dimensions]] — bundle size effects
