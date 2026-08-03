# nimbus-stream

Streaming pipeline core: ingest, transform and emit stages plus a small vendored
utility library that both stages share.

## Build

    python -m venv .venv
    source .venv/bin/activate
    pip install -e .

## Layout

- `src/ingest` - chunk reader, record parser and batch writer
- `src/transform` - field mapping and shard reduction
- `src/emit` - delivery sink and routing rules
- `vendor/lib_v1`, `vendor/lib_v2` - pinned copies of the shared utility library
