---
type: "concept"
title: "Custom Hooks"
description: "Extracting reusable stateful logic"
tags: [react", "hooks", "reusability", "javascript", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/learn/reusing-logic-with-custom-hooks", "https://react.dev/reference/react/hooks"]
---

# Custom Hooks

## Summary
Custom hooks extract reusable stateful logic into functions that can call other hooks. Named with the use prefix, they package state, effects, and memoization so components stay declarative. They are React's primary mechanism for sharing non-visual behavior — data fetching, subscriptions, timers, and local storage sync.

## Details
- Shape: a plain function calling useState, useEffect, and friends; return values and setters like a public API.
- Rules of hooks: call hooks unconditionally at the top level and only inside components or other hooks.
- Composition: hooks call hooks, so useAuth can build on useLocalStorage and useEffect.
- Testing: renderHook from testing-library exercises hooks without mounting full components.
- Conventions: name hooks use*, keep them single-purpose, and return stable references (useCallback, useMemo) to limit re-renders.
- Ecosystem: thousands of libraries ship hooks, from form state to media queries to optimistic updates.

## Related
- [[wiki/frontend/render-props|Render Props]] — the pattern hooks replaced
- [[wiki/frontend/component-composition|Component Composition]] — how hooks fit in components
- [[wiki/frontend/reactive-state|Reactive State]] — the state primitives hooks wrap
- [[wiki/frontend/frontend-testing|Frontend Testing]] — renderHook testing
- [[wiki/web-platforms/component-architecture|Component Architecture]] — component design context
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — hooks as stores
