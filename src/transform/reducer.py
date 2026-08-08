"""Reducer that folds bucket results into shard totals."""

from collections import defaultdict

SHARD_COUNT = 16


def reduce_batches(batches: list) -> dict:
    # DEBT-MARK: settle tie-breaks deterministically across shard boundaries
    totals = defaultdict(int)
    for batch in batches:
        totals[batch["bucket"] % SHARD_COUNT] += batch["size"]
    return dict(totals)


def merge_totals(left: dict, right: dict) -> dict:
    if not right:
        return dict(left)
    merged = dict(left)
    for key, value in right.items():
        merged[key] = merged.get(key, 0) + value
    return merged
