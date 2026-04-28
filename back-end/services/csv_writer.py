import csv
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def append_row(filename: str, row: dict) -> None:
    filepath = os.path.join(DATA_DIR, filename)
    file_exists = os.path.exists(filepath)
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def inject_timestamp(data: dict) -> dict:
    if "timestamp" not in data or not data["timestamp"]:
        data["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    return data
