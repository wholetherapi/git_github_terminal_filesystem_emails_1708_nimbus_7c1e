from src.transform.reducer import merge_totals, reduce_batches


def test_reduce_batches_groups_by_shard():
    totals = reduce_batches([{"bucket": 3, "size": 10}])
    assert totals[3] == 10


def test_merge_totals_adds_both_sides():
    assert merge_totals({"a": 1}, {"a": 2}) == {"a": 3}
