"""Unit tests for rsis.error_classifier (ported from Agent OS)."""

from rsis.error_classifier import (
    ErrorCategory,
    classify_error,
    classify_error_text,
    is_retryable,
)


class TestClassifyText:
    def test_rate_limit_tokens(self):
        assert classify_error_text("429 Too Many Requests") is ErrorCategory.RATE_LIMIT
        assert classify_error_text("we are rate limited, retry later") is ErrorCategory.RATE_LIMIT
        assert classify_error_text("requests throttled") is ErrorCategory.RATE_LIMIT

    def test_fatal_codes(self):
        for msg in ("400 Bad Request", "invalid_api_key", "401 unauthorized",
                    "SyntaxError: invalid syntax"):
            assert classify_error_text(msg) is ErrorCategory.FATAL, msg

    def test_transient_tokens(self):
        for msg in ("500 Internal Server Error", "502 bad gateway",
                    "503 service unavailable", "connection reset",
                    "connection refused", "timed out", "temporary failure"):
            assert classify_error_text(msg) is ErrorCategory.TRANSIENT, msg

    def test_unknown_defaults_to_transient(self):
        assert classify_error_text("some random failure") is ErrorCategory.TRANSIENT


class TestClassifyError:
    def test_fatal_exception_types(self):
        for exc in (ValueError("bad"), SyntaxError("bad syntax"),
                    TypeError("bad type"), PermissionError("denied")):
            assert classify_error(exc) is ErrorCategory.FATAL

    def test_transient_by_message(self):
        assert classify_error(RuntimeError("503 service unavailable")) is ErrorCategory.TRANSIENT
        assert classify_error(ConnectionError("connection reset")) is ErrorCategory.TRANSIENT

    def test_rate_limit_by_message(self):
        assert classify_error(RuntimeError("429 rate limit")) is ErrorCategory.RATE_LIMIT


class TestIsRetryable:
    def test_retryable_strings(self):
        assert is_retryable("connection reset")
        assert is_retryable("429 rate limit")
        assert is_retryable("timed out")

    def test_retryable_exceptions(self):
        assert is_retryable(TimeoutError("connection timed out"))
        assert is_retryable(ConnectionError("connection reset"))

    def test_fatal_not_retryable(self):
        assert not is_retryable("400 bad request")
        assert not is_retryable(ValueError("nope"))
