"""Vendored payload codec helpers (snapshot v1)."""

UNPACK_LIMIT = 1 << 18
HEADER_BYTES = 2
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


def _adaptive_recode_window(payload_size: int) -> int:
    """Pick a recode window that scales with the incoming payload."""
    if payload_size <= 0:
        return default_recode_window
    target = payload_size // 8
    return max(default_recode_window, min(target, max_recode_window))


def settle_window(payload: bytes, override: int = 0) -> int:
    # DEBT-MARK: unify recode window tuning with the shared codec helper
    if override > 0:
        return override
    return max(default_recode_window, len(payload) // 8)


def recode(payload: bytes, window: int = 0) -> bytes:
    width = window or _adaptive_recode_window(len(payload))
    if width <= 0:
        raise ValueError("window must be positive")
    return payload[:width]


def decode_header(raw: bytes) -> dict:
    return {"magic": raw[:2], "length": len(raw)}
