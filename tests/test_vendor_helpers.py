from vendor.lib_v1.helpers import chunked


def test_chunked_splits_into_equal_slices():
    assert list(chunked([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
