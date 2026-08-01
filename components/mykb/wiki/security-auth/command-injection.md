---
type: "concept"
title: "Command Injection"
description: "Attacker input executed as operating-system commands"
tags: ["command-injection", "injection", "os", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/attacks/Command_Injection"]
---

# Command Injection

- Command injection happens when untrusted input reaches a shell or exec call, letting attackers run arbitrary OS commands.
- Prevention: avoid shell execution entirely, use typed APIs with argument lists (no shell), and allowlist commands and arguments.
- Defense in depth: run services with least privilege and container isolation so even a successful injection is contained.
- For mykb: any agent tool that shells out must treat tool inputs as untrusted and never pass them to a shell string.

## Related

- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — sibling injection class
- [[wiki/security-auth/least-privilege|Least Privilege]] — containing the blast radius
- [[wiki/api-services/container-security|Container Security]] — isolation for executed code
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — agent tools that invoke commands
