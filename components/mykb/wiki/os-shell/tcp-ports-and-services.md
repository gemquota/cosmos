---
type: "concept"
title: "TCP Ports & Services"
description: "Port ranges, well-known ports, and /etc/services"
tags: ["ports", "tcp", "services", "iana"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml", "https://man7.org/linux/man-pages/man5/services.5.html"]
---

# TCP Ports & Services

## Summary
Ports are 16-bit numbers that address services within a host: a TCP connection is (src IP, src port, dst IP, dst port). IANA divides the space into well-known, registered, and ephemeral ranges, and /etc/services maps names to numbers locally.

## Details
- Ranges: 0-1023 well-known (privileged, often root-only to bind), 1024-49151 registered, 49152-65535 dynamic/ephemeral.
- Common ports: 22 ssh, 53 dns, 80 http, 443 https, 3306 mysql, 5432 postgres, 6379 redis, 8080 http-alt, 8443 https-alt.
- /etc/services lists service-name/port/protocol for human lookup; getent services and ss -tlnp read it.
- The client's ephemeral source port comes from ip_local_port_range (default 32768-60999), the pool that exhausts under TIME_WAIT pressure.
- ss -tlnp shows listening sockets with process; netstat -tulpn is the legacy equivalent; both show local and peer endpoints.
- Binding below 1024 needs root or CAP_NET_BIND_SERVICE, which systemd services get declaratively.
- Scanning: nmap probes port lists to find services; a closed port replies RST, filtered means no reply.

## Related
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]] — connections are defined by ports
- [[wiki/os-shell/network-sockets|Network Sockets]] — the API that binds ports
- [[wiki/os-shell/http-basics|HTTP Basics]] — the service on 80/443
- [[wiki/os-shell/ssh-and-remote-access|SSH & Remote Access]] — the service on 22
- [[wiki/os-shell/firewalls-and-netfilter|Firewalls & netfilter]] — filtering by port
