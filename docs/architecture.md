# Architecture

The pipeline is split into three stages:

1. `ingest` - reads chunks, parses rows and buffers batches.
2. `transform` - maps fields into buckets and reduces shard totals.
3. `emit` - routes batches to one of the delivery sinks.

Both stages share a vendored utility library under `vendor/`.
