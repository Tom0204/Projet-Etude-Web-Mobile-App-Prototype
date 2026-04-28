from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from services.csv_reader import read_csv, filter_rows, select_fields, paginate, apply_date_filter
from services.csv_writer import append_row, inject_timestamp
from models.weather_models import WeatherInput

router = APIRouter()

WEATHER_FILE = "weather.csv"

ALL_FIELDS = ["timestamp", "station_id", "rain_mm", "wind_speed_kmh", "wind_direction", "sunshine_hours", "uv_index"]


def _get_weather_data(
    station_id: Optional[str],
    date_from: Optional[str],
    date_to: Optional[str],
    fields: Optional[list[str]],
    limit: int,
    offset: int,
) -> list[dict]:
    rows = read_csv(WEATHER_FILE)
    rows = filter_rows(rows, {"station_id": station_id})
    rows = apply_date_filter(rows, date_from, date_to)
    rows = select_fields(rows, fields)
    return paginate(rows, limit, offset)


@router.get("/")
def get_all_weather(
    station_id: Optional[str] = Query(None, description="Filtrer par station (ex: W001)"),
    fields: Optional[str] = Query(None, description="Colonnes souhaitées séparées par virgule"),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    field_list = [f.strip() for f in fields.split(",")] if fields else None
    if field_list:
        invalid = [f for f in field_list if f not in ALL_FIELDS]
        if invalid:
            raise HTTPException(status_code=400, detail=f"Champs invalides : {invalid}. Disponibles : {ALL_FIELDS}")
    return _get_weather_data(station_id, date_from, date_to, field_list, limit, offset)


@router.get("/rain")
def get_rain(
    station_id: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    return _get_weather_data(station_id, date_from, date_to, ["timestamp", "station_id", "rain_mm"], limit, offset)


@router.get("/wind")
def get_wind(
    station_id: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    return _get_weather_data(station_id, date_from, date_to, ["timestamp", "station_id", "wind_speed_kmh", "wind_direction"], limit, offset)


@router.get("/sunshine")
def get_sunshine(
    station_id: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    return _get_weather_data(station_id, date_from, date_to, ["timestamp", "station_id", "sunshine_hours", "uv_index"], limit, offset)


@router.get("/latest")
def get_latest_weather(station_id: Optional[str] = Query(None)):
    rows = read_csv(WEATHER_FILE)
    rows = filter_rows(rows, {"station_id": station_id})
    if not rows:
        raise HTTPException(status_code=404, detail="Aucune donnée trouvée.")
    return rows[-1]


@router.get("/stations-list")
def list_stations():
    rows = read_csv(WEATHER_FILE)
    ids = sorted(set(r["station_id"] for r in rows if r.get("station_id")))
    return {"station_ids": ids}


@router.post("/", status_code=201)
def add_weather_reading(data: WeatherInput):
    row = inject_timestamp(data.model_dump())
    append_row(WEATHER_FILE, row)
    return {"status": "created", "data": row}
