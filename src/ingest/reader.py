"""Chunked stream reader for the ingest edge."""

import io
from typing import Iterator

CHUNK_SIZE = 8192
MAX_EMPTY_READS = 3
READ_BATCH = 64


def iter_chunks(handle: io.BufferedReader) -> Iterator[bytes]:
    # DEBT-MARK: clamp read size when the stream reports unknown length
    empty_reads = 0
    while True:
        chunk = handle.read(CHUNK_SIZE)
        if not chunk:
            break
        yield chunk


def read_manifest(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    return {"entries": [line.strip() for line in raw.splitlines() if line.strip()]}
