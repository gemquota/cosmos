---
type: "concept"
title: "Template Injection"
description: "Server- or client-side template engines evaluating attacker-controlled expressions"
tags: ["security", "injection", "templates", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Template Injection

## Summary
Template injection (SSTI on the server, CSTI on the client) occurs when attacker-controlled input is interpolated into a template that the engine evaluates, letting the attacker run expressions with the template engine's privileges. What starts as a formatting bug — `Hello {{user.name}}` where the name is user-supplied — can end as remote code execution on the server.

## Details
- Mechanism: template engines like Jinja2, Twig, Velocity, and Angular evaluate expressions inside delimiters ({{ }}, ${ }, {{ }}). If user input lands in the template source rather than in the data passed to it, the engine treats it as code. In Jinja2, an input like `{{ 7*7 }}` renders 49, confirming evaluation, and a crafted chain such as `{{ ''.__class__.__mro__[1].__subclasses__() }}` walks Python's object model to reach dangerous classes and execute commands. Angular's client-side variant achieves XSS by injecting expressions evaluated in the client context.
- Concrete examples: a personalized greeting feature that builds `Hello {{ name }}` by concatenating the name into the template string; an email template editor where users can edit the template itself (intentionally or not) and escalate to file reads and command execution; a markdown or JSON renderer that passes user content through a template pass for "formatting"; client-side rendering frameworks that interpolate raw values into Angular expressions.
- Failure modes: sandboxes are the classic false defense — most engine sandboxes leak via object traversal, attribute access on `__class__`, or built-in functions that are not actually blocked, and bypass chains are published for every major engine. Escaping with the wrong context is the second failure: auto-escaping protects HTML output but not template evaluation, because the damage happens during parsing, before any escaping can apply. The subtlest failure is treating templates as a feature (user-editable themes) without realizing that templates are code by design.
- Operational tradeoffs: the secure pattern is to keep templates in trusted, version-controlled code and pass data as values only, never as source. If user-authored templates are a product requirement, run them in a real sandbox (a separate process with OS-level isolation, no filesystem, no network) and treat them as untrusted code with a tight capability budget, not as a configuration string. Static analysis that flags string concatenation into template calls and code review of every new interpolation point are the practical controls.
- RSIS3/mykb relevance: MyKB renders article content and search snippets; any template pass over stored content is a template-injection surface, so the renderer must treat article bodies as data and escape at output, mirroring RSIS3's rule that untrusted input never becomes executable structure.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/sql-injection-practice|SQL Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/xml-injection|XML Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/nosql-injection|NoSQL Injection]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
