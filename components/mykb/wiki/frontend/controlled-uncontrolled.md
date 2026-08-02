---
type: "concept"
title: "Controlled vs Uncontrolled"
description: "Managing component state internally or externally"
tags: [react", "forms", "state", "components", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/learn/sharing-state-between-components", "https://react.dev/reference/react-dom/components/input"]
---

# Controlled vs Uncontrolled

## Summary
Controlled components derive their displayed value from React state via value plus onChange; uncontrolled components let the DOM own the value and read it through refs. Controlled gives full programmatic control and validation on every change; uncontrolled is simpler and matches native behavior for forms that only need values on submit.

## Details
- Controlled: value={text} onChange={setText} — every keystroke flows through state, enabling live validation and cross-field logic.
- Uncontrolled: defaultValue plus a ref; the DOM tracks the value, reducing renders but hiding intermediate state.
- Hybrid: form libraries manage values internally and expose them on submit, combining both models.
- Keys matter: resetting an uncontrolled input requires remounting it (changing key) since the DOM ignores value afterward.
- Defaults: defaultValue and defaultChecked initialize uncontrolled inputs; controlled inputs always reflect state.
- Choice guide: use controlled when logic reacts to input; use uncontrolled (or library-managed) when submit-only data suffices.

## Related
- [[wiki/frontend/html-forms|HTML Forms]] — the native form model behind both
- [[wiki/frontend/form-validation|Form Validation]] — validation needs controlled values
- [[wiki/frontend/component-composition|Component Composition]] — how inputs fit components
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — who owns the value
- [[wiki/frontend/frontend-testing|Frontend Testing]] — firing change events in tests
- [[wiki/web-platforms/state-management|State Management]] — platform context
