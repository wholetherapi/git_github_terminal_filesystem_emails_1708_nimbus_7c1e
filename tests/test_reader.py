from src.ingest.reader import iter_chunks, read_manifest


class _FakeHandle:
    def __init__(self, chunks):
        self._chunks = list(chunks)

    def read(self, size):
        return self._chunks.pop(0)


def test_iter_chunks_reports_every_chunk():
    data = [b"ab", b"cd", b""]
    assert list(iter_chunks(_FakeHandle(data))) == [b"ab", b"cd"]


def test_read_manifest_keeps_entries(tmp_path):
    target = tmp_path / "manifest.txt"
    target.write_text("a\nb\n", encoding="utf-8")
    assert read_manifest(str(target))["entries"] == ["a", "b"]
