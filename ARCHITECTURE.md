# COSMOS — Architecture

## System Context

```
┌────────────────────────────────────────────────────────────┐
│                    COSMOS Ecosystem                         │
│                                                             │
│  ┌──────────┐  ┌────────────────────────────────────────┐ │
│  │          │  │           Shared Infrastructure         │ │
│  │   CLI    │  │  ┌──────────┐ ┌──────┐ ┌──────────┐   │ │
│  │ (cosmos) │──┼─▶│ Heartbeat│ │ CI/CD│ │Dashboard │   │ │
│  │          │  │  └──────────┘ └──────┘ └──────────┘   │ │
│  └──────────┘  └────────────────────────────────────────┘ │
│       │                                                    │
│       │ controls                                           │
│       ▼                                                    │
│  ┌──────────────────────────────────────────────────┐     │
│  │                   Components                      │     │
│  │  ┌───────┐ ┌──────┐ ┌───────┐ ┌────────┐ ┌───┐  │     │
│  │  │ SPACE │ │ myKB │ │myRSIKB│ │myRSISKB│ │RSIS3│  │     │
│  │  │  TS   │ │MD/Py │ │  Py   │ │  Py    │ │ Py  │  │     │
│  │  └───────┘ └──────┘ └───────┘ └────────┘ └───┘  │     │
│  └──────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────┘
```

## Component Communication

| From | To | Mechanism | Data |
|------|----|-----------|------|
| SPACE | myKB | File export | Spec documents → wiki pages |
| myKB | myRSISKB | File read | Knowledge → bridge processing |
| RSIS3 | myRSISKB | API/file | RSI outputs → bridge processing |
| myRSISKB | myKB | File write | Processed insights → wiki |
| Dashboard | All | HTTP health check | Status polling |

## Deployment Model

```
GitHub ──► CI/CD ──► Build ──► GitHub Pages / Local Servers
                                      │
                                      ▼
                              Sentry Heartbeat
                              (auto-restart on failure)
```
