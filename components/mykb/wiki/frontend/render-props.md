---
type: "concept"
title: "Render Props"
description: "Sharing logic through function-as-prop APIs"
tags: [react", "render-props", "composition", "javascript", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://legacy.reactjs.org/docs/render-props.html", "https://react.dev/learn"]
---

# Render Props

## Summary
Render props share logic by passing a function as a prop or child that receives state and returns JSX. The pattern gave consumers full control of rendering while the parent owned behavior — a technique used by React Router and Formik. Custom hooks largely replaced it because hooks compose more cleanly without nesting.

## Details
- Shape: <DataProvider render={data => <List items={data} />} />, with children-as-function as a variant.
- Inversion of control: the provider decides logic, the consumer decides markup, both stay decoupled.
- History: predates hooks; solved prop-drilling-adjacent sharing for mouse position, media queries, and data fetching.
- Downsides: components nest deeply, and logic lives in components rather than plain functions.
- Hook replacement: useMousePosition() and useData() deliver the same sharing with less nesting and better tree-shaking.
- Relevance: the pattern survives in libraries and legacy code; understanding it explains many existing APIs.

## Related
- [[wiki/frontend/custom-hooks|Custom Hooks]] — the modern replacement
- [[wiki/frontend/component-composition|Component Composition]] — the composition family it belongs to
- [[wiki/frontend/prop-drilling|Prop Drilling]] — related data-passing problem
- [[wiki/software-engineering/functional-programming|Functional Programming]] — functions as values
- [[wiki/web-platforms/component-architecture|Component Architecture]] — where the pattern lives
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — the shared state it carried
