---
type: "concept"
title: "dig & DNS Tools"
description: "dig/nslookup/host query workflows"
tags: ["dig", "dns", "nslookup", "host"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/dig.1.html", "https://man7.org/linux/man-pages/man1/host.1.html"]
---

# dig & DNS Tools

## Summary
dig is the DNS query tool with the most control: it asks a chosen server for a chosen record type and shows the full answer, authority, and additional sections. host and nslookup are simpler front ends for quick lookups.

## Details
- Basics: dig example.com shows A records with TTLs; dig example.com MX queries a specific type; AAAA, TXT, NS, SOA work the same.
- Server selection: dig @1.1.1.1 example.com bypasses the local resolver; dig +trace walks root to authoritative to prove delegation.
- Output control: +short prints bare answers; +noall +answer hides headers; +tcp forces TCP (useful to test truncated UDP responses).
- Reverse lookups: dig -x 8.8.8.8 maps an address back to a name via PTR records.
- Checking propagation: query different resolvers and compare TTLs; dig +dnssec shows RRSIG records to verify DNSSEC.
- host is the terse variant: host example.com, host -t MX example.com; nslookup is the legacy tool with interactive mode.
- Common diagnostics: NXDOMAIN (name missing), SERVFAIL (server problem), and timeout (no response) each point at different causes.

## Related
- [[wiki/os-shell/dns-resolution|DNS Resolution]] — the protocol being queried
- [[wiki/os-shell/udp-and-datagrams|UDP & Datagrams]] — DNS's usual transport
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — port 53 details
- [[wiki/cloud-infra/dns-management|DNS Management]] — zones managed at scale
- [[wiki/os-shell/icmp-and-network-diagnostics|ICMP & Diagnostics]] — the broader diagnostic toolkit
