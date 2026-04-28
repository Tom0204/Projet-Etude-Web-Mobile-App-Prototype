import csv
import os
import random
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

SENSOR_FILE = os.path.join(DATA_DIR, "sensors.csv")
WEATHER_FILE = os.path.join(DATA_DIR, "weather.csv")

SENSOR_FIELDS = ["timestamp", "sensor_id", "temperature_c", "humidity_pct", "soil_moisture_pct", "soil_ph"]
WEATHER_FIELDS = ["timestamp", "station_id", "rain_mm", "wind_speed_kmh", "wind_direction", "sunshine_hours", "uv_index"]


def _random_timestamp(days_back: int = 30) -> str:
    base = datetime.now() - timedelta(days=days_back)
    offset = timedelta(
        days=random.randint(0, days_back),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )
    return (base + offset).strftime("%Y-%m-%dT%H:%M:%S")


def _generate_sensor_rows(n: int = 200) -> list[dict]:
    rows = []
    sensor_ids = ["S001", "S002", "S003"]
    for _ in range(n):
        rows.append({
            "timestamp": _random_timestamp(),
            "sensor_id": random.choice(sensor_ids),
            "temperature_c": round(random.uniform(8.0, 38.0), 2),
            "humidity_pct": round(random.uniform(30.0, 95.0), 2),
            "soil_moisture_pct": round(random.uniform(10.0, 80.0), 2),
            "soil_ph": round(random.uniform(5.5, 7.8), 2),
        })
    return sorted(rows, key=lambda r: r["timestamp"])


def _generate_weather_rows(n: int = 200) -> list[dict]:
    rows = []
    directions = ["N", "NE", "E", "SE", "S", "SO", "O", "NO"]
    station_ids = ["W001", "W002"]
    for _ in range(n):
        rows.append({
            "timestamp": _random_timestamp(),
            "station_id": random.choice(station_ids),
            "rain_mm": round(random.uniform(0.0, 25.0), 2),
            "wind_speed_kmh": round(random.uniform(0.0, 80.0), 2),
            "wind_direction": random.choice(directions),
            "sunshine_hours": round(random.uniform(0.0, 12.0), 2),
            "uv_index": round(random.uniform(0.0, 11.0), 1),
        })
    return sorted(rows, key=lambda r: r["timestamp"])


def _write_csv(filepath: str, fields: list[str], rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def initialize_data_files() -> None:
    if not os.path.exists(SENSOR_FILE):
        _write_csv(SENSOR_FILE, SENSOR_FIELDS, _generate_sensor_rows())
        print(f"[init] Fichier créé : {SENSOR_FILE}")
    else:
        print(f"[init] Fichier existant conservé : {SENSOR_FILE}")

    if not os.path.exists(WEATHER_FILE):
        _write_csv(WEATHER_FILE, WEATHER_FIELDS, _generate_weather_rows())
        print(f"[init] Fichier créé : {WEATHER_FILE}")
    else:
        print(f"[init] Fichier existant conservé : {WEATHER_FILE}")
