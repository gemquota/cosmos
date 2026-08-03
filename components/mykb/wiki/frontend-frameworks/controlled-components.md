---
type: "concept"
title: "Controlled Components"
description: "Inputs whose value and updates are owned by React state"
tags: ["react", "forms", "components", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Controlled Components

## Summary
A controlled component is an input whose displayed value is owned by React state: the input's `value` prop comes from state, and every keystroke fires an `onChange` handler that updates that state, which re-renders the input with the new value. React is the single source of truth for the field, which makes validation, formatting, and cross-field logic natural but re-renders on every keystroke.

## Details
- Mechanism: the pattern is `value={stateValue} onChange={e => setStateValue(e.target.value)}`. Because the DOM input's value is always overwritten by the prop on render, the state and the field cannot drift apart — the input can never contain anything the app does not know about. That determinism is the whole point: validation can run on each change, derived values (character counts, enabled buttons) compute from the same state, and programmatic resets or prefills work by setting state.
- Concrete examples: a login form that disables submit until email matches a regex and password has 8+ characters; a credit-card input that formats digits and adds spaces as you type; a price field that filters non-numeric input at the handler; a rich-text editor where the value prop holds the serialized document and `onChange` saves edits. Form libraries like React Hook Form and Formik build controlled behavior with less boilerplate while keeping the same value-owned-by-state model.
- Failure modes: the classic failures are stale state in `onChange` (reading the old value because the update has not applied yet), synchronous formatting that fights the cursor position (replacing characters under the caret), and re-rendering huge trees per keystroke when the input's state lives high up. Controlled inputs that mutate state on every keystroke also make undo/redo and IME composition (Chinese/Japanese input) tricky, because intermediate composition states need careful handling.
- Operational tradeoffs: controlled inputs trade per-keystroke render cost for total determinism, which is the right deal for most forms; uncontrolled inputs (default values, refs) avoid re-renders but require imperative reads and lose the single-source-of-truth property. For large documents or high-frequency inputs, the fix is not to go uncontrolled but to colocate state, debounce expensive side effects, and use `useDeferredValue` or memoized field components to isolate the render cost.
- RSIS3/mykb relevance: controlled inputs are declarative single-source-of-truth discipline applied to the DOM; MyKB's search and article editors use the same model so the displayed query, the URL, and the daemon's search request always agree — mirroring RSIS3's rule that derived outputs never drift from their source state.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/uncontrolled-components|Uncontrolled Components]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/refs-practice|Refs in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/portals-practice|Portals in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/web-components|Web Components]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
