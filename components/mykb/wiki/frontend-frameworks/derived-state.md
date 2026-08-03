---
type: "concept"
title: "Derived State"
description: "Computing values from source state instead of duplicating it"
tags: ["state", "derivation", "frontend", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Derived State

## Summary
Derived state is any value computed from source state rather than stored alongside it: a filtered list derived from the raw list and the filter, a total derived from line items, a `isFormValid` derived from field values. The rule is to keep one source of truth and derive everything else, because every duplicated value is an opportunity for the copies to disagree.

## Details
- Mechanism: a derived value is recomputed during render from the source state (`const visibleItems = items.filter(i => i.matches(filter))`), so it is always correct by construction. Memoization (`useMemo`) skips recomputation when the sources are unchanged, and signal-based frameworks derive with `computed` so invalidation is automatic and lazy. Storing the derived value as state (`setFilteredItems(...)` inside an effect that watches `items`) duplicates truth: two effects may disagree, the stored copy can go stale, and the update adds an extra render pass.
- Concrete examples: a todo app derives `completedCount` from the todos array and the `activeFilter` view from todos plus filter; a cart computes the total and item count from line items; a settings form derives `canSubmit` from field validity, so the button always reflects the current fields without a separate `setCanSubmit` call. Selector libraries (Redux `createSelector`, Zustand selectors) move the same derivation into the store layer with memoization, so many components share one derived computation.
- Failure modes: the classic failures are derived state stored as real state (stale copies, update loops), derivations with side effects (filtering inside an effect that then sets state, causing re-render and re-effect churn), and expensive derivations recomputed for unrelated renders when memoization deps are wrong — too broad (recompute on every render) or too narrow (stale results). Derived state that reads multiple sources also tempts "compute in event handler" shortcuts that skip reactive updates entirely.
- Operational tradeoffs: pure derivation is cheap to reason about but can be expensive to compute, which memoization and selectors solve at the cost of dependency-array discipline. The design question is where derivation lives: in the component (fine for local UI state), in a memoized selector (shared, cached, testable), or in the server/backend (when the derivation is business logic or needs the full dataset). Moving derivation to the store centralizes it but adds store complexity for values only one component needs.
- RSIS3/mykb relevance: MyKB's graph stats and RSIS3's success rates are derived from pulse data; computing them with memoized selectors from the raw records, never storing them as independent state, keeps the dashboard consistent with the source of truth and matches the loop hygiene rule that telemetry aggregates are always recomputed from raw telemetry.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/selectors-practice|Selectors in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/memoization-practice|Memoization Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/use-callback|useCallback]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — related coverage in the same cluster
