---
type: "concept"
title: "HTML Forms"
description: "Form controls, submission, and serialization"
tags: [html", "forms", "web-platform", "input", "serialization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form", "https://html.spec.whatwg.org/multipage/forms.html"]
---

# HTML Forms

## Summary
HTML forms collect user input through controls — input, select, textarea, button — and submit name/value pairs to a server. The form element defines the action, method, and encoding; native submission serializes fields automatically. Understanding the native model matters because every framework form eventually maps to it.

## Details
- Controls: input types (text, email, number, date, checkbox, radio, file), select menus, and textareas carry name attributes.
- Submission: method GET puts values in the query string; POST sends them in the body; enctype selects urlencoded, multipart, or text/plain.
- FormData: the FormData API captures form values in JavaScript for fetch-based submission without reloads.
- Labels: label elements associate text with controls, enlarging click targets and naming them for assistive tech.
- Attributes: autocomplete, placeholder, required, pattern, and disabled shape behavior; autofocus and tabindex control entry.
- Structure: fieldset and legend group related controls, improving comprehension and accessibility.

## Related
- [[wiki/frontend/form-validation|Form Validation]] — the constraint model on top of forms
- [[wiki/frontend/semantic-html|Semantic HTML]] — forms as semantic structure
- [[wiki/frontend/fetch-api|Fetch API]] — submitting forms via JavaScript
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — form operability
- [[wiki/web-platforms/web-apis|Web APIs]] — the platform APIs around forms
- [[wiki/frontend/controlled-uncontrolled|Controlled vs Uncontrolled]] — framework form state
