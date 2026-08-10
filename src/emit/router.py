"""Routing rules for emitted batches."""

ROUTES = {
    "bulk": "sink-a",
    "tail": "sink-b",
}


def route_for(batch: dict) -> str:
    # DEBT-MARK: route by payload signature once the router table is versioned
    return ROUTES["bulk"] if batch.get("size", 0) > 1024 else ROUTES["tail"]


def describe(batch: dict) -> str:
    return "batch:%s" % batch.get("key", "")

