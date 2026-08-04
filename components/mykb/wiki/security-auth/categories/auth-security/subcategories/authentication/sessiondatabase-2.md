---
type: "entity"
title: "SessionDatabase"
resource: ""
---
description: "The store that persists sessions and their state across requests and restarts"
tags: ["android", "api", "ast", "auth", "authentication", "entity", "sessions", "database"]
timestamp: "2026-07-19T22:41:42Z"

# SessionDatabase

## Summary
A session database is the store that persists sessions and their state so that requests can be associated with a user across time, restarts, and replicas. It matters because in-memory session state breaks under restarts, load balancing, and multi-node deployments. A proper session store makes authentication and state durable and scalable, so it is a critical piece of the identity stack.

## Details
- **Definition** — a session database maps session identifiers to state such as user identity, expiry, and custom data.
- **Consistency** — sessions are read and written frequently, so the store must balance consistency, latency, and availability.
- **Expiry** — sessions need TTLs and cleanup so abandoned sessions do not accumulate into unbounded storage.
- **Revocation** — invalidating sessions on logout, password change, or compromise requires fast targeted deletes.
- **Scaling** — sharding by session ID and replicating for durability keep the store healthy as session volume grows.
- **Failover** — losing the session store logs everyone out; replication and recovery plans protect availability.
- **Common failure modes** — unbounded growth, stale sessions surviving revocation, and hot keys when one user has many sessions.
- **Worked example** — a login service writes a session row with a TTL; every authenticated request reads it, and logout deletes it before the TTL.
- **Practical relevance** — a durable session store is the foundation of reliable, scalable authentication.

- **Sessions vs tokens** — the store may hold full session state or only references, depending on whether state lives server-side or in the token.
- **Monitoring** — tracking store latency, size, and hit rates reveals when sessions become a bottleneck.
- **Security** — session records are sensitive; access, retention, and logging must follow the same rules as credentials.
## Related
- [[wiki/data-storage/sessionization-and-activity-windows|Sessionization and Activity Windows]] — session boundaries
- [[wiki/identity/session-management|Session Management]] — lifecycle and policy
- [[wiki/data-storage/logical-replication|Logical Replication]] — durable copies
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — expiry mechanics
- [[wiki/api-protocols/session-invalidation|Session Invalidation]] — revocation
- [[wiki/data-storage/backup-restore-and-pitr-revisited|Backup and Restore]] — recovery
