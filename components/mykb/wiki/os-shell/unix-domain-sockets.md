---
type: "concept"
title: "Unix Domain Sockets"
description: "Local IPC via socket files, stream vs datagram modes"
tags: ["unix-sockets", "ipc", "socket", "localhost", "af-unix"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/unix.7.html"]
---

# Unix Domain Sockets

## Summary
Unix domain sockets (AF_UNIX) connect processes on the same host through the filesystem or the abstract namespace, without IP or routing. They are the fastest general-purpose local IPC and the transport behind many system services.

## Details
- SOCK_STREAM sockets behave like TCP but with no network stack; SOCK_DGRAM sockets preserve message boundaries without the overhead of UDP.
- Pathname sockets appear as filesystem entries (mode socket, shown as s by ls) and require directory permissions; abstract sockets use a leading null byte and leave no file.
- The kernel can pass auxiliary data with sendmsg: SCM_RIGHTS hands file descriptors, SCM_CREDENTIALS authenticates the sender's uid/gid/pid.
- A listening socket accepts connections; the listen backlog matters because clients block when it fills.
- Performance beats TCP loopback by avoiding checksums, segmentation, and routing, and data can be copied with sendfile-style tricks.
- systemd-journald, D-Bus, and syslog use Unix sockets; containers rely on them for intra-host service IPC.
- Debugging tools: ss -x lists socket files, and socketpair(2) creates an anonymous connected pair for pipes-like IPC.

## Related
- [[wiki/os-shell/network-sockets|Network Sockets]] — the same API over IP
- [[wiki/os-shell/file-descriptors|File Descriptors]] — sockets are fds and pass fds
- [[wiki/os-shell/named-pipes-fifos|Named Pipes (FIFOs)]] — the message-less sibling
- [[wiki/os-shell/systemd-journal|systemd-journal]] — a datagram Unix-socket consumer
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — socket files on tmpfs mounts
