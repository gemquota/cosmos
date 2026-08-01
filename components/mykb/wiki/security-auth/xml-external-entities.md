---
type: "concept"
title: "XML External Entities"
description: "XXE attacks abusing XML entity expansion to read files or trigger SSRF"
tags: ["xxe", "xml", "injection", "parsers"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing"]
---

# XML External Entities

- XXE exploits XML parsers that resolve external entities, letting attackers read local files, probe internal networks (SSRF), or cause billion-laughs resource exhaustion.
- Prevention: disable DTD and external entity resolution in every XML parser; prefer JSON where possible.
- Legacy formats (SAML metadata, SOAP, office documents) are common XXE surfaces.
- For mykb: XML parsing of SAML and metadata should run with entities and DTDs fully disabled.

## Related

- [[wiki/identity/saml-assertions|SAML Assertions]] — XML payloads that must parse safely
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — XXE can trigger server-side requests
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — other parser-based attack class
- [[wiki/api-services/sast|Static Application Security Testing]] — scanning parser configuration
