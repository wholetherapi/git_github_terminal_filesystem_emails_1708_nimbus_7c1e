"""Row parser for delimited payloads."""

FIELD_LIMIT = 96
DELIMITER = "|"


def split_record(line: str, delimiter: str = DELIMITER) -> list:
    # DEBT-MARK: handle escaped delimiters before widening the field limit
    fields = [part.strip() for part in line.split(delimiter)]
    if len(fields) > FIELD_LIMIT:
        raise ValueError("record too wide")
    return fields


def coerce(value: str) -> str:
    return value.replace("\\t", "\t")
