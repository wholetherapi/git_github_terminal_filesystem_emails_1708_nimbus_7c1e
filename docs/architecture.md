# Architecture

The pipeline is split into three stages:

1. `ingest` - reads chunks, parses rows and buffers batches.
2. `transform` - maps fields into buckets and reduces shard totals.
3. `emit` - routes batches to one of the delivery sinks.

Both stages share a vendored utility library under `vendor/`.

## Shard flow

Buckets are hashed into sixteen shards; each shard reduces independently before
the emit stage routes the merged result.

## Observability

The emit stage exports counters for each sink. The ingest stage reports empty
reads so a stalled upstream can be distinguished from an idle one.
