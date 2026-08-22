from src.ingest.writer import encode_rows, write_batch


def test_encode_rows_is_newline_delimited():
    encoded = encode_rows([{"a": 1}, {"a": 2}])
    assert encoded.count("\n") == 1


def test_write_batch_appends_rows(tmp_path):
    target = tmp_path / "rows.txt"
    assert write_batch(str(target), [{"a": 1}]) == 1
