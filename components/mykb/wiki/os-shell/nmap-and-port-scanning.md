---
type: "concept"
title: "nmap & Port Scanning"
description: "Scan types and host discovery"
tags: ["nmap", "scanning", "ports", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://nmap.org/book/man.html"]
---

# nmap & Port Scanning

## Summary
nmap discovers hosts and services by probing ports and fingerprinting responses. It is the standard tool for network inventory and security assessment, offering a spectrum of scan types from stealthy SYN scans to full service detection.

## Details
- Host discovery: nmap -sn 192.168.1.0/24 pings (and ARPs) the subnet to list live hosts.
- Scan types: -sS SYN scan (half-open), -sT full TCP connect, -sU UDP (slow, often filtered), -sA ACK scan (firewall mapping).
- Port selection: -p 22,80,443, -p- all 65535, --top-ports 1000; default is the top 1000.
- Service and OS detection: -sV version probes banners and responses; -O fingerprinting infers the OS (needs root and open ports).
- Timing: -T0 to -T5 trade stealth for speed; --min-rate and --max-retries tune noisy scans.
- NSE scripts: --script=vuln, http-title, or ssl-cert extend scans into automated checks.
- Output: -oN normal, -oG greppable, -oX XML feed other tools; results show state open/closed/filtered.
- Responsible use: scan only systems you own or have permission to test — scanning is detectable and often prohibited.

## Related
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — what nmap enumerates
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]] — handshake tricks behind SYN scans
- [[wiki/os-shell/netcat-and-raw-sockets|netcat & Raw Sockets]] — manual port probes
- [[wiki/os-shell/firewalls-and-netfilter|Firewalls & netfilter]] — what filters nmap's probes
- [[wiki/security-auth/threat-intelligence|Threat Intelligence]] — using scan results defensively
