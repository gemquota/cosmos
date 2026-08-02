---
type: "concept"
title: "Error Boundaries"
description: "Catching and recovering from render-time errors"
tags: [react", "error-handling", "components", "resilience", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary", "https://legacy.reactjs.org/docs/error-boundaries.html"]
---

# Error Boundaries

## Summary
Error boundaries are React components that catch errors thrown during rendering, in lifecycle methods, and in constructors of their subtree, then render a fallback instead of unmounting the whole app. They are the component-level complement to try/catch, which cannot handle render-time failures. React 19 adds error recovery options to the pattern.

## Details
- Mechanics: a class component implementing static getDerivedStateFromError and componentDidCatch becomes a boundary.
- Coverage: catches render, lifecycle, and constructor errors — but not event handlers, async code, or server-side errors.
- Placement: wrap route shells, feature modules, and third-party widgets so one failure degrades one region.
- Fallbacks: show a recoverable message with a reset button; boundaries can also report to error trackers via componentDidCatch.
- Boundaries do not catch everything: event-handler errors need try/catch; async errors need promise handling.
- Resilience: combined with monitoring, boundaries turn rare crashes into contained, observable incidents.

## Related
- [[wiki/frontend/component-composition|Component Composition]] — how boundaries wrap trees
- [[wiki/frontend/frontend-testing|Frontend Testing]] — testing fallback rendering
- [[wiki/devops-infra/observability|Observability]] — logging boundary catches
- [[wiki/devops-infra/log-aggregation|Log Aggregation]] — where boundary reports land
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — framework error models
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — resetting state after errors
