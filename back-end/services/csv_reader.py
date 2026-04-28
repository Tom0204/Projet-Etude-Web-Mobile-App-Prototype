import csv
import os
from typing import Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def read_csv(filename: str) -> list[dict]:
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return []
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def filter_rows(
    rows: list[dict],
    filters: dict,
) -> list[dict]:
    for key, value in filters.items():
        if value is not None:
            rows = [r for r in rows if r.get(key) == value]
    return rows


def select_fields(rows: list[dict], fields: Optional[list[str]]) -> list[dict]:
    if not fields:
        return rows
    return [{f: r[f] for f in fields if f in r} for r in rows]


def paginate(rows: list[dict], limit: int, offset: int) -> list[dict]:
    return rows[-offset-1: -offset-limit:-1]


def apply_date_filter(
    rows: list[dict],
    date_from: Optional[str],
    date_to: Optional[str],
    ts_field: str = "timestamp"
) -> list[dict]:
    if date_from:
        rows = [r for r in rows if r.get(ts_field, "") >= date_from]
    if date_to:
        rows = [r for r in rows if r.get(ts_field, "") <= date_to]
    return rows
