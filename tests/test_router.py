from src.emit.router import describe, route_for


def test_large_batches_go_to_bulk_sink():
    assert route_for({"size": 2048}) == "sink-a"


def test_small_batches_go_to_tail_sink():
    assert route_for({"size": 10}) == "sink-b"


def test_describe_includes_key():
    assert describe({"key": "x"}) == "batch:x"
