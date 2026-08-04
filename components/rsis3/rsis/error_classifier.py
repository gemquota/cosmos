"""Error classification for retry decisions (ported from Agent OS).

Distinguishes transient/retryable failures (network hiccups, 5xx) and rate
limits (429) from fatal/non-retryable failures (400, auth, syntax) so retry
policies can decide whether a retry is safe and effective.
"""

from __future__ import annotations

from enum import Enum
from typing import Union


class ErrorCategory(Enum):
    """Retry disposition for a failure."""

    TRANSIENT = "TRANSIENT"      # network hiccup, 5xx -> retry with backoff
    RATE_LIMIT = "RATE_LIMIT"    # 429 -> exponential backoff with jitter
    FATAL = "FATAL"              # 400/auth/syntax -> abort, never retry


# Exception types that are never worth retrying in-process.
_FATAL_TYPES = (TypeError, ValueError, SyntaxError, PermissionError)

_RATE_LIMIT_TOKENS = ("429", "rate limit", "throttled")
_FATAL_CODES = ("400", "401", "403", "404", "invalid_api_key",
                 "syntaxerror", "syntax error", "invalid syntax")
_TRANSIENT_TOKENS = (
    "500", "502", "503", "504",
    "timeout", "timed out", "temporary failure", "service unavailable",
    "bad gateway", "connection reset", "connection refused",
)


def classify_error_text(text: str) -> ErrorCategory:
    """Classify a stringified error message (e.g. a ToolCall.error)."""
    exc_str = (text or "").lower()

    # Rate limiting / throttling -> backoff and retry
    if any(tok in exc_str for tok in _RATE_LIMIT_TOKENS):
        return ErrorCategory.RATE_LIMIT

    # Explicit fatal client/auth failures -> abort immediately
    if any(code in exc_str for code in _FATAL_CODES):
        return ErrorCategory.FATAL

    # Explicit transient network/server failures -> retry
    if any(tok in exc_str for tok in _TRANSIENT_TOKENS):
        return ErrorCategory.TRANSIENT

    # Default: unknown failures are treated as transient (safe to retry)
    return ErrorCategory.TRANSIENT


def classify_error(exc: BaseException) -> ErrorCategory:
    """Classify an exception instance (AO-compatible signature)."""
    if isinstance(exc, _FATAL_TYPES):
        return ErrorCategory.FATAL
    return classify_error_text(str(exc))


def is_retryable(failure: Union[BaseException, str]) -> bool:
    """True when a failure may be retried safely."""
    category = (classify_error(failure)
                if isinstance(failure, BaseException)
                else classify_error_text(failure))
    return category in (ErrorCategory.TRANSIENT, ErrorCategory.RATE_LIMIT)
