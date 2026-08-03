---
type: "concept"
title: "React Ecosystem"
description: "React core plus the libraries that surround it: state, data fetching, styling, and build tooling"
tags: ["react", "frontend", "ecosystem", "javascript", "frameworks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://react.dev/", "https://react.dev/learn"]
---
# React Ecosystem

## Summary
React is a component library for building declarative UIs; the ecosystem around it fills the gaps: routing, state, data fetching, forms, styling, and build. React's model — components re-render from props and state — shapes how all those libraries integrate. Understanding the core makes choosing ecosystem tools deliberate.

## Details
- **Core model** — components are functions of props and state; reconciliation diffs the virtual tree; hooks add state, effects, refs, and memoization.
- **State and data** — Context for shallow trees, external stores (Zustand, Redux) for app state, TanStack Query/SWR for server state.
- **Rendering features** — Suspense, transitions, and concurrent rendering keep UIs responsive; memoization guards against re-render storms.
- **Tooling** — Vite, Next.js, and React Native cover web and native; the compiler and RSC blur server/client boundaries.
- **Worked example** — a data-heavy dashboard is a natural fit for React with TanStack Query for API data and an external store for UI state; the current mykb dashboard deliberately stays framework-light (vanilla JS with Tailwind and Chart.js) so a React SPA would only be worth the dependency cost at higher widget complexity.
- **Relevance** — RSIS3's agent UI choices should be evaluated against the same core trade-offs.

## Related
- [[wiki/frontend-frameworks/composition-apis|Composition APIs]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/hooks-practice|Hooks in Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/hoc-patterns|Higher-Order Components]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/context-api|Context API]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — existing coverage
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — existing coverage
