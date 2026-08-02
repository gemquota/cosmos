---
type: "concept"
title: "Component Composition"
description: "Building UIs from composable parts"
tags: [components", "composition", "react", "architecture", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/learn/thinking-in-react", "https://react.dev/learn/passing-props-to-a-component"]
---

# Component Composition

## Summary
Component composition builds interfaces from small parts that own their data and behavior, assembled through children, slots, and props. Instead of configuration flags, layout components receive rendered content — the children pattern — which keeps leaf components dumb and parents structural. It is the core architectural idea behind modern component libraries.

## Details
- Containment: generic containers (Card, Modal) accept children or slots and never care what they render.
- Specialization: components wrap others with defaults — a PrimaryButton that renders a Button with variant props.
- Layout components: grid, stack, and split components compose space, separating structure from content.
- Props as data: data and callbacks flow down; events flow up, keeping direction predictable.
- Trade-off: composition over configuration means more JSX but less prop sprawl and better re-rendering behavior.
- Reuse: composed pieces are independently testable and replaceable, which is why design systems are composition-heavy.

## Related
- [[wiki/frontend/compound-components|Compound Components]] — implicit state among related parts
- [[wiki/frontend/render-props|Render Props]] — logic sharing through function props
- [[wiki/frontend/web-components|Web Components]] — native composition via slots
- [[wiki/frontend/design-systems|Design Systems]] — libraries built from compositions
- [[wiki/frontend/prop-drilling|Prop Drilling]] — the pain composition avoids
- [[wiki/web-platforms/component-architecture|Component Architecture]] — platform notes
