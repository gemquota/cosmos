---
type: "concept"
title: "Message Queues"
description: "POSIX/SysV queues, message boundaries, and priorities"
tags: ["message-queues", "ipc", "posix", "sysv", "queues"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/mq_overview.7.html", "https://man7.org/linux/man-pages/man2/msgget.2.html"]
---

# Message Queues

## Summary
Message queues pass discrete, typed messages between processes, preserving boundaries and (in the POSIX flavor) priorities. They sit between pipes, which are boundary-less byte streams, and shared memory, which needs explicit synchronization.

## Details
- POSIX queues are named objects under /dev/mqueue, created with mq_open, sent with mq_send, and received with mq_receive; they support priority values 0-31.
- SysV queues are identified by keys via msgget and use msgsnd/msgrcv with a message type field for selective reads.
- Every message carries a length and (POSIX) priority; receivers can block or use timeout versions (mq_timedreceive, msgrcv with MSG_NOERROR).
- Kernel limits apply: /proc/sys/fs/mqueue/msg_max caps messages per queue, and SysV has msgmni/msgmax tunables.
- Notification: mq_notify lets a process get SIGEV signals when a message arrives, enabling event-driven consumers.
- Queues are slower than shared memory because the kernel copies each message, but they add structure and don't require locks.
- For distributed equivalents, see broker patterns: same queue semantics over the network.

## Related
- [[wiki/os-shell/shared-memory|Shared Memory]] — the faster but unstructured alternative
- [[wiki/os-shell/named-pipes-fifos|Named Pipes (FIFOs)]] — boundary-less byte streams
- [[wiki/os-shell/semaphores|Semaphores]] — synchronization for queue consumers
- [[wiki/api-protocols/message-queues|Message Queues]] — the distributed abstraction
- [[wiki/os-shell/process-groups-and-sessions|Process Groups & Sessions]] — who owns the consuming processes
