"""Race-safe shared working memory for parallel agents (ported from Agent OS).

Three battle-tested concurrency patterns for shared registers:

  1. Fine-grained per-register mutexes — one ``threading.Lock`` per key, so
     workers serialize only the Read-Modify-Write cycle for the register
     they touch, never the whole memory store.
  2. Optimistic Concurrency Control (OCC) — every register carries a
     monotonic ``version``; ``compare_and_swap()`` raises
     ``MemoryConflictError`` when the version moved, so the caller re-reads
     and retries.
  3. Atomic mutation — ``atomic_mutate()`` runs ``mutate_fn(old_value)``
     while holding the key lock, eliminating lost updates entirely.

The AO original is asyncio-based; this sync-first port uses
``threading.Lock`` so it is safe from the thread-pool dispatchers and from
tool/HTTP threads alike.
"""

from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)


class MemoryConflictError(Exception):
    """Raised when an optimistic update fails due to a version mismatch."""


@dataclass
class MemoryRegister:
    """One versioned register in shared working memory."""

    key: str
    value: Any
    version: int = 1
    updated_at: float = field(default_factory=time.time)
    updated_by: str = "system"


class SharedMemoryManager:
    """Thread-safe working memory with fine-grained locking + OCC."""

    def __init__(self) -> None:
        self._registers: dict[str, MemoryRegister] = {}
        self._locks: dict[str, threading.Lock] = {}
        self._dict_lock = threading.Lock()    # protects dict bookkeeping
        self._global_lock = threading.Lock()  # serializes lock creation

    # ------------------------------------------------------------------ #
    def _get_key_lock(self, key: str) -> threading.Lock:
        """Fetch (or lazily create) the dedicated lock for a register key."""
        with self._global_lock:
            with self._dict_lock:
                if key not in self._locks:
                    self._locks[key] = threading.Lock()
                return self._locks[key]

    @staticmethod
    def _copy(reg: MemoryRegister) -> MemoryRegister:
        """Immutable snapshot so callers cannot mutate stored state."""
        return MemoryRegister(key=reg.key, value=reg.value,
                              version=reg.version,
                              updated_at=reg.updated_at,
                              updated_by=reg.updated_by)

    # --- PATTERN 1: snapshot reads + exclusive writes ----------------- #
    def read(self, key: str) -> Optional[MemoryRegister]:
        """Read a register snapshot (no blocking for other readers)."""
        lock = self._get_key_lock(key)
        with lock:
            with self._dict_lock:
                reg = self._registers.get(key)
                return self._copy(reg) if reg else None

    def write(self, key: str, value: Any, agent_id: str) -> MemoryRegister:
        """Direct write with an exclusive key-level lock."""
        lock = self._get_key_lock(key)
        with lock:
            with self._dict_lock:
                existing = self._registers.get(key)
                version = (existing.version + 1) if existing else 1
                reg = MemoryRegister(key=key, value=value,
                                     version=version,
                                     updated_at=time.time(),
                                     updated_by=agent_id)
                self._registers[key] = reg
                return self._copy(reg)

    # --- PATTERN 2: optimistic concurrency control (CAS) -------------- #
    def compare_and_swap(self, key: str, expected_version: int,
                         new_value: Any, agent_id: str) -> MemoryRegister:
        """Update only when the version still matches; else raise."""
        lock = self._get_key_lock(key)
        with lock:
            with self._dict_lock:
                existing = self._registers.get(key)
                current = existing.version if existing else 0
                if current != expected_version:
                    raise MemoryConflictError(
                        f"Conflict on register [{key}]: expected version "
                        f"{expected_version}, found {current} "
                        f"(last writer: {existing.updated_by if existing else 'unknown'}).")
                reg = MemoryRegister(key=key, value=new_value,
                                     version=current + 1,
                                     updated_at=time.time(),
                                     updated_by=agent_id)
                self._registers[key] = reg
                return self._copy(reg)

    # --- PATTERN 3: atomic read-modify-write --------------------------- #
    def atomic_mutate(self, key: str,
                      mutate_fn: Callable[[Any], Any],
                      agent_id: str) -> MemoryRegister:
        """Run `mutate_fn(old_value)` atomically under the key lock."""
        lock = self._get_key_lock(key)
        with lock:
            with self._dict_lock:
                existing = self._registers.get(key)
                current = existing.value if existing else None
                new_value = mutate_fn(current)
                version = (existing.version + 1) if existing else 1
                reg = MemoryRegister(key=key, value=new_value,
                                     version=version,
                                     updated_at=time.time(),
                                     updated_by=agent_id)
                self._registers[key] = reg
                return self._copy(reg)

    # ------------------------------------------------------------------ #
    def snapshot(self) -> dict[str, MemoryRegister]:
        """Serializable snapshot (thread-safe; for reports/resume)."""
        with self._dict_lock:
            return {k: self._copy(v) for k, v in self._registers.items()}

    def clear(self) -> None:
        with self._dict_lock:
            self._registers.clear()
