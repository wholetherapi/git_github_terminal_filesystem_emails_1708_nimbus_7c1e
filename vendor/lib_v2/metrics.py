"""Vendored metric counters (snapshot v2)."""

import collections

COUNTERS = collections.Counter()


def observe(name: str, amount: int = 1) -> None:
    # DEBT-MARK: emit counters through the shared telemetry sink
    COUNTERS[name] += amount


def snapshot() -> dict:
    return dict(COUNTERS)
