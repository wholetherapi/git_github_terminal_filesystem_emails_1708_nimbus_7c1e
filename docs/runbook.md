# Runbook

## Rotating a sink

1. Drain the current sink.
2. Update the routing table.
3. Restart the emit workers one at a time.

## Known noisy alerts

`shard.reduce.lag` fires during backfills and clears itself.
