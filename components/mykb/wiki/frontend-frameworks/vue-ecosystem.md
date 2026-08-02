---
type: "concept"
title: "Vue Ecosystem"
description: "Vue's reactive core, composition API, and the tooling: router, Pinia, Nuxt, and Vite"
tags: ["vue", "frontend", "reactivity", "javascript", "frameworks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://vuejs.org/", "https://vuejs.org/guide/introduction.html"]
---
# Vue Ecosystem

## Summary
Vue is a progressive framework whose reactive core tracks dependencies with Proxies. The composition API organizes logic in functions; the ecosystem — Vue Router, Pinia, Nuxt, and Vite — covers routing, state, SSR, and build. Vue scales from a script tag to full-stack apps.

## Details
- **Reactivity** — `ref` and `reactive` track reads and writes; computed values and effects update automatically; templates compile into optimized render functions.
- **Composition API** — `setup()` and composables group related logic; `<script setup>` is the modern default.
- **State and routing** — Pinia stores with actions and getters; Vue Router with lazy routes and navigation guards.
- **Meta-framework** — Nuxt adds SSR, file-based routing, and server routes on top of Vue and Vite.
- **Worked example** — a lightweight mykb admin could use Vue 3 with Pinia for theme state and Vue Router for article views.
- **Relevance** — comparing Vue's fine-grained reactivity with React's re-render model informs RSIS3's UI stack choices.

## Related
- [[wiki/frontend-frameworks/vue-composition-api|Vue Composition API]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/vue-reactivity|Vue Reactivity]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/reactivity-pitfalls|Reactivity Pitfalls]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — existing coverage
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — existing coverage
