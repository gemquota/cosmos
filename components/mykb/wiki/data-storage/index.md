## Overview

The **Data Storage** domain (1 concepts) covers database and caching technologies. The preference is for lightweight, embedded solutions with production-ready alternatives.

### Key Technologies

- **SQLite** — primary embedded database for local development
- **PostgreSQL** — production database with full ACID compliance
- **SQLAlchemy** — Python ORM for database abstraction
- **Redis** — in-memory cache and message broker
- **Alembic** — database migration management

### Data Patterns

1. SQLite for single-user agent data and wiki storage
2. PostgreSQL for multi-user production services
3. Redis for session caching and rate limiting
4. ORM-first approach with SQLAlchemy model definitions


---

## Entities by Sub-Group

### Caching

- [CACHE](../../wiki/entities/cache.md)
