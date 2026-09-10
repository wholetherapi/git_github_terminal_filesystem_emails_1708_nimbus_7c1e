# Technical Debt Register

Working register of marker comments that still need follow-up in this repository.
Rows are ordered by file path and then by line number inside the file.

### 📌 Debt Register

- [ ] `src/emit/router.py:11` → route by payload signature once the router table is versioned
- [ ] `src/emit/sink.py:9` → centralise socket teardown when the sink rotates hosts
- [ ] `src/ingest/parser.py:8` → handle escaped delimiters before widening the field limit
- [ ] `src/ingest/reader.py:10` → clamp read size when the stream reports unknown length
- [ ] `src/ingest/writer.py:9` → replace manual newline joins with the shared line codec
- [ ] `src/transform/mapper.py:14` → guard offset arithmetic against zero-width buffers
- [ ] `src/transform/mapper.py:27` → guard offset arithmetic against zero-width buffers
- [ ] `src/transform/reducer.py:9` → settle tie-breaks deterministically across shard boundaries
- [ ] `vendor/lib_v1/codecs.py:8` → drop the duplicated varint tail handling in favour of the shared codec
- [ ] `vendor/lib_v1/helpers.py:10` → replace hand-rolled retry loop with shared backoff helper
- [ ] `vendor/lib_v1/metrics.py:9` → expose per-shard counters instead of a global registry
- [ ] `vendor/lib_v2/codecs.py:8` → drop the duplicated varint tail handling in favour of the shared codec
- [ ] `vendor/lib_v2/helpers.py:10` → replace hand-rolled retry loop with shared backoff helper
- [ ] `vendor/lib_v2/metrics.py:9` → emit counters through the shared telemetry sink
