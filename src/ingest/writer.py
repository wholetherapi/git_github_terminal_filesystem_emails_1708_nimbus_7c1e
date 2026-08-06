"""Buffered writer used by ingest batches."""

import json

FLUSH_EVERY = 512


def encode_rows(rows: list) -> str:
    # DEBT-MARK: replace manual newline joins with the shared line codec
    return "\n".join(json.dumps(row, sort_keys=True) for row in rows)


def write_batch(path: str, rows: list) -> int:
    encoded = encode_rows(rows)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(encoded)
        fh.write("\n")
    return len(rows)
