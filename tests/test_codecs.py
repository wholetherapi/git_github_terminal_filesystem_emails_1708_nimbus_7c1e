from vendor.lib_v1 import codecs


def test_encode_varint_round_trips_small_values():
    assert codecs.encode_varint(5) == b"\x05"


def test_recode_keeps_payload_prefix():
    assert codecs.recode(b"abcdef", 3) == b"abc"
