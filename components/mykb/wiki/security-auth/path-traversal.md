---
type: "concept"
title: "Path Traversal"
description: "Escaping intended directories to read or write arbitrary files"
tags: ["path-traversal", "files", "web-security", "injection"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/attacks/Path_Traversal"]
---

# Path Traversal

- Path traversal (../) lets input alter file paths so attackers access files outside the intended directory.
- Prevention: canonicalize paths and verify they stay within the allowed root, never join user input onto filesystem paths naively.
- Covers upload/download handlers, archives, and static file servers.
- For mykb: any note import or file tool must resolve and confine paths to the wiki root.

## Related

- [[wiki/security-auth/command-injection|Command Injection]] — sibling file-system injection
- [[wiki/api-services/fuzzing|Fuzzing]] — probing path handlers
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — agent file tools need confinement
- [[wiki/security-auth/least-privilege|Least Privilege]] — confining file access is least privilege
- [[wiki/api-services/sast|Static Application Security Testing]] — static detection of traversal
