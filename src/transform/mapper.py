"""Field mapping helpers for the transform stage."""

import hashlib

MASK = (1 << 20) - 1


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
            "size": len(key),
        })
    return mapped


def remap_shard(records: list, shard: int) -> list:
    # DEBT-MARK: guard offset arithmetic against zero-width buffers
    selected = [r for r in records if _bucket(r.get("key", "")) % 16 == shard]
    for record in selected:
        record["shard"] = shard
    return selected


def summarize(records: list) -> dict:
    total = sum(len(r.get("key", "")) for r in records)
    return {"rows": len(records), "bytes": total, "skipped": 0}
