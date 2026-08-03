---
type: "concept"
title: "XML Injection"
description: "Inserting markup or entities into XML documents and parsers"
tags: ["security", "injection", "xml", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# XML Injection

## Summary
XML injection is the insertion of markup, attributes, or entity declarations into XML that an application builds or parses, so that the attacker alters the document's structure or abuses the parser itself. The family spans classic XML tampering (breaking out of a field to inject new elements) and the far more dangerous XXE (XML External Entity) attacks, where a crafted document makes the parser read local files or hit internal URLs.

## Details
- Mechanism: when an application builds XML by concatenating user input into a template, an input containing `</value><admin>true</admin><value>` escapes its intended field and injects new elements, which downstream logic may trust. The parser-side variant exploits the DTD: a document declaring `<!ENTITY xxe SYSTEM "file:///etc/passwd">` and referencing `&xxe;` makes an unconfigured parser expand the entity by reading the file into the document, which the application then returns or logs. External entities can also target `http://169.254.169.254/...` metadata endpoints, turning XML parsing into an SSRF primitive, and billion-laughs style entity nesting turns a tiny document into a multi-gigabyte expansion that exhausts memory.
- Concrete examples: an API that accepts XML configs and renders them into a UI leaks `file:///etc/passwd` contents through the rendered response; a SOAP endpoint with a default parser performs internal port scans via external entities; an import tool that accepts XML exports lets a crafted file overwrite document structure so an authorization check reads a different field than the one the attacker controls.
- Failure modes: the root failure is a parser that resolves DTDs and external entities at all — most libraries enable them by default for legacy compatibility. Escaping input with character substitution is fragile because XML has multiple contexts (elements, attributes, CDATA, comments), and escaping for one context fails in another. Even "safe" parsers can leak through error messages that echo the document, and log injection rides the same channel when user-controlled text is written into XML-shaped logs.
- Operational tradeoffs: the robust answer is to disable DTDs and external entities explicitly in every XML parser configuration (`defusedxml` in Python, secure processor settings in Java, `LIBXML_NONET` elsewhere), and prefer libraries that are safe by default. If XML must be accepted, validate it against a schema that whitelists allowed structure, and never emit raw user input into XML without context-appropriate escaping. The strategic question — when XML is worth choosing over JSON — comes down to ecosystems that still require it (SOAP, SVG, XSLT, some legacy B2B), where the added security surface must be paid for with hardened parsers and strict validation.
- RSIS3/mykb relevance: MyKB ingests and exports structured artifacts; any XML-capable path in the pipeline should apply the same hardened-parser rule, treating documents as data, never as structure to trust, so an uploaded artifact cannot become a file-read or SSRF primitive inside the memory layer.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/nosql-injection|NoSQL Injection]]
- [[wiki/api-protocols/second-order-injection|Second-Order Injection]]
- [[wiki/api-protocols/blind-injection|Blind Injection]]
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]]
- [[wiki/security-auth/command-injection|Command Injection]]
- [[wiki/security-auth/ldap-injection|LDAP Injection]]
