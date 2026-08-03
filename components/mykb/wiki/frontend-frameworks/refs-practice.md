---
type: "concept"
title: "Refs in Practice"
description: "Imperative DOM access and stable identity via refs"
tags: ["react", "refs", "dom", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Refs in Practice

## Summary
Refs are React's escape hatch to the imperative world: a `useRef()` object holds a stable `.current` that survives re-renders and can point at a DOM node, a component instance, or any mutable value. They are for the cases declarative props cannot express — focusing an input, measuring a node, storing an interval handle, or holding the previous value of state.

## Details
- Mechanism: `useRef(initial)` returns a mutable object whose `.current` persists across renders; attaching it to a JSX element (`<input ref={inputRef} />`) populates `.current` with the DOM node after mount. Ref *callbacks* (`ref={(node) => ...}`) run on mount and unmount (with `null` on cleanup), which makes them the reliable way to observe node lifecycles. `forwardRef` passes a ref through to a child's DOM node, and `useImperativeHandle` exposes a custom imperative API from a child. Because refs do not trigger re-renders when `.current` changes, they are ideal for values that must be read imperatively without causing updates.
- Concrete examples: focusing a search input on mount or after a button click; measuring an element's bounding rect for a tooltip position; storing a `setInterval` handle so cleanup can clear it; keeping the previous props for comparison in a layout effect; integrating with imperative libraries (video players, maps, charting) that need a DOM node to initialize.
- Failure modes: the classic failures are reading `.current` too early (before mount, or after unmount — both give `null`), relying on refs for state that other components must react to (ref changes do not notify anyone; that is state's job), and stale ref callbacks in older code that recreate closures on each render. Refs that point at DOM inside portals or fragments need care, because the node belongs to a different tree, and refs to components only work on class components or via `forwardRef`.
- Operational tradeoffs: refs are the right tool for imperative interop and stable identity, and the wrong tool for anything reactive — the boundary is the question "does the rest of the UI need to know?" If yes, use state; if no, a ref is cheaper. The modern guidance is to minimize refs: prefer derived values, effects, and controlled props, and reserve refs for genuinely imperative cases, keeping every ref's lifecycle (set, read, cleanup) inside the component that owns it.
- RSIS3/mykb relevance: refs are a controlled escape hatch — imperative access exactly where it is needed, bounded and explicit; RSIS3 applies the same principle to loop hooks that touch external systems, keeping imperative operations isolated instead of scattering them through declarative flows.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/portals-practice|Portals in Practice]]
- [[wiki/frontend-frameworks/controlled-components|Controlled Components]]
- [[wiki/frontend-frameworks/uncontrolled-components|Uncontrolled Components]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/web-components|Web Components]]
- [[wiki/web-platforms/state-management|State Management]]
