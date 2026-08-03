---
type: "concept"
title: "Uncontrolled Components"
description: "Inputs whose value lives in the DOM until read via refs"
tags: ["react", "forms", "components", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Uncontrolled Components

## Summary
An uncontrolled component is an input whose value lives in the DOM rather than in React state: the input keeps its own internal value, and the component reads it on demand through a ref (`<input ref={inputRef} defaultValue="hi" />`). Because typing does not trigger re-renders, uncontrolled inputs are the cheapest way to handle large or high-frequency forms.

## Details
- Mechanism: with `defaultValue` and no `value` prop, React lets the DOM manage the input's value; `inputRef.current.value` reads it when needed (on submit, on blur, on demand). No `onChange` handler and no state update per keystroke means typing never re-renders the component tree. `defaultChecked`, `defaultValue`, and plain `<select>`/`<textarea>` all behave this way. This is also the foundation of React Hook Form's registration model — register stores a ref, and values are read from the DOM at the right moment.
- Concrete examples: a large document editor where controlled state per keystroke would re-render a heavy tree — uncontrolled inputs keep typing at native speed; a form with a hundred fields where values are only needed at submit; a file input whose value cannot be set programmatically anyway; a search-as-you-type box that reads the input's value on a debounced timer instead of re-rendering per key.
- Failure modes: the classic failure is losing the single source of truth: if other parts of the UI need to react to the input's value (a character count, an enabled submit button), an uncontrolled input hides it in the DOM and you end up re-reading imperatively or fighting stale values. Programmatic control also breaks: you cannot reset, prefill, or transform an uncontrolled input's value without imperative `setValue` calls, and validation errors cannot be computed from the value without reading it somewhere. Mixing `value` and `defaultValue` on the same input is a silent no-op that confuses everyone.
- Operational tradeoffs: uncontrolled inputs win on performance and simplicity for read-rarely, write-often fields; controlled inputs win on determinism and reactivity for fields whose value drives other UI. The modern default (React Hook Form's model) is a hybrid: uncontrolled inputs with registered refs, plus a form library that reads values and manages errors on its own schedule — the best of both. The rule: if the value matters to other UI, control it (or use a form library); if it only matters at submit, leave it uncontrolled.
- RSIS3/mykb relevance: the dashboard's article editor and search box face the same choice: read-on-demand (uncontrolled) keeps typing cheap, while controlled state is needed where the value drives derived UI (previews, counts) — matching RSIS3's principle of reading state only where and when it is needed.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/refs-practice|Refs in Practice]]
- [[wiki/frontend-frameworks/portals-practice|Portals in Practice]]
- [[wiki/frontend-frameworks/controlled-components|Controlled Components]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/web-components|Web Components]]
- [[wiki/web-platforms/state-management|State Management]]
