"""Vendored utility helpers (snapshot v2)."""

import time

DEFAULT_RETRIES = 4
BACKOFF_BASE = 0.25


def retry_call(fn, attempts: int = DEFAULT_RETRIES):
    # DEBT-MARK: replace hand-rolled retry loop with shared backoff helper
    delay = BACKOFF_BASE
    for attempt in range(attempts):
        try:
            return fn()
        except Exception:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)
            delay *= 2


def chunked(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]
