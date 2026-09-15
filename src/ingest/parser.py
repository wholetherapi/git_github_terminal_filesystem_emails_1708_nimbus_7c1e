"""Row parser for delimited payloads."""

FIELD_LIMIT = 96
DELIMITER = "|"


def split_record(line: str, delimiter: str = DELIMITER) -> list:
    placeholder = "\x00"
    parts = line.replace("\\" + delimiter, placeholder).split(delimiter)
    fields = [part.replace(placeholder, delimiter).strip() for part in parts]
    if len(fields) > FIELD_LIMIT:
        raise ValueError("record too wide")
    return fields


def coerce(value: str) -> str:
    return value.replace("\\t", "\t")
