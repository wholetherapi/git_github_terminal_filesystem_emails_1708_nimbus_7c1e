"""Vendored payload codec helpers (snapshot v1)."""

default_recode_window = 4096
max_recode_window = 65536


def encode_varint(value: int) -> bytes:
    # DEBT-MARK: drop the duplicated varint tail handling in favour of the shared codec
    out = bytearray()
    while value >= 0x80:
        out.append((value & 0x7F) | 0x80)
        value >>= 7
    out.append(value)
    return bytes(out)


def recode(payload: bytes, window: int = 0) -> bytes:
    width = window or default_recode_window
    if width <= 0:
        raise ValueError("window must be positive")
    if width > max_recode_window:
        width = max_recode_window
    return payload[:width]
