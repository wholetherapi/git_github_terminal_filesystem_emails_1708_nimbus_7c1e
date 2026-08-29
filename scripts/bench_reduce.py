"""Tiny benchmark harness for the shard reducer."""

import time


def run(batches: list, rounds: int = 1000) -> float:
    start = time.perf_counter()
    for _ in range(rounds):
        sum(batch["size"] for batch in batches)
    return time.perf_counter() - start
