---
type: "concept"
title: "Higher-Order Components"
description: "Component factories that wrap others to share logic"
tags: ["react", "patterns", "composition", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Higher-Order Components

## Summary
A higher-order component (HOC) is a function that takes a component and returns an enhanced component: `const withAuth = (Component) => (props) => ...`. HOCs were React's main logic-sharing tool before hooks — Redux's `connect`, React Router's `withRouter`, and many permission wrappers are HOCs — and they still appear in legacy codebases and libraries.

## Details
- Mechanism: a HOC wraps the input component, injects additional props (data, callbacks, styling), and renders it. Composition is by nesting: `withAuth(withTheme(Page))` applies wrappers outside-in, each layer seeing the props the previous layer provided. Because the wrapper is a normal component, it can subscribe to state, render a fallback (a login gate or a spinner), and forward the original props untouched, which keeps the wrapped component ignorant of the enhancement.
- Concrete examples: Redux `connect(mapState, mapDispatch)` injects state slices and action creators; a `withTracking` HOC wraps a button and fires analytics on click; an `withData` HOC fetches on mount and renders a spinner until data arrives; a permission HOC renders the child only when the user's role passes, otherwise showing an access-denied view. Libraries use HOCs when they need to attach behavior without requiring the consumer to call hooks at the top level.
- Failure modes: the classic pitfalls are prop name collisions (a HOC injects `data` that the component also receives from a parent, silently overwriting it), ref forwarding (the ref attaches to the wrapper, not the inner component, unless `forwardRef` is used), and static-method loss (wrapped components lose their class statics unless copied). HOC stacks also create deep, opaque component trees in the devtools, and ordering bugs — where two HOCs assume different prop shapes — are hard to trace.
- Operational tradeoffs: hooks supersede HOCs for most new code because they colocate logic, avoid wrapper nesting, and have no ref or static pitfalls; HOCs remain appropriate for library APIs that must work with class components, for cross-cutting behavior applied uniformly (e.g., wrapping every route), and for cases where the enhancement must be invisible to the wrapped component. The migration path is mechanical: most HOCs become `useX` hooks called inside the component, with the injected props replaced by hook returns.
- RSIS3/mykb relevance: the HOC-to-hooks migration is a case study in how explicit data flow beats invisible wrappers: RSIS3's own rule that dependencies should be visible and composable (functions over inheritance, wrappers over magic) is the same principle, keeping the dashboard's components traceable as features accumulate.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/context-api|Context API]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/composition-apis|Composition APIs]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/hooks-practice|Hooks in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
