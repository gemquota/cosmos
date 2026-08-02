---
type: "concept"
title: "DNS Resolution"
description: "Recursive lookup, record types, and resolv.conf"
tags: ["dns", "resolver", "records", "nameserver"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc1035", "https://man7.org/linux/man-pages/man5/resolv.conf.5.html"]
---

# DNS Resolution

## Summary
The Domain Name System maps hostnames to IP addresses (and much more) through a hierarchy of authoritative servers. A resolver walks that hierarchy — root, TLD, authoritative — caching answers according to TTL so the system scales to billions of queries.

## Details
- Record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (metadata/SPF), NS (authoritative servers), SOA (zone parameters).
- Resolution modes: recursive resolvers (typically ISP or 8.8.8.8) do the walking; iterative queries step through the hierarchy one level at a time.
- The client side reads /etc/resolv.conf for nameserver and search domains; systemd-resolved or NetworkManager manage it dynamically.
- Caching with TTLs keeps hot names fast; negative caching remembers NXDOMAIN answers for a while.
- nsswitch.conf (hosts: files dns) controls order: /etc/hosts wins locally, then DNS — the classic local-override mechanism.
- Modern hardening: DNS over TLS (853) and DNS over HTTPS encrypt queries, and DNSSEC validates answers against signed zones.
- Troubleshooting: dig +trace shows each step, and dig @server name type bypasses the cache to test directly.

## Related
- [[wiki/os-shell/dig-and-dns-tools|dig & DNS Tools]] — the query front end
- [[wiki/os-shell/udp-and-datagrams|UDP & Datagrams]] — DNS's usual transport (port 53)
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — where 53 fits
- [[wiki/cloud-infra/dns-management|DNS Management]] — zones and records at platform scale
- [[wiki/os-shell/tls-and-https|TLS & HTTPS]] — the encryption DNS-over-TLS provides
