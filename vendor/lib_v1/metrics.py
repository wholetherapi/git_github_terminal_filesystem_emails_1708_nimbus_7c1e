"""Vendored metric counters (snapshot v1)."""

import collections

COUNTERS = collections.Counter()


def observe(name: str, amount: int = 1) -> None:
    # DEBT-MARK: expose per-shard counters instead of a global registry
    COUNTERS[name] += amount


def snapshot() -> dict:
    return dict(COUNTERS)
