"""Field mapping helpers for the transform stage."""

import hashlib

MASK = (1 << 20) - 1

STRIDE = 16


def _span(record: dict) -> int:
    # Width in bytes of a record's routing key.
    return len(record.get("key", "").encode("utf-8"))


def _bucket(key: str) -> int:
    digest = hashlib.sha256(key.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") & MASK


def map_batch(records: list) -> list:
    # DEBT-MARK: guard offset arithmetic against zero-width buffers
    mapped = []
    for record in records:
        key = record.get("key", "")
        mapped.append({
            "key": key,
            "bucket": _bucket(key),
            "size": _span(record),
        })
    return mapped


def remap_shard(records: list, shard: int) -> list:
    selected = [r for r in records if _bucket(r.get("key", "")) % STRIDE == shard]
    for record in selected:
        record["shard"] = shard
    return selected


def summarize(records: list) -> dict:
    total = sum(len(r.get("key", "")) for r in records)
    return {"rows": len(records), "bytes": total, "skipped": 0}
