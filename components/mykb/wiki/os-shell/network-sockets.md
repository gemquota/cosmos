---
type: "concept"
title: "Network Sockets"
description: "Socket API, address families, and connection semantics"
tags: ["sockets", "socket-api", "tcp", "udp", "ipc"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/socket.2.html", "https://man7.org/linux/man-pages/man7/socket.7.html"]
---

# Network Sockets

## Summary
The socket API is how programs speak to the network: socket(2) creates an endpoint, bind(2) gives it an address, and connect/listen/accept establish or receive connections. The same calls cover TCP, UDP, and Unix domain sockets.

## Details
- socket(domain, type, protocol): AF_INET/AF_INET6 for IP, AF_UNIX for local; SOCK_STREAM for TCP-like, SOCK_DGRAM for datagrams.
- Server flow: socket, bind to a port, listen with a backlog, then accept returns a new socket per connection.
- Client flow: socket, connect to (addr, port); connect on TCP triggers the handshake, on UDP just sets the default peer.
- Blocking versus non-blocking: default calls block; O_NONBLOCK makes them return EAGAIN/EWOULDBLOCK, driving event loops.
- Options: SO_REUSEADDR (rebind quickly after TIME_WAIT), SO_KEEPALIVE, SO_LINGER, TCP_NODELAY disable Nagle.
- The socket is a file descriptor: dup, close, and pass between processes; poll/select/epoll wait on many sockets at once.
- getsockname/getpeername and /proc/net/tcp expose endpoint state; ss shows the same data in human form.

## Related
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]] — the state machine sockets drive
- [[wiki/os-shell/udp-and-datagrams|UDP & Datagrams]] — SOCK_DGRAM semantics
- [[wiki/os-shell/unix-domain-sockets|Unix Domain Sockets]] — the same API without IP
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — addressing with ports
- [[wiki/os-shell/http-basics|HTTP Basics]] — the protocol on top of sockets
