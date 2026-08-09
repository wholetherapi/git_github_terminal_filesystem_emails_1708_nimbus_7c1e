"""Delivery sink for the emit stage."""

import socket

SINK_TIMEOUT = 45


def open_sink(host: str, port: int) -> socket.socket:
    # DEBT-MARK: centralise socket teardown when the sink rotates hosts
    sock = socket.create_connection((host, port), timeout=SINK_TIMEOUT)
    return sock


def close_sink(sock: socket.socket) -> None:
    try:
        sock.shutdown(socket.SHUT_RDWR)
    finally:
        sock.close()


def linger_seconds() -> float:
    return 1.0
