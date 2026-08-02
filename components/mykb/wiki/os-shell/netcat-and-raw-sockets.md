---
type: "concept"
title: "netcat & Raw Sockets"
description: "Port checks, piping, and ad-hoc connections"
tags: ["netcat", "sockets", "network", "debugging"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/nc.1.html"]
---

# netcat & Raw Sockets

## Summary
netcat (nc) opens raw TCP or UDP connections from the command line: connect to a port, listen on one, or pipe data in both directions. It is the Swiss-army knife for port checks, quick file transfers, and speaking protocols by hand.

## Details
- Connect: nc -vz host 22 checks whether a port accepts connections; -z scans without sending data, -v reports verbosely.
- Listen: nc -l 8080 accepts one connection and echoes stdin to it; a poor man's test server.
- Transfer: cat file | nc -l 9000 on one host and nc host 9000 > file on the other streams data without ssh.
- UDP mode: nc -u host 53 sends datagrams for protocol testing; note UDP has no connect confirmation.
- Speaking protocols: printf 'GET / HTTP/1.0

' | nc host 80 issues raw HTTP; nc host 25 talks SMTP.
- socat is the advanced cousin: it connects sockets of different kinds (unix, tcp, ssl) and forwards streams.
- Security: a listening nc is a backdoor in disguise — never leave one bound to a public interface; prefer ssh tunnels for real work.

## Related
- [[wiki/os-shell/network-sockets|Network Sockets]] — the API netcat wraps
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — what -z probes
- [[wiki/os-shell/nmap-and-port-scanning|nmap & Port Scanning]] — the proper scanner
- [[wiki/os-shell/unix-domain-sockets|Unix Domain Sockets]] — nc -U for local sockets
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]] — verifying what nc sends
