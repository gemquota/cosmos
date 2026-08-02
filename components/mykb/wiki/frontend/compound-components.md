---
type: "concept"
title: "Compound Components"
description: "Implicit state sharing among related components"
tags: [react", "compound-components", "context", "component-architecture", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/learn/passing-data-deeply-with-context", "https://www.radix-ui.com/primitives/docs/overview/introduction"]
---

# Compound Components

## Summary
Compound components are a set of related components that share implicit state through context — Tabs with TabList, Tab, and TabPanel, or Select with Trigger and Options. The parent provides state via context; children subscribe and wire themselves. Radix, Headless UI, and Reach popularized the pattern for accessible primitives.

## Details
- Structure: a root component owns state and exposes a context; child components consume it instead of receiving every prop.
- API ergonomics: consumers write <Tabs><TabList><Tab/></TabList><TabPanel/></Tabs> — readable, composable markup.
- Accessibility wiring: the root wires keyboard navigation, focus management, and ARIA attributes across children automatically.
- Flexibility: children render in any order and can include custom wrappers, unlike rigid configuration arrays.
- Costs: context re-renders can touch many consumers; memoization and state splitting mitigate it.
- Fit: tablists, accordions, menus, comboboxes, and steppers — anything where parts must stay in sync.

## Related
- [[wiki/frontend/component-composition|Component Composition]] — the composition model it extends
- [[wiki/frontend/prop-drilling|Prop Drilling]] — what context-based sharing avoids
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — implicit shared state
- [[wiki/frontend/design-systems|Design Systems]] — how libraries ship these APIs
- [[wiki/frontend/controlled-uncontrolled|Controlled vs Uncontrolled]] — state ownership options
- [[wiki/web-platforms/component-architecture|Component Architecture]] — component design context
