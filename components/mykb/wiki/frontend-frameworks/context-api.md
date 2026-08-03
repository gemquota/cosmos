---
type: "concept"
title: "Context API"
description: "Prop-drilling-free sharing of values through a component tree"
tags: ["react", "context", "state", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Context API

## Summary
React's Context API lets a component provide a value that any descendant can read without passing it through every intermediate level as a prop. It is the built-in answer to prop drilling for things like themes, locales, current user, or feature flags — values that many components need but few change.

## Details
- Mechanism: a context is created with `createContext(defaultValue)`; a provider (`<MyContext.Provider value={...}>`) makes the value available to its subtree, and consumers read it with `useContext(MyContext)` or the `<MyContext.Consumer>` render-prop form. When the provider's value changes, every consumer in the subtree re-renders — context has no built-in granularity, so the whole consuming component re-renders even if it reads only one field of a large value. The default value is used when a consumer has no provider above it, which makes testing components in isolation easy but can silently hide missing providers.
- Concrete examples: a theme provider exposes `{ theme, toggleTheme }` to every button and card; an auth provider exposes the user object and login/logout actions so any screen can gate on authentication; a locale provider supplies translations and a formatter. Libraries use it too: React Router's router, Redux's `Provider`, and TanStack Query's `QueryClientProvider` all rely on context to give nested components access without prop threading.
- Failure modes: the classic failures are over-use (putting frequently-changing state like form values or a ticking timer in context, so the entire app re-renders on every change), value instability (creating a new object literal `value={{...}}` on every provider render, defeating memoization and re-rendering all consumers even when nothing meaningful changed), and shallow-read blindness (a consumer reading one field of a big object still re-renders on any field change). Missing providers surface late, as default values that look correct in tests but wrong in production.
- Operational tradeoffs: context is a dependency-injection mechanism, not a state-management system — it excels for stable, widely-shared values and is poor for high-frequency state. Split contexts (separate context per concern: theme, auth, locale), memoized values with `useMemo`, and moving state into selectors or stores all reduce the re-render blast radius. The rule of thumb: if a value changes rarely, context is ideal; if it changes often and many components read it, a store with selectors is a better fit.
- RSIS3/mykb relevance: the unified dashboard passes shared context (selected pulse, active article, daemon status) to embedded views; treating that as stable context with memoized values keeps the wiki browser and graph responsive, mirroring RSIS3's rule that shared state should change rarely and propagate explicitly.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/composition-apis|Composition APIs]]
- [[wiki/frontend-frameworks/hooks-practice|Hooks in Practice]]
- [[wiki/frontend-frameworks/hoc-patterns|Higher-Order Components]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
