---
type: "concept"
title: "Form Validation"
description: "Constraint validation API and custom validation patterns"
tags: [forms", "validation", "html", "accessibility", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation", "https://web.dev/learn/forms/validation/"]
---

# Form Validation

## Summary
Form validation checks input before submission using the Constraint Validation API: required, min/max, pattern, and type constraints trigger built-in browser behavior. CSS pseudo-classes like :valid and :invalid style states, and setCustomValidity handles business rules the attributes cannot express. Accessible validation announces errors without trapping users.

## Details
- Native constraints: required, minlength, maxlength, min, max, step, pattern, and input type enforce rules without JavaScript.
- CSS states: :user-invalid styles after interaction; :valid and :invalid apply on every change.
- Custom validity: setCustomValidity adds messages for cross-field rules; validationMessage carries them to the UI.
- Submission: novalidate disables native blocking for custom flows; checkValidity and reportValidity drive JS validation.
- Accessibility: announce errors via aria-live, associate messages with fields via aria-describedby, and move focus to the first invalid field.
- Server parity: client validation is convenience; the server must always re-validate.

## Related
- [[wiki/frontend/html-forms|HTML Forms]] — the control model validation runs on
- [[wiki/frontend/aria|ARIA]] — announcing validation states
- [[wiki/frontend/wcag|WCAG]] — error identification criteria
- [[wiki/frontend/frontend-testing|Frontend Testing]] — testing validation flows
- [[wiki/frontend/state-machines|State Machines]] — modeling wizard and form flows
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — accessible error handling
