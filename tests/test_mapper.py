from src.transform.mapper import map_batch, remap_shard, summarize


def test_map_batch_assigns_bucket():
    rows = map_batch([{"key": "alpha"}])
    assert rows[0]["bucket"] >= 0


def test_remap_shard_keeps_requested_shard():
    rows = remap_shard([{"key": "beta"}], 3)
    for row in rows:
        assert row["shard"] == 3


def test_summarize_counts_rows():
    assert summarize([{"key": "gamma"}])["rows"] == 1
